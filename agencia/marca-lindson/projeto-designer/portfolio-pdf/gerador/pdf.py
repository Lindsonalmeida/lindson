import asyncio,os
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={"width":1920,"height":1080})
    await pg.goto("file://"+os.path.abspath("portfolio.html"),wait_until="networkidle");await pg.evaluate("document.fonts.ready");await pg.wait_for_timeout(1000)
    await pg.pdf(path="lindson-almeida-portfolio.pdf",width="1920px",height="1080px",print_background=True)
    for i in [1,3,5,6,24,25]:
      await pg.screenshot(path=f"chk{i:02d}.jpg",clip={"x":0,"y":(i-1)*1080,"width":1920,"height":1080},full_page=True,type="jpeg",quality=60)
    await b.close()
asyncio.run(m())
