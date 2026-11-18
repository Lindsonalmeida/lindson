"""Site institucional Al Kántara Group (fase 2, conta Zuleide/Webdesigner, 16/11/2026).
Gera fase2/site/*.html. Referências: Lippincott (serifada editorial gigante), Landor (símbolo gigante cortado na borda),
Wolff Olins (marca em volume, prova aplicada). Sem número inventado, sem promessa.
  python3 gerador/site.py"""
import os
D = os.environ.get('SITE_DIR') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
WA = 'https://wa.me/5598985621808?text='
from urllib.parse import quote
P = ['M0,0 L100,480 L164,480 L164,0 Z', 'M196,0 L196,199.19 L380.54,0 Z', 'M480,0 L424.16,0 L201.32,240.53 L384.39,458.93 Z', 'M360.3,480 L196,283.99 L196,480 Z']
def simb(cores=('currentColor',) * 4, cls='simb'):
    return f'<svg class="{cls}" viewBox="0 0 480 480" aria-hidden="true">' + ''.join(f'<path fill="{c}" d="{p}"/>' for c, p in zip(cores, P)) + '</svg>'
CORES = ('#2E4BFF', '#E8461E', '#F0A202', '#0E8C66')
DIV = {
 'labs': dict(n='Labs', num='01', cor='#2E4BFF', area='IA e software', verbo='Construímos a tecnologia.', pedra='a haste do símbolo',
   lead='Sistemas, automações e agentes de IA para empresas de serviço com processo que se repete. Sua equipe usa no primeiro dia, com responsável e prazo por escrito.',
   para='Diretores de operação, clínicas, redes de serviço e times comerciais que perdem horas em tarefa repetida.',
   faz=[('Automação de atendimento', 'Fluxos no WhatsApp que respondem, agendam e passam para a pessoa certa.'), ('Agentes de IA', 'Assistentes treinados no seu processo, rodando no seu servidor e com os seus dados.'), ('Painéis de operação', 'Os números do dia numa tela só, para decidir sem planilha.'), ('Apps internos', 'Ferramentas sob medida para a rotina da equipe, com suporte com nome e telefone.')],
   prod=[('Dublê', 'clone de voz e vídeo com o seu próprio material'), ('Central de Comando', 'pedidos por voz que viram tarefas para a equipe'), ('VEKTOR', 'assistente de voz dentro da página')],
   como=['Conversa de 30 minutos com o seu fluxo na tela', 'Piloto curto, com relatório semanal', 'Entrega com código, dados e acessos no seu nome', 'Suporte com responsável definido'],
   msg='Olá! Quero conversar com a Al Kántara Labs sobre automação.'),
 'studio': dict(n='Barzakh', full='Barzakh · um estúdio Al Kántara', num='02', cor='#E8461E', area='Marca, design e vendas', verbo='Damos forma e voz.', pedra='a pedra do topo',
   lead='Identidade, site, conteúdo e comercial para negócios locais que querem cobrar o preço que valem. Sua marca no nível do preço que você quer cobrar.',
   para='Donas e donos de clínica, loja, escritório e restaurante que já entregam bem e ainda parecem pequenos.',
   faz=[('Identidade visual', 'Símbolo, cor, letra e manual: um sistema, não um logo solto.'), ('Sites e mini sites', 'Rápidos no celular, com WhatsApp a um toque.'), ('Social media', 'Linha editorial, artes e Reels na mesma identidade.'), ('Comercial', 'Abordagem, proposta e SDR para transformar conversa em cliente.')],
   prod=[('Limiar · Travessia · Horizonte', 'pacotes de identidade, site e conteúdo'), ('Apps SDR', 'prospecção com a mensagem pronta no WhatsApp')],
   como=['Diagnóstico da marca e da persona', 'Pesquisa premium de referências no mundo todo', 'Sistema visual e aplicações', 'Lançamento e acompanhamento'],
   msg='Olá! Quero conversar com a Barzakh sobre a minha marca.'),
 'media': dict(n='Media', num='03', cor='#F0A202', area='Canais e audiência', verbo='Levamos longe.', pedra='a pedra do meio',
   lead='Canais próprios em nichos claros, com audiência real e medida. Para anunciantes que querem falar com quem importa, sem número inflado.',
   para='Marcas e anunciantes de nicho que querem audiência qualificada em vez de alcance vazio.',
   faz=[('Canais próprios', 'Produção contínua no YouTube e nas redes, com identidade e roteiro.'), ('Formatos para marca', 'Integração editorial que respeita o canal e o público.'), ('Distribuição', 'Cortes, Shorts e Reels que levam cada conteúdo mais longe.'), ('Relatório honesto', 'Só número real, direto da plataforma.')],
   prod=[('Passaporte da Bíblia', 'histórias bíblicas com gravuras clássicas'), ('Raposa e Leão', 'poder e estratégia a partir dos clássicos')],
   como=['Escolha do nicho e da promessa editorial', 'Identidade e formato do canal', 'Produção e publicação em ritmo fixo', 'Medição e ajuste mensal'],
   msg='Olá! Quero conversar com a Al Kántara Media sobre anunciar nos canais.'),
 'ventures': dict(n='Ventures', num='04', cor='#0E8C66', area='Negócios próprios', verbo='Provamos na prática.', pedra='a pedra da base',
   lead='Negócios que o grupo cria e opera, usando a tecnologia da Labs, a marca da Barzakh e a audiência da Media. O que vendemos, usamos primeiro.',
   para='Parceiros, sócios operadores e investidores que querem negócios com estrutura desde o primeiro dia.',
   faz=[('Criar', 'Tese, marca e operação mínima para testar no mercado real.'), ('Operar', 'Processos, pessoas e números acompanhados de perto.'), ('Escalar', 'Tecnologia e canal próprios para crescer sem depender de terceiros.'), ('Endossar', 'Cada empresa mantém a própria marca, com o endosso do grupo.')],
   prod=[('Orégano Turbo', 'operação de pizzaria com tecnologia própria'), ('Estado Próprio', 'marca própria em construção')],
   como=['Tese escrita e validada', 'Operação piloto com números reais', 'Estrutura de governança', 'Decisão de escalar ou parar'],
   msg='Olá! Quero conversar com a Al Kántara Ventures sobre parceria.'),
}
CASES = [
 ('labs', 'Dublê', 'App de clonagem de voz e vídeo, rodando no servidor do próprio dono, com interface no padrão premium do grupo.', 'App interno · IA', ''),
 ('labs', 'Central de Comando', 'Sistema único onde os pedidos chegam por voz e são distribuídos entre as equipes, com fila e resultado.', 'Sistema · IA', ''),
 ('studio', 'Clínica Dra. Jaci Cunha', 'Site institucional de odontologia dentro das regras do conselho, pensado para quem chega pelo Instagram.', 'Site · Saúde', 'https://drajacicunha.pages.dev'),
 ('studio', 'Tribuna 98', 'Mini site da emissora com acesso direto ao conteúdo e ao contato.', 'Mini site · Mídia', 'https://tribuna98.pages.dev'),
 ('studio', 'Rafael Imports', 'Mini site de catálogo com pedido pelo WhatsApp a um toque.', 'Mini site · Varejo', 'https://rafaelimports.pages.dev'),
 ('studio', 'Desentupidora SF', 'Site de serviço urgente: telefone e WhatsApp visíveis sem rolar a tela.', 'Site · Serviços', 'https://desentupidorasf.pages.dev'),
 ('media', 'Passaporte da Bíblia', 'Canal no YouTube com gravuras clássicas em cor de cinema e roteiro próprio.', 'Canal · YouTube', ''),
 ('media', 'Raposa e Leão', 'Canal sobre poder e estratégia com identidade de retrato em preto e dourado.', 'Canal · YouTube', ''),
 ('ventures', 'Orégano Turbo', 'Operação de pizzaria com site, cardápio e pedidos em sistema próprio do grupo.', 'Negócio próprio · Alimentação', ''),
]
def mv(nome, leg='', cls='', ratio=''):
    st = f' style="aspect-ratio:{ratio}"' if ratio else ''
    return f'<figure class="mv {cls}" data-m="f/{nome}"{st}><div class="ph-in"></div><figcaption class="mono">{leg}<span>{nome}</span></figcaption></figure>'
