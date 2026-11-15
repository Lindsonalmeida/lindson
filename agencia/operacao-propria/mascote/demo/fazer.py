"""Vídeo demo do Seu Turbo (conta Pedro, 15/11/2026). Uso: python3 demo/fazer.py ["texto novo"]
Voz Antonio +4% (a aprovada nos Reels), lip-sync por volume, trilha Mixkit, SFX e VFX.
Para outro vídeo: troque TEXTO (ou passe na linha de comando) e as palavras-gatilho em GATILHOS."""
import os, sys, json, subprocess, asyncio
import numpy as np, soundfile as sf
AQUI = os.path.dirname(os.path.abspath(__file__)); BANCO = os.path.join(AQUI, '../../reels/banco')
TEXTO = sys.argv[1] if len(sys.argv) > 1 else 'Prazer, eu sou o Seu Turbo, parceiro do dono de pizzaria. O forno é seu. O turbo, pra pedido chegar no WhatsApp, é comigo.'
GATILHOS = {'apresenta': 'parceiro', 'aponta': 'turbo,', 'joinha': 'comigo.'}
OUT = os.path.join(AQUI, 'saida'); os.makedirs(OUT, exist_ok=True)
FPS = 30; INICIO = 0.6  # a voz entra depois do pouso

if os.path.exists('/root/.ccr/ca-bundle.crt'):
    import certifi; certifi.where = lambda: '/root/.ccr/ca-bundle.crt'
import edge_tts
async def tts():
    c = edge_tts.Communicate(TEXTO, 'pt-BR-AntonioNeural', rate='+4%', boundary='WordBoundary', proxy=os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy')); a, w = bytearray(), []
    async for ch in c.stream():
        if ch['type'] == 'audio': a += ch['data']
        elif ch['type'] == 'WordBoundary': w.append([ch['text'], ch['offset'] / 1e7 + INICIO, (ch['offset'] + ch['duration']) / 1e7 + INICIO])
    return bytes(a), w
mp3, palavras = asyncio.run(tts())
open(f'{OUT}/voz.mp3', 'wb').write(mp3)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{OUT}/voz.mp3', '-ac', '1', '-ar', '44100', f'{OUT}/voz.wav'], check=True)
a, S = sf.read(f'{OUT}/voz.wav'); fala = len(a) / S
DUR = round(INICIO + fala + 1.1, 2)
n = int(DUR * FPS); vol, zcr = [], []
for i in range(n):
    j = int((i / FPS - INICIO) * S); seg = a[max(0, j):max(0, j) + S // FPS] if j >= 0 else np.zeros(10)
    r = float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0; vol.append(r)
    zcr.append(float(np.mean(np.abs(np.diff(np.sign(seg))) > 0)) if len(seg) > 2 else 0)
vol = np.array(vol); vol = np.clip(vol / (np.percentile(vol[vol > 0], 95) if (vol > 0).any() else 1), 0, 1)
zcr = np.array(zcr); zcr = np.clip(zcr / .35, 0, 1)
def t_de(p, ult=False):
    hits = [w for w in palavras if w[0].lower().strip(',.') == p.strip(',.').lower()]
    return (hits[-1] if ult else hits[0])[1] if hits else DUR
marcas = {'aceno': .9, 'apresenta': t_de('parceiro'), 'aponta': t_de('turbo', True) - .1, 'joinha': t_de('comigo')}
TL = dict(vol=vol.round(3).tolist(), zcr=zcr.round(3).tolist(), palavras=palavras, marcas=marcas, fim=INICIO + fala, dur=DUR)
json.dump(TL, open(f'{OUT}/tl.json', 'w'))
subprocess.run(['node', os.path.join(AQUI, 'quadros.js'), f'{OUT}/tl.json', f'{OUT}/q'], check=True, env=dict(os.environ, NODE_PATH=subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()))
# som: voz + trilha baixa + SFX (whoosh na entrada, impacto no pouso, pop na comanda e no joinha)
sfx = [('whoosh-rapido', 0.0, 0), ('impacto-intro', .55, -3), ('pop-forte', marcas['aponta'] + .15, -4), ('pop-longo', marcas['joinha'], -4), ('whoosh-cinematico', DUR - 1.0, -8)]
ins = ['-i', f'{OUT}/q/%05d.png', '-i', f'{OUT}/voz.wav', '-stream_loop', '-1', '-i', f'{BANCO}/trilha/midnight-funk-117bpm.mp3']
fil = [f'[1]adelay={int(INICIO*1000)}|{int(INICIO*1000)},volume=1.6[v]', f'[2]atrim=0:{DUR},volume=0.12,afade=t=out:st={DUR-1}:d=1[m]']
mix = '[v][m]'
for i, (nome, t, db) in enumerate(sfx):
    ins += ['-i', f'{BANCO}/sfx/{nome}.mp3']; k = i + 3
    fil.append(f'[{k}]adelay={int(t*1000)}|{int(t*1000)},volume={db}dB[s{i}]'); mix += f'[s{i}]'
fil.append(f'{mix}amix=inputs={2+len(sfx)}:normalize=0,alimiter=limit=0.95[a]')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), *ins, '-filter_complex', ';'.join(fil), '-map', '0:v', '-map', '[a]',
                '-t', str(DUR), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '23', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k',
                '-movflags', '+faststart', os.path.join(AQUI, 'seu-turbo-demo.mp4')], check=True)
print('ok', DUR, 's', marcas)
