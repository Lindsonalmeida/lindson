# Perfil do Instagram @oreganoturbo · Paollo · 06/11/2026
# Gera: avatar 1080 (e 320 / prova a 40 px), 6 capas de destaque 1080×1920 e a prévia do perfil no celular.
# Base: kit v3 aprovado (../v3/gerar.py), funções de marca CARREGADAS de lá. Avatar parte do v4-16-avatar (símbolo da folha
# com seta, creme sobre verde) e ganha anel de xadrez de cantina, como o selo da marca.
# Uso: python3 gerar_perfil.py && node render.js && python3 montar.py
import os, json
D = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.normpath(os.path.join(D, '../v3/gerar.py'))
src = open(V3, encoding='utf-8').read()
exec(src.split('# ================================================================== 01')[0])
exec(src[src.index('FONTS = ('):src.index("open(os.path.join(D, 'pecas.html')")])
D = os.path.dirname(os.path.abspath(__file__))
FONTS = FONTS.replace('&family=Inter:', '&family=Kaushan+Script&family=Inter:').replace('wght@500;600;700&', 'wght@400;500;600;700&')
BIO = json.load(open(os.path.join(D, 'bio.json'), encoding='utf-8'))
P = []
sec = lambda i, w, h, html: P.append((i, w, h, html))

# ------------------------------------------------------------------ AVATAR 1080×1080 (o Instagram corta em círculo)
# Folha grande (ocupa ~60% do círculo) para ser lida a 40 px; anel de xadrez tomate e creme na borda (selo da marca);
# fio carvão separando anel e miolo; sombra dura curta sob a folha (profundidade sem degradê).
def folha_svg(tam, folha=CREME, seta=VERDE, sombra=True):
    sh = (f'<path transform="translate(2.2 2.6)" d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{CARVAO}" fill-opacity=".35"/>' if sombra else '')
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block;overflow:visible">{sh}'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
def avatar(t=1080):
    k = t / 1080
    return (f'<div class="a" style="inset:0;background:{xadrez(TOMATE, CREME, 27 * k)}"></div>'
            f'<div class="a" style="left:{62 * k}px;top:{62 * k}px;width:{956 * k}px;height:{956 * k}px;border-radius:50%;background:{CARVAO}"></div>'
            f'<div class="a" style="left:{74 * k}px;top:{74 * k}px;width:{932 * k}px;height:{932 * k}px;border-radius:50%;background:radial-gradient(circle at 50% 42%,#23704A 0,{VERDE} 55%,#174A30 100%)"></div>'
            f'<div class="a" style="left:{74 * k}px;top:{74 * k}px;width:{932 * k}px;height:{932 * k}px;border-radius:50%;background:{padrao(CREME, .07, 300 * k)}"></div>'
            + A(175 * k, 155 * k, folha_svg(735 * k)))
sec('avatar-1080', 1080, 1080, avatar() + GRAO)

