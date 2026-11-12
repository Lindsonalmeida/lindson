# Brand book premium · template único (conta Pedro, 12/11/2026)
# Uso: python3 gerar.py <realtime|wf|curso|leo|lindson|todos>
# Composição copiada de: NASA Graphics Standards Manual (número de seção gigante, grade técnica, rótulo mono),
# Collins/Dropbox Brand Guidelines (blocos de cor chapada, tipo enorme) e Pentagram/Mastercard (proteção e usos incorretos).
# Ver TEMPLATE.md. Fotos e PDFs saem no privado CentralLindsonALmeida (nunca no repo público).
import sys, os, html
from PIL import Image

L = '/home/user/lindson/agencia'
P = '/home/user/centrallindsonalmeida/dados'
CUR = P + '/clientes-arquivos/curso'
SCR = os.environ.get('BB_TMP', '/tmp/bb')

def f(p):
    # cópia reduzida (máx. 1400 px) para o PDF não passar de poucos MB
    if not p.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): return 'file://' + p
    import hashlib
    os.makedirs(SCR + '/img', exist_ok=True)
    im = Image.open(p); alpha = im.mode in ('RGBA', 'LA', 'P') and p.lower().endswith('.png')
    out = SCR + '/img/' + hashlib.md5(p.encode()).hexdigest() + ('.png' if alpha else '.jpg')
    if not os.path.exists(out):
        im.thumbnail((1400, 1400))
        if alpha: im.convert('RGBA').save(out, optimize=True)
        else: im.convert('RGB').save(out, quality=82)
    return 'file://' + out

def rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def cmyk(h):
    r, g, b = [x/255 for x in rgb(h)]; k = 1-max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    return tuple(round(v*100) for v in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))

def media(p, fit='contain', pos='center', pad=0):
    if p.lstrip().startswith('<'): return f'<div style="width:100%;height:100%;display:grid;place-items:center">{p}</div>'
    return f'<img src="{f(p)}" style="width:100%;height:100%;object-fit:{fit};object-position:{pos};padding:{pad}px;display:block">'

def img(p, cls='', st=''):
    return f'<img class="{cls}" style="{st}" src="{f(p)}">'

# ---------------------------------------------------------------- CLIENTES
C = {}

C['realtime'] = dict(
    nome='Real Time', sub='Full Jobs · produtora audiovisual', ano='2026',
    saida=P+'/clientes-arquivos/rt-full-jobs/brand-book',
    fonts='Geist:wght@400;600;700;800&family=Manrope:wght@400;600;700&family=Geist+Mono:wght@500',
    disp="'Geist'", body="'Manrope'", mono="'Geist Mono'", dw=700, up=False,
    bg='#05070B', bg2='#11161F', fg='#F4F7FB', mut='#8C96A6', ac='#2E9BFF', ac2='#FF3B3B', on_ac='#05070B',
    logo=img(L+'/clientes/rt-full-jobs/identidade/v1/marca/assinatura-horizontal.svg', '', 'width:100%'),
    simbolo=L+'/clientes/rt-full-jobs/identidade/v1/marca/simbolo.svg',
    versoes=[('Assinatura horizontal', L+'/clientes/rt-full-jobs/identidade/v1/marca/assinatura-horizontal.svg', '#05070B'),
             ('Assinatura vertical', L+'/clientes/rt-full-jobs/identidade/v1/marca/assinatura-vertical.svg', '#11161F'),
             ('Versão clara', L+'/clientes/rt-full-jobs/identidade/v1/marca/assinatura-horizontal-claro.svg', '#F4F7FB'),
             ('Uma cor (branco)', L+'/clientes/rt-full-jobs/identidade/v1/marca/assinatura-horizontal-mono-branco.svg', '#2E9BFF'),
             ('Símbolo / avatar', L+'/clientes/rt-full-jobs/identidade/v1/marca/simbolo-app.svg', '#11161F'),
             ('Favicon', L+'/clientes/rt-full-jobs/identidade/v1/marca/favicon.svg', '#05070B')],
    conceito='No ar, agora.', proposito='Entregar o job de vídeo completo, do equipamento à equipe, pronto para gravar quando o cliente precisa.',
    essencia=['Técnica sem complicação', 'Pronto para agora', 'O cliente é o herói', 'Equipamento de verdade'],
    persona=['Produtor, agência ou empresa que precisa gravar em São Luís.', '28 a 50 anos, agenda apertada, job com data marcada.',
             'Dor: alugar equipamento num lugar e equipe em outro, e algo falhar no set.', 'Valoriza: equipamento conferido, gente que sabe usar, resposta rápida.',
             'Confia quando vê o set real, a lista de equipamentos e trabalhos entregues.'],
    antes=L+'/clientes/rt-full-jobs/identidade/v1/fotos/logo-antigo.jpg', depois=L+'/clientes/rt-full-jobs/identidade/v1/marca/simbolo-app.svg',
    mudancas=[('Visor da câmera mantido', 'é a herança que o público já reconhece'), ('"rt" em Geist Bold, r branco e t azul', 'lê em tamanho de avatar'),
              ('Ponto REC vermelho', 'conta, num detalhe, que a marca está "no ar"'), ('Paleta escura de set', 'parece estúdio de verdade, não gráfica rápida'),
              ('Família de letra única com mono técnico', 'timecode e dados de equipamento ganham voz própria')],
    protecao='A área livre em volta do logo é a altura do "r" do símbolo, nos quatro lados.', minimo=[('Digital', '120 px de largura'), ('Impresso', '30 mm de largura'), ('Símbolo isolado', '24 px')],
    paleta=[('Preto Set', '#05070B', 60, 'fundo de tudo'), ('Branco Luz', '#F4F7FB', 25, 'texto e respiro'), ('Azul Real', '#2E9BFF', 10, 'palavra-chave, "time"'),
            ('REC', '#FF3B3B', 5, 'só o ponto REC'), ('Índigo Take', '#4338F0', 0, 'faixas'), ('Grafite', '#11161F', 0, 'cartões')],
    tipos=[('Título', 'Geist', "'Geist'", 700, 'Seu job é na Real Time.'), ('Texto', 'Manrope', "'Manrope'", 400, 'Equipamento conferido, equipe que sabe usar e resposta no mesmo dia.'),
           ('Dados técnicos', 'Geist Mono', "'Geist Mono'", 500, 'REC 00:12:48:07 · 4K · 24 FPS')],
    elementos=[('Visor', 'os cantos da câmera enquadram foto e título'), ('Selo REC com timecode', 'rótulo mono com o ponto vermelho'),
               ('Halo de luz', 'brilho azul suave atrás do produto'), ('Faixa índigo', 'tarja para destaque de serviço')],
    elem_img=L+'/clientes/rt-full-jobs/identidade/v1/previa-assinaturas.png',
    fotos=[L+'/clientes/rt-full-jobs/identidade/v1/fotos/set.jpg', L+'/clientes/rt-full-jobs/identidade/v1/fotos/estudio.jpg', L+'/clientes/rt-full-jobs/identidade/v1/fotos/lentes.jpg'],
    foto_regras=['Equipamento real da Real Time em primeiro lugar', 'Luz de set: contraste alto e fundo escuro', 'Gente trabalhando, não pose de banco', 'Mesmo tratamento frio em todas as fotos'],
    voz=['Técnico mas simples', 'Pronto para agora', 'Frases curtas, verbo na frente'], faz=['"Seu job é na Real Time."', '"Equipamento conferido antes de sair."'],
    nao=['Prometer resultado de campanha', 'Jargão sem explicação', 'Preço sem aprovação'],
    apps=[(L+'/clientes/rt-full-jobs/instagram-v2/artes/post-01.jpg', 'Post'), (L+'/clientes/rt-full-jobs/instagram-v2/artes/post-03.jpg', 'Post'),
          (L+'/clientes/rt-full-jobs/instagram-v2/artes/post-05.jpg', 'Post'), (L+'/clientes/rt-full-jobs/identidade/v1/previa-capa.png', 'Manual'),
          (L+'/clientes/rt-full-jobs/instagram-v2/previa-feed.jpg', 'Feed'), (L+'/clientes/rt-full-jobs/instagram-v2/artes/post-02.jpg', 'Post')],
    capa_foto=L+'/clientes/rt-full-jobs/identidade/v1/fotos/set.jpg', fecho='Seu job é na Real Time.')

