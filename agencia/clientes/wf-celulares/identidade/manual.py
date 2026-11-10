# Manual da marca WF Celulares · caminho B (Designer gráfico · conta Leandro · 10/11/2026)
# Estrutura copiada do manual v4.1 da Orégano Turbo (capa, sumário, numeração 01, foto sangrada, ficha curta),
# em 16:9 e na identidade WF (preto, titânio, prata, Inter). Gera manual.html -> node manual-pdf.js
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import gerar3 as g
PRETO, GRAF, TITA, PRATA, BRANCO, TG = g.PRETO, g.GRAF, g.TITA, g.PRATA, g.BRANCO, g.TIT_GRAD
L = lambda *a, w=300: f'<div style="width:{w}px">{g.logo_svg(*a)}</div>'
IMG = lambda n, st='': f'<img src="pecas-final/{n}.jpg" style="display:block;{st}">'
PAGS = []

def pg(titulo, corpo, n=None, fundo=PRETO, cor=BRANCO, sec=''):
    n = n or len(PAGS) + 1
    cab = '' if not titulo else (f'<div style="position:absolute;left:90px;top:70px;font:500 18px Inter;letter-spacing:.24em;color:{TITA}">{n:02d} · {sec.upper()}</div>'
          f'<div style="position:absolute;left:90px;top:110px;font:600 64px/1.05 Inter;letter-spacing:-.04em;color:{cor}">{titulo}</div>')
    rod = f'<div style="position:absolute;left:90px;right:90px;bottom:40px;display:flex;justify-content:space-between;font:400 15px Inter;color:{TITA}"><span>WF Celulares · Manual da marca · v1 · 11/2026</span><span>{n:02d}</span></div>'
    PAGS.append(f'<section class="p" style="background:{fundo};color:{cor}">{cab}{corpo}{rod}</section>')

txt = lambda t, x, y, w=700, s=26, c=PRATA: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font:400 {s}px/1.5 Inter;color:{c}">{t}</div>'
box = lambda x, y, w, h, c: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{c}"></div>'

# 01 capa
pg('', f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 70% 40%,#2a2a2e,#000 65%)"></div>'
   f'<div style="position:absolute;right:220px;top:200px">{L(w=420)}</div>'
   f'<div style="position:absolute;left:90px;top:330px;font:600 110px/1 Inter;letter-spacing:-.05em">Manual<br><span style="background:{TG};-webkit-background-clip:text;color:transparent">da marca.</span></div>'
   + txt('Especialista em iPhone · São Luís (MA)<br>Lacrados · Seminovos · Assistência técnica', 90, 600, 700, 28))

# 02 sumário
itens = ['A marca', 'Persona', 'Tom de voz', 'Logo', 'Construção', 'Proteção e mínimo', 'Versões', 'Usos proibidos', 'Paleta', 'Tipografia',
         'Elementos gráficos', 'Fotografia', 'Instagram', 'Posts', 'Stories', 'Papelaria', 'Fachada', 'Uniforme e embalagem', 'Assinaturas', 'Uso da marca Apple']
lis = ''.join(f'<div style="display:flex;gap:24px;border-top:1px solid #2a2a2c;padding:12px 0;font:400 24px Inter"><span style="color:{TITA};width:40px">{i+3:02d}</span>{t}</div>' for i, t in enumerate(itens))
pg('Sumário', f'<div style="position:absolute;left:90px;right:90px;top:230px;columns:2;column-gap:100px">{lis}</div>', sec='índice')

# 03 marca
pg('Celular com procedência.', f'{box(1100, 0, 820, 1080, "background:url(pecas-final/10-post-produto.jpg) center/cover")}'
   + txt('A WF vende iPhone (e Xiaomi e iPad) lacrado e seminovo, e conserta. O que separa a WF da loja da esquina não é o preço: é a <b style="color:#fff">procedência</b>.<br><br>Todo aparelho e todo conserto sai com o <b style="color:#fff">Laudo WF</b>: testado, bateria medida, garantia e nota fiscal.<br><br><b style="color:#fff">Promessa:</b> "Celular com procedência: testado, com garantia e com nota."<br><br>Sem promessa de prazo ou resultado que dependa de peça.', 90, 250, 900, 28), sec='a marca')

