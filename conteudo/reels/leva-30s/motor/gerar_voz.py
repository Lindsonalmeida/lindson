"""Troca a voz provisória pela voz clonada do Lindson em TODA a leva, com um comando (motor v2, 08/11/2026).

  1. Ponha o áudio dele (WhatsApp limpo, 30 s a 2 min, só a voz dele) em agencia/marca-lindson/voz/ref.wav
     (essa pasta está no .gitignore: dado biométrico, nunca vai para o GitHub).
  2. python3 gerar_voz.py                 # todos os 10
     python3 gerar_voz.py L30-01 L30-05   # só alguns

Usa o motor do Dublê (apps/clone-studio/motor_voz.py, Chatterbox Multilingual) em blocos de até ~220 caracteres
(regra de 03/11). Precisa de um Python com chatterbox-tts (venv com torch CPU ou GPU). Aponte com PY_DUBLE=<python>.
Na nuvem (CPU, 4 núcleos) leva ~1 min para carregar + ~15 s por segundo de fala; na RTX 3050 do Lindson, segundos.
Saída: render/NN-slug-v2.mp4 (sem a marca "voz provisória").
"""
import os, subprocess, sys
M = os.path.dirname(os.path.abspath(__file__))
REF = os.path.abspath(os.path.join(M, '../../../../agencia/marca-lindson/voz/ref.wav'))
if not os.path.exists(REF):
    sys.exit(f'Falta {REF}. Converta o áudio: ffmpeg -i audio-do-whatsapp.ogg -ac 1 -ar 24000 {REF}')
py = os.environ.get('PY_DUBLE')
if not py:
    for c in [os.path.expanduser('~/cbx/bin/python'), os.path.join(M, '.venv-duble/bin/python')]:
        if os.path.exists(c): py = c; break
if not py:
    sys.exit('Instale o Dublê: python3 -m venv ~/cbx && ~/cbx/bin/pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu && ~/cbx/bin/pip install chatterbox-tts')
subprocess.run([sys.executable, os.path.join(M, 'render_leva.py'), '--voz', 'duble', *sys.argv[1:]], check=True, env={**os.environ, 'PY_DUBLE': py})
