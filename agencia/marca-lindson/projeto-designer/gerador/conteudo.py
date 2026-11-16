# -*- coding: utf-8 -*-
# Textos do Projeto Designer (conta Leandro, 16/11/2026). Troque STUDIO/HANDLE e rode gerar.py de novo.
STUDIO = "Lindson Almeida Studio"
HANDLE = "lindsonalmeidastudio"
SITE = "https://lindsonalmeida.pages.dev/site/portfolio/"
LANDING = "https://lindsonalmeida.pages.dev/site/identidade/"
WA = "https://wa.me/5598985621808?text=" + "Oi%2C%20Lindson!%20Quero%20um%20or%C3%A7amento%20de%20identidade%20visual."

NOMES = [
    ("Lindson Almeida Studio", "@lindsonalmeidastudio",
     "RECOMENDADO. Usa a autoridade que já existe (Instagram @lindsonalmeida_, site lindsonalmeida.pages.dev, brand book da marca). Quem compra identidade visual em São Luís compra de uma pessoa em quem confia: o nome dele na frente passa isso. 'Studio' diz que é serviço de design, não perfil pessoal. Funciona igual no Behance, Pinterest e LinkedIn."),
    ("Âmbar Estúdio de Marca", "@ambar.estudio",
     "Vem da luz âmbar da marca do Lindson (preto + #F5C518). Nome curto, premium, fácil de falar. Contra: começa do zero em autoridade e 'âmbar' é palavra comum, chance maior de o @ estar ocupado."),
    ("Forja Branding", "@forja.branding",
     "Ideia de construir marca forte, ligada ao universo 'Estado Próprio' (pedra, fortaleza). Soa de estúdio grande. Contra: separa o estúdio do rosto do Lindson, que é o que mais vende hoje."),
]

PERSONA = """1. Quem: dono(a) de negócio local de São Luís/MA e interior (clínica, loja, restaurante, escritório, profissional liberal, criador de curso), 28 a 50 anos, fatura com o boca a boca e já tem Instagram.
2. Rotina: atende o dia inteiro, posta quando dá, faz arte no Canva ou com sobrinho; decide pelo celular, à noite, pelo WhatsApp.
3. Dor: a marca parece amadora perto do concorrente, cada post sai de um jeito, tem vergonha de mandar o perfil para cliente maior; quer cobrar mais e não consegue.
4. Valoriza: ver trabalho real de gente da região, processo claro, prazo cumprido, alguém que entende de venda, não só de 'desenho'.
5. Confia quando: vê cases completos (antes e depois, aplicações reais), fala com o próprio designer no WhatsApp e recebe proposta organizada. Está no Instagram, Google e WhatsApp; empresas maiores e online olham Behance e LinkedIn.
Teste: essa pessoa compraria disso? Sim, se a peça mostrar o case pronto e aplicado, sem jargão e com caminho direto para o WhatsApp."""

# ---------- BEHANCE ----------
BEHANCE_PERFIL = {
    "Nome de exibição": STUDIO,
    "Usuário (URL)": "behance.net/" + HANDLE,
    "Ocupação / título": "Identidade visual, brand book e web design",
    "Local": "São Luís, MA, Brasil",
    "Bio (Sobre)": "Estúdio de marca do designer Lindson Almeida, em São Luís (MA). Crio identidades visuais completas para negócios que querem parecer do tamanho que já são: logo, paleta, tipografia, brand book e aplicações, do papel ao Instagram e ao site. Cada projeto começa pela persona de quem compra e termina com a marca aplicada no mundo real. Atendo todo o Brasil, online.",
    "Serviços (Hire me)": "Identidade visual · Brand book · Rebranding · Social kit para Instagram · Site e landing page · Direção de arte",
    "Ferramentas": "Figma, Adobe Illustrator, Adobe Photoshop, Claude, HTML/CSS",
    "Links": "Site: " + SITE + " · Instagram: instagram.com/lindsonalmeida_ · WhatsApp: wa.me/5598985621808",
}

