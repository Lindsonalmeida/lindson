# WF Celulares · 5 criativos de vídeo para a campanha nova (conta Pedro, 15/11/2026)
# Cena = foto de produto (ilustrativa) + manchete Inter + logo B; voz Antonio +4% por cena (sincronizada),
# punch-in (zoompan), flash branco no corte, whoosh, impacto no 0, trilha Mixkit com ducking, grão. Sem preço (campanha nova).
import os, json, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(D, '..'); S = os.path.join(W, 'video-processo', 'som'); T = os.path.join(D, 'tmp'); os.makedirs(T, exist_ok=True)
F = '/usr/share/fonts/opentype/inter/'; fb = lambda s: ImageFont.truetype(F + 'InterDisplay-Black.otf' if os.path.exists(F+'InterDisplay-Black.otf') else F+'Inter-ExtraBold.otf', s)
fm = lambda s: ImageFont.truetype(F + 'Inter-SemiBold.otf', s)
AZ, SI, CA, PR = (199,201,204), (199,201,204), (0,0,0), (142,138,132)
LUZ = (47,107,255)  # azul só como luz (identidade aprovada B: preto, grafite, titânio, prata, branco)
LOGO = Image.open(os.path.join(W, 'identidade/logo-b/wf-logo-b-branca.png')).convert('RGBA')
run = lambda a: subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)
dur = lambda f: float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
V = json.load(open(os.path.join(D, 'roteiros.json')))

def cover(p, w=1080, h=1920, fy=0.5):
    im = Image.open(os.path.join(W, p)).convert('RGB'); r = max(w/im.width, h/im.height)
    im = im.resize((int(im.width*r)+1, int(im.height*r)+1), Image.LANCZOS); x = (im.width-w)//2; y = int((im.height-h)*fy)
    return im.crop((x, y, x+w, y+h))

def quebra(d, txt, f, maxw):
    out = []
    for par in txt.split('\n'):
        l = ''
        for p in par.split():
            t = (l+' '+p).strip()
            if d.textlength(t, font=f) > maxw and l: out.append(l); l = p
            else: l = t
        out.append(l)
    return out

def cena(c, n, i, total):
    im = cover(c['img'], fy=c.get('fy', .5))
    g = Image.new('L', (1, 1920)); [g.putpixel((0, y), int(235*max(0, (y-700)/1220)**1.1)) for y in range(1920)]
    im = Image.composite(Image.new('RGB', im.size, CA), im, g.resize(im.size))
    top = Image.new('L', (1, 1920)); [top.putpixel((0, y), int(170*max(0, 1-y/520))) for y in range(1920)]
    im = Image.composite(Image.new('RGB', im.size, CA), im, top.resize(im.size)); d = ImageDraw.Draw(im)
    lg = LOGO.copy(); lg.thumbnail((190, 110)); im.paste(lg, (70, 300), lg)
    if c.get('tag'):
        f = fm(34); tw = d.textlength(c['tag'].upper(), font=f); d.rounded_rectangle((70, 1040, 70+tw+44, 1100), 30, fill=SI); d.text((92, 1051), c['tag'].upper(), font=f, fill=CA)
    sz = c.get('sz', 112); f = fb(sz); ls = quebra(d, c['txt'], f, 940); y = 1130
    for k, l in enumerate(ls):
        cor = AZ if c.get('az') and c['az'] in l else (255, 255, 255)
        d.text((70, y), l, font=f, fill=cor); y += int(sz*1.04)
    if c.get('sub'): d.text((70, y+18), c['sub'], font=fm(42), fill=PR)
    # barra de progresso (zona segura) e assinatura
    d.rectangle((70, 1590, 1010, 1596), fill=(60, 66, 80)); d.rectangle((70, 1590, 70+int(940*(i+1)/total), 1596), fill=LUZ)
    d.text((70, 1610), 'WF Celulares · São Cristóvão | Renascença', font=fm(30), fill=PR)
    p = os.path.join(T, f'{n}-{i}.png'); im.save(p); return p