def ph(nome, ratio='16/9', leg='', cls=''):
    return f'<figure class="ph {cls}" data-img="f/{nome}" style="aspect-ratio:{ratio}"><div class="ph-in"></div><figcaption class="mono">{leg}<span>{nome}</span></figcaption></figure>'
NAV = [('labs.html', 'Labs'), ('studio.html', 'Barzakh'), ('media.html', 'Media'), ('ventures.html', 'Ventures'), ('cases.html', 'Cases'), ('sobre.html', 'Sobre')]

def page(arq, titulo, desc, corpo, tema='escuro', cor='#B8955A'):
    nav = ''.join(f'<a href="{h}"{" class=on" if h == arq else ""}>{t}</a>' for h, t in NAV)
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title><meta name="description" content="{desc}"><meta property="og:title" content="{titulo}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="https://lindsonalmeida.pages.dev/alkantara/i/og.jpg"><meta name="theme-color" content="#0B0C0E">
<link rel="icon" href="i/simbolo-latao.svg"><link rel="stylesheet" href="estilo.css"></head>
<body class="{tema}" style="--div:{cor}"><div class="pre" aria-hidden="true">{simb(CORES, "pre-k")}</div><div class="cur" aria-hidden="true"></div><div class="grao" aria-hidden="true"></div>
<header class="topo"><a class="marca" href="index.html" aria-label="Al Kántara Group, início"><img src="i/horizontal-negativo.svg" alt="Al Kántara Group"></a>
<nav class="menu" id="menu">{nav}</nav><a class="pilula" href="contato.html">Conversar</a>
<button class="abre" aria-label="Abrir menu" onclick="document.body.classList.toggle('aberto')"><i></i><i></i></button></header>
<main>{corpo}</main>
<footer class="rodape"><div class="rod-g"><div><p class="mono">AL KÁNTARA GROUP · SÃO LUÍS, MA</p><p class="serif-m">Estrutura para o que vem.</p></div>
<div class="rod-l"><a href="labs.html">Labs</a><a href="studio.html">Barzakh</a><a href="media.html">Media</a><a href="ventures.html">Ventures</a></div>
<div class="rod-l"><a href="cases.html">Cases</a><a href="sobre.html">Sobre</a><a href="contato.html">Contato</a><a href="{WA}{quote('Olá! Vim pelo site da Al Kántara.')}" target="_blank" rel="noopener">WhatsApp</a></div></div>
<div class="gigante" aria-hidden="true">Al Kántara</div><p class="mono pe">© 2026 Al Kántara Group · Quatro pedras, uma chave.</p></footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script><script src="movimento.js" defer></script><script type="module" src="k3d.js"></script></body></html>'''
    open(os.path.join(D, arq), 'w').write(html)

def cartoes_div():
    return ''.join(f'''<a class="div-card rv" href="{k}.html" style="--c:{v['cor']}"><span class="mono">{v['num']} · {v['area']}</span>
{simb(tuple(v['cor'] if i == list(DIV).index(k) else 'rgba(239,234,225,.12)' for i in range(4)), 'mini')}
<h3>{v['n']}</h3><p>{v['verbo']}</p><span class="seta">Ver divisão →</span></a>''' for k, v in DIV.items())

def case_cards(filtro=None, n=None):
    cs = [c for c in CASES if not filtro or c[0] == filtro][:n]
    out = ''
    for k, nome, txt, tag, link in cs:
        v = DIV[k]; a = f'<a class="ver" href="{link}" target="_blank" rel="noopener">Ver no ar ↗</a>' if link else '<span class="ver apag">Uso interno</span>'
        out += f'''<article class="case rv" style="--c:{v['cor']}"><div class="case-capa" data-img="f/case-{'barzakh' if k=='studio' else k}.jpg">{simb(tuple(v['cor'] if i == list(DIV).index(k) else 'rgba(239,234,225,.08)' for i in range(4)), 'cc')}<span class="mono">{v.get('full','Al Kántara '+v['n'])}</span></div>