CASES = [
    dict(id="leo-pinto", bb="leo", paginas=[6, 3, 7, 8, 10, 11, 12, 9], capa=6,
         titulo="Leo Pinto · Identidade visual 'Do povo para o povo'",
         cliente="Comunicação pública · São João Batista (MA)",
         desafio="A comunicação usava raios, faixas, ícones e fumaça em cada peça; nada se repetia e a marca não era lembrada.",
         conceito="Tirar tudo o que sobrava: só fontes, logo e cores. O sol nascendo no 'O' do LEO vira a assinatura, sustentada por azul e laranja com proporção definida.",
         entregas="Logo e versões, monograma, área de proteção, usos incorretos, paleta com proporção, tipografia, regra de elementos e manual de 17 páginas.",
         tags="identidade visual, branding, brand book, manual de marca, logo, azul e laranja, maranhão, design brasileiro"),
    dict(id="real-time", bb="realtime", paginas=[1, 3, 5, 6, 7, 10, 11, 15], capa=6,
         titulo="Real Time · Rebranding de produtora audiovisual",
         cliente="Produtora e locação de equipamento audiovisual · São Luís (MA)",
         desafio="Uma produtora com equipamento de cinema e uma marca que não mostrava isso.",
         conceito="'No ar, agora.' O símbolo vira um visor de câmera [rt], com wordmark limpo, preto e azul elétrico, e a linguagem do timecode nas aplicações.",
         entregas="Símbolo visor, wordmark, versões, paleta, tipografia, fotografia, tom de voz, aplicações e brand book de 17 páginas.",
         tags="rebranding, identidade visual, produtora audiovisual, logo, brand book, audiovisual, branding brasil"),
    dict(id="processo-legislativo", bb="curso", paginas=[1, 3, 5, 6, 7, 10, 11, 15], capa=6,
         titulo="Processo Legislativo · Identidade para curso de câmaras",
         cliente="Curso para servidores e vereadores de câmaras municipais",
         desafio="Conteúdo técnico e sério com cara de improviso nas redes.",
         conceito="'Chega de improviso na câmara.' Verde institucional e dourado, serifa elegante e um símbolo que lembra o plenário: sério sem ser frio.",
         entregas="Logo, versões, paleta, tipografia, elementos, fotografia, perfil do Instagram com antes e depois, mini site e brand book.",
         tags="identidade visual, educação, curso online, verde e dourado, brand book, rebranding, logo"),
    dict(id="wf-celulares", bb="wf", paginas=[1, 3, 5, 6, 7, 10, 13, 15], capa=6,
         titulo="WF Celulares · Identidade de loja de iPhone",
         cliente="Loja de iPhone · São Luís (MA)",
         desafio="Loja de produto premium vendendo com visual de promoção de bairro.",
         conceito="'Procedência que dá para ver.' Preto, prata e branco, muito respiro e fotografia de produto no centro, como as marcas que ele vende.",
         entregas="Logo e versões, paleta, tipografia, fotografia, aplicações, painel fixado do Instagram, mini site e brand book.",
         tags="identidade visual, loja de celular, iphone, branding minimalista, preto e prata, brand book, logo"),
    dict(id="oregano-turbo", bb="oregano", paginas=[1, 3, 5, 6, 7, 10, 12, 15], capa=6,
         titulo="Orégano Turbo · Marca de marketing para pizzarias",
         cliente="Marketing para pizzarias",
         desafio="Falar com dono de pizzaria com seriedade, sem cair no selo lúdico de pizza.",
         conceito="'Uma folha que sobe.' A folha de orégano vira símbolo de crescimento; verde, tomate e creme, comanda como elemento e a pizza real como protagonista.",
         entregas="Logo e versões, paleta, tipografia, elementos (comanda), fotografia, aplicações, criativos de anúncio e brand book.",
         tags="identidade visual, pizzaria, food branding, marketing gastronômico, brand book, logo, verde e vermelho"),
    dict(id="duble", bb="duble", paginas=[1, 3, 5, 6, 7, 10, 11, 15], capa=6,
         titulo="Dublê · Identidade de app de voz",
         cliente="Aplicativo (produto próprio do estúdio)",
         desafio="Um app de tecnologia sensível (voz) que precisava parecer confiável e simples.",
         conceito="'Só grava quem disse sim.' Grafite e violeta, símbolo de onda sonora dentro de um círculo e linguagem direta sobre consentimento.",
         entregas="Nome, símbolo, wordmark, versões, paleta, tipografia, interface, tom de voz e brand book.",
         tags="identidade visual, app, ui design, tecnologia, violeta, brand book, logo, startup"),
]
for c in CASES:
    c["descricao"] = (f"{c['cliente']}.\n\nDesafio: {c['desafio']}\n\nConceito: {c['conceito']}\n\n"
                      f"Entregas: {c['entregas']}\n\nDesign: {STUDIO} (São Luís, MA). Orçamento de identidade visual pelo WhatsApp: wa.me/5598985621808")
    c["ferramentas"] = "Figma, Adobe Illustrator, Adobe Photoshop, Claude"

