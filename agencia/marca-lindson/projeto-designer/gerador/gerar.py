# -*- coding: utf-8 -*-
# Gerador do Projeto Designer (conta Leandro, 16/11/2026). Uso: python3 gerar.py <saida> <dir_brandbooks_jpg> <dir_site_img>
import sys, os, json, html, shutil
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conteudo import *

OUT, BB, IMG = [os.path.abspath(a) for a in sys.argv[1:4]]
TMP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp"); os.makedirs(TMP, exist_ok=True)
Y, K = "#F5C518", "#0A0A0A"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;600;800&display=swap" rel="stylesheet">'
BASE = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{font-family:Manrope,sans-serif;background:{K};color:#fff;-webkit-font-smoothing:antialiased}}
.a{{font-family:Anton,sans-serif;text-transform:uppercase;line-height:.92;letter-spacing:.5px}} .y{{color:{Y}}} .tag{{font:800 15px Manrope;letter-spacing:3px;text-transform:uppercase}}"""
e = html.escape
def bbp(n, p): return f"{BB}/{n}/h-{p:02d}.jpg"
def fx(s):  # imagem especial "@bb:caso:pagina"
    _, n, p = s.split(":"); return bbp(n, int(p))
def mk(p): os.makedirs(os.path.dirname(p), exist_ok=True); return p
def br(t): return e(t).replace("\n", "<br>")

pw = sync_playwright().start(); bro = pw.chromium.launch(); page = bro.new_page()
def shot(body, w, h, out, css=""):
    f = os.path.join(TMP, "x.html")
    open(f, "w").write(f"<!doctype html><html><head><meta charset=utf-8>{FONTS}<style>{BASE}{css} body{{width:{w}px;height:{h}px;overflow:hidden;position:relative}}</style></head><body>{body}</body></html>")
    page.set_viewport_size({"width": w, "height": h}); page.goto("file://" + f); page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready"); page.wait_for_timeout(150)
    mk(out); page.screenshot(path=out, type="jpeg" if out.endswith(".jpg") else "png", **({"quality": 90} if out.endswith(".jpg") else {}))
    return out
def topdf(imgs, out):
    ims = [Image.open(i).convert("RGB") for i in imgs]; ims[0].save(mk(out), save_all=True, append_images=ims[1:], resolution=144)
SIG = lambda c="#fff": f'<div class=tag style="color:{c};opacity:.85">{e(STUDIO)}</div>'
ALL = []  # (grupo, caminho relativo, titulo)

# ================= BEHANCE =================
for c in CASES:
    d = f"{OUT}/behance/{c['id']}"; n = c["bb"]
    shot(f"""<div style="position:absolute;inset:0;background:url('{bbp(n,c['capa'])}') center/cover"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(transparent,{K} 55%)"></div>
      <div style="position:absolute;left:36px;bottom:30px;right:36px"><div class=tag style="color:{Y}">Identidade visual</div>
      <div class=a style="font-size:46px;margin-top:8px">{e(c['titulo'].split(' · ')[0])}</div></div>""", 808, 632, f"{d}/00-capa-808x632.jpg")
    shot(f"""<div style="padding:90px 100px">{SIG(Y)}<div class=a style="font-size:120px;margin:28px 0 18px">{e(c['titulo'].split(' · ')[0])}</div>
      <div style="font:600 26px Manrope;opacity:.75;margin-bottom:70px">{e(c['cliente'])}</div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:50px;border-top:2px solid {Y};padding-top:36px">
      {''.join(f'<div><div class=tag style="color:{Y};margin-bottom:14px">{t}</div><div style="font:400 22px/1.5 Manrope;opacity:.9">{e(c[k])}</div></div>' for t,k in [("Desafio","desafio"),("Conceito","conceito"),("Entregas","entregas")])}
      </div></div>""", 1400, 900, f"{d}/01-intro.jpg")
    for i, p in enumerate(c["paginas"]):
        Image.open(bbp(n, p)).convert("RGB").save(f"{d}/{i+2:02d}-modulo.jpg", quality=90)
    shot(f"""<div style="background:{Y};color:{K};position:absolute;inset:0;padding:80px 100px;display:flex;justify-content:space-between;align-items:flex-end">
      <div><div class=tag>Design de marca</div><div class=a style="font-size:96px;margin-top:14px">{e(STUDIO)}</div>
      <div style="font:600 24px Manrope;margin-top:18px">São Luís, MA · identidade visual, brand book e web design</div></div>
      <div style="text-align:right;font:800 24px/1.6 Manrope">Orçamento pelo WhatsApp<br>wa.me/5598985621808<br>lindsonalmeida.pages.dev</div></div>""", 1400, 500, f"{d}/{len(c['paginas'])+2:02d}-creditos.jpg")
    open(f"{d}/TEXTO.md", "w").write(f"# {c['titulo']}\n\n## Título\n{c['titulo']}\n\n## Descrição\n{c['descricao']}\n\n## Tags\n{c['tags']}\n\n## Ferramentas\n{c['ferramentas']}\n\n## Ordem dos módulos\nSuba as imagens 01 a {len(c['paginas'])+2:02d} nesta ordem; capa = 00-capa-808x632.jpg.\n")
    ALL.append(("Behance", f"behance/{c['id']}/00-capa-808x632.jpg", c["titulo"]))

# ================= PINTEREST =================
PINS = []
cases_by = {c["bb"]: c for c in CASES}
nomes_pg = {1: "capa do brand book", 3: "essência da marca", 5: "antes e depois", 6: "logo", 7: "versões do logo", 9: "usos incorretos", 10: "paleta de cores", 11: "tipografia", 12: "elementos gráficos", 13: "fotografia", 15: "a marca aplicada"}
pasta_pg = {1: 1, 3: 1, 5: 0, 6: 3, 7: 3, 9: 3, 10: 2, 11: 1, 12: 1, 13: 1, 15: 0}
for c in CASES:
    pgs = [6, 7, 10, 11] if c["bb"] == "leo" else [c["capa"] if c["capa"] != 6 else 1, 6, 10, 15]
    for p in pgs:
        PINS.append(dict(img=bbp(c["bb"], p), titulo=f"{c['titulo'].split(' · ')[0]}: {nomes_pg[p]}", pasta=PASTAS[pasta_pg[p]][0],
                         desc=f"{nomes_pg[p].capitalize()} da identidade visual {c['titulo'].split(' · ')[0]} ({c['cliente']}). {c['conceito']} Design: {STUDIO}, São Luís (MA). Veja o case completo no portfólio."))
extra = [("pf/jaci-manual.webp", "Dra. Jaci Cunha: manual de identidade", 1), ("pf/curso-antes-depois.webp", "Processo Legislativo: Instagram antes e depois", 4),
         ("pf/brasa-viva-identidade.jpg", "Brasa Viva: identidade de pizzaria (conceito)", 0), ("pf/rt-assinaturas.webp", "Real Time: assinaturas da marca", 3),
         ("pf/brasa-viva-site.jpg", "Brasa Viva: site na identidade", 5), ("pf/wf-celulares-mini-site.jpg", "WF Celulares: mini site", 5)]
for f, t, b in extra:
    PINS.append(dict(img=f"{IMG}/{f}", titulo=t, pasta=PASTAS[b][0], desc=f"{t}. Projeto do {STUDIO}, designer em São Luís (MA): identidade visual, brand book e web design. Veja mais no portfólio."))
for i, p in enumerate(PINS):
    bg, fg = (Y, K) if i % 2 else (K, "#fff")
    shot(f"""<div style="position:absolute;left:0;top:0;width:1000px;height:1080px;background:#111 url('{p['img']}') center/{'contain no-repeat' if i>=24 else 'cover'}"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;height:420px;background:{bg};color:{fg};padding:56px 64px">
      <div class=tag style="color:{Y if bg==K else K}">{e(p['pasta'])}</div>
      <div class=a style="font-size:66px;margin-top:18px">{e(p['titulo'])}</div>
      <div style="position:absolute;bottom:46px;left:64px;font:800 22px Manrope">{e(STUDIO)} · lindsonalmeida.pages.dev</div></div>""",
         1000, 1500, f"{OUT}/pinterest/pins/pin-{i+1:02d}.jpg")
    p["arq"] = f"pin-{i+1:02d}.jpg"
ALL.append(("Pinterest", "pinterest/pins/pin-01.jpg", "30 pins"))
md = "# Pinterest · perfil, pastas e 30 pins\n\n## Perfil\n" + "".join(f"- **{k}:** {v}\n" for k, v in PIN_PERFIL.items())
md += "\n## Pastas (nome e descrição SEO)\n" + "".join(f"{i+1}. **{a}**: {b}\n" for i, (a, b) in enumerate(PASTAS))
md += "\n## Pins (imagem em pins/, link de destino igual em todos)\n\nLink: " + SITE + "\n\n"
md += "".join(f"### {p['arq']} · pasta: {p['pasta']}\n- Título: {p['titulo']}\n- Descrição: {p['desc']}\n- Link: {SITE}\n\n" for p in PINS)
open(f"{OUT}/pinterest/PINTEREST.md", "w").write(md)

# ================= LINKEDIN =================
thumbs = "".join(f'<div style="width:300px;height:169px;background:url(\'{bbp(n,p)}\') center/cover;border-radius:6px;transform:rotate({r}deg)"></div>' for n, p, r in [("realtime", 1, -3), ("curso", 6, 2), ("oregano", 10, -2), ("wf", 1, 3)])
shot(f"""<div style="position:absolute;right:40px;top:30px;display:grid;grid-template-columns:300px 300px;gap:18px">{thumbs}</div>
  <div style="position:absolute;left:430px;top:78px"><div class=tag style="color:{Y}">{e(STUDIO)}</div>
  <div class=a style="font-size:70px;margin-top:12px">Identidade visual<br><span class=y>e web design</span></div>
  <div style="font:600 19px Manrope;opacity:.8;margin-top:14px">São Luís, MA para o Brasil · orçamento pelo WhatsApp</div></div>""", 1584, 396, f"{OUT}/linkedin/banner-1584x396.jpg")
ALL.append(("LinkedIn", "linkedin/banner-1584x396.jpg", "Banner"))
def slide_capa(t, sub, img=None):
    bgimg = f"<div style=\"position:absolute;inset:0;background:url('{img}') center/cover;opacity:.35\"></div>" if img else ""
    return f"""{bgimg}<div style="position:absolute;inset:0;padding:90px 80px;display:flex;flex-direction:column;justify-content:flex-end">
      {SIG(Y)}<div class=a style="font-size:150px;margin:24px 0">{br(t)}</div><div style="font:800 30px Manrope">{e(sub)}</div>
      <div style="font:600 24px Manrope;opacity:.7;margin-top:40px">Arraste para o lado →</div></div>"""
def slide_img(img, leg, n):
    return f"""<div style="position:absolute;inset:0;background:{K if n%2 else '#151515'}"></div><div class=tag style="position:absolute;top:80px;left:80px;color:{Y}">{n:02d}</div>
      <div style="position:absolute;left:80px;right:80px;top:150px;height:900px;background:url('{img}') center/contain no-repeat"></div>
      <div class=a style="position:absolute;left:80px;bottom:100px;font-size:60px">{e(leg)}</div>"""
def slide_txt(t, s, n):
    bg, fg = (Y, K) if n % 2 == 0 else (K, "#fff")
    if s.startswith("@"):
        return slide_img(fx(s), t, n)
    return f"""<div style="position:absolute;inset:0;background:{bg};color:{fg};padding:110px 80px;display:flex;flex-direction:column;justify-content:center">
      <div class=a style="font-size:300px;opacity:.12;position:absolute;right:50px;top:60px">{n:02d}</div>
      <div class=a style="font-size:96px">{e(t)}</div><div style="font:600 40px/1.45 Manrope;margin-top:40px">{e(s)}</div></div>"""
def slide_cta():
    return f"""<div style="position:absolute;inset:0;background:{Y};color:{K};padding:110px 80px;display:flex;flex-direction:column;justify-content:center">
      <div class=a style="font-size:140px">Quer uma<br>marca assim?</div><div style="font:800 40px/1.4 Manrope;margin-top:40px">Orçamento de identidade visual pelo WhatsApp</div>
      <div style="font:800 34px Manrope;margin-top:20px">wa.me/5598985621808</div><div class=tag style="margin-top:60px">{e(STUDIO)}</div></div>"""
leg = {1: "Capa do brand book", 3: "Essência", 5: "Antes x depois", 6: "Logo", 7: "Versões", 9: "O que nunca fazer", 10: "Cores com proporção", 11: "Letras da marca", 12: "Elementos", 15: "A marca no mundo"}
mdl = "# LinkedIn · perfil, página do estúdio e 10 posts\n\n" + "".join(f"## {k}\n{v}\n\n" for k, v in LINKEDIN.items())
mdl += "## Banner\n`banner-1584x396.jpg` (perfil pessoal e página do estúdio).\n\n## 10 posts (PDF = carrossel: no LinkedIn, 'Adicionar documento')\n\n"
for po in POSTS:
    d = f"{TMP}/li/{po['id']}"; imgs = []
    imgs.append(shot(slide_capa(po["capa"], po["sub"], bbp(po["case"], po["pgs"][0]) if po["case"] else None), 1080, 1350, f"{d}/s1.jpg"))
    if po["case"]:
        for i, p in enumerate(po["pgs"][1:]): imgs.append(shot(slide_img(bbp(po["case"], p), leg[p], i + 2), 1080, 1350, f"{d}/s{i+2}.jpg"))
    else:
        for i, (t, s) in enumerate(po["slides"]): imgs.append(shot(slide_txt(t, s, i + 2), 1080, 1350, f"{d}/s{i+2}.jpg"))
    imgs.append(shot(slide_cta(), 1080, 1350, f"{d}/cta.jpg"))
    topdf(imgs, f"{OUT}/linkedin/posts/post-{po['id']}.pdf")
    shutil.copy(imgs[0], mk(f"{OUT}/linkedin/posts/post-{po['id']}-capa.jpg"))
    mdl += f"### Post {po['id']}\nArquivo: `posts/post-{po['id']}.pdf` (título do documento: {po['capa'].replace(chr(10),' ').title()})\n\n{po['texto']}\n\n"
open(f"{OUT}/linkedin/LINKEDIN.md", "w").write(mdl)
ALL.append(("LinkedIn", "linkedin/posts/post-01-real-time-capa.jpg", "10 posts"))

# ================= OFERTA =================
od = f"{OUT}/oferta"
# carrossel de anúncio
imgs = []
for i, (t, s, im) in enumerate(ANUNCIO):
    bg, fg = (Y, K) if i in (0, 4) else (K, "#fff")
    vis = ""
    if im == "@grid":
        vis = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:50px">' + "".join(f'<div style="height:250px;background:url(\'{bbp(n,1)}\') center/cover;border-radius:8px"></div>' for n in ["realtime", "wf", "curso", "oregano"]) + "</div>"
    elif im: vis = f'<div style="height:520px;margin-top:50px;background:url(\'{fx(im)}\') center/cover;border-radius:10px"></div>'
    imgs.append(shot(f"""<div style="position:absolute;inset:0;background:{bg};color:{fg};padding:100px 80px;display:flex;flex-direction:column;justify-content:{'flex-start' if vis else 'center'}">
      <div class=tag style="color:{K if bg==Y else Y}">{e(STUDIO)} · {i+1}/5</div><div class=a style="font-size:{120 if vis else 150}px;margin-top:30px">{br(t)}</div>
      {f'<div style="font:600 38px/1.4 Manrope;margin-top:36px">{e(s)}</div>' if s else ''}{vis}</div>""", 1080, 1350, f"{od}/anuncio-carrossel/tela-{i+1}.jpg"))
ALL.append(("Oferta", "oferta/anuncio-carrossel/tela-1.jpg", "Carrossel de anúncio"))
# proposta PDF 16:9
def lam(body, n): return shot(f'<div style="position:absolute;inset:0;padding:90px 110px">{body}</div><div class=tag style="position:absolute;right:110px;bottom:60px;opacity:.6">{e(STUDIO)} · {n:02d}</div>', 1920, 1080, f"{TMP}/prop/{n:02d}.jpg")
P = []
P.append(lam(f'<div style="position:absolute;inset:0;background:url(\'{bbp("realtime",15)}\') center/cover;opacity:.25"></div><div style="position:relative;margin-top:300px"><div class=tag style="color:{Y}">Proposta de identidade visual</div><div class=a style="font-size:170px;margin-top:20px">[Nome do cliente]</div><div style="font:600 34px Manrope;margin-top:24px;opacity:.8">Preparada por {e(STUDIO)} · [data]</div></div>', 1))
P.append(lam(f'<div class=tag style="color:{Y}">O que eu entendi</div><div class=a style="font-size:110px;margin:24px 0 50px">O seu negócio<br>e o seu cliente</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;font:400 32px/1.5 Manrope"><div><b class=y>Negócio</b><br>[resumo do briefing: o que vende, onde, há quanto tempo]</div><div><b class=y>Persona</b><br>[quem compra, o que valoriza, o que faz confiar]</div><div><b class=y>Desafio</b><br>[o que a marca atual não comunica]</div><div><b class=y>Objetivo</b><br>[como a marca precisa ser percebida]</div></div>', 2))
P.append(lam(f'<div class=tag style="color:{Y}">Como eu trabalho</div><div class=a style="font-size:110px;margin:24px 0 60px">6 etapas</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px">' + "".join(f'<div style="border-top:3px solid {Y};padding-top:20px"><div class=a style="font-size:54px">{i+1:02d} {e(a)}</div><div style="font:400 28px/1.45 Manrope;margin-top:12px;opacity:.85">{e(b)}</div></div>' for i, (a, b) in enumerate(ETAPAS)) + "</div>", 3))
for j, pk in enumerate(PACOTES):
    P.append(lam(f'<div class=tag style="color:{Y}">Pacote {j+1} de 3</div><div class=a style="font-size:150px;margin:20px 0">{e(pk["nome"])}</div><div style="font:600 34px Manrope;opacity:.8;margin-bottom:40px">{e(pk["para"])}</div><div style="columns:2;column-gap:80px;font:400 30px/1.6 Manrope">' + "".join(f'<div>— {e(x)}</div>' for x in pk["itens"]) + f'</div><div style="margin-top:40px;font:800 30px Manrope" class=y>Prazo: {e(pk["prazo"])} · Investimento: [preencher]</div>', 4 + j))
P.append(lam(f'<div class=tag style="color:{Y}">Trabalhos do estúdio</div><div class=a style="font-size:110px;margin:24px 0 40px">Cases</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">' + "".join(f'<div><div style="height:300px;background:url(\'{bbp(c["bb"],c["capa"])}\') center/cover;border-radius:8px"></div><div style="font:800 24px Manrope;margin-top:10px">{e(c["titulo"].split(" · ")[0])}</div></div>' for c in CASES) + "</div>", 7))
P.append(lam(f'<div style="position:absolute;inset:0;background:{Y}"></div><div style="position:relative;color:{K};margin-top:260px"><div class=tag>Próximo passo</div><div class=a style="font-size:150px;margin:20px 0">Vamos começar?</div><div style="font:800 38px/1.6 Manrope">1. Escolha o pacote · 2. Sinal para reservar a agenda: [preencher] · 3. Briefing<br>Validade da proposta: [preencher] · WhatsApp: wa.me/5598985621808</div></div>', 8))
topdf(P, f"{od}/proposta-identidade-visual.pdf"); shutil.copy(P[0], f"{od}/proposta-capa.jpg")
ALL.append(("Oferta", "oferta/proposta-capa.jpg", "Proposta em PDF"))
json.dump([[a, b, c] for a, b, c in ALL], open(f"{TMP}/all.json", "w"))
bro.close(); pw.stop(); print("ok", len(PINS))