<span class="mono tag">{tag}</span><h3>{nome}</h3><p>{txt}</p>{a}</article>'''
    return out

# ---------- home
home = f'''
<section class="hero"><video class="hero-vid" data-vid="f/abertura.mp4" data-alt="f/hero-pedra.mp4" muted loop playsinline aria-hidden="true"></video><canvas id="k3d" aria-hidden="true"></canvas><div class="hero-simb" aria-hidden="true">{simb(('#1A1C20', '#1A1C20', '#B8955A', '#1A1C20'), 'gsimb')}</div>
<div class="hero-t"><p class="mono rv">GRUPO DE TECNOLOGIA · SÃO LUÍS, MARANHÃO</p>
<h1 class="h-xl"><span class="lin">Estrutura para</span><span class="lin it">o que vem.</span></h1>
<p class="lead rv">Construímos a tecnologia, a marca e a audiência de negócios que querem ir longe, a partir do Maranhão.</p>
<div class="acoes rv"><a class="btn" href="contato.html">Conversar com o grupo</a><a class="btn b2" href="#divisoes">Conhecer as divisões</a></div></div>
<div class="faixa-div" aria-hidden="true"><span style="background:#2E4BFF"></span><span style="background:#E8461E"></span><span style="background:#F0A202"></span><span style="background:#0E8C66"></span></div></section>