# ---------- PINTEREST ----------
PIN_PERFIL = {
    "Nome": STUDIO + " | Identidade Visual",
    "Usuário": "@" + HANDLE,
    "Bio (até 500)": "Identidade visual, brand book e web design para negócios do Brasil. Designer em São Luís (MA). Cases completos: logo, paleta, tipografia e aplicações. Orçamento pelo WhatsApp.",
    "Site (verificar)": "https://lindsonalmeida.pages.dev",
    "Tipo de conta": "Empresa (Pinterest Business), categoria Design gráfico / Serviços criativos",
}
PASTAS = [
    ("Identidade Visual · Cases Completos", "Projetos de identidade visual completos: logo, paleta de cores, tipografia e aplicações reais. Inspiração de branding para negócios locais e marcas brasileiras."),
    ("Brand Book e Manual de Marca", "Páginas de brand book e manual de identidade visual: essência, persona, uso do logo, cores com proporção, tipografia e tom de voz."),
    ("Paleta de Cores para Marcas", "Paletas de cores de marcas reais com proporção de uso: azul e laranja, verde e dourado, preto e prata, grafite e violeta."),
    ("Logo e Versões de Logo", "Logos, monogramas, versões horizontais e reduzidas, área de proteção e usos incorretos. Referência de logo profissional."),
    ("Instagram com Identidade Visual", "Feeds, destaques e posts de Instagram dentro da identidade visual da marca. Perfil que parece do tamanho do negócio."),
    ("Sites e Landing Pages", "Mini sites, landing pages e sites de bio na identidade visual do cliente. Web design premium para pequenos negócios."),
]

