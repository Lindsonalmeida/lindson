# Recorte por IA (BiRefNet) + troca da cor da camisa (segmentação de roupa U2Net-cloth)
# Uso: python3 recortar.py <pasta_fotos> <saida> f23:amarelo f28:amarelo ...
import sys, os, numpy as np, cv2
from PIL import Image, ImageOps
from rembg import new_session, remove

ALVO = {'amarelo': (255, 194, 14), 'azul': (35, 80, 245), 'laranja': (255, 122, 26), 'marinho': (5, 49, 110), 'original': None}
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
s_pessoa, s_roupa = new_session('birefnet-portrait'), new_session('u2net_cloth_seg')

def recolorir(rgb, mask, alvo):
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    m = mask > 128
    mA, mB, mL = np.median(A[m]), np.median(B[m]), np.median(L[m])
    # só o tecido dominante: exclui listras da gola, botões e sombras muito escuras
    dist = np.hypot(A - mA, B - mB)
    croma = np.hypot(A - 128, B - 128); mC = np.median(croma[m])
    # pele tem croma bem menor que a camisa colorida: exclui mão/braço sobre a camisa
    pele = (croma < mC * .72) if mC > 25 else np.zeros_like(m)
    tecido = m & (dist < 14) & (L > mL * .35) & ~pele
    peso = cv2.GaussianBlur(tecido.astype(np.float32), (0, 0), 2.0)
    t = cv2.cvtColor(np.uint8([[alvo]]), cv2.COLOR_RGB2LAB).astype(np.float32)[0, 0]
    novoL = np.clip(L + (t[0] - mL) * .85, 0, 255)
    novo = np.dstack([novoL, A - mA + t[1], B - mB + t[2]])
    out = lab * (1 - peso[..., None]) + novo * peso[..., None]
    return cv2.cvtColor(np.clip(out, 0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB)

for arg in sys.argv[3:]:
    nome, cor = arg.split(':')
    im = ImageOps.exif_transpose(Image.open(f'{src}/{nome}.jpg')).convert('RGB')
    im.thumbnail((2600, 2600), Image.LANCZOS)
    alpha = remove(im, session=s_pessoa, only_mask=True)
    rgb = np.array(im)
    if ALVO[cor]:
        roupa = remove(im, session=s_roupa, only_mask=True)
        H = im.size[1]
        roupa = np.array(roupa.convert('L'))[:H]  # 1º bloco = parte de cima (camisa)
        roupa = np.minimum(roupa, np.array(alpha))
        rgb = recolorir(rgb, roupa, ALVO[cor])
    out = Image.fromarray(np.dstack([rgb, np.array(alpha)]))
    out = out.crop(out.getchannel('A').point(lambda a: 255 if a > 10 else 0).getbbox())
    out.save(f'{dst}/{nome}-{cor}.png')
    print(nome, cor, out.size, flush=True)
