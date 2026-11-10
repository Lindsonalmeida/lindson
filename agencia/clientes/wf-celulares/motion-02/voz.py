# Narração do motion-02 com voz NATIVA pt-BR + conferência automática com Whisper · conta Leandro · 10/11/2026
# Giuseppe REPROVADO (pronúncia). Padrão: pt-BR-AntonioNeural +4%, sem pitch e sem eco (vozes-ia.md).
# Para cada vídeo: gera, transcreve (faster-whisper small, pt, com tempo por palavra), compara com o texto
# normal (sim >= 0,93 e termos-chave: modelo, número e preço) e salva voz/<n>.mp3 + voz/<n>.json (palavras com tempo).
import os, sys, json, re, subprocess, difflib, unicodedata
from num2words import num2words
from faster_whisper import WhisperModel
D = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(D, 'voz'); os.makedirs(O, exist_ok=True)
V = json.load(open(os.path.join(D, 'roteiros.json')))
W = WhisperModel('small', device='cpu', compute_type='int8')

def norm(s):
    s = s.lower().replace('%', ' por cento')
    s = re.sub(r'(\d)\s*\.\s*(\d{3})', r'\1\2', s); s = re.sub(r'\s*,00', '', s)
    s = re.sub(r'r\s*\$\s*(\d+)\b(?!\s*gb)', r'\1 reais', s); s = re.sub(r'r\s*\$', ' ', s)
    s = re.sub(r'(\d+) reais reais', r'\1 reais', s); s = re.sub(r'\bgb\b', 'gigas', s)
    s = re.sub(r'\d+', lambda m: ' ' + num2words(int(m.group()), lang='pt_BR') + ' ', s)
    s = unicodedata.normalize('NFKD', s); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('i phone', 'iphone').replace('whats app', 'whatsapp').replace('w f', 'wf').replace('dabliu efe', 'wf')
    return re.findall(r'[a-z]+', s)

def tts(texto, out, voz='pt-BR-AntonioNeural', rate='+4%'):
    for _ in range(4):
        r = subprocess.run(['edge-tts', '--proxy', os.environ.get('HTTPS_PROXY', ''), '--voice', voz, f'--rate={rate}', '--text', texto, '--write-media', out], capture_output=True)
        if r.returncode == 0: return
    raise SystemExit('edge-tts falhou')

def confere(mp3, ref, chaves):
    import numpy as np
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp3, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    segs, _ = W.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768, language='pt', word_timestamps=True, beam_size=5)
    pal = [w for s in segs for w in s.words]; txt = ' '.join(w.word.strip() for w in pal)
    a, b = norm(ref), norm(txt); sim = difflib.SequenceMatcher(None, a, b).ratio()
    falta = [k for k in chaves if ' '.join(norm(k)) not in ' '.join(b)]
    return sim, falta, txt, [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for w in pal]

if __name__ == '__main__':
    rel = []
    for v in V:
        if len(sys.argv) > 1 and str(v['n']) not in sys.argv[1:]: continue
        mp3 = os.path.join(O, f"{v['n']}.mp3")
        for tent, texto in enumerate([v['fala']] + v.get('alternativas', [])):
            tts(texto, mp3)
            sim, falta, txt, pal = confere(mp3, v['ref'], v['chaves'])
            print(v['n'], tent, round(sim, 3), falta, '|', txt, flush=True)
            if sim >= .93 and not falta: break
        json.dump({'texto': texto, 'ref': v['ref'], 'whisper': txt, 'sim': round(sim, 3), 'faltou': falta, 'palavras': pal}, open(mp3.replace('.mp3', '.json'), 'w'), ensure_ascii=False, indent=1)
        rel.append((v['n'], round(sim, 3), falta))
    print(rel)