# ------------------------------------------------------------------ DESTAQUES 1080×1920
# O Instagram mostra o centro em círculo (~1080 de diâmetro no meio da tela): o ícone fica ali, grande e em traço gordo
# (mesmo traço dos ícones do padrão da marca). Fora do círculo: xadrez, nome do destaque e logo, para quem abre o story.
ICS = {
 'metodo': '<path d="M12 84 H36 V64 H58 V44 H82 V22"/><path d="M68 22 H82 V36"/><circle cx="24" cy="70" r="5" fill="currentColor"/>',
 'raiox': '<circle cx="42" cy="42" r="28"/><path d="M62 62 L86 86"/><path d="M30 34 Q42 26 54 34 L42 58 Z"/><circle cx="41" cy="38" r="2.5" fill="currentColor"/>',
 'planos': '<rect x="20" y="14" width="60" height="76" rx="6"/><path d="M38 10 H62 V22 H38 Z"/><path d="M32 40 L38 46 L48 34"/><path d="M54 42 H70"/><path d="M32 62 L38 68 L48 56"/><path d="M54 64 H70"/>',
 'duvidas': '<path d="M16 20 H84 V68 H44 L26 84 V68 H16 Z"/><path d="M40 36 Q40 26 50 26 Q60 26 60 35 Q60 42 50 45 V51"/><circle cx="50" cy="59" r="2.5" fill="currentColor"/>',
 'bastidor': '<rect x="10" y="30" width="80" height="54" rx="8"/><path d="M34 30 L40 18 H60 L66 30"/><circle cx="50" cy="57" r="16"/><circle cx="76" cy="42" r="2.5" fill="currentColor"/>',
 'zap': '<path d="M50 12 A36 36 0 1 1 22 76 L14 88 L28 82 A36 36 0 0 1 50 12 Z"/><path d="M38 34 Q36 40 40 48 Q46 58 56 62 Q62 64 66 60 L62 54 L56 56 Q48 52 44 44 L46 38 Z"/>',
}
def ic(n, tam, cor, w=6.5):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block;overflow:visible;color:{cor}"><g fill="none" stroke="{cor}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{ICS[n]}</g></svg>')
DEST = [('metodo', 'Método', VERDE, CREME, ACAFRAO), ('raiox', 'Raio-X', TOMATE, CREME, ACAFRAO), ('planos', 'Planos', ACAFRAO, CARVAO, TOMATE),
        ('duvidas', 'Dúvidas', CARVAO, CREME, ACAFRAO), ('bastidor', 'Bastidor', CREME, VERDE, TOMATE), ('zap', 'Fale comigo', VERDE_ESC, CREME, ACAFRAO)]
for i, (n, nome, bg, fg, ac) in enumerate(DEST, 1):
    sec(f'destaque-{i}-{n}', 1080, 1920,
        BOX(0, 0, 1080, 1920, bg) + f'<div class="a" style="inset:0;background:{padrao(fg, .09, 300)}"></div>' +
        BOX(0, 0, 1080, 150, xadrez(TOMATE if bg != TOMATE else CARVAO, CREME, 37)) + BOX(0, 1770, 1080, 150, xadrez(TOMATE if bg != TOMATE else CARVAO, CREME, 37)) +
        A(0, 200, MONO(f'Destaque {i:02d} · @oreganoturbo', 22, fg, 'opacity:.85'), 'width:1080px;display:flex;justify-content:center') +
        f'<div class="a" style="left:120px;top:540px;width:840px;height:840px;border-radius:50%;border:14px solid {ac};box-shadow:0 0 0 20px {bg},0 0 0 28px {fg}"></div>' +
        A(250, 670, ic(n, 580, fg, 8)) +
        A(0, 300, BAGEL(nome, 150 if len(nome) < 9 else 128, fg, .9, SH(CARVAO if bg != CARVAO else TOMATE, 8)), 'width:1080px;display:flex;justify-content:center') +
        A(0, 1560, logo(40, fg, ac if bg != ac else CARVAO, bg), 'width:1080px;display:flex;justify-content:center') + GRAO)

# ------------------------------------------------------------------ TELA DO PERFIL (prévia, 1080 de largura)
# Ordem do Instagram: a mais nova no canto de cima à esquerda. São as 9 primeiras do feed do calendário (dia 1 12h até dia 5 12h).
GRADE = ['../v3/pecas/p06-cardapio-da-casa.jpg', '../calendario/artes/s1-2/d04-19h-combo-de-terca.jpg', '../v3/pecas/p04-menos-app-mais-zap.jpg',
         '../calendario/artes/s1-2/d03-19h-a-conta-do-pedido.jpg', '../v3/pecas/p05-raio-x-cartaz.jpg', '../calendario/artes/s1-2/d02-19h-5-fotos-que-tiram-a-fome.jpg',
         '../v3/pecas/p02-terca-tambem-tem-fome.jpg', '../v3/pecas/p03-grade-so-pizzarias.jpg', '../v3/pecas/p01-foto-que-da-fome.jpg']
