"""Painel do Tribuna 98 (Thiago Azevedo) = o modelo da Central (../prototipo/painel.html), com:
- o CSS e o menu lateral do modelo, na identidade do Tribuna (azul royal + amarelo da logo, Anton nos títulos);
- as telas próprias do escopo (Visão geral, Escopo, Linha do tempo, Monetização, Próximos passos, Decisões do Lindson);
- prototipo/movimento.js (animações do modelo) por último.
Só entram números já salvos (03/11/2026, README.md) e os caminhos da ANALISE-E-MONETIZACAO.md. Nada de foto dos sócios (item 6 do escopo).
Uso: python3 montar-tribuna.py -> painel-tribuna.html (arquivo único, sem banco). Conta Leandro, 07/11/2026."""
import base64, io, json, os, re
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..')
CL = os.path.join(D, '..', '..', 'clientes', 'tribuna98')

def logo_uri(p, w=280):
    im = Image.open(p).convert('RGBA'); im.thumbnail((w, w))
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()

modelo = open(os.path.join(SC, 'prototipo', 'painel.html')).read()
css_modelo = re.search(r'<style>(.*?)</style>', modelo, re.S).group(1)

# 1 · identidade do Tribuna: azul royal e amarelo da logo (#F0C52E), Anton nos títulos, Manrope no corpo
ROOT = """:root{
  --fundo:#061236;--painel:#0B1F52;--painel2:#112B6B;--linha:#1C3A86;--amarelo:#F0C52E;--amarelo2:#F9DA5C;
  --royal:#3864B4;--texto:#F5F7FF;--apagado:#A7B6DE;--ok:#5CC98A;--alerta:#F2A93B;--erro:#E5604D;
  --f-titulo:'Anton',Impact,'Arial Narrow',sans-serif;--f-corpo:'Manrope',system-ui,sans-serif;--f-dado:'Manrope',system-ui,sans-serif;
  color-scheme:dark;
}"""
css = re.sub(r':root\{.*?\}', lambda m: ROOT, css_modelo, count=1, flags=re.S)
css = css.replace('.menu{position:sticky', '.menu{background:linear-gradient(180deg,#0A2466,#061236)!important;position:sticky', 1)
css += """
/* Tribuna 98: extras do painel (linha do tempo, status e cartões de decisão) */
.tb-status{display:inline-block;padding:3px 10px;border-radius:999px;font:700 11.5px var(--f-dado);white-space:nowrap}
.tb-status.feito{background:rgba(92,201,138,.16);color:var(--ok)}
.tb-status.andamento{background:rgba(240,197,46,.16);color:var(--amarelo)}
.tb-status.espera{background:rgba(242,169,59,.16);color:var(--alerta)}
.tb-status.fazer{background:rgba(167,182,222,.12);color:var(--apagado)}
.tb-linha{display:grid;grid-template-columns:86px 1fr;gap:14px;padding:12px 0;border-bottom:1px solid var(--linha)}
.tb-linha:last-child{border-bottom:0}
.tb-linha b{font:700 13px var(--f-dado);color:var(--amarelo)}
.tb-linha p{margin:0}
.tb-aviso{border:1px dashed var(--linha);border-radius:12px;padding:12px 14px;color:var(--apagado);font-size:12.5px;line-height:1.5}
.tb-tabela{width:100%;border-collapse:collapse;font-size:13.5px}
.tb-tabela th,.tb-tabela td{text-align:left;padding:10px 8px;border-bottom:1px solid var(--linha);vertical-align:top}
.tb-tabela th{color:var(--apagado);font:600 11.5px var(--f-dado);text-transform:uppercase;letter-spacing:.08em}
.tb-barra{height:10px;border-radius:99px;background:var(--painel2);overflow:hidden;margin:10px 0 4px}
.tb-barra i{display:block;height:100%;background:linear-gradient(90deg,var(--royal),var(--amarelo));border-radius:99px}
.tb-decisao{display:grid;gap:8px}
.tb-decisao h4{margin:0;font:400 22px/1.1 var(--f-titulo);text-transform:uppercase;letter-spacing:.02em}
.tb-decisao p{margin:0;color:#D5DCF2;font-size:13.5px;line-height:1.5}
.tb-rodape{color:var(--apagado);font-size:12px;line-height:1.5;margin-top:18px;border-top:1px solid var(--linha);padding-top:12px}
.tb-chip-qtd{background:var(--amarelo);color:#061236;border-radius:999px;padding:0 7px;font:800 11px var(--f-dado);margin-left:6px}
"""

