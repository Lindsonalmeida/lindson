# Saudações animadas do Leo · trilha + efeitos sonoros (conta Leandro, 14/11/2026).
# Reaproveita os efeitos sintetizados do ../motion-v1/audio.py (whoosh, pop, boom, chime), lê as deixas <id>.cues.json
# que o gerar.js escreve, mistura com um trecho de música do Kevin MacLeod (CC BY 4.0), abaixa a música sob os impactos,
# normaliza a -14 LUFS e junta ao vídeo mudo (AAC 192k 48 kHz).  Uso: python3 audio.py <pasta-out> <pasta-musica>
import sys, os, json, glob, subprocess, importlib.util, numpy as np
spec = importlib.util.spec_from_file_location('m1', os.path.join(os.path.dirname(__file__), '..', 'motion-v1', 'audio.py'))
m1 = importlib.util.module_from_spec(spec); sys.argv_bak = sys.argv; spec.loader.exec_module(m1)
SR, DUR = 48000, 8.0; N = int(SR * DUR); m1.DUR, m1.N = DUR, N
OUT, MUS = sys.argv[1], sys.argv[2]
# música por tema (arquivo, início do trecho em s): leve de manhã, calma à noite
TRILHA = {'royal': ('Inspired.mp3', 6), 'sol': ('Life_of_Riley.mp3', 4), 'laranja': ('Carefree.mp3', 2),
          'noite': ('Wholesome.mp3', 30), 'claro': ('Easy_Lemon.mp3', 3)}
NIVEL = {'boom': -13, 'whoosh': -15, 'whooshL': -19, 'chime': -15, 'pop': -18}
for cj in sorted(glob.glob(os.path.join(OUT, '*.cues.json'))):
    vid = cj[:-len('.cues.json')]
    if not os.path.exists(vid + '.mudo.mp4'): continue
    d = json.load(open(cj)); arq, ini = TRILHA[d['tema']]
    mus = m1.music(os.path.join(MUS, arq), ini)
    sfx = np.zeros((N, 2)); duck = np.ones(N); rng = np.random.default_rng(len(vid))
    for i, (t0, k) in enumerate(d['cues']):
        y = {'whoosh': lambda: m1.whoosh(.45, rng), 'whooshL': lambda: m1.whoosh(.9, rng, air=True), 'boom': lambda: m1.boom(rng),
             'chime': m1.chime, 'pop': lambda: m1.pop(rng, i)}[k]() * m1.db(NIVEL[k])
        a = int(t0 * SR); b = min(N, a + len(y)); st = m1.pan(y[:b - a], ((i % 3) - 1) * .25)
        sfx[a:b] += st
        if k == 'boom': duck[a:min(N, a + int(SR * .6))] = np.minimum(duck[a:min(N, a + int(SR * .6))], m1.db(-5))
    from scipy.ndimage import uniform_filter1d
    duck = uniform_filter1d(duck, int(SR * .08))
    mix = mus * duck[:, None] * m1.db(-3) + sfx
    tmp, fin = vid + '.mix.wav', vid + '.mixn.wav'
    m1.write_wav(tmp, mix); m1.loudnorm(tmp, fin)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', vid + '.mudo.mp4', '-i', fin, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', '-movflags', '+faststart', vid + '.mp4'], check=True)
    os.remove(tmp); os.remove(fin); print(vid + '.mp4', arq)
