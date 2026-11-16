# (não usado na versão final: recorte comia a mão; ficou o quadro com fusão suave) Recorte do aparelho · conta Pedro · 16/11/2026
import sys, os, numpy as np, cv2
from PIL import Image, ImageEnhance
from rembg import remove, new_session
from pymatting import estimate_foreground_ml
IMG = '/tmp/claude-0/-home-user/71909cf5-3742-5a17-8357-bcbb30dd10b8/images/'
BOX = {'41': ('41.png', (40, 200, 455, 565)), '42': ('42.webp', (60, 175, 440, 650)),
       '43': ('43.webp', (110, 335, 390, 705)), '44': ('44.webp', (110, 300, 375, 625)),
       '45': ('45.png', (110, 315, 315, 520))}
ses = new_session('isnet-general-use')
D = os.path.dirname(os.path.abspath(__file__))
for k in sys.argv[1:]:
    f, b = BOX[k]; im = Image.open(IMG+f).convert('RGB').crop(b)
    s = 1400 / max(im.size); im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
    im = ImageEnhance.Sharpness(im).enhance(1.6)
    im.save(f'{D}/fotos/quadro-{k}.jpg', quality=95)
    m = np.asarray(remove(im, session=ses, only_mask=True)).astype(np.float32)/255
    I = np.asarray(im).astype(np.float32)/255
    g = cv2.ximgproc.guidedFilter(guide=(I*255).astype(np.uint8), src=(m*255).astype(np.uint8), radius=3, eps=60).astype(np.float32)/255
    a = np.clip((g-.12)/.76, 0, 1)
    nl, lab, st, _ = cv2.connectedComponentsWithStats((a > .5).astype(np.uint8)); kk = 1+np.argmax(st[1:, cv2.CC_STAT_AREA])
    a = a*cv2.dilate((lab == kk).astype(np.uint8), np.ones((9, 9), np.uint8)); a = a*a*(3-2*a); a = cv2.GaussianBlur(a, (0, 0), .8); a[a < .03] = 0
    F = np.clip(estimate_foreground_ml(I.astype(np.float64), a.astype(np.float64)), 0, 1)
    Image.fromarray((np.dstack([F, a])*255+.5).astype(np.uint8), 'RGBA').save(f'{D}/fotos/rec-{k}.png'); print(k, flush=True)
