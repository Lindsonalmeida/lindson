"""Acha o rosto (e o topo da cabeça) nas fotos, para enquadrar sem cortar a pessoa (conta Leandro, 04/11/2026).
Regra do Lindson (04/11): "não corte imagem do rosto dela, sempre deixe ela bem visível, não queremos imagens cortadas".
Modelo YuNet (OpenCV) em ~/.modelos/yunet.onnx (https://huggingface.co/opencv/face_detection_yunet).
Uso: python3 rosto.py <pasta com fotos> > rostos.json   →  {"IMG_3009.jpg": [x, y, w, h] em fração da foto (0–1)}"""
import sys, os, json, cv2
M = os.path.expanduser('~/.modelos/yunet.onnx'); out = {}
for n in sorted(os.listdir(sys.argv[1])):
    if not n.lower().endswith(('.jpg', '.png')): continue
    im = cv2.imread(os.path.join(sys.argv[1], n)); h, w = im.shape[:2]; k = 1024 / max(h, w); sm = cv2.resize(im, (int(w * k), int(h * k)))
    d = cv2.FaceDetectorYN.create(M, '', (sm.shape[1], sm.shape[0]), 0.6); _, f = d.detect(sm)
    if f is None: print('sem rosto:', n, file=sys.stderr); continue
    x, y, fw, fh = max(f, key=lambda r: r[2] * r[3])[:4]
    out[n] = [round(float(x) / sm.shape[1], 4), round(float(y) / sm.shape[0], 4), round(float(fw) / sm.shape[1], 4), round(float(fh) / sm.shape[0], 4)]
print(json.dumps(out, indent=0))
