"""Voz do VEKTOR: frases pré-gravadas com voz neural masculina + efeito de IA (conta Leandro, 10/11/2026).

O Lindson pediu "uma voz marcante de IA, masculina". O padrão é a variante B, "grave e imponente": pt-BR-AntonioNeural
com rate -10% e pitch -18Hz, mais flanger leve, eco duplo e graves +3 dB. As outras variantes ficam em VARIANTES.

Uso:
  python3 gerar_voz_vektor.py frases.txt /home/user/centrallindsonalmeida/painel/comando/voz [B]
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
    'C': ('-6%', '-10Hz', "asplit[a][b];[b]afftfilt=real='hypot(re,im)*cos(0)':imag='hypot(re,im)*sin(0)':win_size=512:overlap=0.75,volume=0.55[r];[a][r]amix=inputs=2:weights=1 0.8,highpass=f=100,aecho=0.8:0.5:25:0.2,loudnorm=I=-15"),
}


def norm(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return ' '.join(re.sub(r'[^a-z0-9 ]', ' ', t).split())


def chave(t):
    h = 0x811c9dc5
    for b in norm(t).encode('utf-8'):
        h ^= b; h = (h * 0x01000193) & 0xffffffff
    return format(h, '08x')


def main():
    src, out = sys.argv[1], sys.argv[2]; var = sys.argv[3] if len(sys.argv) > 3 else 'B'
    rate, pitch, fx = VARIANTES[var]; os.makedirs(out, exist_ok=True)
    frases = [l.strip() for l in open(src, encoding='utf-8') if l.strip() and not l.startswith('#')]
    mapa = {}; novas = 0
    for f in frases:
        k = chave(f); arq = f'{k}.mp3'; mapa[k] = arq; dst = os.path.join(out, arq)
        if os.path.exists(dst): continue
        tmp = dst + '.base.mp3'
        cmd = ['edge-tts', '--voice', 'pt-BR-AntonioNeural', f'--rate={rate}', f'--pitch={pitch}', '--text', f, '--write-media', tmp]
        if os.environ.get('HTTPS_PROXY'): cmd[1:1] = ['--proxy', os.environ['HTTPS_PROXY']]
        subprocess.run(cmd, check=True, capture_output=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af', fx, '-ac', '1', '-b:a', '64k', dst], check=True)
        os.remove(tmp); novas += 1
    open(os.path.join(out, 'voz.js'), 'w').write('window.__VOZ=' + json.dumps(mapa) + ';\n')
    print(f'{len(frases)} frases, {novas} novas, variante {var} -> {out}')


if __name__ == '__main__':
    main()
