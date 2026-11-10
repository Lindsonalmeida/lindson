# Teste de vozes masculinas pt-BR grátis (mesma frase) + Whisper (sim e pausas) · conta Leandro · 10/11/2026
# Saída: vozes-teste/<voz>.mp3 e vozes-teste/resultado.json. Modelos Piper em /tmp (fora do Git).
import os, subprocess, json, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from voz import confere, tts
D = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(D, 'vozes-teste'); os.makedirs(O, exist_ok=True)
PIPER = '/tmp/claude-0/piper'
REF = 'Tem medo de comprar seminovo bichado? Na WF todo iPhone sai testado. E com laudo. Esse é o iPhone 14 Pro Max, 128 gigas, por 3.299 reais. Chama no WhatsApp agora.'
FALA = 'Tem medo de comprar semi-novo bichado? Na dábliu éfe, todo iPhone sai testado. E com laudo. Esse é o iPhone catorze Pro Max, cento e vinte e oito gigas, por três mil duzentos e noventa e nove reais. Chama no WhatsApp agora.'
CH = ['14', 'pro max', '3.299', 'laudo']
def pausas(mp3):
    r = subprocess.run(['ffmpeg', '-i', mp3, '-af', 'silencedetect=n=-35dB:d=0.45', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return len(re.findall('silence_end', r))
def wav2mp3(w, m): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', w, '-b:a', '96k', m], check=True)
res = {}
cands = {
 'antonio-edge-+4': lambda m: tts(FALA, m),
 'piper-faber-medium': lambda m: (subprocess.run(['python3', '-m', 'piper', '-m', f'{PIPER}/pt_BR-faber-medium.onnx', '-f', m + '.wav'], input=FALA, text=True, check=True), wav2mp3(m + '.wav', m)),
 'piper-edresson-low': lambda m: (subprocess.run(['python3', '-m', 'piper', '-m', f'{PIPER}/pt_BR-edresson-low.onnx', '-f', m + '.wav'], input=FALA, text=True, check=True), wav2mp3(m + '.wav', m)),
 'gtts-pt-br-referencia': lambda m: __import__('gtts').gTTS(FALA, lang='pt', tld='com.br').save(m),
}
for k, f in cands.items():
    m = os.path.join(O, k + '.mp3')
    try:
        f(m); sim, falta, txt, _ = confere(m, REF, CH)
        res[k] = {'sim': round(sim, 3), 'pausas': pausas(m), 'faltou': falta, 'whisper': txt}
    except Exception as e:
        res[k] = {'erro': str(e)[:200]}
    if os.path.exists(m + '.wav'): os.remove(m + '.wav')
    print(k, res[k], flush=True)
res['nao-testadas'] = {'coqui-xtts-v2': 'precisa de torch + modelo de ~1,8 GB; a rede aqui baixa a ~350 KB/s (mais de 90 min)',
                       'kokoro': 'pm_alex/pm_santa existem, mas exigem torch (mesmo bloqueio de download)'}
json.dump(res, open(os.path.join(O, 'resultado.json'), 'w'), ensure_ascii=False, indent=1)