<section class="foto-slz" aria-label="Centro histórico de São Luís"><div class="foto-in" style="background-image:url(i/slz.jpg)"></div><p class="mono cred">São Luís, Maranhão · foto: Prburley / Aristeas, CC BY 4.0</p></section>
<section class="manif claro"><p class="mono">MANIFESTO</p><p class="acende" data-acende>Uma ponte não é decoração. É cálculo, peso e paciência. No topo de todo arco existe uma pedra que segura as outras. Ela não aparece mais que as outras. Ela só não falha. Somos essa pedra.</p></section>


<section class="vida" aria-label="Vida"><div class="vida-cab"><p class="mono">VIDA</p><h2 class="h-l">Tecnologia é<br><em>gente fazendo.</em></h2><p class="lead">Por trás de cada pedra existe alguém: quem decide, quem cria, quem conta, quem serve.</p></div>
<div class="vida-trilho">{mv('vida-maos.mp4','Labs · quem decide','vc')}{mv('vida-criacao.jpg','Barzakh · quem cria','vc vt')}{mv('vida-estudio.mp4','Media · quem conta','vc')}{mv('vida-mesa.jpg','Ventures · quem serve','vc vt')}{mv('vida-reuniao.jpg','O grupo · quem constrói junto','vc')}</div></section>
<section class="tec">{mv('tec-nucleo.mp4','','fundo')}<div class="tec-t"><p class="mono">ALTA TECNOLOGIA</p><h2 class="h-xl">Quatro facetas,<br><em>um núcleo.</em></h2><p class="lead">IA, marca, audiência e operação girando em torno do mesmo centro: o seu negócio.</p></div></section>
<section class="tec2">{mv('tec-servidor.jpg','Infraestrutura','', '16/9')}{mv('tec-holograma.mp4','Dados que viram decisão','', '16/9')}</section>
<section class="sec" id="divisoes"><div class="cab"><p class="mono">01 · ARQUITETURA</p><h2 class="h-l">Quatro pedras,<br><em>uma chave.</em></h2>
<p class="lead">Cada divisão se sustenta sozinha e sustenta o grupo. Juntas, constroem, dão forma, levam longe e provam na prática.</p></div>
<div class="grid-div">{cartoes_div()}</div></section>

<section class="marquee" aria-hidden="true"><div class="trilho"><span>Construir</span><i>◆</i><span>Operar</span><i>◆</i><span>Distribuir</span><i>◆</i><span>Escalar</span><i>◆</i><span>Construir</span><i>◆</i><span>Operar</span><i>◆</i><span>Distribuir</span><i>◆</i><span>Escalar</span><i>◆</i></div></section>

