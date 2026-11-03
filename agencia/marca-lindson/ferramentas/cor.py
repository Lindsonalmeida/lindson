# Tratamento de cor cinematográfico (referências Jonatas Torres / INFLURY): mantém a foto colorida, puxa o laranja do estúdio
# para âmbar-amarelo da marca (#F5C518), sombra fria levemente petróleo, contraste e nitidez. Gera também o recorte COLORIDO.
# Saída em agencia/marca-lindson/artes-v1/fotos/ (fora do Git): cNN.jpg (foto inteira) e cNN-rec.png (recorte com transparência).
import sys, os, numpy as np, cv2, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
S = '/tmp/claude-0/-home-user/71909cf5-3742-5a17-8357-bcbb30dd10b8/scratchpad'
OUT = '/home/user/lindson/agencia/marca-lindson/artes-v1/fotos/'
seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(base_options=BaseOptions(model_asset_path='selfie.tflite'), output_category_mask=True))
for f in sys.argv[1:]:
    n = os.path.basename(f)[1:3]
    im = cv2.imread(f).astype(np.float32) / 255
    rgb0 = cv2.cvtColor((im * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
    pm = (seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(rgb0))).category_mask.numpy_view() != 0).astype(np.float32)
    fundo = 1 - cv2.GaussianBlur(cv2.dilate(pm, np.ones((25, 25))), (0, 0), 12)   # só o fundo muda de cor; a pele fica natural
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)  # H em graus 0-360
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    lar = np.clip(1 - np.abs(h - 28) / 22, 0, 1) * (s > .25) * fundo          # tons laranja (luz do estúdio)
    h[:] = h + lar * 16                                                  # laranja → âmbar/amarelo (~44°)
    s[:] = np.clip(s * (1 + .25 * lar) * .92, 0, 1)
    im = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    lum = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)[..., None]
    sombra = np.clip(1 - lum / .35, 0, 1)
    im = im + sombra * np.array([.035, .02, -.01]) * 1.0                 # sombra levemente petróleo (BGR)
    im = np.clip((im - .5) * 1.14 + .49, 0, 1)                           # contraste
    bl = cv2.GaussianBlur(im, (0, 0), 2.0); im = np.clip(im * 1.35 - bl * .35, 0, 1)  # nitidez
    out = (im * 255).astype(np.uint8)
    cv2.imwrite(OUT + f'c{n}.jpg', out, [cv2.IMWRITE_JPEG_QUALITY, 93])
    rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
    cat = seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(rgb))).category_mask.numpy_view()
    m = cv2.GaussianBlur((cat != 0).astype(np.float32), (0, 0), 2.2); m = np.clip((m - .35) / .3, 0, 1)
    rgba = np.dstack([out, (m * 255).astype(np.uint8)])
    ys, xs = np.where(m > .05); rgba = rgba[max(ys.min() - 20, 0):, max(xs.min() - 20, 0):xs.max() + 20]
    cv2.imwrite(OUT + f'c{n}-rec.png', rgba)
    print(n, out.shape)
