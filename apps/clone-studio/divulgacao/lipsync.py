"""Boca sincronizada do Dublê (etapa 2, conta Pedro, 03/11/2026): MuseTalk 1.5 (MIT) sem mmpose.
Recorte do rosto igual ao do MuseTalk (do meio do nariz até o queixo, simétrico), com os pontos do
MediaPipe Face Landmarker; mistura suave só na região da boca e do queixo.
uso: python lipsync.py <video base> <inicio s> <dur s> <audio.wav> <saida.mp4> [segundos_teste]"""
import os, sys, glob, subprocess, tempfile, time
import cv2, numpy as np, torch
MUSE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MuseTalk')
video, ini, dur, audio, saida = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), os.path.abspath(sys.argv[4]), os.path.abspath(sys.argv[5])
teste = float(sys.argv[6]) if len(sys.argv) > 6 else 0
video = os.path.abspath(video); os.chdir(MUSE); sys.path.insert(0, MUSE)
import imageio_ffmpeg; FF = imageio_ffmpeg.get_ffmpeg_exe()
from musetalk.utils.utils import load_all_model, datagen
from musetalk.utils.audio_processor import AudioProcessor
from transformers import WhisperModel
from mediapipe.tasks.python import vision, BaseOptions
import mediapipe as mp
torch.set_num_threads(os.cpu_count())
FPS = 25
tmp = tempfile.mkdtemp()
subprocess.run([FF, '-y', '-loglevel', 'error', '-ss', str(ini), '-t', str(dur), '-i', video, '-vf', f'fps={FPS}', f'{tmp}/%05d.png'], check=True)
quadros = [cv2.imread(f) for f in sorted(glob.glob(f'{tmp}/*.png'))]
H, W = quadros[0].shape[:2]
print('quadros base', len(quadros), W, H, flush=True)

# 1) pontos do rosto e recorte (mesma regra do get_landmark_and_bbox do MuseTalk, v1.5)
lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='models/face_landmarker.task'), num_faces=1))
caixas = []
for q in quadros:
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(q, cv2.COLOR_BGR2RGB)))
    if not r.face_landmarks: caixas.append(None); continue
    p = np.array([[a.x * W, a.y * H] for a in r.face_landmarks[0]])
    meio = p[5, 1]; queixo = p[152, 1]                      # 5 = parte baixa do nariz (≈ ponto 29 do dwpose), 152 = queixo
    x1, x2 = p[234, 0], p[454, 0]                           # laterais do rosto na altura das orelhas (contorno do maxilar)
    caixas.append([x1, max(0, meio - (queixo - meio)), x2, queixo])
ok = [c for c in caixas if c is not None]
caixas = [c if c is not None else ok[0] for c in caixas]
cx = np.array(caixas)
k = 7; cx = np.array([cx[max(0, i - k // 2):i + k // 2 + 1].mean(0) for i in range(len(cx))])   # suaviza o tremor
caixas = [(int(a), int(b), int(c), min(H, int(d) + 10)) for a, b, c, d in cx]                    # +10 px no queixo (extra_margin v1.5)

# 2) modelos
vae, unet, pe = load_all_model(unet_model_path='models/musetalkV15/unet.pth', vae_type='sd-vae',
                               unet_config='models/musetalkV15/musetalk.json', device=torch.device('cpu'))
ap = AudioProcessor(feature_extractor_path='models/whisper')
whisper = WhisperModel.from_pretrained('models/whisper').eval(); whisper.requires_grad_(False)
feat, n = ap.get_audio_feature(audio)
chunks = ap.get_whisper_chunk(feat, 'cpu', unet.model.dtype, whisper, n, fps=FPS, audio_padding_length_left=2, audio_padding_length_right=2)
if teste: chunks = chunks[:int(teste * FPS)]
print('quadros de áudio', len(chunks), flush=True)
lat = []
for (x1, y1, x2, y2), q in zip(caixas, quadros):
    lat.append(vae.get_latents_for_unet(cv2.resize(q[y1:y2, x1:x2], (256, 256), interpolation=cv2.INTER_LANCZOS4)))
ciclo_q, ciclo_c, ciclo_l = quadros + quadros[::-1], caixas + caixas[::-1], lat + lat[::-1]

# 3) máscara suave: só boca, bochechas de baixo e queixo
def mascara(w, h):
    m = np.zeros((h, w), np.float32)
    cv2.ellipse(m, (w // 2, int(h * .72)), (int(w * .36), int(h * .30)), 0, 0, 360, 1, -1)
    m[:int(h * .45)] = 0
    m = cv2.GaussianBlur(m, (0, 0), max(3, w / 18))
    return m[..., None]

saida_q = f'{tmp}/out'; os.makedirs(saida_q)
t0 = time.time(); i = 0
with torch.no_grad():
    for wb, lb in datagen(whisper_chunks=chunks, vae_encode_latents=ciclo_l, batch_size=8, delay_frame=0, device='cpu'):
        pred = unet.model(lb.to(unet.model.dtype), torch.tensor([0]), encoder_hidden_states=pe(wb)).sample
        for rec in vae.decode_latents(pred):
            x1, y1, x2, y2 = ciclo_c[i % len(ciclo_c)]; base = ciclo_q[i % len(ciclo_q)].copy()
            rosto = cv2.resize(rec.astype(np.uint8), (x2 - x1, y2 - y1)).astype(np.float32)
            m = mascara(x2 - x1, y2 - y1); reg = base[y1:y2, x1:x2].astype(np.float32)
            base[y1:y2, x1:x2] = (reg * (1 - m) + rosto * m).clip(0, 255).astype(np.uint8)
            cv2.imwrite(f'{saida_q}/{i:05d}.png', base); i += 1
        print(f'{i}/{len(chunks)} quadros, {time.time() - t0:.0f}s', flush=True)
subprocess.run([FF, '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{saida_q}/%05d.png', '-i', audio, '-shortest',
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '17', '-c:a', 'aac', '-b:a', '192k', saida], check=True)
print('FIM', saida, flush=True)