WF = L+'/clientes/wf-celulares'
C['wf'] = dict(
    nome='WF Celulares', sub='iPhone · procedência e assistência · São Luís', ano='2026',
    saida=P+'/clientes-arquivos/wf-celulares/brand-book',
    fonts='Inter:wght@200;300;400;600;700', disp="'Inter'", body="'Inter'", mono="'Inter'", dw=200, up=False,
    bg='#000000', bg2='#1D1D1F', fg='#F5F5F7', mut='#8E8A84', ac='#C7C9CC', ac2='#8E8A84', on_ac='#000000',
    logo=img(WF+'/identidade/logo-b/wf-logo-b-cor.png', '', 'display:block;margin:auto;max-width:100%;max-height:520px'),
    simbolo=WF+'/identidade/logo-b/wf-logo-b-branca.png',
    versoes=[('Principal (cor)', WF+'/identidade/logo-b/wf-logo-b-cor.png', '#000000'), ('Branca', WF+'/identidade/logo-b/wf-logo-b-branca.png', '#1D1D1F'),
             ('Preta (para gráfica)', WF+'/identidade/logo-b/wf-logo-b-preta.png', '#C7C9CC'), ('Avatar', WF+'/identidade/pecas-final/03-avatar.jpg', '#000000')],
    conceito='Procedência que dá para ver.', proposito='Vender iPhone com laudo, garantia e assistência séria, para o cliente comprar sem medo.',
    essencia=['Procedência', 'Atendimento de perto', 'Universo Apple, sem exagero', 'Preço elegante, sem grito'],
    persona=['Quem quer um iPhone em São Luís, 18 a 45 anos.', 'Compara preço no Instagram e no WhatsApp antes de ir à loja.',
             'Dor: medo de aparelho com defeito escondido ou sem garantia.', 'Valoriza: laudo, garantia, parcelamento claro e loja física.',
             'Confia quando vê a loja de verdade, o laudo e cliente real falando.'],
    antes=SCR+'/wf-antes.jpg', depois=WF+'/identidade/logo-b/wf-logo-b-cor.png',
    mudancas=[('Saiu o 3D, o cromo e o brilho', 'a marca antiga parecia adesivo de capinha'), ('Maçã + WF + CELULARES espaçado', 'conversa com o universo Apple (uso autorizado pelo cliente)'),
              ('Titânio, preto e prata', 'mesma linguagem das lojas premium de iPhone'), ('Inter fina, tipo keynote', 'parece lançamento, não feirão'),
              ('Sem fundo branco nas peças', 'decisão do Lindson: "esse branco parece pobre"')],
    protecao='A área livre em volta do logo é a altura da letra W, nos quatro lados.', minimo=[('Digital', '140 px de largura'), ('Impresso', '35 mm de largura'), ('Marca reduzida (maçã + WF)', '48 px')],
    paleta=[('Preto', '#000000', 60, 'fundo de tudo'), ('Grafite', '#1D1D1F', 20, 'cartões e áreas'), ('Titânio', '#8E8A84', 10, 'degradê do logo, detalhes'),
            ('Prata', '#C7C9CC', 5, 'linhas e ícones'), ('Branco gelo', '#F5F5F7', 5, 'texto')],
    tipos=[('Título', 'Inter ExtraLight', "'Inter'", 200, 'Mesma loja. Outra marca.'), ('Texto', 'Inter Regular', "'Inter'", 400, 'iPhone lacrado e seminovo com laudo e garantia.'),
           ('Rótulo', 'Inter SemiBold', "'Inter'", 600, 'LAUDO WF · GARANTIA · 18X')],
    elementos=[('Luz de estúdio', 'brilho suave por trás do aparelho'), ('Etiqueta Laudo WF', 'cartão de procedência com checklist'), ('Linha fina prata', 'divide informações, nunca moldura grossa')],
    elem_img=WF+'/identidade/pecas-final/14-cartao-etiqueta.jpg',
    fotos=[WF+'/artes-02/02-oferta-12-pro-max.jpg', WF+'/artes-02/03-assistencia.jpg', WF+'/artes-02/04-oferta-17-pro-max-silver.jpg'],
    foto_regras=['Aparelho em fundo escuro, luz de estúdio', 'Imagens de imprensa da Apple só ilustrativas', 'Foto real da loja substitui assim que chegar', 'Nada de fundo branco ou claro'],
    voz=['Elegante e direto', 'Confiança, não pressão', 'Números só os aprovados'], faz=['"Mesma loja. Outra marca."', '"Orçamento antes de mexer."'],
    nao=['Preço em tarja gritando', 'Logo de outro fabricante', 'Depoimento inventado'],
    apps=[(WF+'/artes-02/01-black-30-dias.jpg', 'Post'), (WF+'/artes-02/05-laudo-wf.jpg', 'Post'), (WF+'/identidade/pecas-final/13-fachada.jpg', 'Fachada (mockup)'),
          (WF+'/identidade/pecas-final/14-cartao-etiqueta.jpg', 'Cartão e etiqueta'), (WF+'/painel-fixado/previa-grade.jpg', 'Painel fixado'), (WF+'/artes-02/07-prova-social.jpg', 'Post (exemplo ilustrativo)')],
    capa_foto=WF+'/identidade/pecas-final/13-fachada.jpg', voz_bg='#1D1D1F', voz_fg='#F5F5F7', fecho='Mesma loja. Outra marca.')

C['curso'] = dict(
    nome='Processo Legislativo', sub='Curso prático · Câmara Municipal', ano='2026',
    saida=CUR+'/brand-book',
    fonts='Inter+Tight:wght@400;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500',
    disp="'Inter Tight'", body="'Inter Tight'", mono="'JetBrains Mono'", dw=700, up=False, serif="'Instrument Serif'",
    bg='#0A1F17', bg2='#123528', fg='#EFE6D4', mut='#8FA79A', ac='#C8A96B', ac2='#E6CF9C', on_ac='#0A1F17',
    logo=f'<div style="display:flex;align-items:center;gap:40px">{img(CUR+"/site/assets/simbolo.svg","","width:34%")}<div style="font:700 120px/0.95 Inter Tight;letter-spacing:-.03em">Processo<br><i style="font:italic 400 128px Instrument Serif;color:#C8A96B">Legislativo</i></div></div>',
    simbolo=CUR+'/site/assets/simbolo.svg',
    versoes=[('Símbolo § no hemiciclo', CUR+'/site/assets/simbolo.svg', '#0A1F17'), ('Avatar (marca)', CUR+'/instagram-perfil/foto-perfil-b-logo.png', '#123528'),
             ('Avatar com os professores', CUR+'/instagram-perfil/foto-perfil-v3-mesmo-patamar.png', '#0A1F17'), ('Símbolo no creme', CUR+'/site/assets/simbolo.svg', '#EFE6D4')],
    conceito='Chega de improviso na câmara.', proposito='Ensinar o processo legislativo municipal na prática, do protocolo à publicação, para quem vive a Câmara por dentro.',
    essencia=['Rigor de quem é do ramo', 'Prática, não teoria solta', 'Tradição com cara de hoje', 'Dois professores no mesmo patamar'],
    persona=['Vereador, assessor, advogado ou servidor de Câmara no Maranhão.', '25 a 60 anos, rotina de sessão, prazo e regimento.',
             'Dor: errar rito, perder prazo, ter proposição derrubada.', 'Valoriza: modelos prontos, jurisprudência e professor que atua na área.',
             'Confia em credencial real (OAB/MA) e em material sério, sem cara de curso de internet.'],
    antes=SCR+'/curso-antes-1.jpg', depois=CUR+'/painel-fixado/previa.jpg',
    mudancas=[('Saiu o azul e turquesa genérico do folder', 'parecia apostila, não instituição'), ('Verde plenário, creme e latão', 'remete a tribuna, couro e placa de bronze'),
              ('§ dentro do hemiciclo', 'o símbolo junta a lei e o plenário'), ('Inter Tight + 1 palavra em Instrument Serif itálica', 'peso de tradição sem ficar velho'),
              ('Rafael e Thiago sempre no mesmo patamar', 'mesma altura, brilho e tamanho de nome')],
    protecao='A área livre em volta do símbolo é metade do raio do hemiciclo, nos quatro lados.', minimo=[('Digital', '96 px (símbolo)'), ('Impresso', '15 mm (símbolo)'), ('Assinatura completa', '160 px')],
    paleta=[('Verde plenário', '#0A1F17', 55, 'fundo'), ('Musgo', '#123528', 25, 'áreas e cartões'), ('Creme', '#EFE6D4', 12, 'texto e respiro'),
            ('Latão', '#C8A96B', 8, 'só detalhe e palavra-chave'), ('Sálvia', '#8FA79A', 0, 'texto de apoio')],
    tipos=[('Título', 'Inter Tight', "'Inter Tight'", 700, 'Chega de improviso na'), ('Destaque', 'Instrument Serif itálica', "'Instrument Serif'", 400, 'câmara.'),
           ('Texto', 'Inter Tight', "'Inter Tight'", 400, 'Para vereadores, assessores, advogados e servidores.')],
    elementos=[('§ no hemiciclo', 'símbolo que vira selo e marca-d\'água'), ('Arcos do plenário', 'linhas finas em latão, atrás das fotos'),
               ('Palavra gigante atrás dos professores', 'ex.: PLENÁRIO em verde tom sobre tom'), ('Grão fino', 'tira o "duro" do fundo chapado')],
    elem_img=CUR+'/identidade-hemiciclo/prancha.png',
    fotos=[CUR+'/socios/cut-rafael-araujo-veras/recorte-limpo.png', CUR+'/socios/cut-tiago-azevedo/recorte-limpo.png'],
    foto_regras=['Professores sempre recortados, nunca a foto inteira', 'Mesma altura de rosto, linha dos olhos e brilho', 'Terno, luz quente lateral, fundo verde', 'Nenhum à frente do outro'],
    voz=['Sério e direto', 'Linguagem do plenário, explicada', 'Sem promessa de resultado'], faz=['"Chega de improviso na câmara."', '"Do protocolo à publicação."'],
    nao=['Prometer aprovação de projeto', 'Clichê de martelo e balança', 'Um professor maior que o outro'],
    apps=[(CUR+'/painel-fixado/painel-completo.jpg', 'Painel fixado'), (CUR+'/identidade-premium/carrossel-01.png', 'Carrossel'), (CUR+'/capas-reels/01-rafael-emenda.jpg', 'Capa de Reels'),
          (CUR+'/capas-reels/02-tiago-portaria.jpg', 'Capa de Reels'), (CUR+'/site/assets/og.jpg', 'Site'), (CUR+'/identidade-hemiciclo/story-01.png', 'Story')],
    capa_foto=CUR+'/site/assets/og.jpg', fecho='Chega de improviso na câmara.')

