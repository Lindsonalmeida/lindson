# Tempos das palavras de cada faixa aprovada (faster-whisper small, CPU). Uso: python3 transcrever.py <pasta_audio> <faixas...>
# Lê o mp3 pelo ffmpeg (o PyAV do faster-whisper dá erro neste ambiente) e grava <pasta>/<faixa>.words.json
import sys, json, os, subprocess, numpy as np
from faster_whisper import WhisperModel
AQUI = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(AQUI + '/letras.json'))
m = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=4)
P = sys.argv[1]
for k in sys.argv[2:]:
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{P}/{k}.mp3', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.float32)
    dica = ' '.join(dict.fromkeys(t for _, _, t in L[k]['linhas']))[:600]
    segs, _ = m.transcribe(a, language='pt', word_timestamps=True, initial_prompt=dica, condition_on_previous_text=False, vad_filter=False, beam_size=5)
    out = []
    for s in segs:
        out.append(dict(s=round(s.start, 2), e=round(s.end, 2), t=s.text.strip(), w=[[round(x.start, 2), round(x.end, 2), x.word.strip(), round(x.probability, 2)] for x in (s.words or [])]))
    json.dump(out, open(f'{P}/{k}.words.json', 'w'), ensure_ascii=False)
    print(k, len(out), flush=True)
