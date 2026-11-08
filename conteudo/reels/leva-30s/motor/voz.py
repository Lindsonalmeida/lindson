"""Narração da leva de Reels de 30 s (motor v2, 08/11/2026).

Dois caminhos:
- duble       : voz clonada do Lindson pelo Dublê (Chatterbox Multilingual, apps/clone-studio/motor_voz.py),
                em blocos de até ~220 caracteres (regra do Lindson de 03/11), com o áudio de referência
                em agencia/marca-lindson/voz/ref.wav (FORA do Git: dado biométrico).
- provisoria  : rascunho com pt-BR-AntonioNeural (edge-tts). NÃO é entrega final; o vídeo sai marcado "voz provisória".

Saída: (audio float32 44,1 kHz mono, lista de palavras [(palavra, início_s, fim_s)]).
"""
import asyncio, io, json, os, re, subprocess, sys, tempfile
import numpy as np, soundfile as sf

S = 44100
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
REF = os.path.join(RAIZ, 'agencia/marca-lindson/voz/ref.wav')
# Python com chatterbox-tts instalado (venv separado, porque traz o torch). Ex.: PY_DUBLE=~/cbx/bin/python
PY_DUBLE = os.environ.get('PY_DUBLE', sys.executable)


def _wav(path_or_bytes):
    d = tempfile.mkdtemp(); src = path_or_bytes
    if isinstance(path_or_bytes, (bytes, bytearray)):
        src = os.path.join(d, 'in.mp3'); open(src, 'wb').write(path_or_bytes)
    out = os.path.join(d, 'o.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-ac', '1', '-ar', str(S), out], check=True)
    a, _ = sf.read(out, dtype='float32'); return a


def _edge(txt, rate):
    try:
        import certifi; certifi.where = lambda: os.environ.get('SSL_CERT_FILE', '/root/.ccr/ca-bundle.crt') \
            if os.path.exists('/root/.ccr/ca-bundle.crt') else certifi.where()
    except Exception:
        pass
    import edge_tts

    async def go():
        c = edge_tts.Communicate(txt, 'pt-BR-AntonioNeural', rate=rate, boundary='WordBoundary')
        audio, words = bytearray(), []
        async for ch in c.stream():
            if ch['type'] == 'audio': audio += ch['data']
            elif ch['type'] == 'WordBoundary':
                words.append((ch['text'], ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7))
        return bytes(audio), words
    return asyncio.run(go())


def _apara(a, lim_db=-40):
    e = np.convolve(np.abs(a), np.ones(441) / 441, 'same'); on = np.where(e > e.max() * 10 ** (lim_db / 20))[0]
    if not len(on): return a, 0.0
    i, j = max(0, on[0] - 441), min(len(a), on[-1] + 2205)
    return a[i:j], i / S


def encurta_pausas(a, ws, maxp=0.24):
    """Regra do Dublê (03/11): voz fluida, pausa curta (~0,2 s) entre frases. Corta o excesso de
    silêncio entre palavras e desloca os tempos das palavras seguintes."""
    if not ws: return a, ws
    partes, novo, desloc, pos = [], [], 0.0, 0
    for k, (w, s0, e0) in enumerate(ws):
        if k:
            gap = s0 - ws[k - 1][2]
            if gap > maxp:
                i0 = int((ws[k - 1][2] + maxp / 2) * S); i1 = int((s0 - maxp / 2) * S)
                if i1 > i0:
                    partes.append(a[pos:i0]); pos = i1; desloc += (i1 - i0) / S
        novo.append((w, s0 - desloc, e0 - desloc))
    partes.append(a[pos:])
    return np.concatenate(partes), novo


def provisoria(blocos, rate='+10%', pausa=0.22):
    out, words, t = [], [], 0.0
    for k, b in enumerate(blocos):
        mp3, ws = _edge(b, rate); a = _wav(mp3); a, cut = _apara(a)
        ws = [(w, max(0.0, s - cut), e - cut) for w, s, e in ws]
        a, ws = encurta_pausas(a, ws)
        words += [(w, t + s, t + e) for w, s, e in ws]
        out.append(a); t += len(a) / S
        if k < len(blocos) - 1:
            out.append(np.zeros(int(pausa * S), np.float32)); t += pausa
    return np.concatenate(out), words


def duble(blocos, ref=REF, pausa=0.22):
    """Gera cada bloco inteiro de uma vez com o motor do Dublê. As palavras recebem tempo proporcional
    às letras dentro do bloco, refinado pelas pausas reais (silêncios) entre frases."""
    if not os.path.exists(ref):
        raise SystemExit(f'Falta a voz de referência do Lindson em {ref} (fora do Git). Use --voz provisoria para rascunho.')
    d = tempfile.mkdtemp(); js = os.path.join(d, 'b.json'); json.dump(blocos, open(js, 'w'), ensure_ascii=False)
    code = ("import sys,json,soundfile as sf;sys.path.insert(0,%r);import motor_voz as m\n"
            "bl=json.load(open(%r))\n"
            "for i,b in enumerate(bl):sf.write(%r%%i,m.narrar(b,%r),44100)\n") % (
        os.path.join(RAIZ, 'apps/clone-studio'), js, os.path.join(d, 'b%d.wav'), ref)
    subprocess.run([PY_DUBLE, '-c', code], check=True)
    out, words, t = [], [], 0.0
    for k, b in enumerate(blocos):
        a, _ = sf.read(os.path.join(d, f'b{k}.wav'), dtype='float32'); a, _ = _apara(a)
        words += _alinha(b, a, t); out.append(a); t += len(a) / S
        if k < len(blocos) - 1:
            out.append(np.zeros(int(pausa * S), np.float32)); t += pausa
    return np.concatenate(out), words


def _alinha(txt, a, t0):
    """Tempo aproximado de cada palavra: divide o bloco em frases pelas pausas reais do áudio
    (silêncios > 120 ms) e, dentro de cada frase, reparte pelo número de letras."""
    frases = [f for f in re.split(r'(?<=[.!?…])\s+', txt.strip()) if f]
    e = np.convolve(np.abs(a), np.ones(441) / 441, 'same'); fala = e > e.max() * 0.03
    # trechos de silêncio
    sil, i, n = [], 0, len(fala)
    while i < n:
        if not fala[i]:
            j = i
            while j < n and not fala[j]: j += 1
            if (j - i) / S > .12: sil.append(((i + j) / 2) / S)
            i = j
        else: i += 1
    dur = len(a) / S
    # escolhe as len(frases)-1 pausas mais próximas da divisão proporcional
    tot = sum(len(f) for f in frases); acc, cortes = 0, []
    for f in frases[:-1]:
        acc += len(f); alvo = dur * acc / tot
        cortes.append(min(sil, key=lambda x: abs(x - alvo)) if sil else alvo)
    lim = [0.0] + cortes + [dur]; words = []
    for k, f in enumerate(frases):
        ws = f.split(); s0, s1 = lim[k], lim[k + 1]; L = sum(len(w) + 1 for w in ws); c = 0
        for w in ws:
            a0 = s0 + (s1 - s0) * c / L; c += len(w) + 1; words.append((w, t0 + a0, t0 + s0 + (s1 - s0) * c / L))
    return words


def narrar(blocos, modo='provisoria', **k):
    return duble(blocos, **k) if modo == 'duble' else provisoria(blocos, **k)


if __name__ == '__main__':
    a, w = narrar([sys.argv[1]], sys.argv[2] if len(sys.argv) > 2 else 'provisoria')
    sf.write('/tmp/voz.wav', a, S); print(len(a) / S, w[:8])