# 2 · dados (só o que já está salvo; o que falta aparece como "a confirmar")
DADOS = {
  "fonte": "Números de 03/11/2026 (agencia/clientes/tribuna98/README.md). Prints de 07/11 ainda não salvos: a confirmar.",
  "escopo_total": 8,
  "kpis": [
    ["Instagram @tribuna98_", "71,5 mil", "seguidores · verificado"],
    ["Posts no Instagram", "2.510", "desde a criação da conta"],
    ["TikTok @tribuna098", "7,1 mil", "seguidores · 42,4 mil curtidas"],
    ["YouTube @tribuna098", "296", "inscritos · 30 vídeos"],
    ["Site tribuna98.com.br", "3 por dia", "matérias publicadas (WordPress)"],
    ["Insights e Analytics", "a confirmar", "sem acesso até agora (item 8)"]
  ],
  "canais": [
    ["Instagram", "@tribuna98_", "71,5 mil seguidores", "Principal. Reels do Thiago para a câmera e cards de manchete"],
    ["TikTok", "@tribuna098", "7,1 mil seguidores", "Mesmos Reels, sem linha própria"],
    ["YouTube", "@tribuna098", "296 inscritos", "Entrevistas de 30 a 60 min quase sem visualização"],
    ["Kwai", "@Triibuna98", "65 seguidores", "Espelho do Instagram"],
    ["Site", "tribuna98.com.br", "3 matérias por dia", "Blog sem página Anuncie nem mídia kit"]
  ],
  "escopo": [
    ["1", "Mini site da bio no ar + bio + 7 destaques", "feito", "No ar em tribuna98.pages.dev. Aprovação do cliente: espera"],
    ["2", "Análise das redes + caminhos para monetizar", "feito", "Feita com os números de 03/11. Falta trocar pelos prints de 07/11"],
    ["3", "Painel do Tribuna 98 na Central", "feito", "Este painel. Dados reais entram quando o Lindson mandar os prints"],
    ["4", "Site principal (substituir o WordPress ou ficar ao lado)", "espera", "Decisão do Lindson"],
    ["5", "Instagram do curso de processo legislativo", "andamento", "9 capas de Reels em andamento. Faltam o @ e a estrutura do curso"],
    ["6", "Imagens de IA dos sócios (com autorização)", "espera", "Nome e 5 a 10 fotos de cada sócio, com autorização. Nenhuma imagem sem isso"],
    ["7", "Artes do feed, calendário e roteiros do curso", "fazer", "Depois do item 5 e da estrutura do curso"],
    ["8", "Acessos e Insights do Instagram", "espera", "Print dos últimos 90 dias. Sem isso o painel não tem números reais"]
  ],
  "linha": [
    ["03/11", "Ficha do cliente com todos os canais (Instagram, TikTok, YouTube, Kwai e Linktree)", "feito"],
    ["03/11", "Bio nova, 7 capas de destaques e mini site da bio no ar (tribuna98.pages.dev)", "feito"],
    ["07/11", "Escopo definido pelo Lindson: 8 itens e trava de projeto (Thiago Fonseca, empresa Tribuna 98)", "feito"],
    ["07/11", "Análise das redes e 6 caminhos para monetizar (parte 2 do escopo)", "feito"],
    ["07/11", "Painel do Tribuna 98 na Central (parte 3 do escopo)", "feito"],
    ["07/11", "9 capas de Reels do curso de processo legislativo", "andamento"],
    ["07/11", "Foto de perfil do curso com os sócios: parada até a autorização de cada sócio", "espera"]
  ],
  "caminhos": [
    ["1", "Página Anuncie e mídia kit (site e Linktree)", "Sem ela nenhum anunciante encontra o Tribuna", "Baixo", "Baixo", "Insights do IG e Analytics"],
    ["2", "Anúncio direto para comércio local (banner no blog, post patrocinado, menção em Reels), com a etiqueta Publicidade", "É a compra que o público já faz: lojas, clínicas, escolas", "Médio", "Baixo, se marcado como publicidade", "Mídia kit e lista de 20 comércios"],
    ["3", "Lista própria (WhatsApp Channel ou newsletter)", "A audiência hoje é alugada do Instagram", "Baixo a médio", "Baixo", "Formulário no site e no Linktree"],
    ["4", "Cortes das entrevistas do YouTube em Shorts e Reels", "Transforma o acervo parado em alcance", "Médio", "Baixo", "Edição"],
    ["5", "Anúncios automáticos no blog (rede de display)", "Receita passiva, com pouco tráfego", "Baixo", "Médio: rede pode recusar conteúdo político", "Analytics medido antes"],
    ["6", "Patrocínio de série (ex.: 'Fiscaliza Tribuna')", "Receita maior, mas exige audiência provada", "Alto", "Alto: conflito de interesse", "Passos 1 a 3 feitos"]
  ],
  "cuidados": [
    "Todo conteúdo pago leva a etiqueta Publicidade ou Conteúdo patrocinado.",
    "Quem paga não escolhe a pauta nem o texto. Matéria paga disfarçada fica fora.",
    "Checar fatos e fontes nas matérias de licitação (documento público, PNCP). Direito de resposta registrado.",
    "Ano eleitoral: qualquer venda a candidato passa pelo advogado eleitoral antes.",
    "Nenhuma promessa de receita. Valores de anúncio saem só na conversa com o Thiago e o anunciante."
  ],
  "proximos": [
    ["Lindson", "Mandar os prints de 07/11 (Instagram, YouTube e site) e o print do Insights dos últimos 90 dias"],
    ["Equipe", "Montar a página Anuncie e a mídia kit com os números reais, sem preço, e passar pelo Design Squad"],
    ["Equipe", "Lista de 20 comércios de São Luís e do interior, só com o OK do Lindson sobre quem abordar"],
    ["Equipe", "Levantar o tráfego do site no Analytics quando o acesso chegar, e só então decidir sobre o anúncio no blog"],
    ["Equipe", "Planejar 9 Shorts a partir de 3 entrevistas (uma ideia por corte, com legenda e fonte), depois das aprovações"],
    ["Lindson", "Dizer se quer a lista própria (passo 3) e se aceita a regra do ano eleitoral para o passo 2"]
  ],
  "decisoes": [
    ["Site principal: substituir o WordPress ou ficar ao lado?", "Item 4 do escopo. Substituir é mais trabalho e mais controle; ao lado é mais rápido e não mexe no blog que já publica 3 matérias por dia.", "aguardando"],
    ["@ do curso de processo legislativo", "Item 5. Sem o @ não dá para gerar as capas finais nem a foto de perfil do curso.", "aguardando"],
    ["Autorização dos sócios para usar a imagem", "Item 6. Precisa de nome e 5 a 10 fotos de cada sócio, com autorização escrita de cada um. Sem isso, nenhuma imagem de IA dos sócios.", "aguardando"],
    ["Insights do Instagram (últimos 90 dias)", "Item 8. É a prova de audiência para vender anúncio. Sem ela, a página Anuncie sai sem números.", "aguardando"],
    ["Vender só para comércio, ou também para candidatos?", "Venda a candidato passa pelo advogado eleitoral (Lei 9.504/97). Decisão do Lindson antes de montar a proposta.", "aguardando"]
  ]
}