UI = '#000000'; CIN = '#737373'; LINHA = '#DBDBDB'
f = lambda w, s, c=UI, extra='': f'font:{w} {s}px/1.3 Inter;color:{c};{extra}'
num = lambda n, t: f'<div style="text-align:left"><div style="{f(700, 38)}">{n}</div><div style="{f(400, 32)}">{t}</div></div>'
dest_mini = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px;width:168px">'
                    f'<div style="width:156px;height:156px;border-radius:50%;padding:7px;border:3px solid {LINHA}"><div style="width:100%;height:100%;border-radius:50%;'
                    f'background:url(destaque-{i}-{n}.jpg) center 50%/100% auto"></div></div><div style="{f(500, 26)}">{nome}</div></div>'
                    for i, (n, nome, *_ ) in enumerate(DEST, 1))
bio_html = '<br>'.join(BIO['bio'].split('\n'))
tela = (
    BOX(0, 0, 1080, 2620, '#FFFFFF') +
    A(56, 26, f'<div style="{f(600, 34)}">19:00</div>') + A(860, 26, f'<div style="{f(600, 30)}">5G ▮▮▮ ▭</div>') +
    A(40, 110, f'<div style="display:flex;align-items:center;gap:16px"><span style="{f(700, 44)}">oreganoturbo</span><span style="{f(600, 30)}">⌄</span></div>') +
    A(870, 112, f'<div style="{f(400, 48)}">⊕ &nbsp;☰</div>') +
    A(40, 220, f'<div style="width:230px;height:230px;border-radius:50%;padding:8px;background:conic-gradient({ACAFRAO},{TOMATE},{VERDE},{ACAFRAO})">'
               f'<div style="width:100%;height:100%;border-radius:50%;padding:7px;background:#fff"><div style="width:100%;height:100%;border-radius:50%;'
               f'background:url(avatar-1080.jpg) center/cover"></div></div></div>') +
    A(330, 255, f'<div style="{f(700, 34)}">Orégano Turbo</div>') +
    A(330, 310, f'<div style="display:flex;gap:64px">{num(9, "posts")}{num("—", "seguidores")}{num("—", "seguindo")}</div>') +
    A(40, 480, f'<div style="width:1000px"><div style="{f(700, 32)}">{BIO["nome"]}</div>'
               f'<div style="{f(400, 30, CIN)}">{BIO["categoria"]}</div>'
               f'<div style="{f(400, 32, UI, "margin-top:4px")}">{bio_html}</div>'
               f'<div style="{f(600, 32, "#00376B", "margin-top:6px")}">🔗 {BIO["link_texto"]}</div></div>') +
    A(40, 790, f'<div style="display:flex;gap:14px">' + ''.join(
        f'<div style="width:{w}px;height:76px;border-radius:16px;background:{b};display:grid;place-items:center;{f(600, 30, c)}">{t}</div>'
        for t, w, b, c in [('Seguir', 318, '#0095F6', '#fff'), ('Mensagem', 318, '#EFEFEF', UI), ('WhatsApp', 318, '#EFEFEF', UI)]) + '</div>') +
    A(30, 905, f'<div style="display:flex;gap:6px">{dest_mini}</div>') +
    BOX(0, 1150, 1080, 96, '#fff', f'border-top:1px solid {LINHA};display:flex',
        f'<div style="flex:1;display:grid;place-items:center;border-bottom:3px solid {UI};{f(700, 40)}">▦</div>'
        f'<div style="flex:1;display:grid;place-items:center;{f(400, 40, CIN)}">▷</div><div style="flex:1;display:grid;place-items:center;{f(400, 40, CIN)}">◎</div>') +
    A(0, 1248, '<div style="display:grid;grid-template-columns:repeat(3,358px);gap:3px;width:1080px">' +
          ''.join(f'<div style="height:477px;background:url({g}) center/cover"></div>' for g in GRADE) + '</div>') +
    '')
sec('tela-perfil', 1080, 2690, tela)

FIT_JS = '<script>window.fit=()=>{};</script>'
open(os.path.join(D, 'perfil.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style>{FIT_JS}</head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
print(len(P), 'peças')