LEO = L+'/clientes/leo-pinto'
C['leo'] = dict(
    nome='Leo Pinto', sub='Vereador · São João Batista · MA', ano='2026',
    saida=P+'/clientes-arquivos/leo-pinto/brand-book',
    fonts='Montserrat:wght@500;700;900&family=Anton&family=Kaushan+Script', disp="'Montserrat'", body="'Montserrat'", mono="'Montserrat'", dw=900, up=True,
    bg='#082063', bg2='#2350F5', fg='#FFFFFF', mut='#B9C6EE', ac='#FFC20E', ac2='#F26A1B', on_ac='#082063', grad=True,
    logo=img(LEO+'/instagram-v12-feed/marca/logo_principal.png', '', 'width:100%'),
    simbolo=LEO+'/identidade/v3/marca/monograma.svg',
    versoes=[('Logo oficial', LEO+'/instagram-v12-feed/marca/logo_principal.png', '#082063'), ('Logo no royal', LEO+'/instagram-v12-feed/marca/logo_principal.png', '#2350F5'),
             ('Monograma LP', LEO+'/identidade/v3/marca/monograma.svg', '#FFFFFF'), ('Monograma noite', LEO+'/identidade/v3/marca/monograma-noite.svg', '#082063')],
    conceito='Do povo para o povo.', proposito='Mostrar o trabalho do mandato perto de quem mora em São João Batista, com o Leo de verdade, na rua.',
    essencia=['Jovem e engenheiro', 'Na rua, perto do povo', 'Da Baixada', 'Compromisso com São João Batista'],
    persona=['Morador de São João Batista e da Baixada, 18 a 70 anos.', 'Vê o Instagram e o WhatsApp no celular, à noite.',
             'Dor: não saber o que o vereador está fazendo pela cidade.', 'Valoriza: presença, resposta, obra e ação que dá para ver.',
             'Confia quando vê o Leo em foto real, no lugar, falando simples.'],
    antes=LEO+'/instagram-v12-feed/previa-feed.jpg', depois=LEO+'/instagram-v13-apresentacao/previa-grade.jpg',
    mudancas=[('Saíram raios, faixas, ícones, fumaça e sol', 'decisão de 02/11: só fontes, logo e cores'), ('Retrato grande, de perto, recortado', 'o Leo é o protagonista'),
              ('Nome em blocos de cor: LEO amarelo, PINTO branco', 'lê de longe, no celular'), ('Degradê azul com luz diagonal e grão', 'sofisticação sem enfeite'),
              ('Mapa oficial de São João Batista em camada', 'território, não decoração')],
    protecao='A área livre em volta do logo é a altura da letra L, nos quatro lados. Aplicada sem balão.', minimo=[('Digital', '140 px de largura'), ('Impresso', '35 mm de largura'), ('Monograma LP', '40 px')],
    paleta=[('Marinho', '#082063', 40, 'fundo, base do degradê'), ('Azul royal', '#2350F5', 25, 'topo do degradê'), ('Laranja', '#F26A1B', 15, 'cor principal, etiquetas'),
            ('Amarelo', '#FFC20E', 10, 'caixa do LEO, palavra-chave'), ('Branco', '#FFFFFF', 10, 'texto e caixa do PINTO')],
    tipos=[('Título', 'Montserrat Black', "'Montserrat'", 900, 'JUNTOS PODEMOS MAIS'), ('Impacto', 'Anton', "'Anton'", 400, 'DA BAIXADA'),
           ('Toque humano', 'Kaushan Script', "'Kaushan Script'", 400, 'Prazer, eu sou o Leo')],
    elementos=None,
    fotos=[LEO+'/instagram-v13-apresentacao/leo-v13-1-esquerda.jpg', LEO+'/instagram-v13-apresentacao/leo-v13-2-meio.jpg', LEO+'/instagram-v13-apresentacao/leo-v13-3-direita.jpg'],
    foto_regras=['Retrato grande e de perto, recortado', 'Rosto longe das bordas, sangrando na base', 'Cor realçada de leve, nunca trocar a roupa', 'Foto real do Leo; IA só com aviso'],
    voz=['Simples e próximo', 'Primeira pessoa: "eu", "a gente"', 'Situação: valoriza o trabalho junto'], faz=['"Juntos podemos mais!"', '"Me conta sua demanda."'],
    nao=['Criticar a prefeitura', 'Promessa que o mandato não controla', 'Grafismos (raio, faixa, ícone, fumaça, sol)'],
    apps=[(LEO+'/instagram-v13-apresentacao/leo-v13-2-meio.jpg', 'Apresentação v13'), (LEO+'/instagram-v14-datas/p1-15-11.jpg', 'Data comemorativa'),
          (LEO+'/instagram-v14-datas/p4-25-12.jpg', 'Data comemorativa'), (LEO+'/instagram-v13-apresentacao/previa-grade.jpg', 'Grade do perfil'),
          (LEO+'/instagram-v14-datas/p6-01-01.jpg', 'Data comemorativa'), (LEO+'/instagram-v14-datas/p2-20-11.jpg', 'Data comemorativa')],
    capa_foto=LEO+'/instagram-v13-apresentacao/leo-v13-2-meio.jpg', fecho='Juntos podemos mais!')

ML = L+'/marca-lindson/artes-v2'
C['lindson'] = dict(
    nome='Lindson Almeida', sub='Marketing para negócio local · São Luís · MA', ano='2026',
    saida=P+'/agencia/marca-lindson/brand-book',
    fonts='Anton&family=Manrope:wght@400;600;800&family=JetBrains+Mono:wght@500;700', disp="'Anton'", body="'Manrope'", mono="'JetBrains Mono'", dw=400, up=True,
    bg='#0A0A0A', bg2='#1a1a1a', fg='#FFFFFF', mut='#9a978f', ac='#F5C518', ac2='#FFE27A', on_ac='#0A0A0A',
    logo='<div style="font:400 190px/1.02 Anton;letter-spacing:.01em">LINDSON<br><span style="display:inline-block;background:#F5C518;color:#0A0A0A;padding:4px 18px 0;line-height:1">ALMEIDA</span></div>',
    simbolo=None,
    versoes_html=[('Principal', '<div style="font:400 72px/1.05 Anton;color:#fff">LINDSON<br><span style="display:inline-block;background:#F5C518;color:#0A0A0A;padding:2px 8px 0;line-height:1">ALMEIDA</span></div>', '#0A0A0A'),
                  ('No amarelo', '<div style="font:400 72px/1.05 Anton;color:#0A0A0A">LINDSON<br><span style="display:inline-block;background:#0A0A0A;color:#F5C518;padding:2px 8px 0;line-height:1">ALMEIDA</span></div>', '#F5C518'),
                  ('Horizontal', '<div style="font:400 64px Anton;color:#fff">LINDSON <span style="background:#F5C518;color:#0A0A0A;padding:0 8px">ALMEIDA</span></div>', '#1a1a1a'),
                  ('Uma cor (carimbo)', '<div style="font:400 72px/0.92 Anton;color:#0A0A0A">LINDSON<br>ALMEIDA</div>', '#FFFFFF'),
                  ('Avatar', '<div style="width:170px;height:170px;border-radius:50%;background:#F5C518;display:grid;place-items:center;font:400 92px Anton;color:#0A0A0A">LA</div>', '#0A0A0A'),
                  ('Rótulo mono', '<div style="font:700 26px JetBrains Mono;letter-spacing:.2em;color:#F5C518">@LINDSONALMEIDA_</div>', '#0A0A0A')],
    conceito='Palavra-chave na caixa amarela.', proposito='Fazer o negócio local de São Luís vender mais com Instagram, site e anúncio, mostrando o processo de verdade.',
    essencia=['Impacto, nunca simplista', 'Foto colorida de cinema', 'Prova real, sem número inventado', 'Fala simples de WhatsApp'],
    persona=['Dono de negócio local em São Luís, 28 a 55 anos.', 'Toca a loja o dia todo e olha o Instagram à noite.',
             'Dor: posta sem resultado e não tem tempo para aprender marketing.', 'Valoriza: alguém que faz por ele e mostra o que fez.',
             'Confia quando vê cliente real, antes e depois e o Lindson de rosto.'],
    antes='/home/user/lindson/branding/brand-book/img/story-1.jpg', lbl_antes='ANTES · V1', depois=ML+'/artes/c2y.jpg',
    mudancas=[('Saiu o azul-sinal, o violeta e o REC da v1', 'muitas cores disputavam a atenção'), ('Preto e amarelo #F5C518', 'contraste máximo no feed, lê de longe'),
              ('Anton gigante + Manrope', 'manchete gorda, texto limpo'), ('Palavra-chave em caixa amarela', 'o olho vai direto ao que importa'),
              ('Foto colorida cinematográfica', 'nunca P&B lavada (reprovada)')],
    protecao='A área livre em volta da assinatura é a altura da caixa amarela, nos quatro lados.', minimo=[('Digital', '160 px de largura'), ('Impresso', '30 mm de largura'), ('Avatar LA', '40 px')],
    paleta=[('Preto', '#0A0A0A', 60, 'fundo'), ('Amarelo c2y', '#F5C518', 25, 'caixa da palavra-chave, ação'), ('Branco', '#FFFFFF', 12, 'texto'),
            ('Grafite', '#2A2A2A', 3, 'cartões e linhas')],
    tipos=[('Título', 'Anton', "'Anton'", 400, 'SUA BIO VENDE?'), ('Texto', 'Manrope', "'Manrope'", 600, 'Eu faço o seu Instagram vender, do jeito que você fala.'),
           ('Rótulo', 'JetBrains Mono', "'JetBrains Mono'", 500, '01 · CASE REAL · SÃO LUÍS')],
    elementos=[('Caixa amarela', 'a palavra-chave sempre dentro dela'), ('Rótulo mono numerado', 'cantos com (01), (02)'),
               ('Selo de vidro fosco', 'informação curta sobre a foto'), ('Grão de filme e vinheta', 'acabamento de cinema')],
    elem_img=ML+'/artes/a1p.jpg',
    fotos=[ML+'/fotos/c00.jpg', ML+'/fotos/c01.jpg', ML+'/fotos/c02-full.png'],
    foto_regras=['Sempre colorida e cinematográfica', 'Recortada na arte, sem borda aparente', 'Letra gigante passando por trás', 'Sombra dele projetada na letra'],
    voz=['Português simples de WhatsApp', 'Conexão, dor, desejo, pergunta', 'Prova real, nunca número inventado'], faz=['"Eu mudei a minha marca."', '"Sua bio é uma lista de links. Ou é a sua vitrine."'],
    nao=['Jargão ("gargalo", "funil")', '"Vi que..." na abordagem', 'Foto P&B lavada'],
    apps=[(ML+'/artes/c2y.jpg', 'Post'), (ML+'/artes/a1p.jpg', 'Post'), (ML+'/artes/p1p.jpg', 'Post'), (ML+'/artes/c1_1.jpg', 'Carrossel'),
          (ML+'/artes/antes-depois-c2y.jpg', 'Antes x depois'), (ML+'/artes/a2.jpg', 'Post')],
    capa_foto=ML+'/fotos/c01.jpg', fecho='Bora fazer o seu vender?')

