# Reels 3D v2 "Cinema 2.5D" (conta Leandro, 16/11/2026). Substitui o estilo miniaturas (reprovado).
# Uso: python3 gerar.py 01 [02 03]   -> ../saida/NN.mp4, ../capas/NN.jpg, ../folhas/NN.jpg
# Voz 6 do Lindson (Chatterbox, ref6.wav) com a tabela de pronúncias de ../PRONUNCIAS.md (dicionário PRON abaixo).
import json, os, sys, subprocess, re, http.server, threading, functools
D = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(D)
BANCO = os.path.join(B, '..', 'leva-30s', 'banco')
FOTOS = os.path.abspath(os.path.join(B, '..', '..', '..', 'agencia/marca-lindson/linha-frases/fotos/rec'))
PRON = {'enquete': 'enquéte'}  # texto escrito -> como a voz deve ler (ver PRONUNCIAS.md)
R = {r['id']: r for r in json.load(open(os.path.join(B, 'roteiros.json')))}
FPS = 30
TMP = os.environ.get('TMP3D', '/tmp/reels3dv2')

def sh(*a): subprocess.run(a, check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))

V6 = None
def voz(r):
    """Voz 6 do Lindson (Chatterbox, ref6.wav), uma fala por bloco (<= 220 caracteres), emendas com fade de 40 ms,
    pausas encurtadas para no máximo 0,22 s e tempo das palavras pelo Whisper."""
    global V6
    import numpy as np, hashlib, wave
    import torch, torchaudio as ta
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
    if V6 is None: torch.set_num_threads(os.cpu_count()); V6 = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
    REF = os.path.abspath(os.path.join(B, '..', '..', '..', 'agencia/marca-lindson/voz/ref6.wav'))
    cache = os.path.join(TMP, 'v6'); os.makedirs(cache, exist_ok=True); w = os.path.join(TMP, r['id']); os.makedirs(w, exist_ok=True)
    SR = 44100; blocos = []
    for f in r['falas']:
        txt = f['t']
        for a_, b_ in PRON.items(): txt = txt.replace(a_, b_)
        h = os.path.join(cache, hashlib.md5(txt.encode()).hexdigest()[:12] + '.wav')
        if not os.path.exists(h):
            import difflib
            from faster_whisper import WhisperModel
            global WM
            if 'WM' not in globals(): WM = WhisperModel('small', device='cpu', compute_type='int8')
            import unicodedata
            def norm(z):
                z = z.lower().replace('quinhentos', '500').replace('três', '3').replace('tá ', 'está ').replace('pra ', 'para ')
                z = ''.join(c for c in unicodedata.normalize('NFD', z) if unicodedata.category(c) != 'Mn')
                return list(re.sub(r'[^a-z0-9]', '', z))
            melhor = (-1, None)
            for semente in (6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
                torch.manual_seed(semente)
                wv = V6.generate(txt, language_id='pt', audio_prompt_path=REF, exaggeration=0.75, cfg_weight=0.3, temperature=0.8)
                a16 = ta.functional.resample(wv, V6.sr, 16000)[0].numpy()
                ouv = ' '.join(z.text for z in WM.transcribe(a16, language='pt')[0])
                nota = difflib.SequenceMatcher(None, norm(f['t']), norm(ouv)).ratio()
                if nota > melhor[0]: melhor = (nota, wv)
                print('voz6', semente, round(nota, 2), ouv, flush=True)
                if nota >= .985: break
            ta.save(h, melhor[1], V6.sr)
        x = np.frombuffer(subprocess.check_output(['ffmpeg', '-v', 'error', '-i', h, '-af', 'atempo=1.0', '-f', 's16le', '-ac', '1', '-ar', str(SR), '-']), np.int16).astype(np.float32)
        env = np.sqrt(np.convolve(x * x, np.ones(441) / 441, 'same')); voz_ = np.where(env > 10 ** (-40 / 20) * 32768)[0]
        x = x[max(0, voz_[0] - 400): voz_[-1] + 2200]
        # encurta pausas internas > 0,22 s
        q = np.sqrt(np.convolve(x * x, np.ones(441) / 441, 'same')) < 10 ** (-42 / 20) * 32768
        out, i0, i = [], 0, 0
        while i < len(q):
            if q[i]:
                k = i
                while k < len(q) and q[k]: k += 1
                if (k - i) / SR > .22: out.append(x[i0:i + int(.1 * SR)]); i0 = k - int(.1 * SR)
                i = k
            else: i += 1
        out.append(x[i0:]); x = np.concatenate(out)
        n = int(.04 * SR); x[:n] *= np.linspace(0, 1, n); x[-n:] *= np.linspace(1, 0, n)
        blocos.append(x)
    pre = .35; gap = np.zeros(int(.2 * SR), np.float32); tl = []; partes = [np.zeros(int(pre * SR), np.float32)]; t = pre
    for x in blocos: tl.append({'ini': t, 'fim': t + len(x) / SR}); partes += [x, gap]; t += len(x) / SR + .2
    y = np.concatenate(partes); raw = os.path.join(w, 'narr_raw.wav')
    with wave.open(raw, 'wb') as wf: wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes(np.clip(y, -32768, 32767).astype(np.int16).tobytes())
    sh('ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', 'highpass=f=90,equalizer=f=3500:t=q:w=1:g=2,acompressor=threshold=-20dB:ratio=3:attack=5:release=60:makeup=2,loudnorm=I=-15:TP=-1', '-ar', '44100', os.path.join(w, 'narr.wav'))
    # palavras: Whisper com tempo por palavra, repartido por fala
    from faster_whisper import WhisperModel
    m = WhisperModel('small', device='cpu', compute_type='int8')
    pcm = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', os.path.join(w, 'narr.wav'), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'])
    segs, _ = m.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768, language='pt', word_timestamps=True)
    wsw = [(x.start, x.end, x.word.strip()) for s_ in segs for x in s_.words]
    global TEXTO_WHISPER; TEXTO_WHISPER = ' '.join(z[2] for z in wsw)
    ws = []
    for i, f in enumerate(r['falas']):
        toks = f['t'].split(); a, b2 = tl[i]['ini'], tl[i]['fim']
        dentro = [z for z in wsw if a - .1 <= z[0] < b2 + .05]
        if len(dentro) == len(toks): ts = [(z[0], z[1]) for z in dentro]
        else:
            tot = sum(len(k) + 2 for k in toks); acc = a; ts = []
            for k in toks: d = (b2 - a) * (len(k) + 2) / tot; ts.append((acc, acc + d)); acc += d
        for k, (x0, x1) in zip(toks, ts):
            limpa = re.sub(r'[^\wÀ-ú]', '', k).lower()
            ws.append({'w': k, 'a': x0, 'b': x1, 'f': i, 'k': any(limpa == c.lower() for c in f.get('chave', []))})
    return tl, t + .9, ws

