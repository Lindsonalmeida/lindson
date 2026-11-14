# Narração Antonio (edge-tts pt-BR-AntonioNeural +4%, padrão aprovado em wf-celulares/motion-02) · conta Zuleide · 14/11/2026
# Gera voz/<n>.mp3 + voz/<n>.json com o tempo de cada palavra (fronteiras de palavra do próprio edge-tts).
import os, sys, json, asyncio, edge_tts
D = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(D, 'voz'); os.makedirs(O, exist_ok=True)
async def um(v):
    c = edge_tts.Communicate(v['fala'], 'pt-BR-AntonioNeural', rate='+4%', proxy=os.environ.get('HTTPS_PROXY'), boundary='WordBoundary')
    pal = []; f = open(os.path.join(O, f"{v['n']}.mp3"), 'wb')
    async for ch in c.stream():
        if ch['type'] == 'audio': f.write(ch['data'])
        elif ch['type'] == 'WordBoundary': pal.append([ch['text'], round(ch['offset'] / 1e7, 3), round((ch['offset'] + ch['duration']) / 1e7, 3)])
    f.close(); json.dump({'texto': v['fala'], 'palavras': pal}, open(os.path.join(O, f"{v['n']}.json"), 'w'), ensure_ascii=False)
    print(v['n'], len(pal), pal[-1][2] if pal else 0)
for v in json.load(open(os.path.join(D, 'roteiros.json'))):
    if len(sys.argv) == 1 or str(v['n']) in sys.argv[1:]: asyncio.run(um(v))