# 04 persona
pg('Para quem a gente fala.', txt('''<b style="color:#fff">Ana, 27, ou Diego, 32.</b> CLT ou autônomo em São Luís, usa o celular para trabalhar (WhatsApp, Instagram, Pix).<br><br>
Quer iPhone, mas o novo de loja não cabe no bolso. Tem medo de seminovo com bateria viciada ou de golpe.<br><br>
Quando a tela quebra, precisa do celular de volta rápido e tem medo de trocarem peça.<br><br>
Confia em avaliação real, garantia por escrito, nota fiscal e loja com endereço. Decide pelo story e pela conversa no WhatsApp.''', 90, 250, 1000, 28)
   + box(1250, 250, 580, 700, f"background:{TG};border-radius:30px") + txt('<b style="font-size:40px;color:#111">"Essa pessoa compraria disso?"</b><br><br>Sim, se ver o laudo e a garantia antes do preço.', 1300, 320, 480, 28, '#111'), sec='persona')

# 05 tom
col = lambda t, itens, c: f'<div style="flex:1;background:{GRAF};border-radius:24px;padding:40px"><div style="font:600 30px Inter;color:{c};margin-bottom:20px">{t}</div>' + ''.join(f'<div style="font:400 24px/1.5 Inter;color:{PRATA};padding:8px 0;border-top:1px solid #333">{i}</div>' for i in itens) + '</div>'
pg('Tom de voz: técnico, simples, de confiança.', f'<div style="position:absolute;left:90px;right:90px;top:260px;display:flex;gap:40px">'
   + col('Dizer', ['"Testado, com garantia e com nota."', '"Orçamento antes de mexer."', '"Te mando o laudo pelo WhatsApp."', '"Especialista em iPhone."', 'Frases curtas, sem gíria de promoção.'], BRANCO)
   + col('Não dizer', ['"O mais barato da cidade" (promessa sem prova)', '"Fica pronto em 1 hora" (depende da peça)', '"Revenda autorizada" (não é)', 'Excesso de emoji 🔥🔥🔥 e CAIXA ALTA', '"Original" sem laudo que comprove'], '#ff6b6b') + '</div>', sec='tom de voz')

# 06 logo principal
pg('Logo principal.', f'<div style="position:absolute;left:0;right:0;top:200px;display:flex;justify-content:center">{L(w=520)}</div>'
   + txt('Maçã e WF em titânio, CELULARES espaçado em prata. Versão moderna do logo que o cliente já usa: sem 3D, sem cromo, sem couro.', 1300, 500, 520, 22), sec='logo')

# 07 construção
grid = ''.join(f'<div style="position:absolute;left:{560+i*60}px;top:200px;width:1px;height:720px;background:#2f6bff55"></div>' for i in range(14))
grid += ''.join(f'<div style="position:absolute;left:560px;top:{200+i*60}px;width:780px;height:1px;background:#2f6bff55"></div>' for i in range(13))
pg('Construção e grid.', grid + f'<div style="position:absolute;left:650px;top:220px">{L(w=600)}</div>'
   + txt('Módulo = altura do traço do W.<br>Maçã: 4 módulos de largura.<br>WF: 10 × 5 módulos, traço com ponta arredondada.<br>Última perna do W = haste do F.<br>CELULARES: Inter Medium, espaço de 0,45 em, alinhado ao centro.', 90, 260, 430, 22), sec='construção')

# 08 proteção
pg('Área de proteção e mínimo.', f'<div style="position:absolute;left:200px;top:240px;padding:70px;border:2px dashed {TITA}">{L(w=320)}</div>'
   + txt('<b style="color:#fff">Proteção:</b> a altura da maçã em volta de todo o logo. Nada entra nessa área.', 200, 900, 600, 22)
   + f'<div style="position:absolute;left:1000px;top:300px;display:flex;gap:70px;align-items:flex-end">{L(w=160)}{L(w=90)}<div style="width:50px">{g.sim_bm(50)}</div></div>'
   + txt('<b style="color:#fff">Mínimo:</b> logo completo 25 mm / 90 px.<br>Abaixo disso, use a marca reduzida (maçã + WF, sem CELULARES): 8 mm / 40 px. É a do avatar e dos posts.', 1000, 560, 760, 22), sec='proteção')

