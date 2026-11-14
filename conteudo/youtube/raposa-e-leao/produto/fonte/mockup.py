import asyncio,os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={"width":1640,"height":2000})
        await pg.goto("file://"+D+"/mockup.html");await pg.evaluate("document.fonts.ready");await pg.wait_for_timeout(500)
        await (await pg.query_selector("#h")).screenshot(path=D+"/../venda/img/capa-hubla.jpg",type="jpeg",quality=86)
        await (await pg.query_selector("#q")).screenshot(path=D+"/../venda/img/mockup.jpg",type="jpeg",quality=86)
        await b.close()
asyncio.run(m())
