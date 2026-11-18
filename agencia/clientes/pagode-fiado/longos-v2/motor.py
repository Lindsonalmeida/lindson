# Motor dos vídeos longos do Pagode Fiado v2 (sessão GOMINHO, conta Pedro, 18/11/2026).
# "Ao vivo no Bar do Seu Tião": fotos de referência dos personagens com profundidade 3D (Depth Anything V2),
# letra em karaokê na tira do caderno do fiado, quadro-negro de abertura, retrato em polaroide, luz vazando nos cortes.
# O áudio é a faixa APROVADA copiada sem recodificar (nada é somado por cima da música).
# Uso: python3 motor.py <faixa> <pasta_trabalho> [PREVIA=1 -> 640x360, 12 fps]
import json, sys, os, subprocess, math, zlib
import numpy as np, cv2
cv2.setNumThreads(1)
K, WK = sys.argv[1], sys.argv[2]; AQUI = os.path.dirname(os.path.abspath(__file__))
PREVIA = os.environ.get('PREVIA') == '1'
L = json.load(open(AQUI + '/letras.json'))[K]
TEMPOS = json.load(open(f'{WK}/audio/{K}.tempos.json'))
CAM = f'{WK}/cam{K}'; CX = json.load(open(CAM + '/caixas.json')); TIRAS = json.load(open(CAM + '/tiras.json'))
FPS = 12 if PREVIA else 30; SW, SH = (640, 360) if PREVIA else (1920, 1080); ESC = SW / 1920
AUD = f'{WK}/audio/{K}.mp3'
DUR = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', AUD], capture_output=True, text=True).stdout)
rng = np.random.default_rng(zlib.crc32(K.encode()))
# ---------------------------------------------------------------- imagens
IMG = {'davi': ('01-davi-lua.png', (0, 0, 690, 1024)), 'neguinho': ('02-neguinho-do-cavaco.png', None), 'rafa': ('03-rafa-tanta.png', None),
       'juninho': ('04-juninho-banjo.png', None), 'ze': ('05-mestre-ze-pandeiro.png', None), 'bia': ('06-bia-rebolo.png', None),
       'tiao': ('07-seu-tiao.png', None), 'copo': ('capa-album-copo-americano-3000.jpg', None), 'bar': ('capa-youtube-pagode-fiado.jpg', None)}
# enquadramentos (coordenadas da imagem original): centro x, centro y, largura do recorte 16:9
FR = {'davi': {'rosto': (345, 430, 690)},
      'neguinho': {'rosto': (490, 400, 1024), 'medio': (520, 470, 1024), 'close': (470, 330, 840)},
      'rafa': {'rosto': (540, 420, 1024), 'medio': (520, 480, 1024), 'close': (545, 330, 840)},
      'juninho': {'rosto': (520, 380, 1024), 'medio': (540, 470, 1024), 'close': (530, 290, 840)},
      'ze': {'rosto': (512, 410, 1024), 'medio': (540, 480, 1024), 'close': (480, 300, 840)},
      'bia': {'rosto': (520, 420, 1024), 'close': (520, 330, 840)},
      'tiao': {'rosto': (512, 420, 1024), 'close': (510, 310, 840), 'quadro': (834, 290, 380)},
      'copo': {'mesa': (1500, 1900, 2900), 'copo': (700, 1250, 1500), 'caderno': (1640, 1320, 1550), 'titulo': (1500, 820, 2900)},
      'bar': {'geral': (1280, 720, 2560), 'esq': (540, 760, 1060), 'dir': (2010, 800, 1060)}}
TOPO = {'davi': 150, 'neguinho': 40, 'rafa': 10, 'juninho': 45, 'ze': 10, 'bia': 80, 'tiao': 115}
CARD = {'davi': (0, 0, 690, 1024), 'neguinho': (150, 40, 950, 1024), 'rafa': (150, 0, 950, 984), 'juninho': (130, 20, 930, 1004),
        'ze': (110, 0, 910, 984), 'bia': (130, 40, 930, 1024), 'tiao': (100, 40, 900, 1024)}