def noise():
    out = SCR + '/grao.png'
    if not os.path.exists(out):
        import random; im = Image.new('L', (256, 256))
        im.putdata([random.randint(0, 255) for _ in range(256*256)]); im.save(out)
    return 'file://' + out


OT = L+'/operacao-propria'
OTL = '<div style="display:flex;align-items:center;gap:34px"><img src="'+f(OT+'/identidade/marca-v3/simbolo-creme.svg')+'" style="width:150px"><div><div style="font:800 140px/0.9 Inter Tight;letter-spacing:-.05em;color:#F3EEE6">Orégano Turbo</div><div style="font:500 26px IBM Plex Mono;letter-spacing:.3em;color:#F3EEE6;opacity:.8;margin-top:14px">MARKETING DE VENDAS PARA PIZZARIAS</div></div></div>'
C['oregano'] = dict(
    nome='Orégano Turbo', sub='Marketing de vendas para pizzarias', ano='2026',
    saida=P+'/agencia/oregano-turbo/brand-book',
    fonts='Anton&family=Inter+Tight:wght@600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500',
    disp="'Anton'", body="'Inter'", mono="'IBM Plex Mono'", dw=400, up=True,
    bg='#1E5B3B', bg2='#141311', fg='#F3EEE6', mut='#BFD3C6', ac='#F2B33D', ac2='#D42A1F', on_ac='#141311',
    logo=OTL, simbolo=OT+'/identidade/marca-v3/simbolo-creme.svg',
    versoes=[('Símbolo verde', OT+'/identidade/marca-v3/simbolo-verde.svg', '#F3EEE6'), ('Símbolo creme', OT+'/identidade/marca-v3/simbolo-creme.svg', '#D42A1F'),
             ('Símbolo carvão', OT+'/identidade/marca-v3/simbolo-carvao.svg', '#F2B33D'), ('Símbolo branco', OT+'/identidade/marca-v3/simbolo-branco.svg', '#141311'),
             ('Avatar', OT+'/identidade/pecas-v4/v4-16-avatar.png', '#1E5B3B'), ('Logo sobre foto', OT+'/identidade/pecas-v4/v4-03-logo-foto.png', '#141311')],
    conceito='Uma folha que sobe.', proposito='Fazer a pizzaria vender mais nos dias fracos com Instagram, WhatsApp e anúncio, sem depender de aplicativo.',
    essencia=['Sério, de quem entende de vendas', 'Foto real e mockup, nada de cartum', 'Forno, cor e comida', 'Comanda: "PEDIDO Nº"'],
    persona=['Dono de pizzaria em São Luís, 30 a 55 anos.', 'Fica no forno à noite e vê o celular entre um pedido e outro.',
             'Dor: terça e quarta fracas e taxa alta de aplicativo.', 'Valoriza: pedido no WhatsApp, foto que dá fome, resultado medido.',
             'Confia em coisa séria, foto real e mockup, não em selo fofo.'],
    antes=OT+'/identidade/pecas/prancha-01-capa.png', depois=OT+'/identidade/pecas-v4/v4-01-capa.png', lbl_antes='ANTES · V1 CARTUM', lbl_depois='DEPOIS · V4 IMPACTO',
    mudancas=[('v1 mascote cartum → fora', '"quero algo premium"'), ('v2 selo lúdico → fora', 'parecia brinquedo para o dono de pizzaria'),
              ('v3 séria: folha que sobe, foto real e mockup', '"prefiro coisa mais séria, imagens reais, mockups"'),
              ('v4: Anton, tomate, açafrão, xadrez e comida recortada', '"mais impacto, conexão, menos espaços em branco"'),
              ('A nervura da folha vira seta de vendas', 'o símbolo conta o resultado')],
    protecao='A área livre em volta do logo é a altura do símbolo dividida por dois, nos quatro lados.', minimo=[('Símbolo', '24 px'), ('Nome', '120 px'), ('Impresso (nome)', '30 mm')],
    paleta=[('Verde forno', '#1E5B3B', 40, 'fundo principal'), ('Carvão', '#141311', 25, 'texto e fundos'), ('Creme', '#F3EEE6', 20, 'respiro'),
            ('Tomate', '#D42A1F', 10, 'campanha e destaque'), ('Açafrão', '#F2B33D', 5, 'só detalhe')],
    tipos=[('Manchete', 'Anton', "'Anton'", 400, 'TERÇA FRACA?'), ('Nome e títulos', 'Inter Tight', "'Inter Tight'", 800, 'Orégano Turbo'),
           ('Texto', 'Inter', "'Inter'", 400, 'Pedido no WhatsApp, foto que dá fome.'), ('Comanda', 'IBM Plex Mono', "'IBM Plex Mono'", 500, 'PEDIDO Nº 0427')],
    elementos=[('Xadrez de cantina', 'faixa e fundo de selo'), ('10 ícones em traço', 'padrão de fundo, tom sobre tom'), ('Selos redondos', 'informação curta sobre a foto'),
               ('Comida recortada saindo da arte', 'pizza e ingredientes voando'), ('Comanda "PEDIDO Nº"', 'conceito de toda peça')],
    elem_img=OT+'/identidade/pecas-v4/v4-06-padroes-selos.png',
    fotos=[OT+'/identidade/fotos-v4/fatia-puxando.jpg', OT+'/identidade/fotos-v4/calabresa.jpg', OT+'/identidade/fotos-v3/forno-pizza.jpg'],
    foto_regras=['Foto real da pizzaria cliente primeiro', 'Banco Pexels com crédito só como apoio', 'Flash duro, cor saturada, comida enorme', 'Nada de chef de bigode'],
    voz=['Dono falando com dono', 'Direto, de balcão', 'Número só o real'], faz=['"Terça fraca? A gente resolve."', '"Menos app, mais Zap."'],
    nao=['Prometer faturamento', 'Clichê de pizzaria (chef, bigode)', 'Mascote fofo'],
    apps=[(OT+'/identidade/pecas-v4/v4-08-mockup-caixa.png', 'Caixa de pizza'), (OT+'/identidade/pecas-v4/v4-09-mockup-uniforme.png', 'Uniforme'),
          (OT+'/identidade/pecas-v4/v4-10-mockup-copo-sacola.png', 'Copo e sacola'), (OT+'/identidade/pecas-v4/v4-12-mockup-celular.png', 'Celular'),
          (OT+'/social/v3/previa-feed.jpg' if os.path.exists(OT+'/social/v3/previa-feed.jpg') else OT+'/social/v4/previa-feed.jpg', 'Feed (kit social)'), (OT+'/identidade/pecas-v4/v4-11-mockup-cartao-proposta.png', 'Cartão e proposta')],
    capa_foto=OT+'/identidade/fotos-v4/fatia-puxando.jpg', fecho='Uma folha que sobe.')

