import asyncio,os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__));V=D+"/../venda"
async def m():
    async with async_playwright() as p:
        px=os.environ.get("HTTPS_PROXY")
        b=await p.chromium.launch(proxy={"server":px} if px else None,args=["--ignore-certificate-errors"])
        for n,vp,s in (("celular",{"width":390,"height":844},2),("desktop",{"width":1440,"height":900},1)):
            c=await b.new_context(viewport=vp,device_scale_factor=s,ignore_https_errors=True);pg=await c.new_page()
            await pg.goto("file://"+V+"/index.html",wait_until="networkidle");await pg.evaluate("document.fonts.ready");await pg.wait_for_timeout(800)
            sw=await pg.evaluate("[document.documentElement.scrollWidth,innerWidth]");print(n,sw)
            await pg.add_style_tag(content=".buybar{display:none!important}")
            await pg.screenshot(path=f"{V}/previa-{n}.jpg",full_page=True,type="jpeg",quality=62)
            await c.close()
        await b.close()
asyncio.run(m())
