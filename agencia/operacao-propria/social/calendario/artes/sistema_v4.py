# Sistema v4 para as artes do calendário @oreganoturbo · Paollo · conta Zuleide · 08/11/2026
# Executado (exec) no topo de s1-2/gerar_s12.py, s3-4/gerar_s34.py e fotos/gerar_fotos.py, no lugar do v3/gerar.py.
# Lê as funções de marca de ../../v4/gerar.py SEM alterar nada lá e aplica as lições da pesquisa de 08/11
# (../../../biblioteca-pizzaria/PESQUISA-08-11-IDENTIDADES-E-SOCIAL.md):
#  1. Conceito único: toda arte leva a COMANDA "PEDIDO Nº" = posição da postagem no calendário (01 a 84).
#     A comanda se posiciona sozinha no lugar mais livre da arte (window.fit, no render), sem cobrir texto.
#  2. Paleta fixa: tomate, verde, creme e carvão. Açafrão só em detalhe (nunca fundo inteiro).
#  3. Bagel Fat One em todas as manchetes: ANTON passa a desenhar em Bagel (encolhe sozinho até caber).
#  4. Raio-X sem "explosão de preço": o preço vai escrito na comanda.
import os, json
_ARTES = os.path.normpath(os.path.join(D, '..'))
_V4 = os.path.normpath(os.path.join(_ARTES, '../../v4/gerar.py'))
_src = open(_V4, encoding='utf-8').read()
exec(_src[:_src.index('# ================================================================== 01')])            # marca + comanda do v4
exec(_src[_src.index('FONTS = ('):_src.index("open(os.path.join(D, 'pecas.html')")])                   # fontes, grão e CSS do v4
D = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- Bagel em toda manchete (ANTON vira Bagel, com encaixe automático)
_ANTON_V3 = ANTON
ANTON = lambda t, s, cor, lh=.88, extra='': (f'<div data-fit="1" style="font:400 {s * .78:.0f}px/{max(lh, .92)} \'Bagel Fat One\';letter-spacing:-.01em;color:{cor};'
                                             f'text-transform:uppercase;white-space:nowrap;{extra}">{t}</div>')
ANTON_FAIXA = _ANTON_V3   # Anton só fica na faixa em loop (regra v4)

# ---------------------------------------------------------------- comanda do calendário (PEDIDO Nº = ordem da postagem)
_COMANDA_V4 = comanda   # os geradores usam o nome 'comanda' para outras coisas
_CAL = json.load(open(os.path.join(_ARTES, '..', 'calendario.json'), encoding='utf-8'))
def num_pedido(nome):
    dia, hora = int(nome[1:3]), nome[4:7]
    for k, r in enumerate(_CAL, 1):
        if r['dia'] == dia and r['hora'] == hora:
            return k, r['linha_nome'].lower()
    return 0, 'só pizzarias'

def COMANDA(nome, pos=None):
    """Comanda da campanha. pos=(x, y, rot) fixa o lugar; sem pos, o render escolhe o canto mais livre."""
    n, linha = num_pedido(nome)
    if pos:
        x, y, rot = pos
        return _COMANDA_V4(n, x=x, y=y, rot=rot, txt=linha).replace('<div class="a"', '<div class="a cmd"', 1)
    rot = 3 if n % 2 else -4
    return _COMANDA_V4(n, x=0, y=0, rot=rot, txt=linha).replace('<div class="a"', '<div class="a cmd" data-auto="1"', 1)

