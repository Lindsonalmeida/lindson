# Renderiza cena.js -> painel cru (sem texto). Uso: python3 render.py
import os, base64, urllib.parse
from playwright.sync_api import sync_playwright
H = os.path.dirname(os.path.abspath(__file__))
THREE = '/tmp/claude-0/-home-user-lindson/86a1f243-8cb7-59cd-a94a-2c27aad57cb6/scratchpad/node_modules/three'
W, Hh = 4860, 2160
hp = os.path.join(H, '_cena.html')
open(hp, 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style>
<script type="importmap">{{"imports":{{"three":"file://{THREE}/build/three.module.js","three/addons/":"file://{THREE}/examples/jsm/"}}}}</script>
<script type="module" src="file://{H}/cena.js"></script></head><body></body></html>''')
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux/chrome' if os.path.exists('/opt/pw-browsers/chromium-1243/chrome-linux/chrome') else '/usr/bin/google-chrome', args=['--allow-file-access-from-files', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    p = b.new_page(); p.on('console', lambda m: print('js:', m.text))
    p.goto('file://' + hp + '?' + urllib.parse.urlencode({'tex': 'file://' + H + '/tex', 'w': W, 'h': Hh}))
    p.wait_for_function('window.ready===true', timeout=60000)
    d = p.evaluate('window.render()'); open(os.path.join(H, 'cru.png'), 'wb').write(base64.b64decode(d.split(',')[1])); b.close()
os.remove(hp); print('ok')
