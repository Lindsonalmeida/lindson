# Manual da logo da Desentupidora SF (1920x1080 por página). Gera manual.html; o PDF sai pelo pdf.js.
import os
D=os.path.dirname(os.path.abspath(__file__))
A='../arquivos/svg/';P='../arquivos/png/';O='../arquivos/original/';I='../../img/'
NAVY='#061a4a';NAVY2='#0a2a6e';ROYAL='#1d5fd0';SKY='#3fa9ff';OR='#ff8a00';OFF='#f4f8ff'
def cmyk(h):
    r,g,b=[int(h[i:i+2],16)/255 for i in (1,3,5)];k=1-max(r,g,b)
    if k>=1: return '0 · 0 · 0 · 100'
    return ' · '.join(str(round(100*x)) for x in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def rgb(h): return ' · '.join(str(int(h[i:i+2],16)) for i in (1,3,5))
pages=[];N=[0]
def page(body,cls='',num=True):
    N[0]+=1;n=f'<div class="pn">{N[0]:02d}</div>' if num else ''
    pages.append(f'<section class="pg {cls}">{body}{n}<div class="ft">DESENTUPIDORA SF · MANUAL DA MARCA</div></section>')
def head(k,t,s=''):
    return f'<div class="k">{k}</div><h1>{t}</h1>'+(f'<p class="lead">{s}</p>' if s else '')

# 1 capa
pages.append(f'''<section class="pg capa"><div class="glow"></div><img class="cs" src="{A}simbolo-negativa.svg">
<div class="ct"><div class="k o">MANUAL DA MARCA · 2026</div><h1 class="big">A logo da<br>Desentupidora SF</h1>
<p class="lead w">Símbolo, assinaturas, cores, versões e regras de uso.<br>Tudo para a marca sair igual em qualquer lugar: farda, carro, Instagram e papel.</p></div>
<img class="cl" src="{A}horizontal-negativa.svg"></section>''')
# 2 sumário
items=['A ideia','A logo original em alta','O símbolo, parte por parte','Construção','Assinatura principal','Família de assinaturas','Cores','Tipografia','Versões de cor','Área de proteção e tamanho mínimo','Fundos','O que não fazer','Aplicações','Arquivos entregues']
page(head('SUMÁRIO','O que tem aqui')+'<ol class="sum">'+''.join(f'<li><b>{i+2:02d}</b>{t}</li>' for i,t in enumerate(items))+'</ol>')
# 3 ideia
page(f'''<div class="two"><div>{head('01 · A IDEIA','Proteção que faz a água correr de novo','Quem chama uma desentupidora está com a casa ou o comércio parado: pia, ralo, vaso ou caixa de gordura. Essa pessoa quer três coisas: que resolva, que seja limpo e que dê para confiar em quem entra na casa dela.')}
<p class="txt">A logo responde a isso com quatro sinais simples:</p>
<ul class="lst"><li><b>Escudo</b> · segurança e confiança: técnico de farda, serviço com responsabilidade.</li><li><b>Gota</b> · o assunto da empresa: água e esgoto.</li><li><b>Onda</b> · o cano liberado, a água voltando a correr.</li><li><b>SF em itálico</b> · rapidez e movimento: chega, resolve, testa na hora.</li></ul></div>
<div class="art navy"><img src="{A}simbolo-colorida.svg" style="width:62%"></div></div>''')
# 4 original
page(f'''<div class="two"><div>{head('02 · A LOGO ORIGINAL','A mesma logo, agora em alta qualidade','A logo que a SF já usa foi mantida igual. O arquivo antigo tinha 512 px e borrava em impressão. Ele foi reconstruído com IA de super-resolução para 2048 e 4096 px, com versão de fundo transparente.')}
<ul class="lst"><li><b>Use para:</b> foto de perfil, adesivo grande, banner e qualquer lugar onde o selo cheio, com brilho, fica bonito.</li><li><b>Não use para:</b> bordado, carimbo, gravação ou tamanhos pequenos. Ali entra a versão plana das próximas páginas.</li></ul>
<div class="cmp"><div><img src="{I}logo.jpg" class="px"><span>ANTES · 512 px</span></div><div><img src="{O}logo-original-2048.png"><span>AGORA · 4096 px</span></div></div></div>
<div class="art light"><img src="{O}logo-original-transparente-2048.png" style="width:78%"></div></div>''')
# 5 anatomia
page(f'''{head('03 · O SÍMBOLO','Parte por parte','Para funcionar em bordado, adesivo e ícone, o selo foi desenhado de novo em versão plana (vetor), com os mesmos elementos da logo original e menos detalhes.')}
<div class="anat"><img src="{A}simbolo-colorida.svg">
<div class="lb" style="left:1380px;top:340px"><i></i><b>Gota</b>água, o assunto da empresa</div>
<div class="lb" style="left:1380px;top:500px"><i></i><b>Escudo prata</b>confiança e segurança</div>
<div class="lb" style="left:1380px;top:660px"><i></i><b>SF em itálico</b>rapidez, movimento</div>
<div class="lb" style="left:1380px;top:820px"><i></i><b>Onda</b>o cano liberado</div></div>''')
# 6 construção
grid=''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="420" />' for x in range(0,401,20))+''.join(f'<line x1="0" y1="{y}" x2="400" y2="{y}" />' for y in range(0,421,20))
page(f'''<div class="two"><div>{head('04 · CONSTRUÇÃO','Desenhado numa grade de 20 × 21 módulos','O escudo é simétrico no eixo do meio. A gota fica no centro do topo e passa um módulo acima do escudo. A onda atravessa o terço de baixo e sai pelos dois lados, dando a ideia de movimento.')}
<ul class="lst"><li><b>Módulo x</b> = 1/20 da largura do símbolo.</li><li>Escudo: 14 x de largura · gota: 3,6 x · onda: 18,3 x.</li><li>Letras SF: Montserrat Black Italic, altura de 5,3 x.</li></ul></div>
<div class="art light"><div class="gwrap"><svg viewBox="0 0 400 420" class="grid"><g stroke="#3fa9ff" stroke-width=".6" opacity=".45">{grid}</g>
<line x1="200" y1="0" x2="200" y2="420" stroke="#ff8a00" stroke-width="1.5" stroke-dasharray="6 5"/><line x1="0" y1="282" x2="400" y2="282" stroke="#ff8a00" stroke-width="1.5" stroke-dasharray="6 5"/>
<circle cx="200" cy="70" r="36" fill="none" stroke="#ff8a00" stroke-width="1.5"/></svg><img src="{A}simbolo-mono-azul.svg" style="opacity:.9"></div></div></div>''')
# 7 principal
page(f'''{head('05 · ASSINATURA PRINCIPAL','Horizontal, colorida','É a versão que vem primeiro em tudo: site, cabeçalho de PDF, assinatura de e-mail, cartão, lateral do carro. O nome inteiro, "DESENTUPIDORA SF", com o SF em laranja, a cor de ação da marca.')}
<div class="hero"><img src="{A}horizontal-colorida.svg"></div>''')
# 8 família
fam=[('horizontal-colorida','Horizontal','principal · site, PDF, carro',''),('vertical-colorida','Vertical','espaços altos · cartaz, story, costas da farda',''),('simbolo-colorida','Símbolo','peito da farda, boné, selo, marca d’água',''),('selo-colorido','Selo','adesivo, carimbo, embalagem',''),('icone-perfil','Ícone de perfil','Instagram, WhatsApp, Google',''),('favicon','Favicon','aba do site, app, tamanhos mínimos','')]
page(head('06 · FAMÍLIA','Uma assinatura para cada espaço')+'<div class="fam">'+''.join(f'<div class="fc"><div class="fi"><img src="{A}{f}.svg"></div><b>{t}</b><span>{s}</span></div>' for f,t,s,_ in fam)+'</div>')
# 9 cores
cores=[('Azul Noite',NAVY,'fundo principal, textos, farda'),('Azul Royal',ROYAL,'letras SF, botões, destaques'),('Azul Céu',SKY,'água, onda, brilhos'),('Laranja Ação',OR,'o "SF" do nome, chamadas, botões de WhatsApp'),('Branco Gelo',OFF,'fundos claros, respiro')]
page(head('07 · CORES','Azul da água, laranja da ação','O azul vem da água e da confiança. O laranja aparece pouco, só para chamar a ação (o SF do nome, um botão, uma faixa). Proporção de uso: 60 · 25 · 10 · 5.')+'<div class="cores">'+''.join(f'<div class="cor" style="background:{h};color:{"#061a4a" if h in (OFF,SKY,OR) else "#fff"};flex:{fl}"><b>{n}</b><span>HEX {h.upper()}</span><span>RGB {rgb(h)}</span><span>CMYK {cmyk(h)}</span><em>{u}</em></div>' for (n,h,u),fl in zip(cores,(3,2,1.6,1.4,1.4)))+'</div>')
# 10 tipografia
page(f'''{head('08 · TIPOGRAFIA','Montserrat, em duas forças')}
<div class="typ"><div><div class="ty" style="font-family:MBI">Aa</div><b>Montserrat Black Italic</b><span>nome da marca, títulos, chamadas</span><div class="ab" style="font-family:MBI">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>0123456789</div></div>
<div><div class="ty" style="font-family:MB">Aa</div><b>Montserrat Bold</b><span>apoio, textos, legendas, assinaturas · com espaço entre letras</span><div class="ab" style="font-family:MB;letter-spacing:.12em">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>0123456789</div></div></div>
<p class="txt">Gratuita (Google Fonts). Na logo, os textos já estão convertidos em curva: o arquivo abre igual em qualquer computador, gráfica ou bordadeira.</p>''')
# 11 versões
ver=[('colorida','Colorida','#fff','em fundos claros'),('negativa','Negativa',NAVY,'em fundos azul-noite'),('mono-azul','Uma cor · azul','#fff','bordado de 1 cor, carimbo'),('mono-branca','Uma cor · branca',ROYAL,'sobre foto escura ou azul'),('preta','Preta','#fff','documentos, nota, fax, gravação')]
page(head('09 · VERSÕES DE COR','A mesma logo em cinco situações')+'<div class="vers">'+''.join(f'<div class="vc"><div class="vi" style="background:{b}"><img src="{A}simbolo-{f}.svg"><img src="{A}horizontal-{f}.svg" class="vh"></div><b>{t}</b><span>{s}</span></div>' for f,t,b,s in ver)+'</div>')
# 12 proteção
page(f'''<div class="two"><div>{head('10 · ÁREA DE PROTEÇÃO','Deixe a logo respirar','Em volta da logo, nenhum texto, foto ou borda pode entrar no espaço de uma gota (medida X). Isso faz a marca parecer firme e cara, não espremida.')}
<div class="mins"><div><img src="{A}horizontal-colorida.svg" style="height:40px"><b>Horizontal · mínimo 40 mm / 160 px</b></div><div><img src="{A}simbolo-colorida.svg" style="height:56px"><b>Símbolo · mínimo 12 mm / 48 px</b></div><div><img src="{A}favicon.svg" style="height:32px"><b>Abaixo disso · favicon</b></div></div></div>
<div class="art light"><div class="prot"><img src="{A}vertical-colorida.svg"><span class="x t">X</span><span class="x b">X</span><span class="x l">X</span><span class="x r">X</span></div></div></div>''')
# 13 fundos
page(head('11 · FUNDOS','Onde a logo pode entrar')+f'''<div class="fund">
<div class="fd ok" style="background:#fff"><img src="{A}horizontal-colorida.svg"><span>Branco · colorida</span></div>
<div class="fd ok" style="background:{NAVY}"><img src="{A}horizontal-negativa.svg"><span>Azul-noite · negativa</span></div>
<div class="fd ok" style="background:{ROYAL}"><img src="{A}horizontal-mono-branca.svg"><span>Azul royal · branca</span></div>
<div class="fd ok foto" style="background-image:linear-gradient(rgba(6,26,74,.72),rgba(6,26,74,.72)),url({I}caixa-esgoto.jpg)"><img src="{A}horizontal-mono-branca.svg"><span>Foto · com véu azul de 70%</span></div>
<div class="fd ok" style="background:{OFF}"><img src="{A}horizontal-mono-azul.svg"><span>Branco gelo · uma cor azul</span></div>
<div class="fd ok" style="background:{OR}"><img src="{A}horizontal-mono-branca.svg"><span>Laranja · só branca, só em faixa ou botão</span></div></div>''')
# 14 incorretos
bad=[('transform:scaleX(1.45)','Não esticar nem achatar'),('transform:rotate(-14deg)','Não girar'),('filter:hue-rotate(150deg)','Não trocar as cores'),('filter:drop-shadow(10px 12px 6px rgba(0,0,0,.7))','Não pôr sombra nem efeito'),('opacity:.35','Não usar apagada'),('', 'Não pôr sobre fundo confuso')]
page(head('12 · O QUE NÃO FAZER','Seis erros que enfraquecem a marca')+'<div class="bad">'+''.join(f'<div class="bd"><div class="bi" {"style=\"background-image:url("+I+"flyer.jpg);background-size:cover\"" if not c else ""}><img src="{A}horizontal-colorida.svg" style="{c}"><i>✕</i></div><span>{t}</span></div>' for c,t in bad)+'</div>')
# 15 aplicações
page(head('13 · APLICAÇÕES','A marca no dia a dia')+f'''<div class="apl">
<div class="ap a1" style="background-image:url({I}farda-frente-costas.png)"><span>Farda · símbolo no peito, vertical nas costas</span></div>
<div class="ap a2" style="background-image:url({I}veiculo-van.png)"><span>Carro · horizontal na lateral</span></div>
<div class="ap a3"><div class="ig"><img src="{A}icone-perfil.svg"><div><b>desentupidorasf_slz</b><small>Desentupidora SF · São Luís</small></div></div><span>Perfil · ícone</span></div>
<div class="ap a4"><div class="card"><img src="{A}horizontal-negativa.svg"><small>(98) 92010-5710 · desentupidorasf.pages.dev</small></div><span>Cartão de visita · negativa</span></div></div>''')
# 16 arquivos
page(f'''<div class="two"><div>{head('14 · ARQUIVOS','O que foi entregue','Pasta "arquivos", pronta para mandar para gráfica, bordadeira, adesivista ou site.')}
<ul class="lst files"><li><b>original/</b> a logo original em 2048 e 4096 px, com e sem fundo (PNG e JPG).</li>
<li><b>svg/</b> vetor de todas as versões: abre no Illustrator, Corel, Canva e Figma, e amplia sem perder qualidade. É o arquivo para bordado, adesivo e fachada.</li>
<li><b>png/</b> todas as versões em PNG transparente, em alta.</li></ul>
<p class="txt">Na dúvida, mande o <b>SVG</b> para a gráfica e use o <b>PNG</b> no celular.</p></div>
<div class="art navy"><img src="{A}vertical-negativa.svg" style="width:58%"></div></div>''',num=True)

css=open(os.path.join(D,'manual.css')).read()
open(os.path.join(D,'manual.html'),'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Manual da Logo · Desentupidora SF</title><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print(len(pages),'páginas')
