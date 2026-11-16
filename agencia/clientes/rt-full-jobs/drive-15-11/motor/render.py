"""Lettering + voz Antonio sobre os videos prontos da Real Time (conta Zuleide, 15/11/2026).
Nao altera cortes: so sobrepoe texto (identidade v1) e mixa a narracao com o audio original.
Uso: python3 -I render.py <pasta brutos> <pasta saida> <pasta fontes> <id>"""
import json, os, subprocess, sys, asyncio
from PIL import Image, ImageDraw, ImageFont
import certifi, ssl
if os.path.exists('/root/.ccr/ca-bundle.crt'): certifi.where = lambda: '/root/.ccr/ca-bundle.crt'
import edge_tts
BR, OUT, FT, VID = sys.argv[1:5]
R = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'roteiros.json')))[VID]
W, H = 1080, 1920
PRETO, BRANCO, AZUL, REC, GRAF = (5,7,11), (244,247,251), (46,155,255), (255,59,59), (17,22,31)
f = lambda n, s: ImageFont.truetype(os.path.join(FT, n), s)
T = os.path.join(OUT, VID + '-tmp'); os.makedirs(T, exist_ok=True)
dur = lambda p: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))

PR = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pronuncias.json')))
def fon(t):
    for a, b in PR: t = t.replace(a, b)
    return t
async def tts(txt, p): await edge_tts.Communicate(fon(txt), 'pt-BR-AntonioNeural', rate='+4%').save(p)
partes, chips = [], []
vd0 = dur(os.path.join(BR, R['src']))
for i, (st, fala, letra) in enumerate(R['falas']):
    p = os.path.join(T, f'v{i}.mp3'); asyncio.run(tts(fala, p)); d = dur(p)
    nx = R['falas'][i+1][0] if i+1 < len(R['falas']) else vd0
    if st + d > nx: print('AVISO bloco maior que a cena:', i, fala, round(d,2), round(nx-st,2))
    partes.append((p, st)); chips.append((st, max(st + d + 0.3, min(nx - 0.1, st + 2.5)), letra))
t = st + d
vd = dur(os.path.join(BR, R['src']))
if t > vd: print('AVISO: narracao', t, '> video', vd)

def assinatura():
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    x, y = 64, 132
    d.ellipse((x, y+14, x+22, y+36), fill=REC)
    fr = f('geist-700.ttf', 46); d.text((x+38, y), 'real', font=fr, fill=BRANCO)
    d.text((x+38+d.textlength('real', font=fr), y), 'time', font=fr, fill=AZUL)
    d.text((x+40, y+58), R['tag'], font=f('geist-mono-500.ttf', 24), fill=BRANCO)
    return im

def chip(txt, final=False):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    ft = f('geist-700.ttf', 62); tw = d.textlength(txt, font=ft)
    x0, y0 = 64, 1130; x1 = x0 + tw + 96
    d.rounded_rectangle((x0, y0, x1, y0+118), 22, fill=GRAF + (232,))
    d.rectangle((x0, y0+22, x0+10, y0+96), fill=AZUL)
    d.text((x0+48, y0+22), txt, font=ft, fill=BRANCO)
    d.ellipse((x1-30, y0-8, x1-8, y0+14), fill=REC)
    if final:
        fm = f('geist-mono-500.ttf', 34)
        lab = 'WhatsApp (98) 99133-1727 · @realtime_fulljobs'
        lw = d.textlength(lab, font=fm)
        d.rounded_rectangle((x0, y0+140, x0+lw+60, y0+214), 18, fill=AZUL + (240,))
        d.text((x0+30, y0+156), lab, font=fm, fill=PRETO)
    return im

ins, flt = ['-i', os.path.join(BR, R['src'])], []
assinatura().save(os.path.join(T, 'sig.png')); ins += ['-loop','1','-i', os.path.join(T, 'sig.png')]
for i, (a, b, txt) in enumerate(chips):
    fin = i == len(chips) - 1
    if fin: b = vd
    chip(txt, fin).save(os.path.join(T, f'c{i}.png')); ins += ['-loop','1','-i', os.path.join(T, f'c{i}.png')]
base = '[0:v]scale=1080:1920,setsar=1[b0];[b0][1:v]overlay=0:0:shortest=1[b1]'
k = 1
for i, (a, b, _) in enumerate(chips):
    if i == len(chips) - 1: b = vd
    n = 2 + i
    base += f';[{n}:v]format=rgba,fade=in:st={a:.2f}:d=0.2:alpha=1,fade=out:st={max(a,b-0.2):.2f}:d=0.2:alpha=1[o{i}];[b{k}][o{i}]overlay=0:0:shortest=1[b{k+1}]'
    k += 1
na = 2 + len(chips)
for i, (p, st) in enumerate(partes):
    ins += ['-i', p]
    base += f';[{na+i}:a]adelay={int(st*1000)}|{int(st*1000)},volume=1.6[n{i}]'
base += ';' + ''.join(f'[n{i}]' for i in range(len(partes))) + f'amix=inputs={len(partes)}:normalize=0[voz]'
base += ';[voz]asplit[voz1][voz2];[0:a]volume=0.55[orig];[orig][voz1]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=300[duck]'
base += ';[duck][voz2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]'
outp = os.path.join(OUT, f'rt-{VID}.mp4')
cmd = ['ffmpeg','-nostdin','-y','-v','error'] + ins + ['-filter_complex', base, '-map', f'[b{k}]', '-map', '[a]',
       '-t', f'{vd:.3f}', '-c:v','libx264','-preset','medium','-crf','24','-maxrate','2600k','-bufsize','5200k',
       '-pix_fmt','yuv420p','-threads','2','-c:a','aac','-b:a','160k','-movflags','+faststart', outp]
subprocess.run(cmd, check=True)
# capa: quadro de 1,5 s + chip do gancho
cap = os.path.join(OUT, f'rt-{VID}-capa.jpg')
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-ss','1.5','-i',outp,'-frames:v','1',cap], check=True)
print('ok', outp, os.path.getsize(outp)//1024, 'KB', 'narr', round(t,1), 'video', round(vd,1))