# ---------- LINKEDIN ----------
LINKEDIN = {
    "Título (headline)": "Designer de identidade visual e web design | Fundador do " + STUDIO + " | Brand book, rebranding e sites para negócios que querem parecer do tamanho que são",
    "Sobre": ("Eu ajudo negócios a terem uma marca que passa confiança antes da primeira conversa.\n\n"
              "Sou o Lindson Almeida, designer em São Luís (MA). No " + STUDIO + " eu crio identidade visual completa: logo, paleta, tipografia, brand book de 17 páginas e as aplicações que o cliente usa todo dia (Instagram, site, materiais).\n\n"
              "Como eu trabalho:\n1. Persona: quem compra do seu negócio e o que faz essa pessoa confiar.\n2. Pesquisa premium: referências de estúdios do mundo inteiro antes de desenhar.\n3. Conceito e logo.\n4. Sistema: cores com proporção, letras, fotografia e tom de voz.\n5. Aplicações e brand book para você e sua equipe usarem sem depender de mim.\n\n"
              "Alguns projetos: Real Time (produtora audiovisual), WF Celulares (loja de iPhone), Processo Legislativo (curso para câmaras), Orégano Turbo (marketing para pizzarias), Leo Pinto (comunicação pública) e Dublê (app).\n\n"
              "Orçamento de identidade visual e site pelo WhatsApp: wa.me/5598985621808\nPortfólio: " + SITE),
    "Experiência": ("Cargo: Fundador e designer de marca\nEmpresa: " + STUDIO + " (crie a página do estúdio e vincule)\nTipo: Autônomo · Local: São Luís, MA (híbrido)\nInício: mês/ano em que começou [preencher]\n"
                     "Descrição: Identidade visual, rebranding, brand book, social kit e sites para negócios locais e online. Projetos para produtora audiovisual, loja de iPhone, curso para câmaras municipais, marketing de pizzarias, comunicação pública e app de tecnologia. Processo com persona, pesquisa de referências internacionais, sistema visual e aplicação no Instagram e no site.\n"
                     "Competências: Identidade visual · Branding · Brand book · Web design · Direção de arte · Design para redes sociais"),
    "Serviços em destaque": "Design de logotipo · Identidade visual (branding) · Design gráfico · Web design · Design para redes sociais · Direção de arte",
    "Página do estúdio (nome)": STUDIO,
    "Página do estúdio (slogan)": "Identidade visual e web design. São Luís (MA) para o Brasil.",
    "Página do estúdio (sobre)": STUDIO + " cria identidades visuais completas, brand books e sites para negócios que querem parecer do tamanho que já são. Processo com persona, pesquisa premium e marca aplicada no mundo real. Orçamento pelo WhatsApp.",
}

