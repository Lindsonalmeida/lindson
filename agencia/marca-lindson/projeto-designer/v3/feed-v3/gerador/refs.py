# Capturas da pesquisa premium feed v3 (conta Leandro, 16/11/2026)
import os
from playwright.sync_api import sync_playwright
O=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/referencias/'
R=[('01-behance-social-media-design-br','https://www.www.behance.net/galleries/graphic-design/social-media'),
('02-behance-instagram-agency-us','https://www.www.behance.net/search/projects?search=instagram%20feed%20agency'),
('03-dribbble-instagram-post','https://dribbble.com/search/instagram-post-design'),
('04-dribbble-social-media-agency','https://dribbble.com/search/social-media-agency'),
('05-pinterest-designer-feed','https://www.pinterest.com/search/pins/?q=graphic%20designer%20instagram%20feed'),
('06-thebrandidentity-uk','https://the-brandidentity.com/'),
('07-collins-us','https://www.collinsdesign.com/'),
('08-studiodumbar-nl','https://studiodumbar.com/'),
('09-andwalsh-us','https://andwalsh.com/'),
('10-ruizbranding-br','https://www.behance.net/search/projects/feed%20instagram%20branding%20studio?sort=appreciations'),
('11-inspirationgrid-social','https://theinspirationgrid.com/?s=instagram'),
('12-dribbble-bold-typography-poster','https://dribbble.com/search/bold-typography-poster')]
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'); pg=b.new_page(viewport={'width':1440,'height':1600})
  for n,url in R:
    if os.path.exists(O+n+'.jpg') and os.path.getsize(O+n+'.jpg')>20000: continue
    pg=b.new_page(viewport={'width':1440,'height':1600})
    try:
      pg.goto(url,timeout=30000,wait_until='domcontentloaded'); pg.wait_for_timeout(5000)
      pg.screenshot(path=O+n+'.jpg',type='jpeg',quality=70); print('ok',n); pg.close()
    except Exception as e: print('erro',n,str(e)[:80])
  b.close()
