"""Voz do VEKTOR: frases pré-gravadas com voz neural masculina + efeito de IA (conta Leandro, 10/11/2026).

O Lindson pediu "uma voz marcante de IA, masculina" e depois "QUERO UMA VOZ FLUIDA, QUE FALE AS PALAVRAS CORRETAS".
O padrão agora é a variante D (10/11): pt-BR-AntonioNeural com rate +0% e pitch -12Hz e efeito leve (graves +2,5 dB, brilho +2 dB,
chorus curto, eco curto), masculina e com brilho de IA sem atrapalhar a dicção. A, B e C continuam em VARIANTES.
Pronúncia: voz/pronuncia.json (pares [como está na tela, como falar]) vale só para o texto enviado ao TTS; a chave é a frase da tela.
Números de 0 a 100 viram palavras. Uma fala completa = um clipe (frases.txt traz as falas inteiras, ver frases.py).

Uso:
  python3 gerar_voz_vektor.py frases.txt /home/user/centrallindsonalmeida/painel/comando/voz [D]
- frases.txt traz uma frase por linha, exatamente como a página fala, uma frase por vez.
- Saída: <chave>.mp3 para cada frase e voz.js (window.__VOZ = {chave: 'arquivo.mp3'}).
- Chave: FNV-1a 32 bits, em hex, da frase normalizada (minúsculas, sem acento, só letras, números e espaço,
  espaços colapsados). A página calcula a mesma chave em vkChave(frase).
- Só grava o que falta. Rode de novo quando entrar frase nova.
Requer edge-tts (usa o proxy pelo HTTPS_PROXY) e ffmpeg.
"""
import os, re, subprocess, sys, unicodedata, json

VARIANTES = {
    'A': ('-6%', '-10Hz', "highpass=f=90,chorus=0.6:0.85:28|40:0.35|0.25:0.3|0.4:1.5|1.8,aecho=0.8:0.6:35:0.18,equalizer=f=3200:t=q:w=1:g=3,loudnorm=I=-15"),
    'B': ('-10%', '-18Hz', "highpass=f=70,flanger=delay=1:depth=2:regen=-20:width=60:speed=0.3,aecho=0.8:0.7:60|120:0.25|0.12,equalizer=f=150:t=q:w=1:g=3,loudnorm=I=-15"),
    'D': ('+0%', '-12Hz', "highpass=f=80,equalizer=f=160:t=q:w=1:g=2.5,equalizer=f=3000:t=q:w=1:g=2,chorus=0.5:0.9:20:0.15:0.25:1.2,aecho=0.8:0.4:22:0.08,loudnorm=I=-15"),
    'C': ('-6%', '-10Hz', "asplit[a][b];[b]afftfilt=real='hypot(re,im)*cos(0)':imag='hypot(re,im)*sin(0)':win_size=512:overlap=0.75,volume=0.55[r];[a][r]amix=inputs=2:weights=1 0.8,highpass=f=100,aecho=0.8:0.5:25:0.2,loudnorm=I=-15"),
}


def norm(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return ' '.join(re.sub(r'[^a-z0-9 ]', ' ', t).split())


UN = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
DZ = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
def extenso(n): return UN[n] if n < 20 else DZ[n // 10] + (' e ' + UN[n % 10] if n % 10 else '') if n < 100 else 'cem' if n == 100 else str(n)
PRON = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pronuncia.json'), encoding='utf-8'))
def pronuncia(t):
    for de, para in PRON:
        t = re.sub(r'(?<![\w])' + re.escape(de) + r'(?![\w])', para, t, flags=re.I)
    return re.sub(r'\b\d{1,3}\b', lambda m: extenso(int(m.group())) if int(m.group()) <= 100 else m.group(), t)


def chave(t):
    h = 0x811c9dc5
    for b in norm(t).encode('utf-8'):
        h ^= b; h = (h * 0x01000193) & 0xffffffff
    return format(h, '08x')


def gera(f, out, var):
    rate, pitch, fx = VARIANTES[var]; k = chave(f); dst = os.path.join(out, f'{k}.mp3'); tmp = dst + '.base.mp3'
    cmd = ['edge-tts', '--voice', 'pt-BR-AntonioNeural', f'--rate={rate}', f'--pitch={pitch}', '--text', pronuncia(f), '--write-media', tmp]
    if os.environ.get('HTTPS_PROXY'): cmd[1:1] = ['--proxy', os.environ['HTTPS_PROXY']]
    for tentativa in range(3):
        try: subprocess.run(cmd, check=True, capture_output=True, timeout=60); break
        except Exception:
            if tentativa == 2: raise
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af', fx, '-ac', '1', '-b:a', '40k', dst], check=True)
    os.remove(tmp)


def main():
    from concurrent.futures import ThreadPoolExecutor
    src, out = sys.argv[1], sys.argv[2]; var = sys.argv[3] if len(sys.argv) > 3 else 'D'
    os.makedirs(out, exist_ok=True)
    frases = list(dict.fromkeys(l.strip() for l in open(src, encoding='utf-8') if l.strip() and not l.startswith('#')))
    feito_p = os.path.join(out, '_gerado.txt')  # chave → variante|texto falado: refaz o clipe quando a pronúncia ou a variante muda
    antes = dict(l.rstrip('\n').split('\t', 1) for l in open(feito_p, encoding='utf-8')) if os.path.exists(feito_p) else {}
    mapa, fazer, assin = {}, [], {}
    for f in frases:
        k = chave(f); mapa[k] = f'{k}.mp3'; assin[k] = var + '|' + pronuncia(f)
        if not os.path.exists(os.path.join(out, mapa[k])) or antes.get(k) != assin[k]: fazer.append(f)
    with ThreadPoolExecutor(8) as ex: list(ex.map(lambda f: gera(f, out, var), fazer))
    for arq in os.listdir(out):  # apaga clipes que saíram da lista
        if arq.endswith('.mp3') and arq[:-4] not in mapa: os.remove(os.path.join(out, arq))
    open(feito_p, 'w', encoding='utf-8').write(''.join(f'{k}\t{v}\n' for k, v in assin.items()))
    open(os.path.join(out, 'voz.js'), 'w').write('window.__VOZ=' + json.dumps(mapa) + ';\n')
    print(f'{len(frases)} frases, {len(fazer)} geradas, variante {var} -> {out}')


if __name__ == '__main__':
    main()