POSTS = [
    dict(id="01-real-time", case="realtime", pgs=[1, 5, 6, 10, 15], capa="REBRANDING\nREAL TIME", sub="Produtora audiovisual · São Luís",
         texto="Uma produtora com equipamento de cinema e uma marca que não mostrava isso.\n\nNo rebranding da Real Time, o símbolo virou um visor de câmera [rt] e a frase da marca ficou 'No ar, agora.'\n\nO que entrou:\n· símbolo e wordmark\n· paleta com proporção\n· tipografia e fotografia\n· brand book de 17 páginas\n\nArrasta o carrossel para ver o antes e depois.\n\nQuer uma identidade assim para o seu negócio? Me chama no WhatsApp: wa.me/5598985621808\n\n#identidadevisual #branding #rebranding #design #saoluis"),
    dict(id="02-wf", case="wf", pgs=[1, 5, 6, 10, 15], capa="WF\nCELULARES", sub="Loja de iPhone · identidade",
         texto="Produto premium pede marca premium.\n\nA WF Celulares vende iPhone e vendia com visual de promoção. A nova identidade usa preto, prata e branco, muito respiro e a foto do produto no centro.\n\nConceito: 'Procedência que dá para ver.'\n\nO carrossel mostra logo, cores e aplicações.\n\nOrçamento de identidade visual: wa.me/5598985621808\n\n#identidadevisual #branding #designminimalista #lojadecelular #brandbook"),
    dict(id="03-curso", case="curso", pgs=[1, 5, 6, 10, 15], capa="CHEGA DE\nIMPROVISO", sub="Processo Legislativo · rebranding",
         texto="Conteúdo sério com cara de improviso perde aluno.\n\nPara o curso de Processo Legislativo, criei uma identidade verde e dourado, com serifa elegante e um símbolo que lembra o plenário.\n\nEntrou: logo, paleta, tipografia, perfil do Instagram com antes e depois, mini site e brand book.\n\nVeja as telas no carrossel.\n\n#identidadevisual #educacao #cursoonline #branding #design"),
    dict(id="04-oregano", case="oregano", pgs=[1, 6, 10, 12, 15], capa="UMA FOLHA\nQUE SOBE", sub="Orégano Turbo · marca",
         texto="Como falar com dono de pizzaria sem parecer cardápio infantil?\n\nNa Orégano Turbo, a folha de orégano virou símbolo de crescimento. Verde, tomate e creme, a comanda como elemento gráfico e a pizza real como protagonista.\n\nNada de selo lúdico: o dono de pizzaria quer seriedade.\n\nO sistema completo está no carrossel.\n\n#branding #foodbranding #identidadevisual #pizzaria #design"),
    dict(id="05-duble", case="duble", pgs=[6, 3, 7, 10, 15], capa="SÓ GRAVA\nQUEM DISSE SIM", sub="Dublê · identidade de app",
         texto="Marca de tecnologia precisa passar confiança antes de qualquer botão.\n\nO Dublê é um app de voz. A identidade grafite e violeta tem um símbolo de onda dentro de um círculo e uma frase que resume a regra do produto: 'Só grava quem disse sim.'\n\nNome, símbolo, interface e brand book no carrossel.\n\n#uidesign #branding #identidadevisual #app #design"),
    dict(id="06-leo", case="leo", pgs=[6, 7, 10, 11, 9], capa="SÓ FONTES,\nLOGO E CORES", sub="Leo Pinto · identidade",
         texto="Às vezes a melhor decisão de design é tirar.\n\nA comunicação do Leo Pinto tinha raios, faixas, ícones e fumaça em cada peça. A nova identidade ficou só com fontes, logo e cores, com o sol nascendo no 'O' como assinatura.\n\nResultado visual: uma marca que se reconhece de longe.\n\nVeja versões, cores e usos incorretos no carrossel.\n\n#identidadevisual #branding #design #logo #maranhao"),
    dict(id="07-processo", case=None, pgs=[], capa="COMO NASCE\nUMA MARCA", sub="Meu processo em 5 etapas",
         slides=[("01 · PERSONA", "Antes de desenhar, escrevo em 5 linhas quem compra do seu negócio e o que faz essa pessoa confiar."),
                 ("02 · PESQUISA", "Junto pelo menos 8 referências de estúdios premiados de 3 países ou mais e combino as 3 mais fortes."),
                 ("03 · CONCEITO E LOGO", "Uma ideia curta guia tudo. Dela saem o logo e as versões."),
                 ("04 · SISTEMA E BRAND BOOK", "Cores com proporção, letras, fotografia, tom de voz e aplicações reais.")],
         texto="Identidade visual não começa no logo.\n\nMeu processo tem 5 etapas: persona, pesquisa, conceito, sistema e aplicação. É por isso que a marca funciona no Instagram, no site e no papel, do mesmo jeito.\n\nSalve para lembrar quando for contratar um designer.\n\n#branding #identidadevisual #processocriativo #design #designer"),
    dict(id="08-brand-book", case=None, pgs=[], capa="O QUE TEM\nNUM BRAND BOOK", sub="17 páginas, uma marca inteira",
         slides=[("ESSÊNCIA E PERSONA", "O que a marca é e para quem ela fala."),
                 ("LOGO E VERSÕES", "Logo principal, versões, monograma, área de proteção e o que nunca fazer."),
                 ("CORES E LETRAS", "Paleta com proporção de uso e tipografia com função de cada fonte."),
                 ("FOTOGRAFIA, VOZ E APLICAÇÕES", "Como fotografar, como falar e a marca aplicada no mundo.")],
         texto="Logo sozinho não é marca.\n\nO brand book é o manual que faz a sua equipe, o seu social media e a sua gráfica usarem a marca do mesmo jeito. Os meus têm 17 páginas.\n\nVeja o que entra no carrossel.\n\n#brandbook #manualdemarca #identidadevisual #branding #design"),
    dict(id="09-antes-depois", case=None, pgs=[], capa="ANTES X\nDEPOIS", sub="3 rebrandings do estúdio",
         slides=[("REAL TIME", "@bb:realtime:5"), ("PROCESSO LEGISLATIVO", "@bb:curso:5"), ("WF CELULARES", "@bb:wf:5")],
         texto="Antes e depois de 3 identidades do estúdio.\n\nEm todos, a mesma pergunta guiou o trabalho: o cliente certo confiaria nessa marca na primeira olhada?\n\nArrasta para ver.\n\n#rebranding #antesedepois #identidadevisual #branding #design"),
    dict(id="10-pacotes", case=None, pgs=[], capa="IDENTIDADE\nVISUAL", sub="Essencial · Completo · Premium",
         slides=[("ESSENCIAL", "Logo, versões, paleta e tipografia. Para quem está começando."),
                 ("COMPLETO", "Tudo do Essencial + elementos, fotografia, aplicações e guia de marca."),
                 ("PREMIUM", "Identidade completa + brand book de 17 páginas + kit de Instagram ou site."),
                 ("ORÇAMENTO", "Pelo WhatsApp, depois de entender o seu negócio.")],
         texto="Abri a agenda de identidade visual do estúdio.\n\n3 caminhos: Essencial, Completo e Premium. Todos começam pela persona do seu cliente e terminam com a marca aplicada.\n\nO orçamento é feito no WhatsApp, depois de entender o seu negócio: wa.me/5598985621808\n\n#identidadevisual #branding #designer #saoluis #maranhao"),
]

