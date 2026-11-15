# Reels "miniaturas 3D" (conta Leandro, 14/11/2026).
# Uso: python3 gerar.py 01 [02 03]   -> ../saida/NN.mp4, ../capas/NN.jpg, ../folhas/NN.jpg
# Voz provisória: pt-BR-AntonioNeural +4% (a voz 6 precisa de torch, ausente nesta máquina).
import json, os, sys, subprocess, re, http.server, threading, functools
D = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(D)
BANCO = os.path.join(B, '..', 'leva-30s', 'banco')
R = {r['id']: r for r in json.load(open(os.path.join(B, 'roteiros.json')))}
FPS = 30
TMP = os.environ.get('TMP3D', '/tmp/mini3d')

def sh(*a): subprocess.run(a, check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))

def voz(r):
    """Narração inteira num só bloco (sem emendas), com o tempo de cada palavra dado pelo próprio edge-tts."""
    import asyncio, edge_tts
    w = os.path.join(TMP, r['id']); os.makedirs(w, exist_ok=True)
    falas = [re.sub(r'[.:](?=\s)', ',', f['t']).rstrip('.') for f in r['falas']]
    texto = ' '.join(x if x.endswith('?') else x + ',' for x in falas).rstrip(',') + '.'
    texto = texto.replace('enquete', 'enquéte')
    mp = os.path.join(w, 'narr.mp3'); bd = []
    async def go():
        c = edge_tts.Communicate(texto, 'pt-BR-AntonioNeural', rate='+4%', boundary='WordBoundary', proxy=os.environ['HTTPS_PROXY'])
        with open(mp, 'wb') as fh:
            async for ch in c.stream():
                if ch['type'] == 'audio': fh.write(ch['data'])
                elif ch['type'] == 'WordBoundary': bd.append((ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7, ch['text']))
    for _ in range(6):
        try:
            bd.clear(); asyncio.run(go())
            if bd: break
        except Exception as e: print('tts de novo', e)
    pre = 0.35
    # encurta toda pausa maior que 0,22 s (sem emenda: corte dentro do silêncio, com fade de 30 ms) e remapeia os tempos
    import numpy as np
    SR = 44100
    x = np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',mp,'-f','s16le','-ac','1','-ar',str(SR),'-']), np.int16).astype(np.float32)
    env = np.sqrt(np.convolve(x * x, np.ones(441) / 441, 'same')); quiet = env < 10 ** (-42 / 20) * 32768
    cortes = []; i = 0
    while i < len(quiet):
        if quiet[i]:
            k = i
            while k < len(quiet) and quiet[k]: k += 1
            if (k - i) / SR > 0.22 and i > 0 and k < len(quiet): cortes.append((i + int(.11 * SR), k - int(.11 * SR)))
            i = k
        else: i += 1
    partes, pos = [], 0
    for a0, b0 in cortes: partes.append(x[pos:a0]); pos = b0
    partes.append(x[pos:])
    for q in partes[:-1]: q[-int(.03 * SR):] *= np.linspace(1, 0, int(.03 * SR))
    for q in partes[1:]: q[:int(.03 * SR)] *= np.linspace(0, 1, int(.03 * SR))
    y = np.concatenate(partes)
    def remap(t):
        n0 = t * SR; tira = sum(min(b0, max(a0, n0)) - a0 for a0, b0 in cortes); return (n0 - tira) / SR
    bd[:] = [(remap(a), remap(b2), tx) for a, b2, tx in bd]
    raw = os.path.join(w, 'narr_raw.wav')
    import wave
    with wave.open(raw, 'wb') as wf: wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes(np.clip(y, -32768, 32767).astype(np.int16).tobytes())
    mp = raw
    sh('ffmpeg','-v','error','-y','-i',mp,'-af',f'adelay={int(pre*1000)},highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:makeup=2,loudnorm=I=-15:TP=-1','-ar','44100','-ac','1',os.path.join(w,'narr.wav'))
    n = sum(len(f['t'].split()) for f in r['falas'])
    if len(bd) != n: print('AVISO contagem', len(bd), n, flush=True)
    ws, tl, j = [], [], 0
    for i, f in enumerate(r['falas']):
        toks = f['t'].split(); ini = None
        for k in toks:
            a, b2, _ = bd[min(round(j * len(bd) / n), len(bd) - 1)]; j += 1
            if ini is None: ini = a + pre
            limpa = re.sub(r'[^\wÀ-ú]', '', k).lower()
            ws.append({'w': k, 'a': a + pre, 'b': b2 + pre, 'f': i, 'k': any(limpa == c.lower() for c in f.get('chave', []))})
        tl.append({'ini': ini, 'fim': ws[-1]['b']})
    return tl, dur(os.path.join(w, 'narr.wav')) + 1.0, ws

def palavras(r):
    from faster_whisper import WhisperModel
    import numpy as np
    m = WhisperModel('small', device='cpu', compute_type='int8')
    wav = os.path.join(TMP, r['id'], 'narr.wav')
    pcm = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', wav, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'])
    segs, _ = m.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768, language='pt')
    txt = ' '.join(s.text.strip() for s in segs)
    e = subprocess.run(['ffmpeg', '-i', wav, '-af', 'silencedetect=n=-40dB:d=0.3', '-f', 'null', '-'], capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', e)]
    return txt + f"\n[pausas > 0,3 s no meio da fala: {len([x for x in ini if 0.5 < x < dur(wav) - 0.5])}]"

def servir():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=D)
    h.log_message = lambda *a: None
    s = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start()
    return s.server_address[1]