DB = '/home/user/lindson/apps/clone-studio/identidade'
C['duble'] = dict(
    nome='Dublê', sub='Estúdio de clone de voz e imagem · uso interno', ano='2026',
    saida=P+'/agencia/duble/brand-book',
    fonts='Geist:wght@400;600;700&family=Manrope:wght@400;500;700&family=Geist+Mono:wght@500', disp="'Geist'", body="'Manrope'", mono="'Geist Mono'", dw=600, up=False,
    bg='#0B0B10', bg2='#15151C', fg='#F2F1EC', mut='#9C9AAB', ac='#8B7CFF', ac2='#F5C518', on_ac='#0B0B10',
    logo=img(DB+'/logo.svg', '', 'width:100%'), simbolo=DB+'/simbolo.svg',
    versoes=[('Horizontal', DB+'/logo.svg', '#0B0B10'), ('Símbolo / ícone', DB+'/simbolo.svg', '#15151C'), ('Favicon (2 barras)', DB+'/favicon.svg', '#0B0B10'), ('Prévia oficial', DB+'/previa.png', '#0B0B10')],
    conceito='Só grava quem disse sim.', proposito='Copiar voz e rosto de quem autorizou, e só deixar usar essa cópia com termo assinado e vídeo da própria pessoa.',
    essencia=['Preciso como estúdio', 'Confiável: avisa, pede, registra', 'Moderno e calmo', 'Português simples'],
    persona=['O próprio Lindson e a equipe (uso interno).', 'Produz voz e vídeo de clientes e personagens todo dia.',
             'Dor: ferramenta em inglês, sem controle de autorização.', 'Valoriza: rapidez, uma ação por tela, saber o que está liberado.',
             'Confia quando o app mostra o termo e o selo LIBERADO.'],
    antes='<div style="font:600 92px Geist;color:#9C9AAB;letter-spacing:-.02em;text-align:center">Clone<br>Studio</div>', depois=DB+'/simbolo.svg',
    lbl_antes='ANTES · NOME', lbl_depois='DEPOIS · DUBLÊ',
    mudancas=[('"Clone Studio" virou "Dublê"', 'nome em português, curto, com a ideia do contrato'), ('Círculo partido: rosto + barras de voz', 'o original e o eco num símbolo só'),
              ('"d" e "b" espelhados na palavra', 'o duplo já está no nome'), ('Grafite e violeta Eco', 'família da Central, com destaque próprio'),
              ('Amarelo só no consentimento', 'o único ponto que precisa chamar atenção')],
    protecao='A área livre é a altura de uma barra do meio, em volta de tudo.', minimo=[('Logo horizontal', '96 px'), ('Símbolo', '16 px'), ('Favicon', '16 e 32 px')],
    paleta=[('Grafite', '#0B0B10', 60, 'fundo de tudo'), ('Painel', '#15151C', 30, 'cartões e campos'), ('Eco', '#8B7CFF', 10, 'botão principal, barras de voz'),
            ('Papel', '#F2F1EC', 0, 'texto principal'), ('Apagado', '#9C9AAB', 0, 'texto de apoio'), ('Selo', '#F5C518', 0, 'só consentimento (< 2%)')],
    tipos=[('Títulos', 'Geist SemiBold', "'Geist'", 600, 'Gerar voz'), ('Texto e botões', 'Manrope', "'Manrope'", 500, 'Só com autorização. Termo assinado e vídeo da pessoa.'),
           ('Selos e números', 'Geist Mono', "'Geist Mono'", 500, 'LIBERADO · 00:42 S')],
    elementos=[('Barras de voz', 'onda das 3 barras enquanto gera'), ('Faixa de consentimento', 'borda amarela e fundo a 7%'), ('Selos LIBERADO / BLOQUEADO', 'pílulas mono em verde e vermelho'),
               ('Cartões com borda de 1 px', 'sem sombra, cantos de 12 px')],
    elem_img=DB+'/previa-app.png',
    fotos=[DB+'/tela-v2-1.png', DB+'/tela-v2-3.png', DB+'/tela-v2-celular.png'], foto_regras=['Interface sempre em modo escuro', 'Um único botão Eco por tela', 'Rosto real só com termo e vídeo de consentimento', 'Sem gradiente, sem neon'],
    voz=['Você, frases curtas', 'Avisa, pede e registra', 'Sem jargão técnico'], faz=['"Dublê salvo e liberado."', '"Feito com IA: avise o público quando parecer real."'],
    nao=['Falar em "deepfake" ou "hacker"', 'Texto branco sobre o Eco', 'Escrever "Duble" sem acento'],
    apps=[(DB+'/tela-v2-4.png', 'Tela do app'), (DB+'/tela-v2-6.png', 'Tela do app'), (DB+'/tela-v2-celular.png', 'Celular'),
          (DB+'/previa-app.png', 'Tema aplicado'), (DB+'/tela-v2-1.png', 'Tela do app'), (DB+'/previa.png', 'Logo e símbolo')],
    capa_foto=DB+'/tela-v2-1.png', capa_w=560, fecho='Só grava quem disse sim.')

PF = os.path.dirname(os.path.abspath(__file__)) + '/pagode-fiado'
def pf_logo(w):
    sv = open(PF+'/logo.svg').read(); sv = sv[sv.index('<svg'):]
    import re; sv = re.sub(r'<style>.*?</style>', '', sv, flags=re.S)
    return sv.replace('<svg ', f'<svg style="width:{w}px;height:{w}px;display:block;margin:auto" ', 1)
def pf_bloco(nome, papel, cor, txt='#111'):
    return f'<div style="width:100%;height:100%;background:{cor};display:flex;flex-direction:column;justify-content:flex-end;padding:30px;border-radius:18px;color:{txt}"><div style="font:400 50px/1 Shrikhand">{nome}</div><div style="font:600 20px Work Sans;margin-top:10px">{papel}</div><div style="font:500 14px Work Sans;letter-spacing:.18em;text-transform:uppercase;opacity:.75;margin-top:16px">imagem do personagem a inserir</div></div>'