# 09 versões
v = lambda f, a, t, tc=BRANCO: f'<div style="flex:1;background:{f};border-radius:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px">{L(*a, w=220)}<span style="font:500 20px Inter;color:{tc}">{t}</span></div>'
pg('Versões.', '<div style="position:absolute;left:90px;right:90px;top:240px;bottom:120px;display:flex;gap:24px">'
   + v(PRETO + ';border:1px solid #333', (), 'Cor (titânio) · fundo escuro') + v('#1D1D1F', ('#fff', '#fff', '#fff'), 'Branca') + v(BRANCO, ('#000', '#000', '#000'), 'Preta', '#111')
   + v(TG, ('#1D1D1F', '#1D1D1F', '#1D1D1F'), 'Monocromática · gravação e carimbo', '#111') + '</div>', sec='versões')

# 10 proibidos
X = lambda s, t, f=PRETO: f'<div style="flex:1;background:{f};border:1px solid #333;border-radius:20px;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:20px"><div style="{s}">{L(w=150)}</div><span style="font:500 18px Inter;color:#ff6b6b;text-align:center">✕ {t}</span></div>'
pg('Usos proibidos.', '<div style="position:absolute;left:90px;right:90px;top:240px;height:330px;display:flex;gap:20px">'
   + X('transform:scaleX(1.5)', 'Distorcer') + X('transform:rotate(-20deg)', 'Girar') + X('filter:drop-shadow(8px 8px 0 #2f6bff) drop-shadow(0 0 20px #2f6bff)', 'Sombra, brilho ou 3D') + '</div>'
   + '<div style="position:absolute;left:90px;right:90px;top:600px;height:330px;display:flex;gap:20px">'
   + X('opacity:.35', 'Pouco contraste', '#8E8A84') + X('filter:hue-rotate(180deg) saturate(8)', 'Mudar a cor') + X('', 'Sobre foto poluída', 'url(banco/r-1563770660941-20978e870e26.jpg) center/cover') + '</div>', sec='usos proibidos')

# 11 paleta
cores = [('Preto', '#000000', '0 0 0', '0 0 0 100', '50%'), ('Grafite', '#1D1D1F', '29 29 31', '0 0 0 90', '20%'), ('Titânio', '#8E8A84', '142 138 132', '0 3 7 44', '15%'),
         ('Prata', '#C7C9CC', '199 201 204', '2 1 0 20', '10%'), ('Branco gelo', '#F5F5F7', '245 245 247', '1 1 0 3', '5%')]
cc = ''.join(f'<div style="flex:{p[:-1]};background:{h};padding:30px;display:flex;flex-direction:column;justify-content:flex-end;color:{"#111" if i>2 else "#fff"};border:1px solid #333">'
             f'<b style="font:600 30px Inter">{n}</b><span style="font:400 17px/1.6 Inter">HEX {h}<br>RGB {r}<br>CMYK {c}<br>{p} do uso</span></div>' for i, (n, h, r, c, p) in enumerate(cores))
pg('Paleta.', f'<div style="position:absolute;left:90px;right:90px;top:240px;height:620px;display:flex">{cc}</div>'
   + txt(f'Gradiente titânio (só em logo, títulos curtos e etiqueta): <span style="display:inline-block;width:300px;height:22px;background:{TG};vertical-align:middle;border-radius:11px"></span>', 90, 890, 1200, 20), sec='paleta')