def render(r, dados, total, porta):
    from playwright.sync_api import sync_playwright
    fr = os.path.join(TMP, r['id'], 'q'); os.makedirs(fr, exist_ok=True)
    n = int(total * FPS); prev = os.environ.get('PREVIA')
    quadros = [int(float(x) * FPS) for x in prev.split(',')] if prev else range(n)
    if os.environ.get('SOCAPA'):
        with sync_playwright() as p:
            b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
            pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
            pg.goto(f'http://127.0.0.1:{porta}/palco.html'); pg.wait_for_function('window.pronto===true')
            pg.evaluate('d=>window.carregar(d)', dados); pg.evaluate('window.seek(0.5)'); pg.evaluate('window.modoCapa()')
            pg.screenshot(path=os.path.join(B, 'capas', r['id'] + '.jpg'), type='jpeg', quality=92); b.close()
        return fr, -1
    if not prev and len(os.listdir(fr)) >= n and os.path.exists(os.path.join(B, 'capas', r['id'] + '.jpg')): return fr, n
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
        pg.goto(f'http://127.0.0.1:{porta}/palco.html'); pg.wait_for_function('window.pronto===true')
        pg.evaluate('d=>window.carregar(d)', dados)
        for i in quadros:
            if not prev and os.path.exists(os.path.join(fr, f'{i:05d}.jpg')) and os.path.exists(os.path.join(fr, f'{i+1:05d}.jpg')): continue
            pg.evaluate(f'window.seek({i / FPS})')
            pg.screenshot(path=os.path.join(fr, f'{i:05d}.jpg'), type='jpeg', quality=88)
        pg.evaluate('window.modoCapa()'); pg.screenshot(path=os.path.join(B, 'capas', r['id'] + '.jpg'), type='jpeg', quality=92)
        b.close()
    return fr, n

def mix(r, dados, total, fr):
    w = os.path.join(TMP, r['id']); sfx = os.path.join(BANCO, 'sfx'); trilha = os.path.join(BANCO, 'trilha', 'midnight-funk-117bpm.mp3' if r['id'] != '02' else 'trap-electro-vibes-112bpm.mp3')
    ins = ['-i', os.path.join(w, 'narr.wav'), '-stream_loop', '-1', '-i', trilha]; fil = []; k = 3; tags = []
    eventos = [(0.0, 'impacto-intro.mp3', 0.9)]
    for i, s in enumerate(dados['tl'][1:], 1): eventos.append((max(0, s['ini'] - 0.25), 'whoosh-rapido.mp3' if i % 2 else 'whoosh-cinematico.mp3', 0.55))
    for i, f in enumerate(r['falas']):
        if f.get('num'): eventos.append((dados['tl'][i]['ini'] + 0.6, 'impacto-cinematico.mp3', 0.6))
        if f.get('selo'): eventos.append((dados['tl'][i]['ini'] + 0.3, 'pop-forte.mp3', 0.5))
        if f.get('cta') or f.get('enquete'): eventos.append((dados['tl'][i]['ini'] + 0.2, 'notificacao-positiva.mp3', 0.6))
    for t, nome, v in eventos:
        ins += ['-i', os.path.join(sfx, nome)]
        fil.append(f'[{k}:a]volume={v},adelay={int(t*1000)}|{int(t*1000)}[s{k}]'); tags.append(f'[s{k}]'); k += 1
    fil.append(f'[2:a]volume=0.32,atrim=0:{total},afade=t=out:st={total-1.2}:d=1.2[mus]')
    fil.append('[1:a]asplit=2[v1][v2]')
    fil.append('[mus][v2]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[duck]')
    fil.append(f'[v1][duck]{"".join(tags)}amix=inputs={2+len(tags)}:normalize=0,alimiter=limit=0.95,loudnorm=I=-14:TP=-1[a]')
    os.makedirs(os.path.join(B, 'saida'), exist_ok=True)
    out = os.path.join(B, 'saida', r['id'] + '.mp4')
    sh('ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(fr, '%05d.jpg'), *ins,
       '-filter_complex', ';'.join(fil), '-map', '0:v', '-map', '[a]', '-t', f'{total:.2f}',
       '-c:v', 'libx264', '-preset', 'slow', '-crf', '24', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out)
    # folha de quadros: 12 quadros espalhados
    os.makedirs(os.path.join(B, 'folhas'), exist_ok=True)
    sh('ffmpeg', '-v', 'error', '-y', '-i', out, '-vf', f'fps=12/{total},scale=270:480,tile=6x2:padding=6:color=black', '-frames:v', '1', os.path.join(B, 'folhas', r['id'] + '.jpg'))
    return out

if __name__ == '__main__':
    porta = servir(); os.makedirs(os.path.join(B, 'capas'), exist_ok=True)
    for nn in sys.argv[1:]:
        r = R[nn]; tl, total, ws = voz(r); texto = palavras(r)
        os.makedirs(os.path.join(B, 'whisper'), exist_ok=True); open(os.path.join(B, 'whisper', nn + '.txt'), 'w').write(texto + '\n')
        dados = {'r': r, 'tl': tl, 'ws': ws, 'total': total}
        fr, n = render(r, dados, total, porta)
        if os.environ.get('PREVIA') or os.environ.get('SOCAPA'): print('previa', fr); continue
        print(nn, 'pronto', mix(r, dados, total, fr), f'{total:.1f}s', flush=True)
