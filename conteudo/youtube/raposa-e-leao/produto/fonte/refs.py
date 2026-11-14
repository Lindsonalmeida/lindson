import asyncio, os, sys
from playwright.async_api import async_playwright
U=[("folio-society","https://www.foliosociety.com/"),("lars-muller","https://www.lars-mueller-publishers.com/"),("phaidon","https://www.phaidon.com/"),("einaudi","https://www.einaudi.it/"),("daily-stoic-medallion","https://store.dailystoic.com/collections/medallions"),("stripe-press-book","https://press.stripe.com/the-art-of-doing-science-and-engineering"),
]
async def main():
    async with async_playwright() as p:
        px=os.environ.get("HTTPS_PROXY")
        b=await p.chromium.launch(proxy={"server":px} if px else None,args=["--ignore-certificate-errors"])
        for n,u in U:
            try:
                c=await b.new_context(viewport={"width":1440,"height":900},ignore_https_errors=True)
                pg=await c.new_page()
                r=await pg.goto(u,wait_until="domcontentloaded",timeout=45000)
                await pg.wait_for_timeout(3500)
                t=await pg.title()
                await pg.screenshot(path=f"referencias/{n}.jpg",type="jpeg",quality=60,full_page=False)
                h=await pg.evaluate("document.documentElement.scrollHeight")
                await pg.evaluate("window.scrollTo(0,900)"); await pg.wait_for_timeout(1200)
                await pg.screenshot(path=f"referencias/{n}-2.jpg",type="jpeg",quality=60)
                print(n,r.status if r else None,t[:70],h,flush=True)
                await c.close()
            except Exception as e: print(n,"ERRO",str(e)[:120],flush=True)
        await b.close()
asyncio.run(main())