# ---------------------------------------------------------------- encaixe no render: letra que estoura encolhe; comanda acha lugar livre
FIT_JS = r'''<script>
window.fit = () => {
  document.querySelectorAll('[data-w]').forEach(el => { const w = +el.dataset.w, c = el.firstElementChild;
    let fs = parseFloat(getComputedStyle(c).fontSize); while (c.scrollWidth > w + 1 && fs > 12) { fs -= 2; c.style.fontSize = fs + 'px'; } });
  document.querySelectorAll('[data-fit]').forEach(el => {
    const sec = el.closest('section'); const sr = sec.getBoundingClientRect();
    let L = sr.left + 20, R = sr.right - 20;
    for (let p = el.parentElement; p && p !== sec; p = p.parentElement) {
      if (p.style && p.style.width && p.style.width.endsWith('px')) { const pr = p.getBoundingClientRect(), cs = getComputedStyle(p);
        L = Math.max(L, pr.left + parseFloat(cs.paddingLeft) - 2); R = Math.min(R, pr.right - parseFloat(cs.paddingRight) + 2); break; } }
    let fs = parseFloat(getComputedStyle(el).fontSize), i = 0;
    const rg = document.createRange(); rg.selectNodeContents(el);
    while (i++ < 60 && fs > 14) { const r = rg.getBoundingClientRect(); const over = Math.max(0, r.right - R) + Math.max(0, L - r.left);
      if (over < 1) break; fs *= 0.96; el.style.fontSize = fs.toFixed(1) + 'px'; } });
  document.querySelectorAll('section.f').forEach(sec => {
    const c = sec.querySelector('.cmd[data-auto]'); if (!c) return;
    const sr = sec.getBoundingClientRect(), W = sr.width, H = sr.height, area = W * H;
    const rects = [];
    sec.querySelectorAll('*').forEach(e => { if (c.contains(e) || e.closest('.grao')) return;
      const r = e.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return;
      const temTexto = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const grafico = (e.tagName === 'svg' || e.tagName === 'IMG') && r.width * r.height < area * .45;
      const cs = getComputedStyle(e);
      const caixa = !temTexto && !grafico && r.width * r.height < area * .30 && (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none' || cs.borderTopWidth !== '0px');
      if (temTexto || grafico || caixa) rects.push([r.left - sr.left - 10, r.top - sr.top - 10, r.right - sr.left + 10, r.bottom - sr.top + 10, caixa ? .6 : 1]); });
    const cr = c.getBoundingClientRect(), w = cr.width, h = cr.height;
    let best = null;
    for (let y = 26; y <= H - h - 110; y += 22) for (let x = 26; x <= W - w - 20; x += 22) {
      let s = 0; for (const [a, b, cc, d, k] of rects) { const ix = Math.min(x + w, cc) - Math.max(x, a), iy = Math.min(y + h, d) - Math.max(y, b); if (ix > 0 && iy > 0) s += ix * iy * k; }
      s += ((W - x - w) + y) * .6;            // prefere o canto de cima à direita, como no kit v4
      if (!best || s < best[0]) best = [s, x, y]; }
    if (best) { c.style.left = best[1] + 'px'; c.style.top = best[2] + 'px'; }
  });
};
</script>'''

# ---------------------------------------------------------------- comanda grande do Raio-X (o preço vai escrito nela, como no p05 do v4)
def TICKET(titulo, itens, w=600, rot=-2, fs=32, preco=True, ps=76, ms=15):
    lista = ''.join(f'<div style="display:flex;align-items:center;gap:14px;padding:{fs * .42:.0f}px 0;border-bottom:2px dashed rgba(20,19,17,.25)">'
                    f'<span style="font:600 18px \'IBM Plex Mono\';color:{TOMATE}">{i + 1:02d}</span>'
                    f'<span style="font:700 {fs}px/1.05 Inter;color:{CARVAO}">{t}</span></div>' for i, t in enumerate(itens))
    total = (f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:18px;gap:16px">'
             + BAGEL('R$ 297', ps, TOMATE, 1) + MONO('abatido no 1º mês<br>se fechar em 7 dias', ms, CARVAO, 'line-height:1.5;text-align:right') + '</div>') if preco else ''
    return (f'<div style="width:{w}px;transform:rotate({rot}deg);filter:drop-shadow(14px 16px 0 rgba(0,0,0,.45))">'
            f'<div style="height:12px;background:radial-gradient(circle at 9px 0,transparent 8px,{CREME} 8.5px) -9px 0/18px 100% repeat-x"></div>'
            f'<div style="background:{CREME};padding:22px 34px 26px">' + MONO(titulo, 16, TOMATE) + lista + total + '</div>'
            f'<div style="height:12px;background:radial-gradient(circle at 9px 12px,transparent 8px,{CREME} 8.5px) -9px 0/18px 100% repeat-x"></div></div>')

FIT = lambda html, w, extra='': f'<div data-w="{w}" style="width:{w}px;{extra}">{html}</div>'   # encolhe a letra até caber em w
