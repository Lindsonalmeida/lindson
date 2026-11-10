"""Narração com a VOZ 6 APROVADA do Lindson (09/11, conta Zuleide): mesmos parâmetros e pós-produção do gerador oficial
conteudo/reels/leva-30s/motor/gerar_voz_lindson.py (exaggeration 0,75 · cfg 0,3 · temperatura 0,8; corta pausas, ritmo 1,06×,
brilho +3 dB em 3,5 kHz e 8 kHz, compressor, -15 LUFS). Cada fala é 1 bloco (< 220 caracteres). Conta Pedro, 10/11/2026.
Uso: <venv-chatterbox>/bin/python narra6.py <ref6-aprovada.wav> <pasta-saida> [ids]   (ref no privado dados/agencia/voz-lindson/, fora do Git)"""
import json, os, sys, subprocess, torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
D = os.path.dirname(os.path.abspath(__file__)); REF, SAI = sys.argv[1], sys.argv[2]
F = json.load(open(os.path.join(D, 'falas.json'))); ids = sys.argv[3:] or list(F)
torch.set_num_threads(os.cpu_count()); m = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
POS = ('silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.12:stop_threshold=-45dB,atempo=1.06,highpass=f=90,'
       'equalizer=f=3500:t=q:w=1:g=3,highshelf=f=8000:g=3,acompressor=threshold=-20dB:ratio=3:attack=5:release=60:makeup=3,loudnorm=I=-15:TP=-1')
for s in ids:
    torch.manual_seed(int(os.environ.get('SEMENTE', s)))
    cru = os.path.join(SAI, f'cru-{int(s):02d}.wav')
    ta.save(cru, m.generate(F[s], language_id='pt', audio_prompt_path=REF, exaggeration=0.75, cfg_weight=0.3, temperature=0.8), m.sr)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', cru, '-af', POS, '-ar', '44100', '-ac', '1', os.path.join(SAI, f's{int(s):02d}.wav')], check=True)
    os.remove(cru); print(s, 'ok', flush=True)
