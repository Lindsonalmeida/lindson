"""Painel do curso de processo legislativo (@curso_processo_legislativo_) = o modelo da Central
(../prototipo/painel.html), com:
- o CSS e o menu lateral do modelo SEM trocar as cores: a identidade do curso ainda não foi escolhida,
  com a identidade v10 aprovada pelo Lindson em 07/11 (agencia/clientes/curso-processo-legislativo/identidade/BRANDBOOK-V10.md), não a do Tribuna 98;
- telas do escopo, números do print do perfil (data a confirmar), estrutura do curso (a confirmar),
  próximos passos e decisões do Lindson;
- prototipo/movimento.js (animações do modelo) por último.
Uso: python3 montar-curso.py -> painel-curso.html (arquivo único, sem banco). Conta Leandro, 07/11/2026."""
import json, os, re

D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')

modelo = open(os.path.join(SC, 'prototipo', 'painel.html'), encoding='utf-8').read()
css_modelo = re.search(r'<style>(.*?)</style>', modelo, re.S).group(1)
ROOT = """:root{
  --fundo:#080808;--painel:#101010;--painel2:#161616;--linha:#2A2A2A;--amarelo:#A89048;--amarelo2:#C8A860;
  --texto:#F8F8F8;--apagado:#777671;--ok:#5CC98A;--alerta:#F2A93B;--erro:#E5604D;
  --f-titulo:'Inter Display',Inter,system-ui,sans-serif;--f-corpo:'Inter',system-ui,sans-serif;--f-dado:'Inter',system-ui,sans-serif;
  color-scheme:dark;
}"""
css_modelo = re.sub(r'(?i)245,\s*197,\s*24', '168,144,72', css_modelo).replace('#F5C518', '#A89048').replace('#FFDD55', '#C8A860')
css = re.sub(r':root\{.*?\}', lambda m: ROOT, css_modelo, count=1, flags=re.S)
css += """
/* Curso de processo legislativo: extras do painel (status, linha do tempo, decisões). Identidade v10 aprovada. */
.cp-aviso{border:1px dashed var(--amarelo);border-radius:12px;padding:12px 14px;color:var(--texto);font-size:12.5px;line-height:1.5;background:rgba(245,197,24,.06)}
.cp-status{display:inline-block;padding:3px 10px;border-radius:999px;font:600 11.5px var(--f-dado);white-space:nowrap}
.cp-status.feito{background:rgba(92,201,138,.14);color:var(--ok)}
.cp-status.andamento{background:rgba(245,197,24,.14);color:var(--amarelo)}
.cp-status.espera{background:rgba(242,169,59,.14);color:var(--alerta)}
.cp-status.fazer{background:rgba(142,139,131,.14);color:var(--apagado)}
.cp-status.confirmar{background:rgba(120,160,255,.14);color:#9DB8FF}
.cp-linha{display:grid;grid-template-columns:96px 1fr;gap:14px;padding:12px 0;border-bottom:1px solid var(--linha)}
.cp-linha:last-child{border-bottom:0}
.cp-linha b{font:500 12px var(--f-dado);color:var(--amarelo)}
.cp-linha p{margin:0}
.cp-barra{height:8px;border-radius:8px;background:var(--painel2);overflow:hidden;margin:10px 0 4px}
.cp-barra i{display:block;height:100%;background:var(--amarelo);border-radius:8px}
.cp-decisao{display:grid;gap:8px}
.cp-decisao h4{margin:0;font:800 22px/1.1 var(--f-titulo);text-transform:uppercase}
.cp-decisao p{margin:0;color:#D5D2C8;font-size:13.5px;line-height:1.5}
.cp-rodape{color:var(--apagado);font-size:12px;line-height:1.5;margin-top:18px;border-top:1px solid var(--linha);padding-top:12px}
"""

