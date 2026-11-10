"""Narração dos 4 stories em vídeo na voz clonada do Lindson (Dublê, Chatterbox Multilingual), conta Pedro, 05/11/2026.
Regra do Lindson (05/11): "nunca faça vídeos sem áudio, sempre narração fluida que não pareça IA, VFX e SFX".
Método aprovado do motor_voz.py: melhor trecho de 10 s + identidade média da amostra inteira, temperatura 0,6,
voz limpa e fluida (blocos de até ~220 caracteres, pausas ~0,2 s, sem respiração artificial, estalos aparados, estúdio leve).
A amostra da voz dele NÃO vai para o Git (dado biométrico). Uso:
  <venv-chatterbox>/bin/python narra.py <amostra.wav> <pasta-saida> [4 5 6 7]"""
import sys, os, json, time, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'apps', 'clone-studio'))
import motor_voz as mv
FALAS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'falas.json')))
amostra, saida = sys.argv[1], sys.argv[2]
ids = sys.argv[3:] or list(FALAS)
for s in ids:
    t = time.time(); txt = FALAS[s]
    a = mv.narrar(txt, amostra, 0.45, semente=int(os.environ.get('SEMENTE', s)), humanizar=True)   # SEMENTE=n refaz com outra variação
    sf.write(os.path.join(saida, f's{int(s):02d}.wav'), a, mv.S)
    print(s, round(len(a) / mv.S, 2), 's em', round(time.time() - t), 's ·', txt, flush=True)
