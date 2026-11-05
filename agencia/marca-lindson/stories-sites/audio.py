"""Som dos stories em vídeo (conta Pedro, 05/11/2026). Regra do Lindson (05/11): "nunca faça vídeos sem áudio, sempre narração fluida
que não pareça IA, VFX e SFX".
- Voz: narração na voz clonada do Lindson (narra.py), entra em 0,45 s.
- SFX sintetizados (mesmo sintetizador do motion do Leo, agencia/clientes/leo-pinto/motion-v1/audio.py): whoosh na entrada do aparelho,
  pop em cada texto/selo, impacto leve na palavra-chave, cliques suaves quando a rolagem começa. Deixas em cues-sNN.json (gerar.js).
- Trilha: Kevin MacLeod (incompetech.com), CC BY 4.0, baixinha e abaixada sob a voz (ducking pelo envelope da voz).
- Mix: loudnorm em 2 passadas para -14 LUFS, pico real <= -1,5 dBTP, AAC 192k 48 kHz, trocando o áudio do MP4.
Uso: python3 audio.py <pasta-saida-com-sNN.mp4> <pasta-voz-com-sNN.wav> <pasta-musicas> <pasta-quadros> [4 5 6 7]"""
import sys, os, json, subprocess, importlib.util, numpy as np
D = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('leo_audio', os.path.join(D, '..', '..', 'clientes', 'leo-pinto', 'motion-v1', 'audio.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
SR, FF, db = L.SR, L.FF, L.db
# trilha por vídeo: arquivo, título (crédito), início do trecho (s)
MUSICA = {'4': ('Carefree.mp3', 'Carefree', 2.0), '5': ('Life_of_Riley.mp3', 'Life of Riley', 4.0),
          '6': ('Wholesome.mp3', 'Wholesome', 6.0), '7': ('Carefree.mp3', 'Carefree', 38.0)}
VOZ_EM = 0.45


def loudnorm(src, dst, tp=-2.3):
    """-14 LUFS em 2 passadas. O alvo de pico fica em -2,3 dBTP porque o AAC sobe o pico real uns 0,3-0,5 dB:
    assim o MP4 final fica <= -1,5 dBTP (conferido com ebur128)."""
    a = subprocess.run([FF, '-hide_banner', '-i', src, '-af', f'loudnorm=I=-14:TP={tp}:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
    j = json.loads(a[a.rindex('{'):a.rindex('}') + 1])
    af = (f"loudnorm=I=-14:TP={tp}:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
          f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run([FF, '-v', 'error', '-y', '-i', src, '-af', af, '-ar', str(SR), '-c:a', 'pcm_s16le', dst], check=True)


def ler(path, start=0.0, dur=None, ch=2):
    cmd = [FF, '-v', 'error', '-ss', str(start)] + (['-t', str(dur)] if dur else []) + ['-i', path, '-f', 'f32le', '-ac', str(ch), '-ar', str(SR), '-']
    a = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64)
    return a.reshape(-1, ch) if ch > 1 else a


def um(saida, vozes, musicas, quadros, s):
    mp4 = os.path.join(saida, f's0{s}.mp4')
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4], capture_output=True, text=True).stdout)
    N = int(dur * SR); t = np.arange(N) / SR
    voz = ler(os.path.join(vozes, f's0{s}.wav'), ch=1); voz = voz / (np.abs(voz).max() + 1e-9) * db(-1)
    v = np.zeros(N); a = int(VOZ_EM * SR); b = min(N, a + len(voz)); v[a:b] = voz[:b - a]
    # trilha com fade-in 0,4 s e fade-out 0,8 s, abaixada sob a voz (envelope suavizado, ataque 60 ms, volta 350 ms)
    arq, titulo, ini = MUSICA[s]
    m = np.zeros((N, 2)); mm = ler(os.path.join(musicas, arq), ini, dur + 1); m[:min(N, len(mm))] = mm[:N]
    m = m / (np.abs(m).max() + 1e-9) * np.clip(t / .4, 0, 1)[:, None] * np.clip((dur - t) / .8, 0, 1)[:, None]
    fr = int(SR * .02); rms = np.sqrt(np.convolve(v ** 2, np.ones(fr) / fr, 'same')); fala = (rms > db(-38)).astype(float)
    env = np.zeros(N); e = 0.0; at, rl = np.exp(-1 / (SR * .06)), np.exp(-1 / (SR * .35))
    for i in range(0, N, 48):                                   # 1 ms por passo (rápido e suficiente)
        alvo = fala[i]; c = at if alvo > e else rl; e = alvo + (e - alvo) * c ** 48; env[i:i + 48] = e
    trilha = m * (db(-17) + (db(-27) - db(-17)) * env)[:, None]   # -17 dB sem voz, -27 dB sob a voz
    # efeitos
    cues = json.load(open(os.path.join(quadros, f's0{s}', 'cues.json'))); rng = np.random.default_rng(int(s) * 77); sfx = np.zeros((N, 2)); n_pop = 0
    def poe(st, t0, lvl):
        i = max(0, int(t0 * SR)); j = min(N, i + len(st)); sfx[i:j] += st[:j - i] * db(lvl)
    for c in cues:
        if c['k'] == 'whoosh': poe(L.pan(L.whoosh(.45, rng), np.linspace(-.4, .4, int(SR * .7))), c['t'] - .08, -15)
        elif c['k'] == 'pop': poe(L.pan(L.pop(rng, n_pop), ((n_pop * 37) % 9 - 4) / 14), c['t'], -21); n_pop += 1
        elif c['k'] == 'impacto': poe(L.pan(L.boom(rng), 0), c['t'], -19); poe(L.pan(L.pop(rng, 3), 0), c['t'], -22)
    t_rol = dur * .1 + .1                                       # a rolagem começa depois de 10% do vídeo (gravar.js)
    for k in range(3): poe(L.pan(L.key(rng), rng.uniform(-.25, .25)), t_rol + k * .16, -28)
    mix = v[:, None] * np.ones((1, 2)) + trilha + sfx
    mix /= max(1.0, np.abs(mix).max() / db(-1))
    tmp, fin, nov = (os.path.join(saida, f'.s0{s}-{x}') for x in ('mix.wav', 'norm.wav', 'som.mp4'))
    L.write_wav(tmp, mix)
    for tp in (-2.3, -3.3, -4.3, -5.3):                          # se o AAC passar de -1,5 dBTP, baixa o alvo de pico e refaz
        loudnorm(tmp, fin, tp)
        subprocess.run([FF, '-v', 'error', '-y', '-i', mp4, '-i', fin, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', str(SR),
                        '-shortest', '-movflags', '+faststart', nov], check=True)
        r = subprocess.run([FF, '-hide_banner', '-i', nov, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
        lufs, pk = float(r[r.rindex('I:'):].split()[1]), float(r[r.rindex('Peak:'):].split()[1])
        if pk <= -1.5: break
    os.replace(nov, mp4); os.remove(tmp); os.remove(fin)
    print(f'    {lufs} LUFS · pico real {pk} dBTP')
    print(f's0{s}', round(dur, 2), 's ·', titulo, '·', len(cues), 'deixas')


if __name__ == '__main__':
    for s in sys.argv[5:] or ['4', '5', '6', '7']: um(*sys.argv[1:5], s)
