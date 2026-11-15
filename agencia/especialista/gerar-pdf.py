"""Gera 1 página A4 de resumo por guia (conta Leandro, 15/11/2026). Uso: python3 gerar-pdf.py <pasta_saida>"""
import re, sys, html, pathlib
from playwright.sync_api import sync_playwright
BASE = pathlib.Path(__file__).parent
TEMAS = ["google-meu-negocio","seo","venda-whatsapp","automacao-vendas","meta-negocios-locais","ranqueamento-sites"]
def inl(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", t)
    return re.sub(r"`(.+?)`", r"\1", t)
def secoes(md):
    s, cur = {}, None
    for l in md.splitlines():
        m = re.match(r"## (\d)\. (.*)", l)
        if m: cur = m.group(1); s[cur] = [m.group(2)]; continue
        if cur: s[cur].append(l)
    return s
def lista(lines, n=7):
    it = [re.sub(r"^(\s*[-\d]+\.?\s*)", "", l) for l in lines if re.match(r"^(-|\d+\.) ", l)]
    return "<ul>" + "".join(f"<li>{inl(x)}</li>" for x in it[:n]) + "</ul>"
def tabela(lines):
    rows = [l for l in lines if l.startswith("|") and not re.match(r"^\|[-| ]+\|$", l)]
    out = ""
    for i, r in enumerate(rows):
        c = [x.strip() for x in r.strip("|").split("|")]
        tag = "th" if i == 0 else "td"
        out += "<tr>" + "".join(f"<{tag}>{inl(x)}</{tag}>" for x in c) + "</tr>"
    return f"<table>{out}</table>"
CSS = """@page{size:A4;margin:0}body{margin:0;font:9.2px/1.38 'Helvetica Neue',Arial,sans-serif;color:#151515;background:#fff}
.p{padding:13mm 13mm 10mm}header{border-bottom:3px solid #c8a24a;padding-bottom:6px;margin-bottom:8px}
.k{font-size:8px;letter-spacing:.18em;text-transform:uppercase;color:#8a6d1f}h1{font-size:21px;margin:2px 0 0;letter-spacing:-.01em}
h2{font-size:10.5px;margin:9px 0 3px;color:#0e2a3a;text-transform:uppercase;letter-spacing:.06em}
ul{margin:0;padding-left:14px}li{margin:1px 0}.g{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.msg{background:#f5efe0;border-left:3px solid #c8a24a;padding:5px 8px;font-style:italic}
table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #e3e3e3;padding:2px 4px;text-align:left;vertical-align:top}th{background:#0e2a3a;color:#fff}
footer{margin-top:8px;font-size:7.5px;color:#777}"""
def pagina(t):
    md = (BASE/t/"README.md").read_text()
    titulo = re.search(r"^# (.+)", md, re.M).group(1)
    s = secoes(md)
    msg = "<br>".join(inl(l.lstrip("> ").strip()) for l in s["4"] if l.startswith("  >"))
    oferta = next((l for l in s["4"] if "**Oferta:**" in l), "")
    return f"""<!doctype html><meta charset=utf-8><style>{CSS}</style><div class=p><header><div class=k>Guia de especialista · Lindson Almeida · São Luís/MA</div><h1>{inl(titulo)}</h1></header>
<h2>O que o especialista sabe</h2>{lista(s['1'],6)}
<div class=g><div><h2>Checklist para o cliente</h2>{lista(s['3'],10)}</div><div><h2>Como vender</h2><p>{inl(oferta.lstrip('- '))}</p><div class=msg>{msg}</div><h2>Regras</h2>{lista(s['5'],4)}</div></div>
<h2>Próxima ação nos clientes</h2>{tabela(s['6'])}
<footer>Guia completo, trilha de 7 dias e fontes oficiais: agencia/especialista/{t}/README.md · conta Leandro, 15/11/2026 · sem promessa de resultado.</footer></div>"""
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for t in TEMAS:
        pg.set_content(pagina(t)); pg.pdf(path=str(out/f"{t}.pdf"), format="A4", print_background=True)
        print(t, pg.evaluate("document.body.scrollHeight"))
    b.close()
