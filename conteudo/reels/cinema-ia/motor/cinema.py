# Motor "Cinema IA" (conta Leandro, 21/11/2026)
# Cena gerada no Gemini (rosto do Lindson) -> plano de cinema 9:16:
# parallax 2.5D em 2 camadas (recorte rembg + fundo reconstruído por inpaint), push-in/pan/pull,
# luz volumétrica com ruído, poeira em profundidade, flare anamórfico, grão, vinheta,
# whip pan e zoom punch nos cortes, Anton gigante com UMA palavra neon com glow entrando no tempo da fala,
# legenda palavra por palavra (Whisper), assinatura LINDSON ALMEIDA, SFX em cada corte, -14 LUFS.
# Uso: python3 cinema.py plano.json saida.mp4   (o plano aponta imagens, máscaras, voz e palavras do Whisper)
import json, sys, os, subprocess, math, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
AQUI = os.path.dirname(os.path.abspath(__file__))
ANTON = os.path.join(AQUI, 'Anton.ttf')
INTER = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
if not os.path.exists(INTER): INTER = ANTON
rng = np.random.default_rng(7)

def ease(u): return u * u * (3 - 2 * u)
def eout(u): return 1 - (1 - u) ** 3

def prep(c):
    im = cv2.cvtColor(cv2.imread(c['img']), cv2.COLOR_BGR2RGB).astype(np.float32) / 255
    s = W * 1.12 / im.shape[1]                                   # margem de 12 % para o movimento
    im = cv2.resize(im, (round(im.shape[1] * s), round(im.shape[0] * s)), interpolation=cv2.INTER_AREA)
    m = cv2.imread(c['mask'], 0); m = cv2.resize(m, (im.shape[1], im.shape[0])).astype(np.float32) / 255
    m = cv2.GaussianBlur(m, (0, 0), 1.6)
    # fundo sem a pessoa: inpaint em resolução baixa, depois sobe
    sm = 0.25; small = cv2.resize((im * 255).astype(np.uint8), None, fx=sm, fy=sm)
    hole = cv2.dilate((cv2.resize(m, (small.shape[1], small.shape[0])) > 0.1).astype(np.uint8) * 255, np.ones((9, 9), np.uint8))
    bgs = cv2.inpaint(small, hole, 6, cv2.INPAINT_TELEA)
    bgs = cv2.GaussianBlur(bgs, (0, 0), 3)
    bg = cv2.resize(bgs, (im.shape[1], im.shape[0])).astype(np.float32) / 255
    bg = np.where(m[..., None] > 0.05, bg, im)
    return dict(fg=im, a=m, bg=bg)