C['pagode'] = dict(
    nome='Pagode Fiado', sub='Ao vivo no Bar do Seu Tião', ano='2026',
    saida=P+'/agencia/pagode-fiado/brand-book',
    fonts='Shrikhand&family=Caveat+Brush&family=Permanent+Marker&family=Work+Sans:wght@400;500;600;700', disp="'Shrikhand'", body="'Work Sans'", mono="'Work Sans'", dw=400, up=False,
    bg='#1E6B52', bg2='#111111', fg='#F3E9D2', mut='#CFE0D6', ac='#F2B705', ac2='#C0392B', on_ac='#111111',
    logo=pf_logo(560), simbolo=None,
    versoes_html=[('Principal (no amarelo)', pf_logo(240), '#F2B705'), ('No verde azulejo', pf_logo(240), '#1E6B52'), ('No preto', pf_logo(240), '#111111'),
                  ('Uma cor (carimbo)', '<div style="font:400 64px/1 Caveat Brush;color:#C0392B;text-align:center">Pagode<div style="font:400 74px Permanent Marker;color:#111">FIADO</div></div>', '#F3E9D2'),
                  ('Avatar', '<div style="width:190px;height:190px;border-radius:50%;overflow:hidden">'+pf_logo(190)+'</div>', '#111111'),
                  ('Slogan', '<div style="font:400 54px Caveat Brush;color:#F3E9D2">Pendura na conta.</div>', '#C0392B')],
    conceito='Pendura na conta.', proposito='Seis amigos tocam toda sexta no Bar do Seu Tião, um boteco de esquina, até pagar a conta do fiado. Cada música é um lançamento no caderno.',
    essencia=['Emoção de pagode romântico', 'Humor de boteco', 'O caderno do fiado', 'Ao vivo no Bar do Seu Tião'],
    persona=['Quem ouve pagode romântico e sofrência.', '18 a 40 anos, sexta de resenha com os amigos.',
             'Dor: saudade, recaída, visualizou e não voltou.', 'Valoriza: letra que parece a vida dele, roda de samba, bar de esquina.',
             'Se reconhece no bar, na mesa amarela e no copo americano.'],
    antes='<div style="background:#F3E9D2;width:80%;padding:40px;border-radius:6px;background-image:repeating-linear-gradient(#F3E9D2 0 46px,#9DB8D9 46px 48px);font:400 40px/48px Caveat Brush;color:#111">Mesa 7 .......... 1 samba<br>Davi ........... 2 sofrência<br>Zé Pandeiro ... 1 causo<br><b style="color:#C0392B">Total: pendura!</b></div>',
    depois=pf_logo(470), lbl_antes='O OBJETO · CADERNO DO FIADO', lbl_depois='A MARCA',
    mudancas=[('O caderno do fiado vira o logo', 'círculo de papel pautado sobre o amarelo'), ('"Pagode" manuscrito em vermelho', 'a anotação do dono do bar'),
              ('"FIADO" em marcador grosso, sublinhado', 'a conta que ninguém paga'), ('O "O" é um copo americano', 'o objeto mais boteco do Brasil'),
              ('Cores do próprio bar', 'mesa amarela, toalha xadrez, azulejo verde')],
    protecao='A área livre em volta do logo é a altura do copo americano, nos quatro lados.', minimo=[('Digital', '96 px'), ('Avatar', '110 px (conferir no celular)'), ('Impresso', '25 mm')],
    paleta=[('Amarelo mesa de bar', '#F2B705', 35, 'fundo do logo, destaque'), ('Verde azulejo', '#1E6B52', 25, 'fundo'), ('Preto', '#111111', 20, 'texto, FIADO'),
            ('Creme caderno', '#F3E9D2', 12, 'papel, respiro'), ('Vermelho toalha', '#C0392B', 8, '"Pagode", xadrez')],
    tipos=[('Títulos (placa pintada)', 'Shrikhand', "'Shrikhand'", 400, 'Copo Americano'), ('Anotação', 'Caveat Brush', "'Caveat Brush'", 400, 'Pendura na conta.'),
           ('Marcador', 'Permanent Marker', "'Permanent Marker'", 400, 'FIADO'), ('Texto', 'Work Sans', "'Work Sans'", 400, 'Pagode de boteco direto do Bar do Seu Tião.')],
    elementos=[('Caderno pautado', 'fundo de lista de faixas e créditos'), ('Toalha xadrez vermelha', 'faixa de rodapé'), ('Azulejo verde', 'textura do balcão'),
               ('Varal de lâmpadas', 'luz quente no topo'), ('Quadro "FIADO"', 'placa com a música da semana')],
    elem_img='<div style="width:92%;height:92%;border-radius:18px;overflow:hidden;display:grid;grid-template-rows:1fr 110px"><div style="background:#1E6B52;background-image:linear-gradient(#ffffff22 2px,transparent 2px),linear-gradient(90deg,#ffffff22 2px,transparent 2px);background-size:90px 90px;display:grid;place-items:center"><div style="background:#111;border:10px solid #8B5A2B;padding:30px 50px;transform:rotate(-3deg);font:400 54px Permanent Marker;color:#F3E9D2;text-align:center">FIADO<div style="font:400 40px Caveat Brush;color:#F2B705">06 · Copo Americano</div></div></div><div style="background:repeating-conic-gradient(#C0392B 0 25%,#F3E9D2 0 50%) 0 0/55px 55px"></div></div>',
    fotos=[pf_bloco('Davi Lua', 'Vocal · romântico', '#F2B705'), pf_bloco('Neguinho do Cavaco', 'Cavaco · piadista', '#C0392B', '#F3E9D2'), pf_bloco('Bia Rebolo', 'Rebolo · forte e irônica', '#F3E9D2')],
    foto_regras=['Luz quente de lâmpada, grão de filme', 'Tons âmbar e verde', 'Mesa amarela, toalha xadrez, azulejo, varal', 'Personagens fictícios: não afirmar nem revelar IA'],
    voz=['Emoção e humor de boteco', 'Coloquial, de mesa de bar', 'Ficção sempre mantida'], faz=['"Pendura na conta."', '"Ao vivo no Bar do Seu Tião."'],
    nao=['Anunciar show real', 'Pedir PIX', 'Dizer que é IA ou que não é'],
    apps=[('<div style="width:100%;height:100%;background:#111;border-radius:18px;padding:40px;display:flex;flex-direction:column;justify-content:space-between"><div style="font:600 22px Work Sans;color:#F2B705">YOUTUBE · @PagodeFiado</div><div style="font:400 92px/1 Shrikhand;color:#F3E9D2">Copo<br>Americano</div><div style="font:400 40px Caveat Brush;color:#C0392B">ao vivo no Bar do Seu Tião</div></div>', 'Capa de vídeo'),
          ('<div style="width:100%;height:100%;background:#F2B705;border-radius:18px;padding:40px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px">'+pf_logo(300)+'<div style="font:700 26px Work Sans;color:#111">@pagodefiado</div><div style="font:500 20px Work Sans;color:#111;text-align:center">Pagode de boteco direto do Bar do Seu Tião<br>Pendura na conta</div></div>', 'Perfil Instagram e TikTok'),
          ('<div style="width:100%;height:100%;background:#F3E9D2;border-radius:18px;padding:36px;background-image:repeating-linear-gradient(#F3E9D2 0 40px,#9DB8D9 40px 42px);font:400 30px/42px Caveat Brush;color:#111"><div style="font:400 44px Shrikhand;color:#C0392B">Álbum 01</div>00 Mesa Sete<br>01 Sexta de Resenha<br>02 Maré Boa<br>03 Tantã do Coração<br>04 Recaída de Domingo<br>05 Bilhete na Geladeira<br><b style="color:#C0392B">06 Copo Americano</b><br>07 Visualizou e Não Voltou<br>08 Causo do Mestre Zé<br>09 Chorar Não, Sambar<br>10 Roda Até o Sol Raiar</div>', 'Lista de faixas'),
          (pf_bloco('Rafa Tantã', 'Tantã · calado e místico', '#1E6B52', '#F3E9D2'), 'Personagem'),
          ('<div style="width:100%;height:100%;border-radius:18px;background:#1E6B52;display:grid;place-items:center"><div style="width:560px;height:560px;background:#111;box-shadow:0 30px 60px #0008;display:grid;place-items:center;position:relative"><div style="position:absolute;inset:0;background:repeating-conic-gradient(#C0392B 0 25%,#F3E9D2 0 50%) 0 0/70px 70px;opacity:.9"></div><div style="position:relative;background:#F2B705;padding:30px;border-radius:50%">'+pf_logo(300)+'</div><div style="position:absolute;bottom:26px;font:400 50px Shrikhand;color:#111;background:#F3E9D2;padding:4px 24px">Copo Americano</div></div></div>', 'Capa do álbum 01'),
          (pf_bloco('Mestre Zé Pandeiro', 'Pandeiro · contador de causos', '#F2B705'), 'Personagem')],
    capa_foto=None, fecho='Pendura na conta.')

# ---------------------------------------------------------------- PÁGINAS
SEC = ['Essência', 'Persona', 'Rebranding', 'Logo', 'Versões', 'Proteção', 'Usos incorretos', 'Paleta', 'Tipografia', 'Elementos', 'Fotografia', 'Tom de voz', 'Aplicações']

