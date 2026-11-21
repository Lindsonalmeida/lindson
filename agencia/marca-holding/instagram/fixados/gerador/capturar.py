# Captura referências (Playwright). Uso: python3 capturar.py
import os
from playwright.sync_api import sync_playwright
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../referencias')
URLS = {
 'behance-stationery': 'https://www.behance.net/search/projects/brand%20identity%20mockup%20stationery',
 'behance-grid3': 'https://www.behance.net/search/projects/instagram%20grid%203%20posts%20branding',
 'pentagram': 'https://www.pentagram.com/work',
 'koto': 'https://koto.studio/work/',
 'mucho': 'https://wearemucho.com/',
 'anagrama': 'https://www.anagrama.com/',
 'futura': 'https://byfutura.com/',
 'collins': 'https://www.wearecollins.com/',
 'bureau-borsche': 'https://bureauborsche.com/',
 'manual': 'https://manualcreative.com/',
}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux/chrome')
    for k, u in URLS.items():
        p = b.new_page(viewport={'width': 1440, 'height': 1100})
        try:
            p.goto(u, timeout=30000, wait_until='domcontentloaded'); p.wait_for_timeout(4000)
            p.screenshot(path=f'{O}/{k}.jpg', type='jpeg', quality=80); print(k, 'ok')
        except Exception as e: print(k, 'ERRO', str(e)[:80])
        p.close()
    b.close()