<section class="sec"><div class="cab"><p class="mono">02 · TRABALHO</p><h2 class="h-l">Prova aplicada,<br><em>não promessa.</em></h2></div>
<div class="grid-case">{case_cards(n=6)}</div><a class="link-g" href="cases.html">Todos os cases →</a></section>


<section class="materia">{mv('materia-latao.mp4','Latão','m1')}<div class="m-t"><p class="mono">MATÉRIA</p><h2 class="h-l">Feito para<br><em>durar.</em></h2><p class="lead">Pedra, metal e luz. O que construímos é pensado para atravessar o tempo, não a temporada.</p></div>{mv('materia-pedra.jpg','Basalto','m2','21/9')}</section>
<section class="sec claro"><div class="cab"><p class="mono">03 · COMO TRABALHAMOS</p><h2 class="h-l">Um preço, um prazo,<br><em>um responsável.</em></h2></div>
<div class="valores">{''.join(f'<div class="val rv"><span class="mono">0{i+1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate([('Rigor', 'Medimos antes de prometer. Entregamos o que foi combinado, do jeito que foi combinado.'), ('Clareza', 'Português simples. Proposta com escopo, prazo e responsável por escrito.'), ('Peso próprio', 'Cada divisão se sustenta sozinha. Nenhuma pedra é enfeite.'), ('Longo prazo', 'Código, marca e dados ficam no seu nome. Construímos para durar.')]))}</div></section>

<section class="final final-v">{mv("final-horizonte.mp4","","fundo")}<p class="mono">PRÓXIMO PASSO</p><h2 class="h-xl">Vamos medir<br><em>antes de prometer.</em></h2>
<p class="lead">Uma conversa de 30 minutos para entender o seu caso e dizer, com franqueza, se e como podemos ajudar.</p>
<div class="acoes"><a class="btn" href="{WA}{quote('Olá! Quero conversar com a Al Kántara.')}" target="_blank" rel="noopener">Chamar no WhatsApp</a><a class="btn b2" href="contato.html">Outros contatos</a></div></section>'''
page('index.html', 'Al Kántara Group', 'Grupo de tecnologia de São Luís (MA): Labs, Barzakh, Media e Ventures. Estrutura para o que vem.', home)

# ---------- divisões
for k, v in DIV.items():
    i = list(DIV).index(k)
    outras = ''.join(f'<a href="{kk}.html" style="--c:{vv["cor"]}"><span class="mono">{vv["num"]}</span>{vv["n"]}</a>' for kk, vv in DIV.items() if kk != k)
    corpo = f'''
<section class="hero hero-div"><div class="hero-simb" aria-hidden="true">{simb(tuple(v['cor'] if j == i else '#1A1C20' for j in range(4)), 'gsimb')}</div>
<div class="hero-t"><p class="mono rv"><b class="pt"></b>DIVISÃO {v['num']} · {v['area'].upper()}</p>
<h1 class="h-xl">{'<span class="lin it cor">Barzakh</span><span class="lin mono" style="font-size:max(12px,.13em);letter-spacing:.24em;margin-top:1.2em;line-height:1.4">um estúdio Al Kántara</span>' if k=='studio' else f'<span class="lin">Al Kántara</span><span class="lin it cor">{v["n"]}</span>'}</h1>
<p class="lead rv">{v['lead']}</p>
<div class="acoes rv"><a class="btn" href="{WA}{quote(v['msg'])}" target="_blank" rel="noopener">Conversar sobre {v['n']}</a><a class="btn b2" href="#faz">O que fazemos</a></div></div></section>

<section class="banda">{ph('div-' + ('barzakh' if k=='studio' else k) + '.jpg', '21/9', v.get('full','Al Kántara '+v['n']), 'par')}</section>
<section class="manif claro"><p class="mono">{v['pedra'].upper()}</p><p class="acende" data-acende>{v['verbo']} {v['para']}</p></section>

<section class="sec" id="faz"><div class="cab"><p class="mono">O QUE FAZEMOS</p><h2 class="h-l">{v['verbo'].replace('.', ',')}<br><em>com escopo por escrito.</em></h2></div>
<div class="bento">{''.join(f'<div class="b rv{" b-g" if j == 0 else ""}"><span class="mono">0{j+1}</span><h3>{a}</h3><p>{b}</p></div>' for j, (a, b) in enumerate(v['faz']))}</div></section>

<section class="sec claro"><div class="cab"><p class="mono">MARCAS E PRODUTOS</p><h2 class="h-l">Nome próprio,<br><em>endosso do grupo.</em></h2></div>
<ul class="lista-g">{''.join(f'<li class="rv"><span class="nm">{a}</span><span class="ds">{b}</span><span class="mono">por {v.get("full","Al Kántara "+v["n"])}</span></li>' for a, b in v['prod'])}</ul></section>

<section class="sec"><div class="cab"><p class="mono">COMO FUNCIONA</p><h2 class="h-l">Quatro passos,<br><em>sem atalho.</em></h2></div>
<ol class="passos">{''.join(f'<li class="rv"><span class="n">{j+1}</span><p>{t}</p></li>' for j, t in enumerate(v['como']))}</ol></section>

<section class="sec"><div class="cab"><p class="mono">CASES</p><h2 class="h-l">Trabalho<br><em>aplicado.</em></h2></div><div class="grid-case">{case_cards(k)}</div></section>

<section class="final"><p class="mono">{v.get('full','Al Kántara '+v['n']).upper()}</p><h2 class="h-xl">Vamos<br><em>conversar.</em></h2>
<div class="acoes"><a class="btn" href="{WA}{quote(v['msg'])}" target="_blank" rel="noopener">Chamar no WhatsApp</a></div>
<nav class="outras">{outras}</nav></section>'''
    page(f'{k}.html', v.get('full', f'Al Kántara {v["n"]}'), f'{v.get("full", "Al Kántara "+v["n"])}: {v["area"]}. {v["verbo"]}', corpo, cor=v['cor'])

# ---------- cases
filtros = '<button class="on" data-f="">Todos</button>' + ''.join(f'<button data-f="{k}" style="--c:{v["cor"]}">{v["n"]}</button>' for k, v in DIV.items())
cs = case_cards().replace('<article class="case rv"', '<article class="case rv" data-d="X"')
partes = cs.split('data-d="X"'); cs = partes[0] + ''.join(f'data-d="{CASES[j][0]}"' + partes[j + 1] for j in range(len(CASES)))
page('cases.html', 'Cases · Al Kántara Group', 'Trabalho aplicado das quatro divisões da Al Kántara.', f'''
<section class="hero hero-p"><div class="hero-t"><p class="mono">CASES</p><h1 class="h-xl"><span class="lin">Prova aplicada,</span><span class="lin it">não promessa.</span></h1>
<p class="lead">Projetos no ar e produtos em uso. Sem número inflado: quando houver resultado medido e autorizado, ele entra aqui com a fonte.</p></div></section>
<section class="sec"><div class="filtros">{filtros}</div><div class="grid-case" id="cases">{cs}</div></section>''')

# ---------- sobre
page('sobre.html', 'Sobre · Al Kántara Group', 'O grupo, o nome, o propósito e os valores da Al Kántara.', f'''
<section class="hero hero-p"><div class="hero-simb" aria-hidden="true">{simb(('#B8955A', '#1A1C20', '#1A1C20', '#1A1C20'), 'gsimb')}</div><div class="hero-t"><p class="mono">SOBRE O GRUPO</p><h1 class="h-xl"><span class="lin">Al-qantara,</span><span class="lin it">o arco.</span></h1>
<p class="lead">Em árabe, al-qantara é a ponte de pedra, o arco. No topo de todo arco existe uma pedra-chave que segura as outras. As juntas entre as nossas quatro pedras desenham um K.</p></div></section>
<section class="banda">{ph('materia-arco-slz.jpg', '21/9', 'Al-qantara, o arco', 'par')}</section>
<section class="sec claro duas"><div><p class="mono">PROPÓSITO</p><h2 class="h-m">Dar estrutura ao que vem.</h2></div><p class="lead">Tecnologia, marca e audiência para negócios que querem ir longe a partir do Maranhão. Nossa missão é criar, operar e escalar produtos digitais, marcas e canais com rigor de engenharia e sensibilidade de design.</p></section>
<section class="sec duas"><div><p class="mono">VISÃO</p><h2 class="h-m">Referência de rigor no Norte e no Nordeste.</h2></div><p class="lead">Ser o grupo de tecnologia que a região usa como referência de rigor, e que o resto do país reconhece.</p></section>
<section class="sec"><div class="cab"><p class="mono">POSICIONAMENTO</p><h2 class="h-l">Construir, operar e distribuir<br><em>no mesmo lugar.</em></h2>
<p class="lead">Software, marca, audiência e negócio próprio sob uma estrutura só, para empresas da região que querem crescer num tempo em que a tecnologia ficou barata e a execução ficou rara.</p></div>
<div class="arvore">{''.join(f'<div class="ramo rv" style="--c:{v["cor"]}"><span class="mono">{v["num"]} · {v["area"]}</span><h3>{v["n"]}</h3><p>{" · ".join(p[0] for p in v["prod"])}</p></div>' for v in DIV.values())}</div></section>
<section class="sec claro"><div class="cab"><p class="mono">FUNDADOR</p><h2 class="h-l">Lindson Almeida</h2><p class="lead">Designer, especialista em web design, social media e vendas, em São Luís. Fundou o grupo para juntar sob uma marca só o que já construía separado: software, estúdio, canais e negócios próprios.</p></div></section>''')

# ---------- contato
page('contato.html', 'Contato · Al Kántara Group', 'Fale com a Al Kántara: WhatsApp e São Luís, MA.', f'''
<section class="hero hero-p"><div class="hero-t"><p class="mono">CONTATO</p><h1 class="h-xl"><span class="lin">Uma conversa,</span><span class="lin it">30 minutos.</span></h1>
<p class="lead">Conte o que você quer construir. Respondemos com franqueza se e como podemos ajudar, e com qual divisão.</p></div></section>
<section class="banda">{ph('contato-mesa.jpg', '21/9', 'Uma conversa', 'par')}</section>
<section class="sec"><div class="contato">
<form class="form" id="form" onsubmit="return enviar(event)"><label>Seu nome<input name="nome" required autocomplete="name"></label>
<label>Empresa<input name="empresa" autocomplete="organization"></label>
<label>Assunto<select name="div"><option>Labs · IA e software</option><option>Barzakh · Marca, design e vendas</option><option>Media · Anunciar nos canais</option><option>Ventures · Parceria e investimento</option><option>Outro assunto</option></select></label>
<label>Em poucas palavras<textarea name="msg" rows="4" required></textarea></label>
<button class="btn" type="submit">Enviar pelo WhatsApp</button><p class="mono pe">Abre o WhatsApp com a mensagem pronta. Nada é guardado neste site.</p></form>
<div class="dados"><div><p class="mono">WHATSAPP</p><a class="h-m" href="{WA}{quote('Olá! Vim pelo site da Al Kántara.')}" target="_blank" rel="noopener">(98) 98562-1808</a></div>
<div><p class="mono">ONDE</p><p class="h-m">São Luís, Maranhão</p></div><div><p class="mono">REDES</p><a class="h-m" href="https://alkantaragroup.pages.dev" target="_blank" rel="noopener">@alkantaragroup</a><p class="mono" style="margin-top:10px">Instagram · TikTok · YouTube</p></div></div></div></section>
<script>function enviar(e){{e.preventDefault();const f=new FormData(e.target);const t=`Olá! Sou ${{f.get('nome')}}${{f.get('empresa')?' ('+f.get('empresa')+')':''}}. Assunto: ${{f.get('div')}}. ${{f.get('msg')}}`;window.open('{WA}'+encodeURIComponent(t),'_blank');return false}}</script>''')
print('site ok')
