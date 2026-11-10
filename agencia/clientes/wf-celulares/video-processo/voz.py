# Narração do vídeo do processo WF com a voz 6 do Lindson (mesmos parâmetros e pós do gerar_voz_lindson.py).
# Conta Leandro, 10/11/2026. Referência fora do Git: agencia/marca-lindson/voz/ref6.wav. "WF" escrito "dábliu éfe".
# Uso: python3 voz.py  -> voz/bN.wav (um por cena) ; fallback: python3 voz.py edge (voz D do VEKTOR, provisória)
import os, sys, subprocess
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.abspath(os.path.join(D, '..', '..', '..', '..'))
edge0 = len(sys.argv) > 1 and sys.argv[1] == 'edge'
SAI = os.path.join(D, 'voz-edge' if edge0 else 'voz'); os.makedirs(SAI, exist_ok=True)
BLOCOS = [
 'Olha o que eu fiz pela dábliu éfe Celulares. Uma loja de iPhone, aqui de São Luís. Antes, o logo tinha muito efeito e sumia na tela do celular.',
 'Primeiro, eu fiz a engenharia reversa: o perfil, a foto, o arroba, tudo que o cliente via. O produto era bom, mas a marca não contava isso.',
 'Daí nasceu a nova marca. Limpa, moderna, cor de titânio. E uma ideia forte: celular com procedência.',
 'Todo iPhone sai com laudo: testado, com garantia e com nota. Isso vira etiqueta, cartão e conversa de venda.',
 'Depois, o manual da marca, com vinte e duas páginas: cores, letras, fachada e até a etiqueta do laudo.',
 'E o feed: nove artes escuras, com cara de vitrine de luxo.',
 'Quer isso na sua loja? Me chama no direct.',
]
POS = ('silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.12:stop_threshold=-45dB,atempo=1.06,highpass=f=90,'
       'equalizer=f=3500:t=q:w=1:g=3,highshelf=f=8000:g=3,acompressor=threshold=-20dB:ratio=3:attack=5:release=60:makeup=3,loudnorm=I=-15:TP=-1')
edge = len(sys.argv) > 1 and sys.argv[1] == 'edge'
if not edge:
    import torch, torchaudio as ta
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
    torch.set_num_threads(os.cpu_count())
    m = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
    REF = os.path.join(RAIZ, 'agencia/marca-lindson/voz/ref6.wav')
for i, b in enumerate(BLOCOS, 1):
    bruto, out = os.path.join(SAI, f'b{i}-bruto.wav'), os.path.join(SAI, f'b{i}.wav')
    if os.path.exists(out) and not edge: continue
    if edge:
        subprocess.run(['edge-tts', '--proxy', os.environ.get('HTTPS_PROXY', ''), '--voice', 'pt-BR-AntonioNeural', '--rate', '+4%', '--text', b, '--write-media', bruto.replace('.wav', '.mp3')], check=True)
        bruto = bruto.replace('.wav', '.mp3')
    else:
        w = m.generate(b, language_id='pt', audio_prompt_path=REF, exaggeration=0.75, cfg_weight=0.3, temperature=0.8)
        ta.save(bruto, w, m.sr)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', bruto, '-af', POS, '-ar', '44100', '-ac', '1', out], check=True)
    print('ok', out, flush=True)
