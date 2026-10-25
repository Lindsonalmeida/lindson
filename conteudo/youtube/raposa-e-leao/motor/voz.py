"""Narração fluida (Microsoft Antonio neural) com tempo de cada palavra.
python3 voz.py <pasta> "<texto>"  -> gera voz.wav e palavras.json"""
import asyncio,sys,os,json,subprocess,edge_tts
P,txt=sys.argv[1],sys.argv[2];os.makedirs(P,exist_ok=True)
async def main():
    c=edge_tts.Communicate(txt,'pt-BR-AntonioNeural',rate='+7%',pitch='-6Hz',proxy=os.environ.get('HTTPS_PROXY'),boundary='WordBoundary')
    ws=[];mp=open(P+'/voz.mp3','wb')
    async for ch in c.stream():
        if ch['type']=='audio':mp.write(ch['data'])
        elif ch['type']=='WordBoundary':ws.append([ch['text'],round(ch['offset']/1e7,3)])
    mp.close();json.dump(ws,open(P+'/palavras.json','w'),ensure_ascii=False)
asyncio.run(main())
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',P+'/voz.mp3','-ar','44100','-ac','1',P+'/voz.wav'],check=True);os.remove(P+'/voz.mp3')
print(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',P+'/voz.wav']).decode().strip(),'s')
