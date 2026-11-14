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
    w = os.path.join(TMP, r['id']); os.makedirs(w, exist_ok=True); partes = []; t = 0.35; tl = []
    for i, f in enumerate(r['falas']):
        mp = os.path.join(w, f'f{i}.mp3'); wav = os.path.join(w, f'f{i}.wav')
        if not os.path.exists(mp):
            for _ in range(4):
                if subprocess.run(['edge-tts', '--proxy', os.environ['HTTPS_PROXY'], '--voice', 'pt-BR-AntonioNeural', '--rate=+4%', '--text', f['t'], '--write-media', mp]).returncode == 0: break
            else: sh('edge-tts', '--proxy', os.environ['HTTPS_PROXY'], '--voice', 'pt-BR-AntonioNeural', '--rate=+4%', '--text', f['t'], '--write-media', mp)
        sh('ffmpeg','-v','error','-y','-i',mp,'-af','silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse','-ar','44100','-ac','1',wav)
        d = dur(wav); tl.append({'ini': t, 'fim': t + d}); partes.append(wav); t += d + 0.18
    lst = os.path.join(w, 'l.txt'); sil = os.path.join(w, 'sil.wav')
    sh('ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=44100:cl=mono','-t','0.18',sil)
    open(lst,'w').write("file '%s'\n" % os.path.join(w,'sil0.wav') + ''.join(f"file '{p}'\nfile '{sil}'\n" for p in partes))
    sh('ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=44100:cl=mono','-t','0.35',os.path.join(w,'sil0.wav'))
    sh('ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-af','highpass=f=80,acompressor=threshold=-20dB:ratio=3:makeup=2,loudnorm=I=-15:TP=-1','-ar','44100',os.path.join(w,'narr.wav'))
    return tl, t + 1.2

def palavras(r, tl):
    """Whisper (faster-whisper small) dá o tempo de cada palavra e confere o texto."""
    from faster_whisper import WhisperModel
    m = WhisperModel('small', device='cpu', compute_type='int8')
    import numpy as np
    pcm = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', os.path.join(TMP, r['id'], 'narr.wav'), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'])
    segs, _ = m.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768, language='pt', word_timestamps=True)
    ws = [{'w': x.word.strip(), 'a': x.start, 'b': x.end} for s in segs for x in s.words]
    texto = ' '.join(x['w'] for x in ws)
    # legenda usa o texto do roteiro (grafia certa), com os tempos do Whisper repartidos por fala
    out = []
    for i, f in enumerate(r['falas']):
        toks = f['t'].split(); a, b = tl[i]['ini'], tl[i]['fim']
        dentro = [x for x in ws if x['a'] >= a - 0.15 and x['a'] < b + 0.1]
        if len(dentro) == len(toks): ts = [(x['a'], x['b']) for x in dentro]
        else:  # reparte pelo tamanho das palavras
            tot = sum(len(k) + 2 for k in toks); acc = a; ts = []
            for k in toks: d = (b - a) * (len(k) + 2) / tot; ts.append((acc, acc + d)); acc += d
        for k, (x, y) in zip(toks, ts):
            limpa = re.sub(r'[^\wÀ-ú]', '', k).lower()
            out.append({'w': k, 'a': x, 'b': y, 'f': i, 'k': any(limpa == c.lower() for c in f.get('chave', []))})
    return out, texto

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
        r = R[nn]; tl, total = voz(r); ws, texto = palavras(r, tl)
        os.makedirs(os.path.join(B, 'whisper'), exist_ok=True); open(os.path.join(B, 'whisper', nn + '.txt'), 'w').write(texto + '\n')
        dados = {'r': r, 'tl': tl, 'ws': ws, 'total': total}
        fr, n = render(r, dados, total, porta)
        if os.environ.get('PREVIA') or os.environ.get('SOCAPA'): print('previa', fr); continue
        print(nn, 'pronto', mix(r, dados, total, fr), f'{total:.1f}s', flush=True)
