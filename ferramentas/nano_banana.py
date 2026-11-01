"""Nano Banana (Gemini, geração e edição de imagem) pela API do Google. Conta Lindson, 01/11/2026.
Chave: de preferência em "Segredos de rede" do ambiente da nuvem (host generativelanguage.googleapis.com, cabeçalho x-goog-api-key);
o proxy coloca a chave sozinho e ela nunca aparece aqui. Também aceita a variável GEMINI_API_KEY. Nunca no repositório.
Uso:
  python3 ferramentas/nano_banana.py "prompt" saida.png                      # gera do zero
  python3 ferramentas/nano_banana.py "prompt" saida.png foto1.jpg logo.png   # edita/combina imagens de referência
  NANO_MODELO=gemini-3-pro-image-preview python3 ...                         # outro modelo (padrão: gemini-2.5-flash-image)
Uso previsto: mockups reais (boné e bandeira do Leo, identidade v3), capas e artes com fotos reais de clientes."""
import base64, json, mimetypes, os, sys, urllib.request, urllib.error
CHAVE = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
MODELO = os.environ.get('NANO_MODELO', 'gemini-2.5-flash-image')
if len(sys.argv) < 3: sys.exit(__doc__)
prompt, saida, refs = sys.argv[1], sys.argv[2], sys.argv[3:]
partes = [{'text': prompt}] + [{'inline_data': {'mime_type': mimetypes.guess_type(r)[0] or 'image/jpeg', 'data': base64.b64encode(open(r, 'rb').read()).decode()}} for r in refs]
corpo = json.dumps({'contents': [{'parts': partes}], 'generationConfig': {'responseModalities': ['IMAGE', 'TEXT']}}).encode()
req = urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{MODELO}:generateContent', data=corpo,
                             headers={'Content-Type': 'application/json', **({'x-goog-api-key': CHAVE} if CHAVE else {})})  # sem chave aqui: o proxy injeta o segredo de rede
try: r = json.load(urllib.request.urlopen(req, timeout=180))
except urllib.error.HTTPError as e: sys.exit(f'Erro {e.code}: {e.read().decode()[:400]}' + ('\nSem chave: confira o segredo de rede (host generativelanguage.googleapis.com, cabeçalho x-goog-api-key) e abra uma sessão nova.' if e.code in (401, 403) else ''))
img = [p['inlineData'] for c in r.get('candidates', []) for p in c.get('content', {}).get('parts', []) if 'inlineData' in p]
txt = [p['text'] for c in r.get('candidates', []) for p in c.get('content', {}).get('parts', []) if 'text' in p]
if not img: sys.exit('Nenhuma imagem voltou. ' + ' '.join(txt)[:400])
open(saida, 'wb').write(base64.b64decode(img[0]['data'])); print('ok:', saida, '·', ' '.join(txt)[:200])