DADOS = {
  "fonte": "Print do perfil (data a confirmar): 98 posts, 4.535 seguidores, 1.628 seguindo. Fonte: TRAVA-MAQUIAVEL.md, item 5. Marca: BRANDBOOK-V10.md (aprovada pelo Lindson em 07/11/2026).",
  "escopo_total": 8,
  "kpis": [
    ["Seguidores", "4.535", "@curso_processo_legislativo_ · data a confirmar"],
    ["Posts", "98", "print do perfil · data a confirmar"],
    ["Seguindo", "1.628", "print do perfil · data a confirmar"],
    ["Estrutura do curso", "a confirmar", "sem a lista de aulas no repositório"],
    ["Identidade", "v10 aprovada", "marca em texto; capas v11 aguardam escolha"]
  ],
  "perfil": [
    ["Instagram", "@curso_processo_legislativo_", "confirmado pelo print do perfil"],
    ["Bio", "Conteúdos práticos para atuação parlamentar", "texto do print"],
    ["Link da bio", "curso-processo-legislativo.my.canva.site/…", "placeholder do Canva: trocar por link definitivo"],
    ["Foto de perfil", "cartaz do curso com os dois instrutores", "uso da imagem: parado até a autorização (item 6)"],
    ["Nome da marca", "PROCESSO LEGISLATIVO", "logo em texto, aprovada em 07/11"]
  ],
  "escopo": [
    ["1", "@ do curso confirmado pelo print do perfil", "feito", "@curso_processo_legislativo_, 4.535 seguidores (data a confirmar)"],
    ["2", "Capas de Reels na identidade do Tribuna 98", "espera", "REPROVADAS em 07/11 (identidade do Tribuna). Não publicar"],
    ["3", "Identidade própria do curso (marca v10)", "feito", "Aprovada em 07/11. Pesquisa premium ainda parcial (ver TEMPLATE.md)"],
    ["4", "Nome da marca do curso", "feito", "PROCESSO LEGISLATIVO, logo em texto, aprovada em 07/11"],
    ["5", "Link da bio (hoje é placeholder do Canva)", "espera", "Link definitivo: a informar"],
    ["6", "Estrutura do curso (aulas, ordem e títulos)", "espera", "Sem ela as capas não viram aulas: é o que destrava o item 7"],
    ["7", "Artes do feed, calendário e roteiros do curso", "fazer", "Capas v11: escolha A, B ou C. Depois a estrutura (item 6)"],
    ["8", "Turma de 10 de abril (se ainda vale)", "confirmar", "O post é de 19/03. Hoje é 07/11/2026: confirmar se a turma já passou"]
  ],
  "linha": [
    ["19/03", "Post do curso com a turma de 10 de abril e os dois instrutores (data do post, a confirmar o ano)", "confirmar"],
    ["07/11", "@ confirmado pelo print do perfil (4.535 seguidores)", "feito"],
    ["07/11", "9 capas de Reels feitas na identidade do Tribuna 98", "espera"],
    ["07/11", "Capas REPROVADAS pelo Lindson: o curso tem identidade própria", "espera"],
    ["07/11", "Marca v10 aprovada pelo Lindson (prancha e brandbook)", "feito"],
    ["07/11", "Painel do curso na Central (esta tela), com a identidade v10", "andamento"]
  ],
  "pesquisa": [
    ["Referências confirmadas pela própria página", "4 de 8 (meta: 8 de 3 países)", "espera"],
    ["Países confirmados", "1 (Países Baixos)", "espera"],
    ["Fontes bloqueadas", "Awwwards (conexão recusada), Behance (erro 400/403), Framer (página fora do ar), Koto (404)", "espera"]
  ],
  "decisoes": [
    ["Escolha da capa v11 (A, B ou C)", "Item 7. As três variações estão em agencia/clientes/curso-processo-legislativo/identidade/. Sem a escolha, as capas dos Reels não saem.", "aguardando"],
    ["Link definitivo da bio", "Item 5. Hoje é placeholder do Canva. Qual endereço usar (site próprio, pages.dev ou outro)?", "aguardando"],
    ["Turma de 10 de abril", "Item 8. Se já passou, o próximo post precisa de nova data. Confirmar com o Lindson.", "aguardando"],
    ["Quem é quem entre os instrutores", "O post traz dois nomes de instrutores. Confirmar quem são, o papel de cada um e o nome legal antes de usar qualquer nome (regra da trava: nomes antigos ficam sem uso até o Lindson confirmar).", "aguardando"]
  ],
  "proximos": [
    ["Lindson", "Escolher a capa v11 (A, B ou C) e mandar a foto do instrutor, uma por mensagem"],
    ["Lindson", "Mandar a estrutura do curso (lista de aulas, ordem e títulos)"],
    ["Lindson", "Informar o link definitivo da bio e confirmar a turma de 10 de abril"],
    ["Equipe", "Completar a pesquisa premium (8 referências de 3 países) e a persona de 5 linhas"],
    ["Equipe", "Depois da identidade e da estrutura: artes do feed, calendário e roteiros (itens 3, 6 e 7)"]
  ]
}

