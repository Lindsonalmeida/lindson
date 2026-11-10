# Black Friday Jaci: vídeo de cada story (9:16) com narração feminina neutra (edge-tts pt-BR-FranciscaNeural),
# trilha Kevin MacLeod (CC BY 4.0) em ducking, SFX sintetizado (whoosh na entrada) e VFX (zoom lento + flash de luz).
# Narração v2 (10/11, conta Zuleide): texto fonético (Jáci, bê efe) — tabela em README.md, seção Pronúncia.
# Também gera os criativos 4:5 dos anúncios. Uso: python3 video.py <pasta com storyN-limpo.png>  (conta Pedro, 10/11/2026)
import sys, os, asyncio, subprocess, edge_tts
D = sys.argv[1]; A = os.path.join(D, 'audio'); os.makedirs(A, exist_ok=True)
FALAS = {
 1: "Black Friday na Clínica Doutora Jáci Cunha! De vinte e três a trinta de novembro, condição especial em toxina botulínica e preenchimento.",
 2: "Antes de correr atrás da promoção mais barata, lembre: o seu rosto não é liquidação. Aqui muda a condição, não o cuidado.",
 3: "A toxina botulínica relaxa os músculos que marcam a expressão. A dose é decidida na avaliação, para suavizar sem deixar o rosto parado.",
 4: "O preenchimento com ácido hialurônico é planejado para o seu rosto: lábios, mandíbula, queixo. Só quando há indicação.",
 5: "E aí, qual te dá mais vontade? Toxina botulínica ou preenchimento? Vota aqui!",
 6: "Funciona assim: mande bê efe vinte e seis no WhatsApp, marque sua avaliação de trinta minutos e, se for indicado, a condição vale até trinta de novembro.",
 7: "Dói? Fica artificial? Quanto tempo dura? Manda a sua pergunta aqui, que a Doutora Jáci responde nos stories.",
 8: "Os horários são poucos, o cuidado, não. Chama no WhatsApp para saber a condição de Black Friday!",
}
MUS = os.path.join(A, 'Inspired.mp3')
if not os.path.exists(MUS):
    subprocess.run(['curl', '-sSL', '-o', MUS, 'https://incompetech.com/music/royalty-free/mp3-royaltyfree/Inspired.mp3'], check=True)
async def tts(i, t):
    await edge_tts.Communicate(t, 'pt-BR-FranciscaNeural', rate='+4%', proxy=os.environ.get('HTTPS_PROXY'), connect_timeout=30).save(f'{A}/n{i}.mp3')
async def todas(): await asyncio.gather(*[tts(i, t) for i, t in FALAS.items()])
asyncio.run(todas())
def dur(f): return float(subprocess.check_output(['ffprobe','-v','0','-show_entries','format=duration','-of','csv=p=0',f]))
# whoosh: ruído rosa filtrado com envelope
subprocess.run(['ffmpeg','-y','-v','error','-f','lavfi','-i','anoisesrc=c=pink:d=0.6:a=0.6','-af','highpass=f=300,lowpass=f=4000,afade=t=in:d=0.35,afade=t=out:st=0.35:d=0.25',f'{A}/whoosh.wav'],check=True)
lista = []; off = 0.0
for i in range(1, 9):
    n = f'{A}/n{i}.mp3'; T = round(dur(n) + 1.6, 2); fr = int(T * 30)
    out = f'{D}/story{i}.mp4'
    vf = (f"scale=2160:-1,zoompan=z='1+0.06*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps=30,"
          f"eq=brightness='0.25*max(0,1-t/0.25)':eval=frame,format=yuv420p")
    af = (f"[1:a]adelay=500|500,volume=1.25,asplit[v][v2];[2:a]atrim={off}:{off+T},asetpts=PTS-STARTPTS,volume=0.22,afade=t=in:d=0.4,afade=t=out:st={T-0.6}:d=0.6[m];"
          f"[m][v]sidechaincompress=threshold=0.05:ratio=6:release=300[md];[3:a]volume=0.5[w];[md][v2][w]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5[a]")
    subprocess.run(['ffmpeg','-y','-v','error','-i',f'{D}/story{i}-limpo.png','-i',n,'-i',MUS,'-i',f'{A}/whoosh.wav',
        '-filter_complex',f'[0:v]{vf}[vv];{af}','-map','[vv]','-map','[a]','-t',str(T),'-c:v','libx264','-crf','20','-c:a','aac','-b:a','192k','-ar','48000',out],check=True)
    lista.append(out); off += T; print(out, T)
with open(f'{A}/lista.txt','w') as f: f.write(''.join(f"file '{x}'\n" for x in lista))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',f'{A}/lista.txt','-c','copy',f'{D}/sequencia-completa.mp4'],check=True)
# 4:5 dos anúncios: miolo da arte + rodapé com CRO
from PIL import Image
for i in (1, 2, 6, 8):
    im = Image.open(f'{D}/story{i}-limpo.png').convert('RGB'); y = {1:150,2:300,6:230,8:260}[i]
    c = im.crop((0, y, 1080, y + 1350 - 150)); W = Image.new('RGB', (1080, 1350)); W.paste(c, (0, 0)); W.paste(im.crop((0, 1770, 1080, 1920)), (0, 1200))
    W.save(f'{D}/ad-4x5-story{i}.jpg', quality=92)
print('ok')