for v in V:
    n = v['n']; partes = []; ini = []; t = 0
    if os.path.exists(os.path.join(D, f"wf-criativo-{n:02d}-{v['slug']}.mp4")) and '-f' not in sys.argv: continue
    for i, c in enumerate(v['cenas']):
        a = os.path.join(T, f'{n}-{i}.mp3')
        if not os.path.exists(a): subprocess.run(['edge-tts', '--voice', 'pt-BR-AntonioNeural', '--rate', '+4%', '--text', c['voz'], '--write-media', a] + (['--proxy', os.environ['HTTPS_PROXY']] if os.environ.get('HTTPS_PROXY') else []), check=True, env={**os.environ, 'SSL_CERT_FILE': '/root/.ccr/ca-bundle.crt'})
        dd = round(dur(a) + .22, 2); png = cena(c, n, i, len(v['cenas'])); fr = int(dd*30)
        clip = os.path.join(T, f'{n}-{i}.mp4'); z = '1.0+0.10*on/%d' % fr if i % 2 == 0 else '1.10-0.08*on/%d' % fr
        run(['-loop', '1', '-i', png, '-vf', f"scale=2160:-1,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps=30,fade=in:st=0:d=0.12:color=white,format=yuv420p", '-frames:v', str(fr), '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', clip])
        partes.append((clip, a, dd)); ini.append(t); t += dd
    lst = os.path.join(T, f'{n}.txt'); open(lst, 'w').write(''.join(f"file '{p[0]}'\n" for p in partes))
    ins = ['-f', 'concat', '-safe', '0', '-i', lst]; fc = []; mix = []
    for i, (_, a, _) in enumerate(partes):
        ins += ['-i', a]; fc.append(f"[{i+1}:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay={int(ini[i]*1000)}|{int(ini[i]*1000)}[v{i}]"); mix.append(f'[v{i}]')
    k = len(partes)+1
    fc.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0,asplit[vz1][vz2]")
    ins += ['-i', os.path.join(S, 'trilha.mp3'), '-i', os.path.join(S, 'impacto.mp3')]
    fc.append(f"[{k}:a]atrim=start={20+n*23},asetpts=PTS-STARTPTS,atrim=0:{t},volume=0.4,afade=t=out:st={t-0.8}:d=0.8,aformat=sample_rates=44100:channel_layouts=stereo[tr]")
    fc.append("[tr][vz2]sidechaincompress=threshold=0.03:ratio=8:attack=15:release=250[trd]"); fc.append(f"[{k+1}:a]volume=0.8,aformat=sample_rates=44100:channel_layouts=stereo[im]")
    mm = ['[vz1]', '[trd]', '[im]']
    for i in range(1, len(partes)):
        ins += ['-i', os.path.join(S, 'whoosh.mp3')]; ms = int(max(0, ini[i]-.12)*1000)
        fc.append(f"[{k+1+i}:a]volume=0.35,adelay={ms}|{ms},aformat=sample_rates=44100:channel_layouts=stereo[w{i}]"); mm.append(f'[w{i}]')
    fc.append(''.join(mm) + f"amix=inputs={len(mm)}:normalize=0,atrim=0:{t},loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    fc.append("[0:v]noise=alls=5:allf=t,format=yuv420p[v]")
    out = os.path.join(D, f"wf-criativo-{n:02d}-{v['slug']}.mp4")
    run(ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-t', str(t), '-c:v', 'libx264', '-crf', '24', '-preset', 'medium', '-maxrate', '5M', '-bufsize', '10M', '-c:a', 'aac', '-b:a', '160k', '-ar', '44100', '-movflags', '+faststart', out])
    run(['-ss', '0.5', '-i', out, '-frames:v', '1', '-q:v', '3', os.path.join(D, f'capa-{n:02d}.jpg')])
    print('ok', out, round(t, 1), 's', os.path.getsize(out)//1024, 'KB', flush=True)
