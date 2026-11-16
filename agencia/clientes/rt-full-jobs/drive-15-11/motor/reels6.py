"""6 Reels novos da Real Time a partir dos crus (conta Zuleide, 16/11/2026).
Cada bloco de voz = uma cena (video cru, foto com push-in ou cartao de texto). Identidade v1
(Geist, Preto Set, Azul Real, ponto REC), voz Antonio +4%, trilha Mixkit com ducking forte, whoosh nos cortes,
flash leve e push-in (VFX). Um ffmpeg por vez.
Uso: python3 -I reels6.py <crus> <saida> <fontes> <sfx/trilha banco> <id> [blocos a regerar,...]"""
import json, os, subprocess, sys, asyncio, glob, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import certifi
if os.path.exists('/root/.ccr/ca-bundle.crt'): certifi.where = lambda: '/root/.ccr/ca-bundle.crt'
import edge_tts
CR, OUT, FT, BANCO, VID = sys.argv[1:6]
AQUI = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(AQUI, 'roteiros6.json')))[VID]
PR = json.load(open(os.path.join(AQUI, 'pronuncias.json')))
W, H, FPS = 1080, 1920, 30
PRETO, BRANCO, AZUL, REC, GRAF = (5,7,11), (244,247,251), (46,155,255), (255,59,59), (17,22,31)
f = lambda n, s: ImageFont.truetype(os.path.join(FT, n), s)
T = os.path.join(OUT, VID + '-tmp'); os.makedirs(T, exist_ok=True)
dur = lambda p: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
VS = sorted(glob.glob(os.path.join(CR, '*.mp4'))); FS = sorted(glob.glob(os.path.join(CR, '*.jpeg')))
def src(k): return VS[int(k[1:])-1] if k[0] == 'V' else FS[int(k[1:])-1]
def fon(t):
    for a, b in PR: t = t.replace(a, b)
    return t
async def tts(txt, p): await edge_tts.Communicate(fon(txt), 'pt-BR-AntonioNeural', rate='+4%').save(p)
def run(c): subprocess.run(['ffmpeg','-nostdin','-y','-v','error'] + c, check=True)

def quebra(d, txt, ft, maxw):
    ls, cur = [], ''
    for w in txt.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=ft) > maxw and cur: ls.append(cur); cur = w
        else: cur = t
    return ls + [cur]

def overlay(i, letra, gancho, final):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    x, y = 64, 132
    d.ellipse((x, y+14, x+22, y+36), fill=REC)
    fr = f('geist-700.ttf', 46); d.text((x+38, y), 'real', font=fr, fill=BRANCO)
    d.text((x+38+d.textlength('real', font=fr), y), 'time', font=fr, fill=AZUL)
    d.text((x+40, y+58), R['tag'], font=f('geist-mono-500.ttf', 24), fill=BRANCO)
    if gancho:   # gancho grande no alto nos 2 primeiros segundos
        ft = f('geist-700.ttf', 92); ls = quebra(d, letra, ft, W-160); y0 = 300
        for l in ls:
            tw = d.textlength(l, font=ft)
            d.rounded_rectangle((60, y0, 60+tw+64, y0+124), 20, fill=GRAF+(235,)); d.rectangle((60, y0+24, 70, y0+100), fill=AZUL)
            d.text((96, y0+14), l, font=ft, fill=BRANCO); y0 += 138
        d.ellipse((60+tw+40, 286, 60+tw+64, 310), fill=REC)
    else:
        ft = f('geist-700.ttf', 62); ls = quebra(d, letra, ft, W-240); y0 = 1130
        for l in ls:
            tw = d.textlength(l, font=ft); x1 = 64+tw+96
            d.rounded_rectangle((64, y0, x1, y0+118), 22, fill=GRAF+(232,)); d.rectangle((64, y0+22, 74, y0+96), fill=AZUL)
            d.text((112, y0+22), l, font=ft, fill=BRANCO); y0 += 132
        d.ellipse((x1-30, 1122, x1-8, 1144), fill=REC)
    if final:
        fm = f('geist-mono-500.ttf', 34); lab = 'WhatsApp (98) 99133-1727 · @realtime_fulljobs'
        lw = d.textlength(lab, font=fm); y0 += 10
        d.rounded_rectangle((64, y0, 64+lw+60, y0+74), 18, fill=AZUL+(240,)); d.text((94, y0+16), lab, font=fm, fill=PRETO)
    p = os.path.join(T, f'o{i}.png'); im.save(p); return p

def cartao(i, txt):
    im = Image.new('RGB', (W, H), GRAF); d = ImageDraw.Draw(im)
    for yy in range(0, H, 6): d.line((0, yy, W, yy), fill=(20,26,36))
    fm = f('geist-mono-700.ttf', 40); d.text((96, 640), 'NO CELULAR', font=fm, fill=REC)
    ft = f('geist-700.ttf', 96); y0 = 720
    for l in quebra(d, txt, ft, W-200): d.text((96, y0), l, font=ft, fill=BRANCO); y0 += 116
    p = os.path.join(T, f'k{i}.png'); im.save(p); return p