def warp(img, s, ax, ay, dx, dy, border=cv2.BORDER_REFLECT):
    # escala s em torno do ponto (ax, ay) da imagem, que vai parar no centro de enquadramento + (dx, dy)
    cx, cy = W * c_anchor[0], H * c_anchor[1]
    M = np.float32([[s, 0, cx - s * ax + dx], [0, s, cy - s * ay + dy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=border)

def texto(txt, font, size, track=0):
    f = ImageFont.truetype(font, size)
    ws = [f.getbbox(ch)[2] for ch in txt]
    w = sum(ws) + track * (len(txt) - 1); h = f.getbbox('ÁgH')[3] + 20
    im = Image.new('L', (int(w) + 40, h + 20)); d = ImageDraw.Draw(im); x = 20
    for ch, cw in zip(txt, ws): d.text((x, 10), ch, font=f, fill=255); x += cw + track
    return np.asarray(im).astype(np.float32) / 255

def cola(base, alpha, cor, x, y, op=1.0):
    h, w = alpha.shape; x0, y0 = int(x), int(y)
    xa, ya = max(0, -x0), max(0, -y0); xb, yb = min(w, W - x0), min(h, H - y0)
    if xb <= xa or yb <= ya: return
    a = alpha[ya:yb, xa:xb, None] * op
    reg = base[y0 + ya:y0 + yb, x0 + xa:x0 + xb]
    reg[:] = reg * (1 - a) + np.array(cor, np.float32) * a

def soma(base, alpha, cor, x, y, op=1.0):
    h, w = alpha.shape; x0, y0 = int(x), int(y)
    xa, ya = max(0, -x0), max(0, -y0); xb, yb = min(w, W - x0), min(h, H - y0)
    if xb <= xa or yb <= ya: return
    base[y0 + ya:y0 + yb, x0 + xa:x0 + xb] += alpha[ya:yb, xa:xb, None] * np.array(cor, np.float32) * op

def main(plano, saida):
    global c_anchor
    P = json.load(open(plano)); B = os.path.dirname(os.path.abspath(plano))
    pj = lambda p: p if os.path.isabs(p) else os.path.join(B, p)
    voz = pj(P['voz']); words = json.load(open(pj(P['whisper'])))
    total = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', voz]))
    cenas = P['cenas']
    for i, c in enumerate(cenas):
        c['img'] = pj(c['img']); c['mask'] = pj(c['mask'])
        c['t1'] = cenas[i + 1]['t0'] if i + 1 < len(cenas) else total
    cache = {}
    # legenda: palavras do roteiro, com o tempo do Whisper dentro de cada fala
    leg = []
    for c in cenas:
        wsp = [w for w in words if c['t0'] - 0.05 <= w[1] < c['t1'] - 0.05]
        sw = c['fala'].split()
        for k, t in enumerate(sw):
            j = min(len(wsp) - 1, int(k * len(wsp) / len(sw)))
            leg.append((t, wsp[j][1] if wsp else c['t0'] + k * 0.3))
    grupos = [leg[i:i + 3] for i in range(0, len(leg), 3)]
    # títulos
    tit = []
    for c in cenas:
        l1 = texto(c['l1'], ANTON, 118, 4) if c.get('l1') else None
        if l1 is not None and l1.shape[1] > 990: l1 = cv2.resize(l1, None, fx=990 / l1.shape[1], fy=990 / l1.shape[1], interpolation=cv2.INTER_AREA)
        l2 = texto(c['l2'], ANTON, c.get('tam', 300), 2)
        if l2.shape[1] > 1010: l2 = cv2.resize(l2, None, fx=1010 / l2.shape[1], fy=1010 / l2.shape[1], interpolation=cv2.INTER_AREA)
        glow = cv2.GaussianBlur(l2, (0, 0), 22) * 1.6 + cv2.GaussianBlur(l2, (0, 0), 6) * 0.8
        tit.append((l1, l2, glow))
    assin = texto('LINDSON ALMEIDA', INTER, 30, 9)
    # poeira (x, y, z, fase)
    N = 160; pz = rng.uniform(0.2, 1, N); px = rng.uniform(0, W, N); py = rng.uniform(0, H, N); ph = rng.uniform(0, 6.28, N)
    dot = {r: cv2.GaussianBlur(np.pad(np.ones((1, 1), np.float32), r * 2), (0, 0), r / 2.2) for r in (2, 3, 4, 6, 9)}
    for r in dot: dot[r] /= dot[r].max()
    grao = [rng.normal(0, 1, (H // 2, W // 2)).astype(np.float32) for _ in range(6)]
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    vin = np.clip(1 - 0.55 * (((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H * 0.45) / (H * 0.7)) ** 2), 0.25, 1)[..., None]
    baixo = np.clip((yy - H * 0.5) / (H * 0.42), 0, 1)[..., None] ** 1.4 * 0.82   # terço inferior escuro p/ tipografia
    ruido = cv2.resize(rng.random((24, 14)).astype(np.float32), (W, H * 2), interpolation=cv2.INTER_CUBIC)
    nfr = int(total * FPS) + 1
    os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                           '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', saida + '.video.mp4'], stdin=subprocess.PIPE)
    cortes = [c['t0'] for c in cenas[1:]]
    teste = [int(float(x) * FPS) for x in os.environ.get('QUADROS', '').split(',') if x]
    for f in (teste or range(nfr)):
        t = f / FPS
        k = max(i for i, c in enumerate(cenas) if c['t0'] <= t + 1e-6); c = cenas[k]
        if c['img'] + c['mask'] not in cache: cache[c['img'] + c['mask']] = prep(c)
        L = cache[c['img'] + c['mask']]
        u = (t - c['t0']) / (c['t1'] - c['t0']); e = ease(u)
        c_anchor = c.get('quadro', [0.5, 0.42])
        ax, ay = c['foco'][0] * L['fg'].shape[1], c['foco'][1] * L['fg'].shape[0]
        mv = c.get('mov', 'push'); s0 = c.get('esc', 0.9)
        if mv == 'push': sb, sf, dx, dy = s0 * (1 + 0.04 * e), s0 * (1 + 0.075 * e), 0, 0
        elif mv == 'pull': sb, sf, dx, dy = s0 * (1.05 - 0.04 * e), s0 * (1.08 - 0.07 * e), 0, 0
        elif mv == 'panl': sb, sf, dx, dy = s0 * 1.03, s0 * 1.05, 30 - 60 * e, 0
        elif mv == 'panr': sb, sf, dx, dy = s0 * 1.03, s0 * 1.05, -30 + 60 * e, 0
        else: sb, sf, dx, dy = s0 * (1 + 0.03 * e), s0 * (1 + 0.05 * e), 0, 20 - 40 * e
        # zoom punch logo depois do corte
        tc = t - c['t0']; tr = c.get('trans', 'whip')
        if k > 0 and tr == 'punch' and tc < 0.3: p = 1 + 0.22 * (1 - eout(tc / 0.3)); sb *= p; sf *= p
        bgw = warp(L['bg'], sb, ax, ay, dx * 0.5, dy * 0.5)
        fgw = warp(L['fg'], sf, ax, ay, dx * 1.4, dy * 1.4)
        aw = warp(L['a'], sf, ax, ay, dx * 1.4, dy * 1.4, cv2.BORDER_CONSTANT)[..., None]
        fr = bgw * (1 - aw) + fgw * aw
        # luz volumétrica: cone a partir da fonte de luz da cena, com ruído que corre
        lx, ly = c.get('luz', [0.85, 0.05]); lx *= W; ly *= H
        ang = np.arctan2(yy - ly, xx - lx); dirc = math.atan2(H * 0.55 - ly, W * 0.45 - lx)
        cone = np.clip(1 - np.abs(np.angle(np.exp(1j * (ang - dirc)))) / 0.32, 0, 1) ** 1.6
        dist = np.sqrt((xx - lx) ** 2 + (yy - ly) ** 2) / H
        n = ruido[int(t * 40) % H: int(t * 40) % H + H]
        beam = cone * np.exp(-dist * 1.7) * (0.55 + 0.45 * n) * (0.92 + 0.08 * math.sin(t * 9))
        cor_luz = np.array(c.get('cor_luz', [1.0, 0.86, 0.66]), np.float32)
        fr = fr + beam[..., None] * cor_luz * c.get('forca_luz', 0.32) * (1 - 0.6 * aw)
        # poeira em profundidade (mais brilhante dentro do feixe)
        poe = np.zeros((H, W), np.float32)
        for i in range(N):
            x = (px[i] + t * 18 * pz[i] + math.sin(t * 0.7 + ph[i]) * 25) % W
            y = (py[i] - t * 30 * pz[i]) % H
            r = (2, 3, 4, 6, 9)[min(4, int(pz[i] * 5))]; d = dot[r]; h_ = d.shape[0]
            x0, y0 = int(x) - h_ // 2, int(y) - h_ // 2
            if 0 <= x0 < W - h_ and 0 <= y0 < H - h_:
                poe[y0:y0 + h_, x0:x0 + h_] += d * (0.15 + 0.85 * beam[int(y), int(x)] * 2.2) * (0.35 if pz[i] > 0.8 else 0.6)
        fr = fr + np.clip(poe, 0, 1)[..., None] * cor_luz * 0.55
        # flare anamórfico na fonte de luz
        fl = np.exp(-((yy - ly) / 7) ** 2) * np.exp(-np.abs(xx - lx) / 420) * (0.75 + 0.25 * math.sin(t * 5))
        fr = fr + fl[..., None] * np.array([0.55, 0.75, 1.0], np.float32) * 0.35
        # grade: pretos profundos, contraste, leve teal nas sombras
        fr = np.clip(fr, 0, 1); lum = fr.mean(2, keepdims=True)
        fr = fr + (0.5 - lum) * 0 + np.where(lum < 0.3, 1, 0) * np.array([-0.012, 0.004, 0.018], np.float32)
        fr = np.clip((fr - 0.035) / 0.965, 0, 1) ** 1.08
        fr = fr * vin; fr = fr * (1 - baixo)
        # título: linha 1 branca + palavra neon (entra quando a palavra é dita)
        l1, l2, glow = tit[k]; tn = c.get('t_neon', c['t0'] + 0.15)
        ty = c.get('ty', 1150)
        if l1 is not None:
            a1 = eout(min(1, max(0, (t - c['t0'] - 0.05) / 0.25)))
            cola(fr, l1, (1, 1, 1), (W - l1.shape[1]) / 2, ty - l1.shape[0] + 12 + 30 * (1 - a1), a1)
        a2 = min(1, max(0, (t - tn) / 0.18))
        if a2 > 0:
            sc = 1 + 0.35 * (1 - eout(a2))
            g2 = cv2.resize(glow, None, fx=sc, fy=sc); t2 = cv2.resize(l2, None, fx=sc, fy=sc)
            neon = np.array(c.get('neon', [0.85, 1.0, 0.15]), np.float32)
            pis = 0.9 + 0.1 * math.sin(t * 23) * (1 if (t - tn) < 0.6 else 0.2)
            xg, yg = (W - g2.shape[1]) / 2, ty - 10 + (l2.shape[0] - g2.shape[0]) / 2
            soma(fr, g2, neon, xg, yg, 0.42 * a2 * pis)
            cola(fr, t2, neon * 0.8 + 0.2, (W - t2.shape[1]) / 2, ty - 10 + (l2.shape[0] - t2.shape[0]) / 2, a2)
        # legenda palavra por palavra
        gi = max([i for i, g in enumerate(grupos) if g[0][1] <= t + 0.02] or [0]); g = grupos[gi]
        if t < g[-1][1] + 1.2:
            fs = 56; fnt = ImageFont.truetype(INTER, fs)
            pal = [w for w, _ in g]; wid = [fnt.getbbox(w)[2] for w in pal]; esp = 16
            x = (W - sum(wid) - esp * (len(pal) - 1)) / 2; yl = c.get('yl', 1610)
            for (wtxt, ts), wd in zip(g, wid):
                if ts > t + 0.02: x += wd + esp; continue
                m = texto(wtxt, INTER, fs); ativo = (ts <= t) and (gi + 1 >= len(grupos) or True) and all(not (ts < ts2 <= t) for _, ts2 in g)
                cola(fr, cv2.GaussianBlur(m, (0, 0), 4), (0, 0, 0), x - 20, yl - 8, 0.7)
                cola(fr, m, (0.85, 1.0, 0.15) if ativo else (1, 1, 1), x - 20, yl - 10)
                x += wd + esp
        # assinatura
        cola(fr, assin, (1, 1, 1), (W - assin.shape[1]) / 2, 96, 0.78)
        # grão
        gr = cv2.resize(grao[f % 6], (W, H), interpolation=cv2.INTER_NEAREST)[..., None]
        fr = np.clip(fr + gr * 0.028, 0, 1)
        # whip pan: borrão horizontal e deslocamento em volta do corte
        for tc0 in cortes:
            d = t - tc0; idx = cortes.index(tc0) + 1
            if abs(d) < 0.2 and cenas[idx].get('trans', 'whip') == 'whip':
                q = 1 - abs(d) / 0.2; desl = int((1 if d < 0 else -1) * q * q * 260)
                fr = np.roll(fr, -desl, axis=1)
                kl = int(9 + q * 120) | 1; ker = np.ones((1, kl), np.float32) / kl
                fr = cv2.filter2D(fr, -1, ker); fr = fr + q * 0.18
            if 0 <= d < 0.1 and cenas[idx].get('trans') == 'punch':
                fr = fr + (1 - d / 0.1) * 0.6
                sh = 14; fr[..., 0] = np.roll(fr[..., 0], sh, 1); fr[..., 2] = np.roll(fr[..., 2], -sh, 1)
        if teste: Image.fromarray((np.clip(fr, 0, 1) * 255).astype(np.uint8)).save(f'{saida}.q{f:05d}.jpg', quality=88); continue
        ff.stdin.write((np.clip(fr, 0, 1) * 255).astype(np.uint8).tobytes())
        if f % 150 == 0: print('quadro', f, '/', nfr, flush=True)
    ff.stdin.close(); ff.wait()
    if teste: return
    # áudio: voz + SFX em cada corte, -14 LUFS
    sfx = P.get('sfx', {}); ins = ['-i', saida + '.video.mp4', '-i', voz]; fil = []; lab = ['[1:a]']
    for j, tc0 in enumerate(cortes):
        nome = sfx.get(cenas[j + 1].get('trans', 'whip'))
        if not nome: continue
        ins += ['-i', pj(nome)]; n = len(ins) // 2 - 1; atraso = max(0, int((tc0 - 0.18) * 1000))
        fil.append(f'[{n}:a]volume={P.get("vol_sfx", 0.45)},adelay={atraso}|{atraso}[s{j}]'); lab.append(f'[s{j}]')
    fil.append(''.join(lab) + f'amix=inputs={len(lab)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fil), '-map', '0:v', '-map', '[a]',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '44100', '-shortest', '-movflags', '+faststart', saida], check=True)
    os.remove(saida + '.video.mp4')

if __name__ == '__main__':
    c_anchor = [0.5, 0.42]
    main(sys.argv[1], sys.argv[2])
