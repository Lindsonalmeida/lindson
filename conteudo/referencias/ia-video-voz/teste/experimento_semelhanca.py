"""Experimento: o que deixa a voz clonada mais parecida com a do Lindson. Juiz independente: Resemblyzer."""
import glob, json, sys, time, numpy as np, librosa, soundfile as sf, torch
from resemblyzer import VoiceEncoder as Juiz, preprocess_wav
torch.manual_seed(0)
juiz = Juiz('cpu')
reais = ['a1.wav', 'a2.wav'] + sorted(glob.glob('vid*.wav'))
# pedaços de 6 s da voz real
ped = []
for f in reais:
    w, _ = librosa.load(f, sr=16000)
    for i in range(0, len(w) - 16000 * 4, 16000 * 6):
        p = w[i:i + 16000 * 6]
        if np.sqrt((p ** 2).mean()) > .01: ped.append((f, i / 16000, p))
E = np.array([juiz.embed_utterance(preprocess_wav(p, 16000)) for _, _, p in ped])
cent = E.mean(0); cent /= np.linalg.norm(cent)
# teto: cada pedaço real contra a média dos outros
teto = [float(E[k] @ (lambda c: c / np.linalg.norm(c))(np.delete(E, k, 0).mean(0))) for k in range(len(E))]
print(f'REAL (teto): média {np.mean(teto):.3f}  mín {np.min(teto):.3f}  pedaços {len(E)}', flush=True)
nota = lambda w, sr: float(juiz.embed_utterance(preprocess_wav(w, sr)) @ cent)

from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from chatterbox.models.s3tokenizer import S3_SR
m = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
# melhores trechos de 10 s para o prompt (nota do juiz em janelas de 10 s, passo 2 s)
cand = []
for f in reais:
    w, _ = librosa.load(f, sr=16000)
    for i in range(0, len(w) - 160000, 32000):
        p = w[i:i + 160000]
        if (np.abs(p) > .02).mean() > .25: cand.append((nota(p, 16000), f, i / 16000))
cand.sort(reverse=True); print('melhores trechos:', [(round(a, 3), f, t) for a, f, t in cand[:4]], flush=True)
def recorta(f, t, nome):
    w, sr = sf.read(f); sf.write(nome, w[int(t * sr):int((t + 10) * sr)], sr); return nome
bom = recorta(cand[0][1], cand[0][2], 'ref-melhor.wav')
# média da identidade em todo o áudio real (as duas "impressões digitais" que o modelo usa)
todos16 = [librosa.load(f, sr=16000)[0] for f in reais]
ve_media = torch.from_numpy(m.ve.embeds_from_wavs(todos16, sample_rate=S3_SR)).mean(0, keepdim=True)
xv = torch.stack([m.s3gen.speaker_encoder.inference(torch.from_numpy(w[None]).float()) for w in todos16 if len(w) > 32000]).mean(0)

txt = 'Fala, pessoal, aqui é o Lindson. Hoje eu vou te mostrar como conseguir mais clientes pelo Instagram, sem gastar nada.'
variantes = [
    ('1 atual (trecho 1:06, padrão)', 'ref-lindson-limpa.wav', False, .5, .5, .8),
    ('2 identidade média de todo o áudio', 'ref-lindson-limpa.wav', True, .5, .5, .8),
    ('3 melhor trecho', bom, False, .5, .5, .8),
    ('4 melhor trecho + identidade média', bom, True, .5, .5, .8),
    ('5 = 4 + ritmo mais solto (cfg .3)', bom, True, .5, .3, .8),
    ('6 = 4 + menos variação (temp .6)', bom, True, .45, .5, .6),
]
res = []
for nome, ref, media, ex, cfg, temp in variantes:
    t0 = time.time(); m.prepare_conditionals(ref, exaggeration=ex)
    if media:
        m.conds.t3.speaker_emb = ve_media.to(m.conds.t3.speaker_emb)
        m.conds.gen['embedding'] = xv.to(m.conds.gen['embedding'])
    notas = []
    for s in (0, 1):
        torch.manual_seed(s)
        w = m.generate(txt, language_id='pt', exaggeration=ex, cfg_weight=cfg, temperature=temp).squeeze().cpu().numpy()
        notas.append(nota(w, m.sr)); sf.write(f'var{nome[0]}-{s}.wav', w, m.sr)
    res.append((nome, float(np.mean(notas)))); print(f'{nome}: nota {np.mean(notas):.3f} ({notas[0]:.3f}/{notas[1]:.3f}) em {time.time() - t0:.0f}s', flush=True)
json.dump({'teto': float(np.mean(teto)), 'res': res, 'melhor_trecho': cand[0][1:]}, open('experimento.json', 'w'), ensure_ascii=False)
print('FIM', flush=True)