# 12 tipografia
pg('Tipografia: Inter.', f'<div style="position:absolute;left:90px;top:240px;font:600 260px/1 Inter;letter-spacing:-.05em">Aa<span style="background:{TG};-webkit-background-clip:text;color:transparent">Gg</span></div>'
   + f'<div style="position:absolute;left:900px;top:250px;font:600 54px/1.1 Inter;letter-spacing:-.04em">Títulos · Inter SemiBold<br><span style="font-weight:400;font-size:30px;letter-spacing:0;color:{PRATA}">Textos · Inter Regular 400, entrelinha 1,5</span><br><span style="font-weight:500;font-size:22px;letter-spacing:.4em;color:{TITA}">RÓTULOS · INTER MEDIUM ESPAÇADA</span></div>'
   + txt('Uma família só, com variação de peso. Título em 2 linhas: a 2ª em gradiente titânio. Gratuita no Google Fonts. Nunca usar a fonte San Francisco.', 900, 620, 850, 24), sec='tipografia')

# 13 elementos
pg('Elementos gráficos.', f'<div style="position:absolute;left:90px;top:250px;width:520px;height:600px;border-radius:30px;overflow:hidden">{IMG("14-cartao-etiqueta","width:1100px;margin-left:-560px;margin-top:-80px")}</div>'
   + f'<svg viewBox="0 0 100 100" width="360" height="360" style="position:absolute;left:720px;top:280px">{g.DEFS}<circle cx="50" cy="50" r="44" fill="none" stroke="url(#ti)" stroke-width="2"/><rect x="47.6" y="88" width="4.8" height="9" rx="2.4" fill="url(#ti)"/></svg>'
   + box(1250, 280, 580, 360, "border-radius:30px;background:radial-gradient(circle at 50% 30%,#2b2b2e,#000 72%)")
   + txt('<b style="color:#fff">Laudo WF</b><br>etiqueta titânio com checklist. Vai na caixa, no post e no story.', 90, 870, 520, 20)
   + txt('<b style="color:#fff">Anel</b><br>contorno fino de titânio para ícones e destaques.', 720, 870, 420, 20)
   + txt('<b style="color:#fff">Luz de vitrine</b><br>radial grafite → preto: fundo padrão de toda peça escura.', 1250, 870, 560, 20), sec='elementos')

# 14 fotografia
pg('Fotografia.', f'<div style="position:absolute;left:90px;top:240px;width:820px;height:560px;background:url(banco/1592750475338-74b7b21085ab.jpg) center/cover;border-radius:24px"></div>'
   + f'<div style="position:absolute;left:1000px;top:240px;width:820px;height:560px;background:url(banco/r-1563770660941-20978e870e26.jpg) center/cover;border-radius:24px;filter:grayscale(.3)"></div>'
   + txt('<b style="color:#fff">Usar:</b> aparelho real, fundo escuro, luz lateral, muito respiro; mãos reais no conserto; a loja e a equipe de verdade (prioridade).', 90, 830, 820, 22)
   + txt('<b style="color:#ff6b6b">Evitar:</b> foto de banco fingindo ser a loja, montagem com fogo e cifrão, print de catálogo, foto tremida. Banco só com crédito "foto ilustrativa".', 1000, 830, 820, 22), sec='fotografia')

# 15 instagram
dest = ''.join(f'<div style="text-align:center"><img src="pecas-final/{n}.jpg" style="width:150px;height:150px;border-radius:50%;display:block"></div>' for n in ['04-destaque-lacrados', '05-destaque-seminovos', '06-destaque-assistencia', '07-destaque-avaliacoes', '08-destaque-entrega', '09-destaque-localizacao'])
pg('Instagram.', f'<img src="pecas-final/03-avatar.jpg" style="position:absolute;left:90px;top:250px;width:300px;height:300px;border-radius:50%">'
   + f'<img src="pecas-final/03-avatar.jpg" style="position:absolute;left:420px;top:440px;width:110px;height:110px;border-radius:50%">'
   + txt('Avatar = logo completo. Conferido em 110 px. Nunca promoção no avatar.', 560, 450, 500, 20)
   + f'<div style="position:absolute;left:90px;top:640px;display:flex;gap:30px">{dest}</div>'
   + f'<div style="position:absolute;left:1260px;top:240px;width:570px;display:grid;grid-template-columns:repeat(3,1fr);gap:6px">'
   + ''.join(IMG(n, 'width:100%;aspect-ratio:4/5;object-fit:cover') for n in ['10-post-produto', '11-post-assistencia', '12-post-prova', '11-post-assistencia', '12-post-prova', '10-post-produto']) + '</div>'
   + txt('Grid: alternar escuro e claro, produto e conserto. Nunca 2 iguais seguidos.', 1260, 960, 570, 18), sec='instagram')