def palavras(r):
    wav = os.path.join(TMP, r['id'], 'narr.wav')
    e = subprocess.run(['ffmpeg', '-i', wav, '-af', 'silencedetect=n=-40dB:d=0.3', '-f', 'null', '-'], capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', e)]
    return TEXTO_WHISPER + f"\n[pausas > 0,3 s no meio da fala: {len([x for x in ini if 0.5 < x < dur(wav) - 0.6])}]"

def servir():
    www = os.path.join(TMP, 'www'); os.makedirs(www, exist_ok=True)
    for f in os.listdir(D):
        if not os.path.exists(os.path.join(www, f)): os.symlink(os.path.join(D, f), os.path.join(www, f))
    for r in R.values():
        q = os.path.join(www, 'foto_' + r['id'] + '.png')
        if not os.path.exists(q): os.symlink(os.path.join(FOTOS, r['foto'] + '.png'), q)
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=www)
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
            pg.evaluate('d=>window.carregar(d)', dados); pg.wait_for_function('window.pronto2===true'); pg.evaluate('window.seek(0.5)'); pg.evaluate('window.modoCapa()')
            pg.screenshot(path=os.path.join(B, 'capas', r['id'] + '.jpg'), type='jpeg', quality=92); b.close()
        return fr, -1
    if not prev and len(os.listdir(fr)) >= n and os.path.exists(os.path.join(B, 'capas', r['id'] + '.jpg')): return fr, n
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
        pg.goto(f'http://127.0.0.1:{porta}/palco.html'); pg.wait_for_function('window.pronto===true')
        pg.evaluate('d=>window.carregar(d)', dados); pg.wait_for_function('window.pronto2===true')
        for i in quadros:
            if not prev and os.path.exists(os.path.join(fr, f'{i:05d}.jpg')) and os.path.exists(os.path.join(fr, f'{i+1:05d}.jpg')): continue
            pg.evaluate(f'window.seek({i / FPS})')
            pg.screenshot(path=os.path.join(fr, f'{i:05d}.jpg'), type='jpeg', quality=88)
        pg.evaluate(f"window.seek({dados['tl'][0]['ini'] + 1.2})"); pg.evaluate('window.modoCapa()'); pg.screenshot(path=os.path.join(B, 'capas', r['id'] + '.jpg'), type='jpeg', quality=92)
        b.close()
    return fr, n

def mix(r, dados, total, fr):
    w = os.path.join(TMP, r['id']); sfx = os.path.join(BANCO, 'sfx'); trilha = os.path.join(BANCO, 'trilha', {'01': 'midnight-funk-117bpm.mp3', '02': 'trap-electro-vibes-112bpm.mp3', '03': 'pop-track-03-108bpm.mp3'}[r['id']])
    ins = ['-i', os.path.join(w, 'narr.wav'), '-stream_loop', '-1', '-i', trilha]; fil = []; k = 3; tags = []
    eventos = [(0.0, 'impacto-intro.mp3', 0.9)]
    for i, s in enumerate(dados['tl'][1:], 1): eventos.append((max(0, s['ini'] - 0.25), 'whoosh-rapido.mp3' if i % 2 else 'whoosh-cinematico.mp3', 0.55))
    for i, s_ in enumerate(dados['tl']):
        fim = dados['tl'][i + 1]['ini'] if i + 1 < len(dados['tl']) else total
        if r['falas'][i].get('tec') == 'split': continue
        m = 1
        while s_['ini'] + 2.6 * m < fim - .6 and r['modo'] != 'tunel': eventos.append((s_['ini'] + 2.6 * m - .05, ['click.mp3', 'sweep-curto.mp3', 'pop-longo.mp3'][m % 3], .35)); m += 1
    for i, f in enumerate(r['falas']):
        if f.get('tec') == 'quarta': eventos.append((max(0, dados['tl'][i]['ini'] - .05), 'impacto-cinematico.mp3', .55))
        if f.get('tec') == 'explode': eventos.append((dados['tl'][i]['ini'] + .1, 'glitch-quebra.mp3', .4))
        if f.get('lista'):
            for j in range(len(f['lista'])): eventos.append((dados['tl'][i]['ini'] + .3 + j * .5, 'pop-forte.mp3', .35))
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
    sh('ffmpeg', '-v', 'error', '-y', '-i', out, '-vf', f'select=not(mod(n\\,{int(total*FPS/12)+1})),scale=270:480,tile=6x2:padding=6:color=black', '-vsync', 'vfr', '-frames:v', '1', os.path.join(B, 'folhas', r['id'] + '.jpg'))
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