JS = r"""
const D = __DADOS__;
const $ = s => document.querySelector(s), main = $('#conteudo');
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const ST = {feito:['feito','✅ Feito'], andamento:['andamento','🟡 Em andamento'], espera:['espera','⏳ Depende de outro'], fazer:['fazer','⬜ A fazer'], confirmar:['confirmar','❔ A confirmar'], aguardando:['espera','⏳ Aguardando']};
const st = k => { const [c, t] = ST[k] || ST.fazer; return `<span class="cp-status ${c}">${t}</span>`; };
const nota = () => `<p class="cp-rodape">${esc(D.fonte)} Sem promessa de resultado.</p>`;
const feitos = () => D.escopo.filter(x => x[2] === 'feito').length;
const pct = () => Math.round(feitos() / D.escopo_total * 100);

const V = {
  inicio() {
    const kpis = D.kpis.map(([r, v, n]) => `<div class="card kpi"><div class="rot">${esc(r)}</div><div class="val">${esc(v)}</div><div class="var"><span>${esc(n)}</span></div></div>`).join('');
    const agora = D.escopo.filter(x => x[2] !== 'feito').map(x => `<div class="item" style="margin-bottom:8px"><div style="flex:1"><div class="t">${esc(x[0])}. ${esc(x[1])}</div><div class="d">${esc(x[3])}</div></div>${st(x[2])}</div>`).join('');
    return `<div class="cp-aviso"><b>Identidade v10 aprovada (07/11).</b> Marca em texto PROCESSO LEGISLATIVO, preto, dourado fosco e branco. Não é a identidade do Tribuna 98.</div>
    <div class="grade g4">${kpis}</div>
    <div class="grade g21" style="margin-top:16px">
      <div class="card"><h3>Escopo do curso</h3><p class="sub">Partes concluídas do projeto (regra da trava: 30% para abrir projeto novo).</p>
        <div class="cp-barra"><i style="width:${pct()}%"></i></div>
        <p style="margin:0;font-weight:700">${feitos()} de ${D.escopo_total} partes concluídas (${pct()}%)</p>
        <p class="sub" style="margin:8px 0 0">Projeto em andamento, sem novas funções até a identidade e a estrutura do curso.</p></div>
      <div class="card"><h3>O que falta agora</h3><p class="sub">Itens abertos e quem depende de quem.</p>${agora}</div>
    </div>` + nota();
  },
  escopo() {
    return `<div class="card"><h3>Escopo do curso</h3><p class="sub">Os 8 itens do Instagram e da identidade do curso. Status conferido com TRAVA-MAQUIAVEL.md.</p>
    <div style="overflow-x:auto"><table><thead><tr><th>#</th><th>Item</th><th>Status</th><th>O que falta</th></tr></thead><tbody>
    ${D.escopo.map(x => `<tr><td>${esc(x[0])}</td><td><b>${esc(x[1])}</b></td><td>${st(x[2])}</td><td>${esc(x[3])}</td></tr>`).join('')}
    </tbody></table></div></div>` + nota();
  },
  perfil() {
    return `<div class="card"><h3>Perfil e números</h3><p class="sub">Números do print do perfil. Data do print: a confirmar.</p>
    <div style="overflow-x:auto"><table><thead><tr><th>Campo</th><th>Valor</th><th>Situação</th></tr></thead><tbody>
    ${D.perfil.map(x => `<tr><td><b>${esc(x[0])}</b></td><td>${esc(x[1])}</td><td>${esc(x[2])}</td></tr>`).join('')}
    </tbody></table></div></div>
    <div class="card" style="margin-top:16px"><h3>Estrutura do curso</h3><p class="sub">Aulas, ordem e títulos.</p>
    <div class="cp-aviso">A confirmar. O repositório não tem a lista de aulas. Quando o Lindson mandar, entra aqui e nas capas de Reels.</div></div>` + nota();
  },
  pesquisa() {
    return `<div class="card"><h3>Pesquisa premium (identidade)</h3><p class="sub">Regra: 8 referências de 3 países, confirmadas pela própria página, antes de qualquer peça visual.</p>
    <div style="overflow-x:auto"><table><thead><tr><th>Ponto</th><th>Situação</th><th>Status</th></tr></thead><tbody>
    ${D.pesquisa.map(x => `<tr><td><b>${esc(x[0])}</b></td><td>${esc(x[1])}</td><td>${st(x[2])}</td></tr>`).join('')}
    </tbody></table></div>
    <p class="sub" style="margin:12px 0 0">Detalhes e capturas em agencia/clientes/tribuna98/curso-processo-legislativo/TEMPLATE.md.</p></div>` + nota();
  },
  linha() {
    return `<div class="card"><h3>Linha do tempo</h3><p class="sub">O que já aconteceu, em ordem.</p>
    ${D.linha.map(x => `<div class="cp-linha"><b>${esc(x[0])}</b><p>${esc(x[1])} ${st(x[2])}</p></div>`).join('')}
    </div>` + nota();
  },
  proximos() {
    return `<div class="card"><h3>Próximos passos</h3><p class="sub">Na ordem. Quem faz está ao lado de cada passo.</p>
    ${D.proximos.map((x, i) => `<div class="cp-linha"><b>${i + 1}. ${esc(x[0])}</b><p>${esc(x[1])}</p></div>`).join('')}
    </div>` + nota();
  },
  decisoes() {
    return `<div class="sub" style="margin:0 0 14px">Decisões que só o Lindson toma. Cada uma destrava parte do escopo.</div>
    <div class="grade g21">${D.decisoes.map(x => `<div class="card cp-decisao"><div>${st(x[2])}</div><h4>${esc(x[0])}</h4><p>${esc(x[1])}</p></div>`).join('')}</div>` + nota();
  }
};
const T = {inicio:'Visão geral', escopo:'Escopo', perfil:'Perfil e números', pesquisa:'Pesquisa premium', linha:'Linha do tempo', proximos:'Próximos passos', decisoes:'Decisões do Lindson'};

function render() {
  const v = (location.hash || '#inicio').slice(1), view = V[v] ? v : 'inicio';
  $('#titulo').textContent = T[view];
  document.querySelectorAll('.grupo a').forEach(a => a.dataset.v === view ? a.setAttribute('aria-current', 'page') : a.removeAttribute('aria-current'));
  const n = D.decisoes.filter(x => x[2] === 'aguardando').length;
  $('#n-dec').textContent = n || '';
  main.innerHTML = V[view]();
  $('#menu').classList.remove('aberto'); $('#abrir').setAttribute('aria-expanded', 'false');
}
addEventListener('hashchange', render);
$('#abrir').onclick = () => { const m = $('#menu'); m.classList.toggle('aberto'); $('#abrir').setAttribute('aria-expanded', m.classList.contains('aberto')); };
render();
"""
JS = JS.replace('__DADOS__', json.dumps(DADOS, ensure_ascii=False).replace('</', '<\\/'))