def build(k):
    c = C[k]; e = html.escape
    up = 'uppercase' if c['up'] else 'none'
    serif = c.get('serif', c['disp'])
    bgimg = f"linear-gradient(135deg,{c['bg2']} 0%,{c['bg']} 70%)" if c.get('grad') else c['bg']
    css = f"""
@page{{size:1920px 1080px;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;font-family:{c['body']},sans-serif;color:{c['fg']}}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;background:{bgimg};page-break-after:always;padding:96px 120px}}
.pg:after{{content:'';position:absolute;inset:0;pointer-events:none;opacity:.07;background-image:url('{noise()}')}}
.top{{position:absolute;top:44px;left:120px;right:120px;display:flex;justify-content:space-between;font:500 17px {c['mono']},monospace;letter-spacing:.22em;text-transform:uppercase;color:{c['mut']};border-bottom:1px solid {c['fg']}22;padding-bottom:14px;z-index:3}}
.top b{{color:{c['ac']};font-weight:600}}
.num{{position:absolute;right:90px;bottom:-60px;font:{c['dw']} 520px/1 {c['disp']};color:{c['fg']};opacity:.06;letter-spacing:-.04em;z-index:0}}
h1{{font:{c['dw']} 104px/0.95 {c['disp']};letter-spacing:{'-.03em' if not c['up'] else '.005em'};text-transform:{up};margin-top:70px;max-width:1200px;position:relative;z-index:2}}
h1 em{{font-family:{serif};font-style:{'italic' if c.get('serif') else 'normal'};color:{c['ac']};font-weight:{400 if c.get('serif') else c['dw']}}}
.lead{{font-size:30px;line-height:1.4;color:{c['mut']};max-width:880px;margin-top:28px;position:relative;z-index:2}}
.lbl{{font:500 16px {c['mono']},monospace;letter-spacing:.2em;text-transform:uppercase;color:{c['ac']}}}
.card{{background:{c['bg2']};border:1px solid {c['fg']}18;border-radius:22px;padding:34px;position:relative;z-index:2}}
.grid{{display:grid;gap:28px;position:relative;z-index:2}}
.ph{{width:100%;height:100%;object-fit:cover;border-radius:18px;display:block}}
.cap{{font:500 15px {c['mono']},monospace;letter-spacing:.16em;text-transform:uppercase;color:{c['mut']};margin-top:12px}}
.x{{position:absolute;top:14px;right:14px;width:44px;height:44px;border-radius:50%;background:#E5484D;color:#fff;display:grid;place-items:center;font:700 26px sans-serif}}
"""
    pages = []
    n = [0]
    def page(title_lbl, body, num=None, extra=''):
        n[0] += 1
        num_html = f'<div class="num">{num}</div>' if num else ''
        pages.append(f'<section class="pg" style="{extra}"><div class="top"><span><b>{e(c["nome"])}</b> · Brand book</span><span>{title_lbl}</span><span>{n[0]:02d}</span></div>{num_html}{body}</section>')

    # 01 capa (Collins: tipo enorme sobre foto)
    page('Edição ' + c['ano'], f'''
{('<img src="'+f(c['capa_foto'])+'" style="position:absolute;right:0;top:0;width:58%;height:100%;object-fit:cover;opacity:.9">') if c['capa_foto'] else '<div style="position:absolute;right:0;top:0;width:58%;height:100%;background:repeating-conic-gradient('+c['ac2']+' 0 25%,'+c['fg']+' 0 50%) 0 0/120px 120px;opacity:.9"></div>'}
<div style="position:absolute;right:0;top:0;width:58%;height:100%;background:linear-gradient(90deg,{c['bg']} 0%,{c['bg']}00 45%)"></div>
<div style="position:relative;z-index:2;width:{c.get('capa_w',860)}px;margin-top:150px">{c['logo']}</div>
<div style="position:absolute;left:120px;bottom:110px;z-index:2"><div class="lbl">Brand book · manual da marca</div>
<div style="font:{c['dw']} 64px/1 {c['disp']};text-transform:{up};margin-top:18px;max-width:900px">{e(c['conceito'])}</div>
<div class="cap" style="margin-top:22px">{e(c['sub'])} · {c['ano']}</div></div>''')
    # 02 índice (NASA: lista numerada técnica)
    items = ''.join(f'<div style="display:flex;gap:26px;align-items:baseline;border-top:1px solid {c["fg"]}22;padding:16px 0"><span class="lbl">{i+3:02d}</span><span style="font:{c["dw"]} 40px {c["disp"]};text-transform:{up}">{s}</span></div>' for i, s in enumerate(SEC))
    page('Índice', f'<h1>O que tem<br><em>neste livro.</em></h1><div style="columns:2;column-gap:90px;margin-top:50px;position:relative;z-index:2;width:1500px">{items}</div>')
    # 03 essência
    ess = ''.join(f'<div class="card" style="border-top:6px solid {c["ac"]}"><div class="lbl">{i+1:02d}</div><div style="font:{c["dw"]} 40px/1.05 {c["disp"]};text-transform:{up};margin-top:18px">{e(x)}</div></div>' for i, x in enumerate(c['essencia']))
    page('Essência', f'<div class="lbl" style="margin-top:60px">Conceito</div><h1 style="margin-top:14px;font-size:132px">{e(c["conceito"])}</h1><p class="lead">{e(c["proposito"])}</p><div class="grid" style="grid-template-columns:repeat(4,1fr);margin-top:60px">{ess}</div>', '03')
    # 04 persona
    pl = ['Quem é', 'Rotina', 'Dor', 'Valoriza', 'Confia quando']
    per = ''.join(f'<div style="display:grid;grid-template-columns:260px 1fr;border-top:1px solid {c["fg"]}22;padding:20px 0"><span class="lbl">{pl[i]}</span><span style="font-size:30px;line-height:1.3">{e(x)}</span></div>' for i, x in enumerate(c['persona']))
    page('Persona', f'<div style="display:grid;grid-template-columns:600px 1fr;gap:90px;position:relative;z-index:2"><div><h1>Para quem<br><em>a marca fala.</em></h1><p class="lead">Toda peça passa pelo teste: essa pessoa compraria disso?</p></div><div style="margin-top:80px">{per}</div></div>', '04')
    # 05 rebranding
    mud = ''.join(f'<div style="border-top:1px solid {c["fg"]}22;padding:14px 0"><div style="font:700 25px {c["body"]}">{e(a)}</div><div style="font-size:21px;color:{c["mut"]};margin-top:4px">{e(b)}</div></div>' for a, b in c['mudancas'])
    def box(p, t, hl):
        return f'<div style="position:relative;height:620px;border-radius:22px;overflow:hidden;background:{c["bg2"]};border:{"3px solid "+c["ac"] if hl else "1px solid #ffffff22"}">{media(p, pad=24)}<div style="position:absolute;top:18px;left:18px;background:{c["ac"] if hl else "#00000099"};color:{c["on_ac"] if hl else "#fff"};font:600 18px {c["mono"]},monospace;letter-spacing:.18em;padding:8px 16px;border-radius:40px">{t}</div></div>'
    page('Rebranding', f'<h1 style="margin-top:50px;font-size:84px">Antes x depois:<br><em>o que mudou e por quê.</em></h1><div style="display:grid;grid-template-columns:1fr 1fr 640px;gap:30px;margin-top:40px;position:relative;z-index:2">{box(c["antes"],c.get("lbl_antes","ANTES"),0)}{box(c["depois"],c.get("lbl_depois","DEPOIS"),1)}<div>{mud}</div></div>', '05')
    # 06 logo (Pentagram: logo grande isolado)
    page('Logo', f'<div style="position:absolute;inset:0;display:grid;place-items:center;z-index:2"><div style="width:1000px">{c["logo"]}</div></div><div style="position:absolute;left:120px;bottom:90px;z-index:2"><div class="lbl">Assinatura principal</div><div style="font-size:24px;color:{c["mut"]};margin-top:10px;max-width:760px">Use esta versão sempre que houver espaço. O logo é arquivo fechado: nunca redesenhar, recolorir ou montar de novo.</div></div>', '06')
    # 07 versões
    if c.get('versoes_html'):
        vs = c['versoes_html']; cell = lambda v: v[1]
    else:
        vs = c['versoes']; cell = lambda v: v[1] if v[1].startswith('<') else f'<img src="{f(v[1])}" style="{"width:60%;" if v[1].endswith(".svg") else ""}max-width:82%;max-height:200px;object-fit:contain">'
    cols = 3 if len(vs) > 4 else 4
    vh = ''.join(f'<div><div style="height:{300 if cols==3 else 420}px;border-radius:20px;background:{v[2]};display:grid;place-items:center;border:1px solid #ffffff22;overflow:hidden">{cell(v)}</div><div class="cap">{e(v[0])}</div></div>' for v in vs)
    page('Versões', f'<h1 style="margin-top:50px;font-size:84px">Uma marca,<br><em>várias situações.</em></h1><div class="grid" style="grid-template-columns:repeat({cols},1fr);margin-top:44px">{vh}</div>', '07')
    # 08 proteção e mínimo
    mins = ''.join(f'<div style="border-top:1px solid {c["fg"]}22;padding:18px 0;display:flex;justify-content:space-between"><span style="font-size:26px">{e(a)}</span><span style="font:700 26px {c["mono"]},monospace;color:{c["ac"]}">{e(b)}</span></div>' for a, b in c['minimo'])
    page('Proteção', f'''<div style="display:grid;grid-template-columns:1fr 620px;gap:90px;position:relative;z-index:2;margin-top:60px">
<div style="height:760px;border:2px dashed {c['ac']};border-radius:8px;display:grid;place-items:center;position:relative;background:{c['bg2']}">
<div style="position:absolute;inset:90px;border:1px solid {c['ac']}66"></div>
<div style="width:620px;position:relative">{c['logo']}</div>
<span class="lbl" style="position:absolute;top:30px;left:50%;transform:translateX(-50%)">x</span><span class="lbl" style="position:absolute;bottom:30px;left:50%">x</span>
<span class="lbl" style="position:absolute;left:36px;top:50%">x</span><span class="lbl" style="position:absolute;right:36px;top:50%">x</span></div>
<div><h1 style="margin-top:0;font-size:80px">Respiro e<br><em>tamanho mínimo.</em></h1><p class="lead" style="font-size:26px">{e(c['protecao'])}</p><div style="margin-top:40px">{mins}</div><div class="cap" style="margin-top:14px">Recomendação técnica para leitura</div></div></div>''', '08')
    # 09 usos incorretos (Pentagram: grade 3x2 com X)
    base = c['logo'] if not c.get('simbolo') else f'<img src="{f(c["simbolo"])}" style="width:100%">'
    base = c['logo']
    wrong = [('Não distorcer', 'transform:scaleX(1.45)'), ('Não inclinar', 'transform:rotate(-14deg)'), ('Não trocar as cores', 'filter:hue-rotate(150deg) saturate(2)'),
             ('Sem sombra ou brilho', f'filter:drop-shadow(0 0 22px {c["ac"]}) drop-shadow(10px 10px 0 #E5484D)'), ('Sem contorno ou 3D', 'filter:blur(.6px) contrast(2) drop-shadow(4px 4px 0 #888)'),
             ('Não usar em fundo poluído', '')]
    wh = ''
    for t, st in wrong:
        bgw = (f"background:url('{f(c['capa_foto'])}') center/cover" if c['capa_foto'] else f"background:repeating-conic-gradient({c['ac2']} 0 25%,{c['fg']} 0 50%) 0 0/60px 60px") if not st else f'background:{c["bg2"]}'
        wh += f'<div><div style="height:300px;border-radius:20px;{bgw};display:grid;place-items:center;position:relative;overflow:hidden;border:1px solid #ffffff22"><div style="width:330px;{st}"><div style="zoom:.42;width:786px">{base}</div></div><div class="x">✕</div></div><div class="cap">{t}</div></div>'
    page('Usos incorretos', f'<h1 style="margin-top:46px;font-size:80px">O que <em>nunca</em> fazer.</h1><div class="grid" style="grid-template-columns:repeat(3,1fr);margin-top:36px;width:1380px">{wh}</div>', '09')
    # 10 paleta (Collins: faixas com proporção + Unimark: tabela)
    pal = c['paleta']; tot = sum(max(p[2], 3) for p in pal)
    bars = ''.join(f'<div style="flex:{max(p[2],3)};background:{p[1]};border-right:1px solid #00000022;position:relative"><span style="position:absolute;left:18px;bottom:18px;font:700 26px {c["mono"]},monospace;color:{"#000" if sum(rgb(p[1]))>380 else "#fff"}">{p[2] or "apoio"}{"%" if p[2] else ""}</span></div>' for p in pal)
    rows = ''.join(f'<div style="display:grid;grid-template-columns:60px 260px 170px 220px 240px 1fr;align-items:center;border-top:1px solid {c["fg"]}22;padding:13px 0;font:500 21px {c["mono"]},monospace"><span style="width:38px;height:38px;border-radius:50%;background:{p[1]};border:1px solid #ffffff44"></span><span style="font:700 23px {c["body"]}">{e(p[0])}</span><span>{p[1].upper()}</span><span>RGB {" ".join(map(str,rgb(p[1])))}</span><span>CMYK {" ".join(map(str,cmyk(p[1])))}</span><span style="color:{c["mut"]};font-family:{c["body"]}">{e(p[3])}</span></div>' for p in pal)
    page('Paleta', f'<h1 style="margin-top:46px;font-size:80px">Cores com <em>proporção.</em></h1><div style="display:flex;height:250px;border-radius:20px;overflow:hidden;border:1px solid #ffffff33;margin-top:34px;position:relative;z-index:2">{bars}</div><div style="margin-top:22px;position:relative;z-index:2">{rows}</div><div class="cap">CMYK convertido para referência; para gráfica, pedir prova de cor.</div>', '10')
    # 11 tipografia
    th = ''
    for role, fam, css_f, w, sample in c['tipos']:
        it = 'italic' if 'itálica' in fam or 'Instrument' in fam else 'normal'
        th += f'<div class="card" style="display:grid;grid-template-columns:330px 1fr;gap:30px;align-items:center;padding:28px 34px"><div><div class="lbl">{e(role)}</div><div style="font:700 26px {c["body"]};margin-top:8px">{e(fam)}</div><div class="cap">Google Fonts · peso {w}</div></div><div style="font:{it} {w} 50px/1.1 {css_f}">{e(sample)}</div></div>'
    page('Tipografia', f'<div style="display:grid;grid-template-columns:520px 1fr;gap:70px;position:relative;z-index:2"><div><h1 style="font-size:84px">Letras<br><em>da marca.</em></h1><div style="font:{c["dw"]} 260px/1 {c["tipos"][0][2]};margin-top:30px;color:{c["ac"]}">Aa</div></div><div class="grid" style="margin-top:70px;gap:22px">{th}</div></div>', '11')
    # 12 elementos
    if c['elementos']:
        el = ''.join(f'<div style="border-top:1px solid {c["fg"]}22;padding:18px 0"><div style="font:700 28px {c["body"]}">{e(a)}</div><div style="font-size:22px;color:{c["mut"]};margin-top:4px">{e(b)}</div></div>' for a, b in c['elementos'])
        page('Elementos', f'<div style="display:grid;grid-template-columns:620px 1fr;gap:70px;position:relative;z-index:2"><div><h1 style="font-size:84px">Elementos<br><em>gráficos.</em></h1><div style="margin-top:40px">{el}</div></div><div style="height:860px;margin-top:20px"><div style="height:100%;background:{c["bg2"]};border-radius:18px">{media(c["elem_img"])}</div></div></div>', '12')
    else:
        proib = ['Raios', 'Faixas', 'Ícones', 'Fumaça', 'Sol', 'Adesivo', 'Emoji', 'Balão no logo']
        ph = ''.join(f'<div class="card" style="text-align:center;padding:30px 10px"><div style="font:900 34px Montserrat;text-transform:uppercase">{p}</div><div class="x" style="position:static;margin:16px auto 0">✕</div></div>' for p in proib)
        page('Elementos', f'<h1 style="margin-top:50px">Sem grafismos.<br><em>Só fontes, logo e cores.</em></h1><p class="lead">Decisão de 02/11/2026. A força vem do retrato grande, do nome em blocos de cor e do degradê azul. Padrão aprovado: apresentação v13, versão 3.</p><div class="grid" style="grid-template-columns:repeat(4,1fr);margin-top:50px;width:1400px">{ph}</div>', '12')
    # 13 fotografia (Koto: regras ao lado das fotos)
    fr = ''.join(f'<div style="border-top:1px solid {c["fg"]}22;padding:16px 0;font-size:25px"><span class="lbl" style="margin-right:16px">{i+1:02d}</span>{e(x)}</div>' for i, x in enumerate(c['foto_regras']))
    fh = ''.join(f'<div style="height:860px;background:{c["bg2"]};border-radius:18px;overflow:hidden">{media(p, "contain" if p.endswith(".png") else "cover")}</div>' for p in c['fotos'])
    page('Fotografia', f'<div style="display:grid;grid-template-columns:560px 1fr;gap:60px;position:relative;z-index:2"><div><h1 style="font-size:84px">Fotografia<br><em>de verdade.</em></h1><div style="margin-top:40px">{fr}</div></div><div class="grid" style="grid-template-columns:repeat({len(c["fotos"])},1fr);gap:20px;margin-top:20px">{fh}</div></div>', '13')
    # 14 tom de voz (Collins: bloco de cor cheia)
    vz = ''.join(f'<div style="font:{c["dw"]} 54px/1.05 {c["disp"]};text-transform:{up};border-top:2px solid {c.get("voz_fg", c["on_ac"])}33;padding:18px 0">{e(x)}</div>' for x in c['voz'])
    fz = ''.join(f'<div style="font-size:26px;padding:10px 0">{e(x)}</div>' for x in c['faz'])
    nz = ''.join(f'<div style="font-size:26px;padding:10px 0">✕ {e(x)}</div>' for x in c['nao'])
    page('Tom de voz', f'<div style="display:grid;grid-template-columns:1fr 640px;gap:80px;position:relative;z-index:2;color:{c.get("voz_fg", c["on_ac"])}"><div><h1 style="font-size:96px;color:{c.get("voz_fg", c["on_ac"])}">Como a marca fala.</h1><div style="margin-top:40px">{vz}</div></div><div style="margin-top:90px"><div class="lbl" style="color:{c.get("voz_fg", c["on_ac"])}">Fala assim</div>{fz}<div class="lbl" style="color:{c.get("voz_fg", c["on_ac"])};margin-top:40px">Nunca</div>{nz}</div></div>', '14', f'background:{c.get("voz_bg", c["ac"])}')
    # 15-16 aplicações
    ap = c['apps']
    a1 = ''.join(f'<div><div style="height:640px;border-radius:18px;overflow:hidden;background:{c["bg2"]}">{media(p)}</div><div class="cap">{e(t)}</div></div>' for p, t in ap[:3])
    page('Aplicações', f'<h1 style="margin-top:40px;font-size:80px">A marca <em>no mundo.</em></h1><div class="grid" style="grid-template-columns:repeat(3,1fr);margin-top:34px">{a1}</div>', '15')
    a2 = ''.join(f'<div><div style="height:{760}px;border-radius:18px;overflow:hidden;background:{c["bg2"]}">{media(p)}</div><div class="cap">{e(t)}</div></div>' for i, (p, t) in enumerate(ap[3:6]))
    page('Aplicações', f'<div class="grid" style="grid-template-columns:1fr 1.5fr 1fr;margin-top:50px">{a2}</div>', '16')
    # 17 contracapa
    page('Contracapa', f'<div style="position:absolute;inset:0;display:grid;place-items:center;text-align:center;z-index:2"><div><div style="width:640px;margin:0 auto">{c["logo"]}</div><div style="font:{c["dw"]} 70px/1 {c["disp"]};text-transform:{up};margin-top:70px;color:{c["ac"]}">{e(c["fecho"])}</div><div class="cap" style="margin-top:40px">Brand book {c["ano"]} · design: Lindson Almeida · São Luís · MA</div></div></div>')

    return f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family={c["fonts"]}&display=swap" rel="stylesheet"><style>{css}</style></head><body>{"".join(pages)}</body></html>'

