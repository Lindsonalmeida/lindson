import time, torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
t=time.time(); m=ChatterboxMultilingualTTS.from_pretrained(device="cpu"); print('carregou',round(time.time()-t),'s',flush=True)
txt="Oi, Lindson! Esse é o primeiro teste do nosso aplicativo de clone de voz, rodando sem placa de vídeo. No seu notebook vai ser bem mais rápido."
t=time.time(); w=m.generate(txt, language_id="pt", audio_prompt_path="ref.wav")
ta.save("saida_clone.wav", w, m.sr); print('gerou',round(time.time()-t),'s', w.shape[-1]/m.sr,'s de áudio',flush=True)
