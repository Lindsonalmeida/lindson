# Narrações dos Reels 30 s com a voz clonada do Lindson (Chatterbox Multilingual, o mesmo motor do Dublê).
# Conta Zuleide, 08/11/2026. A referência da voz fica FORA do Git: agencia/marca-lindson/voz/ref.wav (dado biométrico).
# Uso: python3 gerar_voz_lindson.py [NN ...]   → conteudo/reels/leva-30s/voz/NN-bK.wav e NN.wav (blocos unidos)
import json, os, sys, subprocess
import torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

D = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(D, '..', '..', '..', '..'))
REF = os.path.join(RAIZ, 'agencia/marca-lindson/voz/ref.wav')
SAI = os.path.join(D, '..', 'voz'); os.makedirs(SAI, exist_ok=True)
R = json.load(open(os.path.join(D, '..', 'roteiros.json')))
R = R if isinstance(R, list) else R.get('reels', R.get('roteiros'))
so = set(sys.argv[1:])
torch.set_num_threads(os.cpu_count())
m = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
for i, r in enumerate(R, 1):
    nn = f'{i:02d}'
    if so and nn not in so: continue
    partes = []
    for j, b in enumerate(r['blocos_voz'], 1):
        out = os.path.join(SAI, f'{nn}-b{j}.wav')
        if not os.path.exists(out):
            # fluida e natural: exageração moderada e cfg baixo deixam o ritmo de conversa
            w = m.generate(b, language_id='pt', audio_prompt_path=REF, exaggeration=0.55, cfg_weight=0.4, temperature=0.75)
            ta.save(out, w, m.sr)
            print('ok', out, flush=True)
        partes.append(out)
    # une os blocos com 0,15 s de respiro, corta silêncio sobrando e normaliza
    lst = os.path.join(SAI, f'{nn}.txt')
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in partes))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst,
                    '-af', 'silenceremove=stop_periods=-1:stop_duration=0.35:stop_threshold=-42dB,loudnorm=I=-16:TP=-1.5',
                    '-ar', '44100', os.path.join(SAI, f'{nn}.wav')], check=True)
    os.remove(lst)
    print('reels', nn, 'pronto', flush=True)