# 16 posts
pg('Posts.', '<div style="position:absolute;left:90px;right:90px;top:230px;display:flex;gap:40px">'
   + ''.join(IMG(n, 'width:560px;height:700px;object-fit:cover;border-radius:16px') for n in ['10-post-produto', '11-post-assistencia', '12-post-prova']) + '</div>', sec='posts')

# 17 stories (mockup no próprio manual, 9:16)
st = lambda corpo, f=PRETO: f'<div style="width:400px;height:711px;border-radius:30px;overflow:hidden;position:relative;background:{f};border:8px solid #222">{corpo}</div>'
pg('Stories.', '<div style="position:absolute;left:0;right:0;top:220px;display:flex;justify-content:center;gap:60px">'
   + st(f'<div style="position:absolute;inset:0;background:url(banco/1592750475338-74b7b21085ab.jpg) 50% 60%/cover"></div><div style="position:absolute;inset:0;background:linear-gradient(#000 30%,transparent 60%)"></div><div style="position:absolute;left:30px;top:60px;font:600 44px/1.05 Inter;letter-spacing:-.04em;color:#fff">Chegou<br><span style="background:{TG};-webkit-background-clip:text;color:transparent">seminovo.</span></div><div style="position:absolute;left:30px;right:30px;bottom:40px;background:#fff;color:#111;border-radius:40px;padding:16px;text-align:center;font:600 20px Inter">Pedir laudo no WhatsApp</div>')
   + st(f'<div style="position:absolute;left:30px;right:30px;top:120px;background:{TG};border-radius:20px;padding:30px;color:#111;font:400 22px/1.7 Inter"><b>Laudo WF</b><br>✓ Testado<br>✓ Bateria medida<br>✓ Garantia<br>✓ Nota fiscal</div><div style="position:absolute;left:30px;bottom:60px;font:600 34px/1.1 Inter;color:#fff">Todo aparelho<br>sai assim.</div><div style="position:absolute;left:30px;top:40px;font:400 14px Inter;color:{TITA}">dado ilustrativo</div>', 'radial-gradient(circle at 50% 30%,#2b2b2e,#000 72%)')
   + st(f'<div style="position:absolute;top:120px;left:0;right:0;display:flex;justify-content:center">{L(w=200)}</div><div style="position:absolute;left:30px;right:30px;bottom:120px;font:600 34px/1.15 Inter;color:#fff;text-align:center">Quebrou?<br>Orçamento antes<br>de mexer.</div><div style="position:absolute;left:30px;right:30px;bottom:40px;border:1px solid {TITA};border-radius:40px;padding:14px;text-align:center;font:500 18px Inter;color:#fff">São Cristóvão · Renascença</div>')
   + '</div>', sec='stories')

# 18 papelaria
pg('Papelaria.', IMG('14-cartao-etiqueta', 'position:absolute;left:90px;top:220px;width:1300px;border-radius:20px')
   + txt('Cartão 90 × 50 mm: frente preta com logo titânio (hot stamping prata), verso branco com dados.<br><br>Etiqueta de laudo 70 × 50 mm, papel metalizado: vai colada na caixa de todo aparelho vendido ou consertado.', 1430, 260, 400, 22), sec='papelaria')

# 19 fachada
pg('Fachada e sinalização.', IMG('13-fachada', 'position:absolute;left:90px;top:220px;width:1300px;border-radius:20px')
   + txt('Letreiro preto fosco, logo em ACM escovado prata com luz de fundo (backlight branco frio).<br><br>Faixa "ESPECIALISTA EM IPHONE" em Inter Medium espaçada.<br><br>Vitrine com o produto, nunca cartaz de preço colado no vidro.', 1430, 260, 400, 22), sec='fachada')