def cena(i, vis, D, ov, outp):
    fl = f'fade=in:st=0:d=0.14:color=white,fps={FPS},format=yuv420p'
    if vis.startswith('CARD:'):
        img = cartao(i, vis[5:])
        run(['-loop','1','-t',f'{D:.3f}','-i',img,'-loop','1','-t',f'{D:.3f}','-i',ov,'-filter_complex',
             f"[0:v]scale=w='1080*(1+0.04*t/{D:.2f})':h=-2:eval=frame,crop=1080:1920,setsar=1[b];[b][1:v]overlay=0:0,{fl}[v]",
             '-map','[v]','-t',f'{D:.3f}','-c:v','libx264','-preset','veryfast','-crf','18','-threads','2',outp]); return
    k, *ss = vis.split('@'); s = src(k); st = float(ss[0]) if ss else 0
    zoom = f"scale=w='1188*(1+0.06*t/{D:.2f})':h=-2:eval=frame,crop=1080:1920"
    if k[0] == 'V':
        vd = dur(s); ins = ['-stream_loop','-1','-ss',f'{min(st, max(0, vd-0.5)):.2f}','-i',s]
        g = f"[0:v]scale=1188:2112:force_original_aspect_ratio=increase,crop=1188:2112,{zoom},setsar=1,eq=contrast=1.06:saturation=1.08[b]"
    else:
        iw, ih = Image.open(s).size; ins = ['-loop','1','-t',f'{D:.3f}','-i',s]
        if iw / ih > 0.7:   # paisagem: fundo desfocado + foto inteira com push-in
            g = (f"[0:v]split[a][c];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.12[bg];"
                 f"[c]scale=w='1080*(1+0.08*t/{D:.2f})':h=-2:eval=frame[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2-80,setsar=1[b]")
        else:
            g = f"[0:v]scale=1188:2112:force_original_aspect_ratio=increase,crop=1188:2112,{zoom},setsar=1[b]"
    run(ins + ['-loop','1','-t',f'{D:.3f}','-i',ov,'-filter_complex', g + f";[b][1:v]overlay=0:0,{fl}[v]",
         '-map','[v]','-t',f'{D:.3f}','-an','-c:v','libx264','-preset','veryfast','-crf','18','-threads','2',outp])

regerar = set(sys.argv[6].split(',')) if len(sys.argv) > 6 else None
B = R['blocos']; cenas, vozes, t0 = [], [], 0.0
for i, b in enumerate(B):
    pv = os.path.join(T, f'v{i}.mp3')
    if not os.path.exists(pv) or (regerar and str(i) in regerar): asyncio.run(tts(b['fala'], pv))
    D = round(dur(pv) + (0.55 if i == len(B)-1 else 0.32), 3)
    if i == len(B)-1: D += 1.2
    ov = overlay(i, b['letra'], i == 0, i == len(B)-1)
    pc = os.path.join(T, f'c{i}.mp4'); cena(i, b['vis'], D, ov, pc)
    cenas.append(pc); vozes.append((pv, t0 + 0.08)); t0 += D
total = t0
lst = os.path.join(T, 'l.txt'); open(lst, 'w').write(''.join(f"file '{c}'\n" for c in cenas))
sfx = os.path.join(BANCO, 'sfx'); tri = os.path.join(BANCO, 'trilha', R['trilha'])
ins = ['-f','concat','-safe','0','-i',lst,'-stream_loop','-1','-i',tri]
fc = f"[1:a]atrim=0:{total:.2f},volume=0.30,afade=in:d=0.6,afade=out:st={total-1.4:.2f}:d=1.4[mus]"
n = 2; vz = []
for j, (p, st) in enumerate(vozes):
    ins += ['-i', p]; fc += f";[{n}:a]adelay={int(st*1000)}|{int(st*1000)},volume=1.7[n{j}]"; vz.append(f'[n{j}]'); n += 1
cortes, acc = [], 0.0
for c in cenas[:-1]: acc += dur(c); cortes.append(acc)
sf = []
for j, ct in enumerate(cortes):
    nome = 'whoosh-rapido.mp3' if j % 2 else 'whoosh-cinematico.mp3'
    ins += ['-i', os.path.join(sfx, nome)]; d0 = max(0, int((ct-0.25)*1000))
    fc += f";[{n}:a]adelay={d0}|{d0},volume=0.45[s{j}]"; sf.append(f'[s{j}]'); n += 1
ins += ['-i', os.path.join(sfx, 'impacto-intro.mp3')]; fc += f";[{n}:a]volume=0.5[si]"; sf.append('[si]'); n += 1
fc += f";{''.join(vz)}amix=inputs={len(vz)}:normalize=0[voz];[voz]asplit[v1][v2]"
fc += ";[mus][v1]sidechaincompress=threshold=0.012:ratio=20:attack=8:release=400:makeup=1[duck]"
fc += f";[duck][v2]{''.join(sf)}amix=inputs={2+len(sf)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
outp = os.path.join(OUT, f'rt-{VID}.mp4')
for crf in (24, 27, 30):
    run(ins + ['-filter_complex', fc, '-map','0:v','-map','[a]','-t',f'{total:.3f}','-c:v','libx264','-preset','medium',
               '-crf',str(crf),'-maxrate','2400k','-bufsize','4800k','-pix_fmt','yuv420p','-threads','2','-c:a','aac','-b:a','160k',
               '-movflags','+faststart', outp])
    if os.path.getsize(outp) < 10*1024*1024: break
cap = os.path.join(OUT, f'rt-{VID}-capa.jpg')
run(['-ss','1.2','-i',outp,'-frames:v','1','-q:v','3',cap])
for c in cenas: os.remove(c)
print('ok', outp, os.path.getsize(outp)//1024, 'KB', round(total, 1), 's')
