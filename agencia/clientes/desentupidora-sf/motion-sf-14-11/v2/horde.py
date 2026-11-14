# Gera foto realista com IA grátis (Stable Horde, chave anônima) · conta Zuleide 14/11/2026
# Uso: python3 horde.py saida.webp "prompt" [modelo] [w] [h]
import sys, time, json, urllib.request
out, prompt = sys.argv[1], sys.argv[2]; modelo = sys.argv[3] if len(sys.argv) > 3 else 'Juggernaut XL'
w = int(sys.argv[4]) if len(sys.argv) > 4 else 768; h = int(sys.argv[5]) if len(sys.argv) > 5 else 1344
H = {'apikey': '0000000000', 'Content-Type': 'application/json', 'Client-Agent': 'motion-gen:1:anon'}
def req(u, d=None, m='GET'):
    r = urllib.request.Request('https://stablehorde.net/api/v2/' + u, data=json.dumps(d).encode() if d else None, headers=H, method=m)
    return json.load(urllib.request.urlopen(r, timeout=60))
neg = 'text, watermark, logo, letters, cartoon, illustration, 3d render, deformed, blurry, lowres'
j = req('generate/async', {'prompt': prompt + ' ### ' + neg, 'params': {'width': w, 'height': h, 'steps': 30 if 'XL' in modelo else 8, 'cfg_scale': 5 if 'XL' in modelo else 1, 'sampler_name': 'k_dpmpp_2m' if 'XL' in modelo else 'k_euler', 'karras': True, 'n': 1},
          'models': [modelo], 'nsfw': False, 'censor_nsfw': True, 'r2': True}, 'POST')
i = j['id']; print('id', i, j.get('kudos'), flush=True)
for _ in range(240):
    s = req('generate/check/' + i)
    if s.get('done'): break
    if s.get('faulted'): sys.exit('falhou')
    time.sleep(5)
g = req('generate/status/' + i)['generations'][0]
urllib.request.urlretrieve(g['img'], out); print('ok', out, g.get('model'), flush=True)