# 20 uniforme e embalagem
cam = f'''<svg viewBox="0 0 200 200" width="480" height="480"><path d="M60 20 L90 14 Q100 26 110 14 L140 20 L180 50 L162 80 L146 70 L146 186 L54 186 L54 70 L38 80 L20 50 Z" fill="#111" stroke="#2a2a2c" stroke-width="2"/></svg>'''
pg('Uniforme e embalagem.', f'<div style="position:absolute;left:120px;top:240px">{cam}</div><div style="position:absolute;left:300px;top:340px">{L(w=110)}</div>'
   + f'<div style="position:absolute;left:820px;top:300px;width:420px;height:420px;background:#0b0b0c;border-radius:12px;box-shadow:30px 30px 60px #000,inset 0 0 0 1px #333;transform:rotate(-6deg);display:flex;align-items:center;justify-content:center">{L(w=170)}</div>'
   + f'<div style="position:absolute;left:1350px;top:280px;width:380px;height:480px;background:{BRANCO};border-radius:8px 8px 20px 20px;box-shadow:30px 30px 60px #000;display:flex;align-items:center;justify-content:center">{L("#111","#111","#111",w=160)}</div>'
   + txt('Camiseta preta, logo titânio no peito (silk prata).', 120, 760, 480, 20) + txt('Caixa preta fosca, logo em hot stamping.', 820, 780, 420, 20) + txt('Sacola branca, logo preto.', 1350, 790, 380, 20)
   + txt('Mockups ilustrativos', 90, 960, 400, 16, TITA), sec='uniforme e embalagem')

# 21 assinaturas
pg('WhatsApp e e-mail.', f'<div style="position:absolute;left:90px;top:240px;width:760px;background:#0b141a;border-radius:24px;padding:40px;font:400 24px/1.5 Inter;color:#e9edef">'
   f'<div style="background:#005c4b;border-radius:14px;padding:20px 24px;margin-left:120px">Oi! Aqui é da WF Celulares 👋<br>Me fala o modelo e o que aconteceu que eu te passo o orçamento antes de mexer.</div>'
   f'<div style="background:#005c4b;border-radius:14px;padding:20px 24px;margin:16px 0 0 120px">📍 São Cristóvão | Renascença<br>WF Celulares · Especialista em iPhone</div></div>'
   + f'<div style="position:absolute;left:960px;top:240px;width:860px;background:#fff;border-radius:24px;padding:40px;display:flex;gap:30px;align-items:center">{L("#111","#111","#111",w=110)}'
   f'<div style="border-left:2px solid #ddd;padding-left:30px;font:400 22px/1.5 Inter;color:#333"><b style="color:#111">Nome Sobrenome</b><br>WF Celulares · Especialista em iPhone<br>(98) 98827-1882 · @wfcelulares (sugerido)<br>São Cristóvão · Renascença · São Luís</div></div>'
   + txt('Mensagem padrão do WhatsApp Business: curta, com nome da loja, o próximo passo e o bairro. No máximo 1 emoji por mensagem.', 960, 600, 860, 22), sec='assinaturas')

# 22 nota Apple
pg('Uso da marca Apple.', txt('''A maçã aparece no logo da WF Celulares porque <b style="color:#fff">o uso foi informado como autorizado pelo cliente</b> (Lindson Almeida, 10/11/2026).<br><br>
<b style="color:#fff">Guardar o documento da autorização</b> no arquivo do cliente (privado: <span style="font-family:monospace">dados/clientes-arquivos/wf-celulares/</span>).<br><br>
iPhone, iPad e a maçã são marcas da Apple Inc. Enquanto o documento não estiver arquivado, não produzir peças impressas de grande tiragem (fachada, uniforme, embalagem) com a maçã.''', 90, 260, 1300, 28), sec='nota legal')

F = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
html = (f'<!doctype html><html><head><meta charset="utf-8">{F}<style>@page{{size:1920px 1080px;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}'
        'body{background:#000}.p{width:1920px;height:1080px;position:relative;page-break-after:always;overflow:hidden}</style></head><body>' + ''.join(PAGS) + '</body></html>')
open(os.path.join(D, 'manual.html'), 'w').write(html); print(len(PAGS), 'páginas')