# 3 · telas (JS do próprio painel; o menu, o topo, os cartões e as animações vêm do modelo)
JS = r"""
const D = __DADOS__;
const $ = s => document.querySelector(s), main = $('#conteudo');
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const ST = {feito:['feito','✅ Feito'], andamento:['andamento','🟡 Em andamento'], espera:['espera','⏳ Depende de outro'], fazer:['fazer','⬜ A fazer'], aguardando:['espera','⏳ Aguardando']};
const st = k => { const [c, t] = ST[k] || ST.fazer; return `<span class="tb-status ${c}">${t}</span>`; };
const nota = () => `<p class="tb-rodape">${esc(D.fonte)} Sem promessa de receita: valores de anúncio só na conversa com o cliente.</p>`;
const feitos = () => D.escopo.filter(x => x[2] === 'feito').length;
const pct = () => Math.round(feitos() / D.escopo_total * 100);

const V = {
  inicio() {
    const kpis = D.kpis.map(([r, v, n]) => `<div class="card kpi"><div class="rot">${esc(r)}</div><div class="val">${esc(v)}</div><div class="var"><span>${esc(n)}</span></div></div>`).join('');
    const agora = D.escopo.filter(x => x[2] !== 'feito').map(x => `<div class="lista-item" style="padding:8px 0;border-bottom:1px solid var(--linha)"><div style="display:flex;justify-content:space-between;gap:10px;align-items:center"><b>${esc(x[0])}. ${esc(x[1])}</b>${st(x[2])}</div><div class="sub" style="margin:4px 0 0">${esc(x[3])}</div></div>`).join('');
    return `<div class="grade g4">${kpis}</div>
    <div class="grade g21" style="margin-top:16px">
      <div class="card"><h3>Escopo do projeto</h3><p class="sub">Pagante. Quanto mais partes concluídas, menos projeto aberto (regra da trava).</p>
        <div class="tb-barra"><i style="width:${pct()}%"></i></div>
        <p style="margin:0;font-weight:700">${feitos()} de ${D.escopo_total} partes concluídas (${pct()}%)</p>
        <p class="sub" style="margin:8px 0 0">Mínimo para abrir projeto novo: 30%. Este projeto já passou desse mínimo.</p></div>
      <div class="card"><h3>O que falta agora</h3><p class="sub">Itens abertos do escopo, com o que depende de quem.</p>${agora}</div>
    </div>
    <div class="card" style="margin-top:16px"><h3>Canais hoje</h3><p class="sub">Números de 03/11. Prints de 07/11 e Insights: a confirmar.</p>
      <div style="overflow-x:auto"><table class="tb-tabela"><thead><tr><th>Canal</th><th>Endereço</th><th>Números</th><th>Leitura</th></tr></thead><tbody>
      ${D.canais.map(c => `<tr><td><b>${esc(c[0])}</b></td><td>${esc(c[1])}</td><td>${esc(c[2])}</td><td>${esc(c[3])}</td></tr>`).join('')}
      </tbody></table></div></div>` + nota();
  },
  escopo() {
    return `<div class="card"><h3>Escopo do Tribuna 98</h3><p class="sub">Os 8 itens definidos pelo Lindson em 07/11. Status conferido com TRAVA-MAQUIAVEL.md.</p>
    <div style="overflow-x:auto"><table class="tb-tabela"><thead><tr><th>#</th><th>Item</th><th>Status</th><th>O que falta</th></tr></thead><tbody>
    ${D.escopo.map(x => `<tr><td>${esc(x[0])}</td><td><b>${esc(x[1])}</b></td><td>${st(x[2])}</td><td>${esc(x[3])}</td></tr>`).join('')}
    </tbody></table></div></div>` + nota();
  },
  linha() {
    return `<div class="card"><h3>Linha do tempo</h3><p class="sub">O que já foi entregue e o que está em andamento, em ordem.</p>
    ${D.linha.map(x => `<div class="tb-linha"><b>${esc(x[0])}</b><p>${esc(x[1])} ${st(x[2])}</p></div>`).join('')}
    </div>` + nota();
  },
  monet() {
    return `<div class="card"><h3>Caminhos para monetizar</h3><p class="sub">Em ordem de prioridade. Detalhes e fontes em ANALISE-E-MONETIZACAO.md.</p>
    <div style="overflow-x:auto"><table class="tb-tabela"><thead><tr><th>#</th><th>Caminho</th><th>Por que este</th><th>Esforço</th><th>Risco</th><th>Precisa de</th></tr></thead><tbody>
    ${D.caminhos.map(x => `<tr><td>${esc(x[0])}</td><td><b>${esc(x[1])}</b></td><td>${esc(x[2])}</td><td>${esc(x[3])}</td><td>${esc(x[4])}</td><td>${esc(x[5])}</td></tr>`).join('')}
    </tbody></table></div></div>
    <div class="card" style="margin-top:16px"><h3>Cuidados</h3><div class="lista">${D.cuidados.map(c => `<div class="item" style="padding:8px 0;border-bottom:1px solid var(--linha)">${esc(c)}</div>`).join('')}</div></div>` + nota();
  },
  proximos() {
    return `<div class="card"><h3>Próximos passos</h3><p class="sub">Na ordem. Quem faz está ao lado de cada passo.</p>
    ${D.proximos.map((x, i) => `<div class="tb-linha"><b>${i + 1}. ${esc(x[0])}</b><p>${esc(x[1])}</p></div>`).join('')}
    </div>` + nota();
  },
  decisoes() {
    return `<div class="sub" style="margin:0 0 14px">Decisões que só o Lindson toma. Cada uma destrava parte do escopo.</div>
    <div class="grade g21">${D.decisoes.map((x, i) => `<div class="card tb-decisao"><div>${st(x[2])}</div><h4>${esc(x[0])}</h4><p>${esc(x[1])}</p></div>`).join('')}</div>` + nota();
  }
};
const T = {inicio:'Visão geral', escopo:'Escopo', linha:'Linha do tempo', monet:'Monetização', proximos:'Próximos passos', decisoes:'Decisões do Lindson'};

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
    <div class="logo" style="display:grid;gap:10px;justify-items:start"><img src="__LOGO__" alt="Tribuna 98" style="width:170px"><span style="font:600 10px var(--f-dado);letter-spacing:.24em;color:var(--amarelo)">PAINEL DO CLIENTE</span></div>
    <div class="grupo"><h4>Visão</h4>
      <a href="#inicio" data-v="inicio"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>Visão geral</a>
      <a href="#escopo" data-v="escopo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg>Escopo</a>
      <a href="#linha" data-v="linha"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h10M4 18h13"/></svg>Linha do tempo</a></div>
    <div class="grupo"><h4>Negócio</h4>
      <a href="#monet" data-v="monet"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>Monetização</a>
      <a href="#proximos" data-v="proximos"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 12h14M13 6l6 6-6 6"/></svg>Próximos passos</a></div>
    <div class="grupo"><h4>Decisões</h4>
      <a href="#decisoes" data-v="decisoes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6M12 17h.01"/></svg>Decisões do Lindson<span class="n" id="n-dec"></span></a></div>
    <div class="rodape-menu"><b>Precisa de algo agora?</b><span>Fale direto com a equipe do Lindson.</span>
      <a class="btn am" href="https://wa.me/5598985621808?text=Oi%2C%20Lindson%21%20Vim%20pelo%20painel%20do%20Tribuna%2098." target="_blank" rel="noopener">Chamar no WhatsApp</a></div>
  </nav>"""

LOGO = logo_uri(os.path.join(CL, 'marca', 'logo.png'))
movimento = open(os.path.join(SC, 'prototipo', 'movimento.js')).read()

html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tribuna 98 · Painel do cliente</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;500;600;700;800&display=swap">
<style>{css}</style>
</head>
<body>
<div class="app">
  {MENU.replace('__LOGO__', LOGO)}
  <div class="area">
    <header class="topo">
      <button class="abrir-menu" id="abrir" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false">☰</button>
      <div><h1 id="titulo">Visão geral</h1><div class="cliente">Tribuna 98 · Thiago Azevedo · jornalismo político do Maranhão</div></div>
      <div class="dir"><span class="exemplo">Dados de 03/11/2026</span><div class="avatar" title="Tribuna 98">T98</div></div>
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

saida = os.path.join(D, 'painel-tribuna.html')
open(saida, 'w').write(html)
print('ok', saida, round(os.path.getsize(saida) / 1024), 'KB')
