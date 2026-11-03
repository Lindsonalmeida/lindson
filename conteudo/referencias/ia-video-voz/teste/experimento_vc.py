"""Etapa 2 do experimento: passar a melhor voz gerada pelo conversor de voz (ChatterboxVC) com o timbre do Lindson."""
import glob, json, numpy as np, librosa, soundfile as sf, torch
from resemblyzer import VoiceEncoder as Juiz, preprocess_wav
juiz = Juiz('cpu'); reais = ['a1.wav', 'a2.wav'] + sorted(glob.glob('vid*.wav'))
E = []
for f in reais:
    w, _ = librosa.load(f, sr=16000)
    for i in range(0, len(w) - 64000, 96000):
        p = w[i:i + 96000]
        if np.sqrt((p ** 2).mean()) > .01: E.append(juiz.embed_utterance(preprocess_wav(p, 16000)))
cent = np.mean(E, 0); cent /= np.linalg.norm(cent)
nota = lambda w, sr: float(juiz.embed_utterance(preprocess_wav(w, sr)) @ cent)
from chatterbox.vc import ChatterboxVC
vc = ChatterboxVC.from_pretrained('cpu')
todos16 = [librosa.load(f, sr=16000)[0] for f in reais]
xv = torch.stack([vc.s3gen.speaker_encoder.inference(torch.from_numpy(w[None]).float()) for w in todos16 if len(w) > 32000]).mean(0)
r = json.load(open('experimento.json')); melhor = max(r['res'], key=lambda x: x[1])[0][0]
print('melhor variante do TTS:', melhor, flush=True)
w0, sr0 = sf.read('a1.wav'); sf.write('ref-alvo2.wav', w0[int(36 * sr0):int(46 * sr0)], sr0)
for alvo, media in [('ref-melhor.wav', False), ('ref-melhor.wav', True), ('ref-alvo2.wav', True)]:
    ns = []
    for s in (0, 1):
        vc.set_target_voice(alvo)
        if media: vc.ref_dict['embedding'] = xv.to(vc.ref_dict['embedding'])
        out = vc.generate(f'var{melhor}-{s}.wav').squeeze().numpy()
        sf.write(f'vc-{alvo[4:-4]}-{int(media)}-{s}.wav', out, vc.sr); ns.append(nota(out, vc.sr))
    print(f'VC alvo {alvo} média={media}: nota {np.mean(ns):.3f}', flush=True)
print('FIM', flush=True)
