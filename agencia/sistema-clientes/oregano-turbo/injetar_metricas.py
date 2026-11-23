"""Injeta a aba "Métricas por Reel" (fonte: metricas-reels.html, ao lado) no painel da Orégano (painel/oregano.html). Idempotente:
põe o link no menu (grupo "Vendas e tráfego", criado se faltar) e o bloco <script> antes do biblioteca.js; se o bloco mudou na fonte, troca. Conta Leandro, 23/11/2026.
  python3 injetar_metricas.py <pasta painel>   (montar-site.py chama sozinho para publico/painel; no privado, rode depois de remontar o oregano.html)"""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
INI = '<script>/* Aba "Métricas por Reel"'
LINK = '<a href="#metricas" data-v="metricas"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>Métricas por Reel</a>'
def bloco():
    t = open(os.path.join(AQUI, 'metricas-reels.html')).read(); i = t.index(INI); return t[i:t.index('</script>', i) + 9]
def injetar_metricas(pasta, nome='oregano.html'):
    p = os.path.join(pasta, nome)
    if not os.path.exists(p): return []
    s = o = open(p).read()
    if 'id="menu"' not in s or 'window.__V' not in s: return []
    if 'data-v="metricas"' not in s:
        if '<h4>Vendas e tráfego</h4>' in s: s = s.replace('<h4>Vendas e tráfego</h4>', '<h4>Vendas e tráfego</h4>' + LINK, 1)
        else: s = re.sub(r'(<div class="grupo"><h4>Gestão</h4>)', lambda m: '<div class="grupo"><h4>Vendas e tráfego</h4>' + LINK + '</div>' + m.group(1), s, count=1)
    b = bloco()
    if INI in s:
        i = s.index(INI); j = s.index('</script>', i) + 9; s = s[:i] + b + s[j:]
    else:
        k = s.find('<script src="/painel/biblioteca.js"'); k = k if k > -1 else s.rfind('</body>')
        s = (s[:k] + b + '\n' + s[k:]) if k > -1 else s + '\n' + b + '\n'
    if s != o: open(p, 'w').write(s); return [nome + ' (métricas por reel)']
    return []
if __name__ == '__main__': print(injetar_metricas(sys.argv[1]) or 'já estava em dia')