GENTE = ['davi', 'neguinho', 'rafa', 'juninho', 'ze', 'bia', 'tiao']
INSTR = {'neguinho': 'medio', 'rafa': 'medio', 'juninho': 'medio', 'ze': 'medio', 'bia': 'rosto', 'tiao': 'quadro', 'davi': 'rosto', 'copo': 'copo', 'bar': 'esq'}
_cache = {}
def carrega(n):
    if n in _cache: return _cache[n]
    arq, reg = IMG[n]; im = cv2.imread(f'{WK}/img/{arq}')[:, :, ::-1]; dp = cv2.imread(f'{WK}/prof/{arq.rsplit(".", 1)[0]}.png', 0)
    if n == 'davi':
        mk = np.zeros(im.shape[:2], np.uint8); mk[438:466, 560:614] = 255
        im = np.ascontiguousarray(cv2.inpaint(np.ascontiguousarray(im[:, :, ::-1]), mk, 7, cv2.INPAINT_TELEA)[:, :, ::-1])
    if reg: x0, y0, x1, y1 = reg; im = im[y0:y1, x0:x1]; dp = dp[y0:y1, x0:x1]
    f = 2.0 if im.shape[1] <= 1100 else 1.0
    if f != 1.0:
        im = cv2.resize(im, None, fx=f, fy=f, interpolation=cv2.INTER_LANCZOS4)
        bl = cv2.GaussianBlur(im, (0, 0), 1.4); im = cv2.addWeighted(im, 1.45, bl, -.45, 0)
    dp = cv2.resize(dp, (im.shape[1], im.shape[0]), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
    # cor da marca: sombras puxando para o verde azulejo, luz âmbar, um pouco mais de contraste
    a = im.astype(np.float32) / 255; lum = a.mean(2, keepdims=True)
    a = a * (1 - .10) + lum * .10
    a = a + (np.array([.02, .045, .035]) * (1 - lum) - np.array([0, .01, .04]) * lum)
    a = np.clip((a - .5) * 1.06 + .5, 0, 1)
    r = dict(im=np.ascontiguousarray((a * 255).astype(np.uint8)), dp=dp, f=f, off=(reg[0], reg[1]) if reg else (0, 0))
    _cache[n] = r; return r
UG, VG = np.meshgrid(np.arange(SW, dtype=np.float32), np.arange(SH, dtype=np.float32))
def quadro_full(n, cx, cy, cw, par, sx, sy):
    """recorte 16:9 com paralaxe pela profundidade (cx, cy, cw na imagem já ampliada)"""
    c = carrega(n); ih, iw = c['im'].shape[:2]; s = cw / SW
    ch = cw * SH / SW; cx = min(max(cx, cw / 2 + 2), iw - cw / 2 - 2); cy = min(max(cy, ch / 2 + 2), ih - ch / 2 - 2)
    X = (UG - SW / 2) * s + cx; Y = (VG - SH / 2) * s + cy
    d = cv2.remap(c['dp'], X, Y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE) - .5
    k = par * s
    return cv2.remap(c['im'], X - d * k * sx, Y - d * k * sy * .4, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
# ---------------------------------------------------------------- camadas
def png(nome):
    """camada RGBA recortada na área visível: (rgb pré-multiplicado, alfa, deslocamento x, deslocamento y)"""
    im = cv2.imread(f'{CAM}/{nome}.png', cv2.IMREAD_UNCHANGED)
    if PREVIA: im = cv2.resize(im, None, fx=ESC, fy=ESC, interpolation=cv2.INTER_AREA)
    al = im[:, :, 3]; ys, xs = np.nonzero(al > 0)
    if len(xs) == 0: ys, xs = np.array([0]), np.array([0])
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    a = (al[y0:y1, x0:x1].astype(np.float32) / 255)[..., None]
    return (im[y0:y1, x0:x1, 2::-1].astype(np.float32) * a, a, int(x0), int(y0))
def cola(fr, cam, x, y, op=1.0):
    rgb, al, ox, oy = cam; h, w = al.shape[:2]; x, y = int(round(x)) + ox, int(round(y)) + oy
    x0, y0, x1, y1 = max(x, 0), max(y, 0), min(x + w, SW), min(y + h, SH)
    if x1 <= x0 or y1 <= y0 or op <= 0: return
    a = al[y0 - y:y1 - y, x0 - x:x1 - x]; c = rgb[y0 - y:y1 - y, x0 - x:x1 - x]
    if op < 1: a = a * op; c = c * op
    roi = fr[y0:y1, x0:x1]; roi *= (1 - a); roi += c
HUD = png('hud'); LUZ = png('luz'); ABRE = png('abre_q'); FIM = png('fim')
_l = np.zeros((SH, SW, 3), np.float32); _l[LUZ[3]:LUZ[3] + LUZ[0].shape[0], LUZ[2]:LUZ[2] + LUZ[0].shape[1]] = LUZ[0]; LUZ = _l
def png_inteiro(nome):
    im = cv2.imread(f'{CAM}/{nome}.png', cv2.IMREAD_UNCHANGED)
    if PREVIA: im = cv2.resize(im, None, fx=ESC, fy=ESC, interpolation=cv2.INTER_AREA)
    return im[:, :, 2::-1].astype(np.float32), im[:, :, 3].astype(np.float32) / 255
NOMES = {k: png(f'n_{k}') for k in GENTE}; MOLD = {k: png_inteiro(f'm_{k}') for k in GENTE}
yy, xx = np.mgrid[0:SH, 0:SW].astype(np.float32)
VIG = (1 - .42 * np.clip(((xx - SW / 2) / (SW * .62)) ** 2 + ((yy - SH / 2) / (SH * .7)) ** 2, 0, 1.6) ** 1.3)[..., None].astype(np.float32)
GRAO = [cv2.GaussianBlur(rng.normal(0, 4.2, (SH, SW)).astype(np.float32), (0, 0), .8)[..., None] for _ in range(6)]
# ---------------------------------------------------------------- tempos: batidas para cortar no tempo
def batidas():
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', AUD, '-ac', '1', '-ar', '22050', '-f', 'f32le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); hop = 220; n = 1024
    fr = np.lib.stride_tricks.sliding_window_view(a, n)[::hop] * np.hanning(n).astype(np.float32)
    mag = np.log1p(np.abs(np.fft.rfft(fr, axis=1))[:, 2:120])
    flux = np.maximum(np.diff(mag, axis=0), 0).sum(1); flux = (flux - flux.mean()) / (flux.std() + 1e-6)
    tt = (np.arange(len(flux)) + 1) * hop / 22050
    pk = [i for i in range(2, len(flux) - 2) if flux[i] > 1.0 and flux[i] == flux[i - 2:i + 3].max()]
    return np.array([tt[i] for i in pk])
BAT = batidas()
def no_tempo(t, jan=.22):
    if not len(BAT): return t
    i = np.argmin(np.abs(BAT - t)); return float(BAT[i]) if abs(BAT[i] - t) <= jan else t
# ---------------------------------------------------------------- roteiro de cenas automático (pela letra e pela história)
CAST = {'00': ['tiao', 'davi', 'copo'], '01': ['davi', 'neguinho', 'bia', 'ze', 'tiao', 'juninho', 'rafa', 'bar'],
        '02': ['davi', 'juninho', 'neguinho', 'bia', 'rafa', 'bar'], '03': ['davi', 'rafa', 'ze', 'neguinho', 'juninho'],
        '04': ['davi', 'bia', 'neguinho', 'rafa', 'juninho'], '05': ['davi', 'copo', 'neguinho', 'tiao', 'ze'],
        '06': ['davi', 'tiao', 'neguinho', 'bia', 'juninho', 'ze', 'rafa', 'copo', 'bar'], '07': ['davi', 'copo', 'juninho', 'bia', 'neguinho'],
        '08': ['ze', 'davi', 'rafa', 'neguinho', 'juninho'], '09': ['bia', 'davi', 'neguinho', 'juninho', 'tiao', 'ze', 'rafa'],
        '10': ['davi', 'bia', 'juninho', 'neguinho', 'ze', 'rafa', 'tiao', 'bar']}[K]
ABRE_IMG = {'00': ('copo', 'mesa'), '01': ('bar', 'esq'), '02': ('bar', 'dir'), '03': ('rafa', 'tanta'), '04': ('copo', 'caderno'), '05': ('copo', 'caderno'),
            '06': ('copo', 'titulo'), '07': ('copo', 'copo'), '08': ('ze', 'pandeiro'), '09': ('bar', 'dir'), '10': ('bar', 'esq')}[K]
CUE = [('seu tiao', 'tiao'), ('neguinho', 'neguinho'), ('cavaco', 'neguinho'), ('rebolo', 'bia'), ('bia ', 'bia'), ('mestre ze', 'ze'), ('pandeiro', 'ze'),
       ('juninho', 'juninho'), ('banjo', 'juninho'), ('tanta', 'rafa'), ('tum', 'rafa'), ('copo', 'copo'), ('mesa', 'copo'), ('bilhete', 'copo'),
       ('geladeira', 'copo'), ('guardanapo', 'copo'), ('cafe', 'copo'), ('caderno', 'tiao')]
QUEM = {'Davi': 'davi', 'Lívia (Bia)': 'bia', 'Seu Tião': 'tiao', 'Mestre Zé': 'ze', 'Bia': 'bia', 'Rafa': 'rafa', 'Juninho': 'juninho', 'Neguinho': 'neguinho'}
import unicodedata, re
def nrm(s): s = unicodedata.normalize('NFD', s.lower()); return ' ' + re.sub(r'[^a-z ]', ' ', ''.join(c for c in s if unicodedata.category(c) != 'Mn')) + ' '
HIST = []
def escolhe(o, ult, i_todos):
    n = escolhe0(o, ult, i_todos)
    if n == 'davi' and len(HIST) >= 2 and HIST[-1] == 'davi' and HIST[-2] == 'davi' and o['parte'] != 'Fala':
        outros = [c for c in CAST if c != 'davi' and c not in HIST[-3:]] or [c for c in CAST if c != 'davi']
        n = outros[len(HIST) % len(outros)]
    HIST.append(n); return n
def escolhe0(o, ult, i_todos):
    if o['parte'] == 'Fala' and o['quem'] in QUEM: return QUEM[o['quem']]
    tx = nrm(o['txt'])
    achou = sorted([(tx.find(k), v) for k, v in CUE if k in tx and (v in CAST or v == 'copo')])
    if achou and achou[0][1] != ult: return achou[0][1]
    if o['quem'] in QUEM: return QUEM[o['quem']]
    if o['quem'] == 'Os dois': return 'davi'
    roda = [c for c in CAST if c in GENTE]
    return roda[i_todos % len(roda)]
linhas = [o for o in TEMPOS if o['ini'] < DUR - 1]
t_voz = linhas[0]['ini'] if linhas else 4.0
t_abre_fim = min(max(t_voz - .35, 5.5), 9.0) if K != '00' else min(t_voz - .3, 9.0)
fim_letra = max(o['fim'] for o in linhas) if linhas else DUR - 8
T_FIM = max(fim_letra + 1.2, DUR - 9.0); T_FIM = min(T_FIM, DUR - 3.5)
cenas = [dict(n=ABRE_IMG[0], fr=ABRE_IMG[1], ini=0.0, lay='full')]
ult = ABRE_IMG[0]; i_todos = 0; lay_davi = 0
blocos = []
for o in linhas:
    if o['ini'] >= T_FIM: break
    n = escolhe(o, ult, i_todos)
    if o['quem'] in ('Todos',): i_todos += 1
    if blocos and blocos[-1]['n'] == n and o['ini'] - blocos[-1]['ini'] < 8.5 and o['parte'] == blocos[-1]['parte']:
        blocos[-1]['fim'] = o['fim']; continue
    blocos.append(dict(n=n, ini=o['ini'], fim=o['fim'], parte=o['parte'], quem=o['quem'])); ult = n
prev_fim = t_abre_fim if K != '00' else 0.0
VAR_INST = ['full', 'trio', 'full', 'duo:bar', 'full', 'card:proprio']
def preenche(t, ate):
    # trecho instrumental (sem voz): a roda tocando, variando o plano a cada 3,6 a 4,8 s, sempre no tempo
    global ii
    while ate - t > 4.0:
        m = cast_inst[ii % len(cast_inst)]; v = VAR_INST[ii % len(VAR_INST)]; ii += 1
        if m == cenas[-1]['n']: m = cast_inst[ii % len(cast_inst)]; ii += 1
        roda = [r for r in RODA0 if r != m]
        if v == 'trio' and len(roda) >= 2 and m in GENTE: cenas.append(dict(n=m, ini=no_tempo(t), lay='trio', outros=[roda[ii % len(roda)], m, roda[(ii + 1) % len(roda)]]))
        elif v == 'duo:bar' and roda and m in GENTE: cenas.append(dict(n=m, ini=no_tempo(t), lay='duo:bar', outros=[m, roda[ii % len(roda)]]))
        elif v == 'card:proprio' and m in GENTE: cenas.append(dict(n=m, ini=no_tempo(t), lay='card:proprio'))
        else: cenas.append(dict(n=m, fr=INSTR.get(m, 'rosto'), ini=no_tempo(t), lay='full'))
        t += rng.uniform(3.6, 4.8)
RODA0 = [c for c in CAST if c in GENTE]
cast_inst = [c for c in CAST if c != 'davi'] or CAST; ii = 0
for b in blocos:
    corte = no_tempo(b['ini'] - .18)
    if corte - prev_fim > 6.5 and cenas: preenche(prev_fim + .4, corte)
    cenas.append(dict(n=b['n'], ini=max(corte, cenas[-1]['ini'] + 1.2), parte=b['parte'], quem=b['quem'])); prev_fim = b['fim']
if T_FIM - prev_fim > 6.5: preenche(prev_fim + .4, T_FIM)
cenas.append(dict(n='bar', fr='geral', ini=T_FIM, lay='full', fim_card=True))
lim = [cenas[0]]
for c in cenas[1:]:
    if c['ini'] >= lim[-1]['ini'] + 1.0 or c.get('fim_card'):
        if c.get('fim_card') and c['ini'] < lim[-1]['ini'] + 1.0: lim.pop()
        lim.append(c)
cenas = lim
# layout e enquadramento de cada cena (sem repetir o mesmo plano em seguida)
RODA = [c for c in CAST if c in GENTE]
CICLO = {'davi': ['full', 'card:mesa', 'full', 'duo', 'card:bar', 'full', 'card:proprio']}
CICLO_OUTROS = ['full', 'card:proprio', 'full', 'card:bar']
cont = {}; i_trio = 0; i_duo = 0
for i, c in enumerate(cenas):
    c['fimt'] = cenas[i + 1]['ini'] if i + 1 < len(cenas) else DUR + .5
    n = c['n']; dur = c['fimt'] - c['ini']; ant = cenas[i - 1] if i else {}
    if 'lay' not in c:
        if n not in GENTE: c['lay'] = 'full'
        elif c.get('parte') == 'Fala': c['lay'] = 'full'; c['fr'] = 'close' if 'close' in FR[n] else 'rosto'
        elif c.get('quem') == 'Todos' and len(RODA) >= 3:
            v = ['trio', 'full', 'duo', 'bar', 'trio', 'full'][i_trio % 6]; i_trio += 1
            if v == 'trio' and dur >= 3: c['lay'] = 'trio'; c['outros'] = [RODA[(i_trio + j) % len(RODA)] for j in range(3)]
            elif v == 'duo' and dur >= 3: c['lay'] = 'duo:mesa'; c['outros'] = [RODA[i_trio % len(RODA)], RODA[(i_trio + 2) % len(RODA)]]
            elif v == 'bar': c['n'] = n = 'bar'; c['lay'] = 'full'
            else: c['n'] = n = RODA[(i_trio * 2) % len(RODA)]; c['lay'] = 'full'
        elif c.get('quem') == 'Os dois':
            v = i_duo % 4; i_duo += 1
            if v == 0: c['lay'] = 'duo'; c['outros'] = ['davi', 'bia']
            elif v == 1: c['n'] = n = 'bia'; c['lay'] = 'full'
            elif v == 2: c['n'] = n = 'davi'; c['lay'] = 'full'
            else: c['lay'] = 'duo:mesa'; c['outros'] = ['bia', 'davi']
        else:
            ciclo = CICLO.get(n, CICLO_OUTROS); j = cont.get(n, 0)
            for _ in range(len(ciclo)):
                lay = ciclo[j % len(ciclo)]; j += 1
                if not (ant.get('n') == n and ant.get('lay', '').split(':')[0] == lay.split(':')[0]): break
            cont[n] = j; c['lay'] = lay
            if lay == 'duo':
                par = [r for r in RODA if r != n]
                if not par: c['lay'] = 'card:proprio'
                else: c['outros'] = [n, par[i_duo % len(par)]] if i_duo % 2 == 0 else [par[i_duo % len(par)], n]; i_duo += 1
    if c['lay'] == 'full' and 'fr' not in c:
        ops = [k for k in FR[n] if not (ant.get('n') == n and ant.get('fr') == k)] or list(FR[n])
        if n == 'copo': ops = [k for k in ops if k != 'titulo' or K == '06'] or ops
        if n == 'bar': ops = [k for k in ops if k != 'geral'] or ops
        c['fr'] = ops[int(rng.integers(len(ops)))]
for i, c in enumerate(cenas):
    c['mov'] = ['in', 'out', 'esq', 'dir'][int(rng.integers(4))]; c['par'] = float(rng.uniform(16, 26)) * (1 if rng.random() < .5 else -1)
    c['lado'] = 'e' if i % 2 == 0 else 'd'; c['rot'] = float(rng.uniform(1.6, 2.8)) * (1 if rng.random() < .5 else -1)
json.dump(cenas, open(f'{WK}/cenas{K}.json', 'w'), ensure_ascii=False, indent=0)
# nomes: primeira aparição de cada personagem em plano aberto (no retrato o nome já está escrito)
NOME_T = {}
for c in cenas:
    if c['lay'] == 'full' and c['n'] in GENTE and c['n'] not in NOME_T and c['ini'] > t_abre_fim - .5 and not c.get('fim_card'): NOME_T[c['n']] = c['ini'] + .5
# ---------------------------------------------------------------- render de uma cena num instante
_bg = {}
def fundo(kind, n):
    key = (kind, n)
    if key in _bg: return _bg[key]
    if kind == 'proprio':
        im = carrega(n)['im']; sig, esc = 26, .42
    else:
        src = 'copo' if kind == 'mesa' else 'bar'; ci = carrega(src); cx, cy, cw = FR[src]['mesa' if kind == 'mesa' else 'geral']
        ch = cw * 9 / 16; im = ci['im'][int(cy - ch / 2):int(cy + ch / 2), int(cx - cw / 2):int(cx + cw / 2)]
        sig, esc = (5, .55) if kind == 'mesa' else (9, .46)
    h, w = im.shape[:2]; sc = max(SW / w, SH / h) * 1.12
    bgi = cv2.resize(im, (int(w * sc), int(h * sc)), interpolation=cv2.INTER_AREA)
    bgi = cv2.GaussianBlur(bgi, (0, 0), sig * ESC + 1).astype(np.float32) * esc
    _bg[key] = bgi; return bgi
def card_img(n, p, par):
    ci = carrega(n); f = ci['f']; ox, oy = ci['off']
    x0, y0, x1, y1 = CARD[n]; x0 = (x0 - ox) * f; y0 = (y0 - oy) * f; x1 = (x1 - ox) * f; y1 = (y1 - oy) * f
    mrgb, mal = MOLD[n]; MH, MW = mal.shape[:2]; bd = int(round(18 * ESC)); fh = int(round(760 * ESC)); fw = MW - 2 * bd
    z = 1.0 + .07 * min(max(p, 0), 1); cw = (x1 - x0) / z; chh = cw * fh / fw; cx = (x0 + x1) / 2; cy = (y0 + y1) / 2 - (y1 - y0 - chh) * .25
    s = cw / fw; ug, vg = np.meshgrid(np.arange(fw, dtype=np.float32), np.arange(fh, dtype=np.float32))
    X = (ug - fw / 2) * s + cx; Y = (vg - fh / 2) * s + cy
    d = cv2.remap(ci['dp'], X, Y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE) - .5
    k = par * .8 * s * (2 * p - 1)
    foto = cv2.remap(ci['im'], X - d * k, Y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT).astype(np.float32)
    card = mrgb * mal[..., None]; card[bd:bd + fh, bd:bd + fw] = foto; al = mal.copy(); al[bd:bd + fh, bd:bd + fw] = 1
    return card, al
def pousa(fr, card, al, cx, cy, ang, esc):
    MH, MW = al.shape[:2]; M = cv2.getRotationMatrix2D((MW / 2, MH / 2), ang, esc); M[0, 2] += cx - MW / 2; M[1, 2] += cy - MH / 2
    cs = np.array([[0, 0, 1], [MW, 0, 1], [0, MH, 1], [MW, MH, 1]], np.float32) @ M.T
    mg = int(50 * ESC) + 2
    x0 = max(int(cs[:, 0].min()) - mg, 0); y0 = max(int(cs[:, 1].min()) - mg, 0); x1 = min(int(cs[:, 0].max()) + mg, SW); y1 = min(int(cs[:, 1].max()) + mg, SH)
    if x1 <= x0 or y1 <= y0: return
    M2 = M.copy(); M2[0, 2] -= x0; M2[1, 2] -= y0; wh = (x1 - x0, y1 - y0)
    sa = cv2.warpAffine(al, M2, wh, flags=cv2.INTER_LINEAR)
    sb = cv2.GaussianBlur(sa, (0, 0), 20 * ESC + 1); sh = int(18 * ESC); sw = int(10 * ESC)
    sb = np.pad(sb, ((sh, 0), (sw, 0)))[:wh[1], :wh[0]]
    roi = fr[y0:y1, x0:x1]; roi *= (1 - .6 * sb[..., None])
    cr = cv2.warpAffine(card, M2, wh, flags=cv2.INTER_LINEAR)
    fr[y0:y1, x0:x1] = roi * (1 - sa[..., None]) + cr
def quadro_cards(c, p, t):
    lay = c['lay']; kind = lay.split(':')[1] if ':' in lay else 'bar'
    gente = c.get('outros') or [c['n']]
    bgi = fundo(kind, c['n'] if kind == 'proprio' else gente[0]); bh, bw = bgi.shape[:2]; pp = min(max(p, 0), 1)
    dx = int((bw - SW) * (.3 + .4 * pp)); dy = int((bh - SH) * .5); fr = bgi[dy:dy + SH, dx:dx + SW].copy()
    if lay.startswith('card'):
        pos = [(SW * (.36 if c['lado'] == 'e' else .64), SH * .435, c['rot'], .9)]
    elif lay.startswith('duo'):
        pos = [(SW * .30, SH * .47, -abs(c['rot']), .86), (SW * .70, SH * .45, abs(c['rot']), .86)]
    else:
        pos = [(SW * .20, SH * .48, -2.6, .7), (SW * .50, SH * .43, 1.4, .74), (SW * .80, SH * .48, -1.8, .7)]
    for j, (g, (cx, cy, ang, esc)) in enumerate(zip(gente, pos)):
        card, al = card_img(g, p, c['par'] * (1 if j % 2 == 0 else -1))
        pousa(fr, card, al, cx, cy + 6 * ESC * math.sin(t * .9 + j), ang + .5 * math.sin(t * .7 + j), esc)
    return fr
def quadro(c, t):
    p = (t - c['ini']) / max(c['fimt'] - c['ini'], .1); p = min(max(p, -.2), 1.2)
    if c['lay'] != 'full': return quadro_cards(c, p, t)
    n = c['n']; ci = carrega(n); f = ci['f']; ox, oy = ci['off']
    cx, cy, cw = FR[n][c['fr']]; cx = (cx - ox) * f; cy = (cy - oy) * f; cw = cw * f
    m = c['mov']
    if m == 'in': cw = cw * (1 - .10 * p)
    elif m == 'out': cw = cw * (.90 + .10 * p)
    elif m == 'esq': cw *= .92; cx += cw * .05 * (1 - 2 * p)
    else: cw *= .92; cx -= cw * .05 * (1 - 2 * p)
    if n in TOPO:   # nunca cortar a cabeça: o alto do recorte fica acima do topo da cabeça
        ch = cw * SH / SW; lim = (TOPO[n] - oy) * f - 34 * f + ch / 2
        cy = min(cy, lim)
    return quadro_full(n, cx, cy, cw, c['par'] * ESC, 2 * p - 1, 1 - 2 * p).astype(np.float32)
# ---------------------------------------------------------------- letra (karaokê)
mostra = []
for i, o in enumerate(linhas):
    chave = ((o['quem'] if o['parte'] == 'Fala' or K == '04' else '') + '|' + o['txt'])
    li = TIRAS.get(chave)
    if li is None: continue
    prox = linhas[i + 1]['ini'] if i + 1 < len(linhas) else DUR
    a = o['ini'] - .25; b = min(max(o['fim'] + .6, o['ini'] + 1.3), prox - .1)
    if b - a < .5: continue
    if mostra and a < mostra[-1]['b'] + .03: a = mostra[-1]['b'] + .03
    if b - a < .5: continue
    mostra.append(dict(a=a, b=b, li=li, pal=o['pal'], ini=o['ini']))
_tira = {}
def tira(li):
    if li not in _tira:
        A = png(f'l{li:02d}a'); B = png(f'l{li:02d}b'); cx = CX[f'l{li:02d}a']
        _tira[li] = (A, B, [(x0 * ESC, x1 * ESC) for x0, x1 in cx['pal']])
    return _tira[li]
def wipe_x(m, t, caixas):
    pal = m['pal']; n = min(len(pal), len(caixas))
    if n == 0 or t < pal[0][0]: return 0
    for i in range(n):
        a, b = pal[i]; x0, x1 = caixas[i]
        if t < a: return caixas[i - 1][1] if i else 0
        if t <= b: return x0 + (x1 - x0) * (t - a) / max(b - a, .05)
    return caixas[n - 1][1] + 40
# ---------------------------------------------------------------- loop dos quadros
saida = f'{WK}/pagode-fiado-{K}-v2{"-previa" if PREVIA else ""}.mp4'
cmd = ['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{SW}x{SH}', '-r', str(FPS), '-i', '-', '-i', AUD,
       '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast' if PREVIA else 'faster', '-crf', '20' if PREVIA else '20', '-maxrate', '9M', '-bufsize', '18M',
       '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', saida]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
NQ = int(min(DUR, float(os.environ.get('LIMITE', DUR))) * FPS); XF = .42
cortes = [c['ini'] for i, c in enumerate(cenas) if i and (c.get('parte') != cenas[i - 1].get('parte') or i % 3 == 0 or c.get('fim_card'))]
for q in range(NQ):
    t = q / FPS
    i = max(j for j, c in enumerate(cenas) if c['ini'] <= t + 1e-6)
    fr = quadro(cenas[i], t)
    if i + 1 < len(cenas) and cenas[i + 1]['ini'] - t < XF / 2 and not cenas[i + 1].get('seco'):
        pass
    if i > 0 and t - cenas[i]['ini'] < XF:      # fusão com a cena anterior
        a = (t - cenas[i]['ini']) / XF; a = a * a * (3 - 2 * a)
        fr = fr * a + quadro(cenas[i - 1], t) * (1 - a)
    fr *= VIG
    # luz quente vazando nos cortes
    lz = 0.0
    for ct in cortes:
        dt = t - ct
        if -.3 < dt < .7: lz = max(lz, (1 - abs(dt + .02) / (.3 if dt < 0 else .7)) * .42)
    if lz > 0: fr += LUZ * lz
    # abertura (quadro-negro) e fecho
    if t < t_abre_fim + .7:
        op = min(1, max(0, (t - .2) / .6)) * min(1, max(0, (t_abre_fim + .6 - t) / .6)); cola(fr, ABRE, 0, 0, op)
    if t >= T_FIM - .2:
        cola(fr, FIM, 0, 0, min(1, (t - T_FIM + .2) / .7))
    # HUD (selo e faixa)
    if t > .5: cola(fr, HUD, 0, 0, min(1, (t - .5) / .8) * (.92 if t < T_FIM else max(0, 1 - (t - T_FIM) / .6)))
    # nome do personagem na primeira aparição
    for k, tn in NOME_T.items():
        if tn <= t < tn + 3.4:
            op = min(1, (t - tn) / .35, (tn + 3.4 - t) / .45); cola(fr, NOMES[k], 64 * ESC, 186 * ESC + (1 - op) * 10 * ESC, op)
    # letra
    for m in mostra:
        if m['a'] <= t <= m['b']:
            (A, B, caixas) = tira(m['li']); h, w = A[1].shape[0] + A[3], A[1].shape[1] + A[2]
            op = min(1, (t - m['a']) / .2, (m['b'] - t) / .25)
            x = (SW - w) / 2; y = SH - 66 * ESC - h + (1 - op) * 14 * ESC
            cola(fr, A, x, y, op)
            wx = int(min(w, max(0, wipe_x(m, t, caixas))))
            if wx > B[2]: cola(fr, (B[0][:, :wx - B[2]], B[1][:, :wx - B[2]], B[2], B[3]), x, y, op)
    fr += GRAO[(q // 2) % len(GRAO)] * (ESC if PREVIA else 1)
    pr.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
    if q % (FPS * 20) == 0: print(f'{K} {t:.0f}/{DUR:.0f}s', flush=True)
pr.stdin.close(); pr.wait()
print('ok', saida)