# ---------- OFERTA ----------
PACOTES = [
    dict(nome="Essencial", para="Para quem está começando e precisa de uma marca profissional.",
         itens=["Reunião de briefing e persona", "Pesquisa de referências", "1 conceito de logo + versões (horizontal, vertical, símbolo)", "Paleta de cores e tipografia", "2 rodadas de ajuste", "Arquivos finais (PNG, SVG, PDF)"],
         prazo="até 10 dias úteis após o briefing"),
    dict(nome="Completo", para="Para quem já vende e quer uma marca consistente em tudo.",
         itens=["Tudo do Essencial", "2 caminhos de conceito para escolher", "Elementos gráficos e direção de fotografia", "Tom de voz", "Aplicações: perfil do Instagram, destaques, cartão e assinatura", "Guia de marca em PDF", "3 rodadas de ajuste"],
         prazo="até 20 dias úteis após o briefing"),
    dict(nome="Premium", para="Para quem quer a marca inteira pronta para crescer.",
         itens=["Tudo do Completo", "Brand book de 17 páginas (essência, persona, antes x depois, logo, cores, letras, fotografia, voz e aplicações)", "Social kit: modelos de post, carrossel e Stories", "Mini site ou landing page na identidade (opcional no lugar do social kit)", "Apresentação da marca em reunião"],
         prazo="até 30 dias úteis após o briefing"),
]
ETAPAS = [("Briefing", "Formulário + conversa: negócio, cliente, concorrentes, gosto."),
          ("Persona e pesquisa", "Quem compra de você e referências premium do mundo inteiro."),
          ("Conceito", "A ideia da marca e o logo, apresentados em mockup."),
          ("Sistema", "Cores, letras, elementos, fotografia e voz."),
          ("Aplicações", "Instagram, papelaria, site: a marca no mundo real."),
          ("Entrega", "Arquivos finais, guia ou brand book e apoio para usar.")]

MENSAGENS = [
    "Oi, [nome]! Tudo bem? Aqui é o Lindson, designer aqui de São Luís.\nMuita loja boa perde cliente porque a marca parece menor do que o negócio é.\nEu crio a identidade visual completa, do logo ao Instagram, pra passar confiança de primeira.\nPosso te mostrar como ficaria a da [negócio]?",
    "Oi, [nome]! Sou o Lindson, aqui de São Luís.\nCada post sai de um jeito e o cliente não lembra da sua marca, né? Isso é muito comum.\nEu monto a marca e um manual simples pra tudo sair com a mesma cara.\nQuer que eu te mande uns trabalhos que já fiz?",
    "Oi, [nome]! Meu nome é Lindson, sou designer.\nQuem quer cobrar mais precisa de uma marca que pareça mais cara que a do concorrente.\nEu faço identidade visual e site pra negócio da região, com processo e prazo certo.\nPosso te mandar como funciona?",
]