MENU = """<nav class="menu" id="menu" aria-label="Menu do painel">
    <div class="logo" style="display:grid;gap:8px;justify-items:start"><div style="font:800 15px/1.05 var(--f-titulo);letter-spacing:.035em"><span style="color:#F8F8F8">PROCESSO</span><br><span style="color:#A89048">LEGISLATIVO</span></div><span style="font:600 10px var(--f-dado);letter-spacing:.24em;color:var(--apagado)">PAINEL DO CURSO</span></div>
    <div class="grupo"><h4>Visão</h4>
      <a href="#inicio" data-v="inicio"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>Visão geral</a>
      <a href="#escopo" data-v="escopo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg>Escopo</a>
      <a href="#perfil" data-v="perfil"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>Perfil e números</a>
      <a href="#linha" data-v="linha"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h10M4 18h13"/></svg>Linha do tempo</a></div>
    <div class="grupo"><h4>Pesquisa</h4>
      <a href="#pesquisa" data-v="pesquisa"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>Pesquisa premium</a></div>
    <div class="grupo"><h4>Próximos</h4>
      <a href="#proximos" data-v="proximos"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 12h14M13 6l6 6-6 6"/></svg>Próximos passos</a></div>
    <div class="grupo"><h4>Decisões</h4>
      <a href="#decisoes" data-v="decisoes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6M12 17h.01"/></svg>Decisões do Lindson<span class="n" id="n-dec"></span></a></div>
    <div class="rodape-menu"><b>@curso_processo_legislativo_</b><span>Marca v10 aprovada em 07/11.</span></div>
  </nav>"""

movimento = open(os.path.join(SC, 'prototipo', 'movimento.js'), encoding='utf-8').read()

html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Curso de processo legislativo · Painel do cliente</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Display:wght@700;800&family=Inter:wght@400;500;600;700&display=swap">
<style>{css}</style>
</head>
<body>
<div class="app">
  {MENU}
  <div class="area">
    <header class="topo">
      <button class="abrir-menu" id="abrir" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false">☰</button>
      <div><h1 id="titulo">Visão geral</h1><div class="cliente">Curso de processo legislativo · @curso_processo_legislativo_ · conteúdos para atuação parlamentar</div></div>
      <div class="dir"><span class="exemplo">Marca v10 aprovada</span><div class="avatar" title="Curso de processo legislativo">CPL</div></div>
    </header>
    <main id="conteudo"></main>
  </div>
</div>
<script>
{JS}
</script>
<script>
{movimento}
</script>
</body>
</html>
"""

saida = os.path.join(D, 'painel-curso.html')
open(saida, 'w', encoding='utf-8').write(html)
print('ok', saida, round(os.path.getsize(saida) / 1024), 'KB')