CHECK = """()=>{const r=[];document.querySelectorAll('.pg').forEach((pg,i)=>{const b=pg.getBoundingClientRect();
pg.querySelectorAll('h1,.lead,.card,.cap,.lbl,img').forEach(el=>{if(el.closest('.num'))return;const q=el.getBoundingClientRect();
if(q.width&&(q.bottom>b.bottom+2||q.right>b.right+2)&&!el.style.position.includes('absolute')&&getComputedStyle(el).position!='absolute')r.push([i+1,el.tagName,el.className,Math.round(q.bottom-b.top),Math.round(q.right-b.left)])})});
document.querySelectorAll('img').forEach(im=>{if(!im.naturalWidth)r.push(['img quebrada',im.src])});return r}"""

def render(k):
    from playwright.sync_api import sync_playwright
    c = C[k]; os.makedirs(c['saida'], exist_ok=True)
    hp = os.path.join(SCR, k + '.html'); open(hp, 'w').write(build(k))
    with sync_playwright() as pw:
        b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
        p = b.new_page(viewport={'width': 1920, 'height': 1080})
        p.goto('file://' + hp, wait_until='networkidle'); p.evaluate('document.fonts.ready'); p.wait_for_timeout(600)
        print(k, 'problemas:', p.evaluate(CHECK))
        pdf = os.path.join(c['saida'], f'brand-book-{k}.pdf')
        p.pdf(path=pdf, width='1920px', height='1080px', print_background=True)
        shots = []
        for i, el in enumerate(p.query_selector_all('.pg')):
            sp = os.path.join(SCR, f'{k}-{i+1:02d}.png'); el.screenshot(path=sp); shots.append(sp)
        b.close()
    # folha de contato 4 colunas
    W, H = 480, 270; cols = 4; rows = (len(shots)+cols-1)//cols
    sheet = Image.new('RGB', (cols*W+(cols+1)*12, rows*H+(rows+1)*12), (20, 20, 20))
    for i, s in enumerate(shots):
        im = Image.open(s).convert('RGB').resize((W, H), Image.LANCZOS)
        sheet.paste(im, (12+(i % cols)*(W+12), 12+(i//cols)*(H+12)))
    sheet.save(os.path.join(c['saida'], 'previa-folha.jpg'), quality=85)
    Image.open(shots[0]).convert('RGB').save(os.path.join(c['saida'], 'previa-capa.jpg'), quality=85)
    print(pdf, os.path.getsize(pdf)//1024, 'KB')

if __name__ == '__main__':
    os.makedirs(SCR, exist_ok=True)
    ks = list(C) if sys.argv[1:] in ([], ['todos']) else sys.argv[1:]
    for k in ks: render(k)