ANUNCIO = [
    ("SUA MARCA\nPARECE MENOR\nQUE O SEU\nNEGÓCIO?", "", None),
    ("O CLIENTE JULGA\nNA PRIMEIRA\nOLHADA.", "Logo improvisado, cada post de um jeito, perfil que não passa confiança.", None),
    ("IDENTIDADE\nVISUAL\nCOMPLETA.", "Logo, cores, letras, brand book e a marca aplicada no Instagram e no site.", "@bb:realtime:6"),
    ("CASES DO\nESTÚDIO.", "Real Time · WF Celulares · Processo Legislativo · Orégano Turbo.", "@grid"),
    ("PEÇA SEU\nORÇAMENTO.", "Pelo WhatsApp. Essencial, Completo ou Premium.", None),
]

BRIEFING = [
    ("Sobre o negócio", ["Nome do negócio e como quer que a marca se chame", "O que você vende e qual o produto ou serviço principal", "Cidade e onde atende (loja, online, os dois)", "Há quanto tempo existe"]),
    ("Sobre o cliente", ["Quem compra de você (idade, rotina, o que valoriza)", "Por que o cliente escolhe você e não o concorrente", "O que o seu cliente precisa sentir ao ver a sua marca (ex.: confiança, sofisticação, proximidade)"]),
    ("Mercado", ["3 concorrentes (nome ou @)", "3 marcas que você admira, de qualquer área, e por quê", "O que você NÃO quer de jeito nenhum (cores, estilos)"]),
    ("Marca atual", ["Já tem logo? Mande o arquivo ou foto", "O que gosta e o que não gosta da marca atual", "Onde a marca vai aparecer (Instagram, fachada, uniforme, embalagem, site)"]),
    ("Projeto", ["Pacote de interesse: Essencial, Completo ou Premium", "Prazo ideal", "Quem aprova a marca (só você ou mais pessoas)"]),
]

PESQUISA = [
    ("Koto", "Reino Unido", "https://koto.studio/work/", "Case contado em blocos: desafio, ideia, sistema, aplicações; capa com o símbolo enorme.", "ESCOLHIDO: ordem dos módulos do Behance."),
    ("Porto Rocha", "EUA / Brasil", "https://portorocha.com/", "Tipografia gigante, fundo escuro, cada case com 1 frase-conceito.", "ESCOLHIDO: tipografia e frase-conceito na capa."),
    ("Collins", "EUA", "https://www.wearecollins.com/", "Página de estúdio que vende processo, não preço; chamada direta para conversa.", "ESCOLHIDO: estrutura da página de venda (processo em etapas, sem preço)."),
    ("Pentagram", "EUA / Reino Unido", "https://www.pentagram.com/work", "Grade de cases com foto de aplicação real como capa.", "Descartado: depende de foto de aplicação física que não temos para todos."),
    ("Lundgren+Lindqvist", "Suécia", "https://lundgrenlindqvist.se/", "Minimalismo radical, muito branco.", "Descartado: frio demais para a persona local."),
    ("Studio Dumbar / DEPT", "Holanda", "https://studiodumbar.com/", "Motion e sistemas dinâmicos.", "Descartado: pede motion que não cabe no Behance estático agora."),
    ("Mucho", "Espanha", "https://wearemucho.com/", "Cases com paleta e tipografia em módulos separados.", "Descartado como base; aproveitado o módulo de paleta."),
    ("Futura", "México", "https://byfutura.com/", "Branding latino ousado, cor chapada.", "Descartado: estética de moda, não de negócio local."),
    ("Brand New (UnderConsideration)", "EUA", "https://www.underconsideration.com/brandnew/", "Formato antes x depois com explicação curta.", "Aproveitado no post 'Antes x depois' do LinkedIn."),
    ("Behance Best of Branding", "Global", "https://www.behance.net/galleries/graphic-design/branding", "Cases em destaque: capa limpa, 8 a 12 módulos, último com créditos.", "Aproveitado: tamanho de módulos e módulo de créditos."),
]
