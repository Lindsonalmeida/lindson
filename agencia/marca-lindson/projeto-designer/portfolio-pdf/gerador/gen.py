# Portfólio PDF luxo · Lindson Almeida. Composição: The Row (imagem enorme + legenda mínima),
# Lemaire (grid editorial com nota em sans miúda), Collins (frase serifada sobre marfim).
P=[];n=[0]
def page(body,cls=""):
  n[0]+=1;P.append(f'<section class="pg {cls}">{body}<div class="folio"><span>Lindson Almeida</span><span>{n[0]:02d}</span></div></section>')
def lab(t):return f'<div class="lab">{t}</div>'
page('''<div class="cimg"><img src="img/rt-hero.jpg"></div>
<div class="cv"><div class="lab l">Portfólio · 2026</div><h1>Marcas que<br><i>se reconhecem</i><br>de longe.</h1>
<div class="sig">LINDSON ALMEIDA<span>Studio · São Luís, Maranhão</span></div></div>''','ivory')
page('''<div class="man">'''+lab('Manifesto')+'''<p class="big">Uma marca não é um logo.<br>É a soma de cada decisão<br><i>que o cliente consegue ver.</i></p>
<p class="small">Trabalho para que o negócio local pareça, em cada tela, aquilo que ele já é por dentro: sério, cuidadoso e pronto para cobrar o que vale. Pouca coisa, muito bem feita. Mesmo sistema em todos os canais, para gerar conexão.</p><div class="acc"></div></div>''','ivory')
page('''<div class="split"><div class="col">'''+lab('Sobre')+'''<h2>Lindson<br><i>Almeida</i></h2>
<p>Há 14 anos com gestão de marketing e redes sociais. Do posicionamento à última peça publicada, junto estratégia, design e venda num só lugar.</p>
<ul class="svc"><li>Identidade visual</li><li>Sites e mini sites</li><li>Social media</li><li>Vídeo e motion</li><li>Tráfego pago</li></ul></div>
<div class="img"><img src="img/or-papelaria.jpg"></div></div>''','ivory')
cases=[("Al Kántara Group","Identidade de holding"),("Real Time","Rebranding audiovisual"),("WF Celulares","Loja de iPhone"),("Processo Legislativo","Curso para câmaras"),("Leo Pinto","Comunicação pública"),("Orégano Turbo","Marketing para pizzarias"),("Dublê","App de voz"),("Dra. Jaci Cunha","Clínica de harmonização"),("Rafael Imports","Mini site"),("Desentupidora SF","Site e Instagram"),("Tribuna 98","Portal de notícias")]
idx="".join(f'<li><span class="nr">{i+1:02d}</span><span class="nm">{a}</span><span class="ds">{b}</span></li>' for i,(a,b) in enumerate(cases))
page(f'<div class="idx">{lab("Índice")}<h2>Seleção<br><i>de trabalhos</i></h2><ol>{idx}</ol></div>','ivory')
def case(i,name,sub,hero,desafio,solucao,entregas,imgs,url="",dark=True):
  page(f'<img class="full" src="img/{hero}"><div class="cap"><span>{i:02d}</span>{name}<em>{sub}</em></div>','dark' if dark else 'ivory')
  g="".join(f'<div class="g"><img src="img/{x}"></div>' for x in imgs)
  ent="".join(f"<li>{e}</li>" for e in entregas)
  u=f'<div class="url">{url}</div>' if url else ''
  page(f'''<div class="cs"><div class="txt"><div class="lab">{i:02d} · {sub}</div><h3>{name}</h3>
<h4>Desafio</h4><p>{desafio}</p><h4>Solução</h4><p>{solucao}</p><h4>Entregas</h4><ul>{ent}</ul>{u}</div>
<div class="gal n{len(imgs)}">{g}</div></div>''','ivory')
case(1,"Al Kántara Group","Identidade de holding","ak1.jpg","Um grupo com várias frentes precisava de uma marca-mãe que segurasse todas sem apagar nenhuma.","Conceito da pedra-chave: a peça que sustenta o arco vira o K. Preto, dourado e serifa editorial; cada sub-marca é uma pedra do mesmo arco.",["Plataforma e personas","Símbolo com grid de construção","Arquitetura de sub-marcas","Brand book e manual","Logo animado"],["ak3.jpg","akg.jpg"])
case(2,"Real Time","Rebranding audiovisual","rt-hero.jpg","Uma produtora com equipamento de cinema e uma marca que não mostrava isso.","“No ar, agora.” O símbolo vira um visor de câmera [rt]; preto e azul elétrico e a linguagem do timecode.",["Símbolo e wordmark","Paleta e tipografia","Tom de voz","Site","Brand book"],["rt-outdoor.jpg","rtd.jpg"],"realtimeslz.pages.dev")
case(3,"WF Celulares","Loja de iPhone","wf-poster.jpg","Produto premium vendido com visual de promoção de bairro.","“Procedência que dá para ver.” Preto, prata e branco, muito respiro e o produto no centro, como as marcas que a loja vende.",["Logo e versões","Fotografia","Painel fixado do Instagram","Mini site","Brand book"],["wf-papelaria.jpg","wfd.jpg"],"wfcelulares.pages.dev")
case(4,"Processo Legislativo","Curso para câmaras","cu-outdoor.jpg","Conteúdo técnico e sério com cara de improviso nas redes.","“Chega de improviso na câmara.” Verde institucional e dourado, serifa elegante e um símbolo que lembra o plenário.",["Logo e paleta","Tipografia","Perfil do Instagram","Site","Brand book"],["cud.jpg","cu-celular.jpg"],"cursoprocessolegislativo.pages.dev")
case(5,"Leo Pinto","Comunicação pública","leo-hero.jpg","Cada peça usava um recurso diferente e a marca não era lembrada.","Tirar tudo o que sobrava: só fontes, logo e cores. O sol no “O” de LEO vira a assinatura, com proporção de cor definida.",["Logo e monograma","Paleta com proporção","Tipografia","Manual de 17 páginas","Feed e datas"],["leo1.jpg","leo2.jpg"])
case(6,"Orégano Turbo","Marketing para pizzarias","or-hero.jpg","Falar com dono de pizzaria com seriedade, sem cair no selo lúdico.","“Uma folha que sobe.” A folha de orégano vira crescimento; tomate, verde e creme, a comanda como elemento e a pizza real como protagonista.",["Logo e versões","Sistema da comanda","Fotografia","Site","Brand book"],["or1.jpg","or-embalagem.jpg"])
case(7,"Dublê","App de voz","du-hero.jpg","Uma tecnologia sensível, a voz, que precisava parecer confiável e simples.","“Só grava quem disse sim.” Grafite e violeta, onda sonora dentro de um círculo e linguagem direta sobre consentimento.",["Nome e símbolo","Interface","Paleta e tipografia","Tom de voz","Brand book"],["du-celular.jpg","du-poster.jpg"])
page('''<div class="cs"><div class="txt"><div class="lab">08 · Clínica de harmonização</div><h3>Dra. Jaci Cunha</h3>
<h4>Desafio</h4><p>Traduzir delicadeza e técnica numa marca de clínica, dentro das regras do conselho.</p>
<h4>Solução</h4><p>Bordô, vinho, dourado e rosé; serifa itálica com sans discreta e o monograma JC com perfil. Assinatura fixa em todas as peças.</p>
<h4>Entregas</h4><ul><li>Manual de identidade</li><li>Site</li><li>Feed e carrosséis</li></ul><div class="url">drajacicunha.pages.dev</div></div>
<div class="gal n3"><div class="g"><img src="img/jaci1.jpg"></div><div class="g"><img src="img/jacis.jpg"></div><div class="g"><img src="img/jaci2.jpg"></div></div></div>''','ivory')
def site(i,name,sub,d,m,txt,ent,url):
  page(f'''<div class="st"><div class="lap"><img src="img/{d}"></div><div class="ph"><img src="img/{m}"></div>
<div class="sttx"><div class="lab">{i:02d} · {sub}</div><h3>{name}</h3><p>{txt}</p><p class="ent">{ent}</p><div class="url">{url}</div></div></div>''','ivory')
site(9,"Rafael Imports","Mini site","rafd.jpg","raf.jpg","Celulares, acessórios e assistência. Um mini site no link da bio que leva direto para o WhatsApp certo: loja, assistência, produtos e localização.","Mini site · identidade aplicada · botões de WhatsApp","rafaelimports.pages.dev")
site(10,"Desentupidora SF","Site e Instagram","sfd.jpg","sfm.jpg","Serviço de urgência pede clareza: o que faz, onde atende e um botão para pedir orçamento pelo WhatsApp, com foto real de quem atende.","Site · feed do Instagram · vídeos","desentupidorasf.pages.dev")
site(11,"Tribuna 98","Portal de notícias","trd.jpg","trm.jpg","Jornalismo político do Maranhão com uma promessa editorial simples: informação com fonte. Manchete condensada, azul profundo e amarelo de destaque.","Site · editorias · destaques do Instagram","tribuna98.pages.dev")
steps=[("Escuta","Conversa, briefing e persona: quem compra e o que faz confiar."),("Pesquisa","Referências premiadas de vários países e o concorrente da esquina."),("Conceito","Uma ideia forte, com significado, que atravessa tudo."),("Sistema","Logo e versões, cores com proporção, letras e grafismos."),("Aplicação","Peças reais: site, Instagram, papelaria, vídeo."),("Entrega","Brand book, arquivos e acompanhamento.")]
st="".join(f'<div class="stp"><span>{i+1:02d}</span><h5>{a}</h5><p>{b}</p></div>' for i,(a,b) in enumerate(steps))
page(f'<div class="proc">{lab("Processo")}<h2>Seis etapas,<br><i>nenhum improviso.</i></h2><div class="steps">{st}</div></div>','ivory')
sv=[("Identidade visual","Conceito, logo, cores, tipografia e brand book."),("Sites","Sites, landing pages e mini sites de bio."),("Social media","Linha editorial, calendário, artes e legendas."),("Vídeo","Reels, motion e vídeos com narração."),("Tráfego","Campanhas de anúncio e acompanhamento.")]
s="".join(f'<li><h5>{a}</h5><p>{b}</p></li>' for a,b in sv)
page(f'<div class="split"><div class="img"><img src="img/cu-papelaria.jpg"></div><div class="col">{lab("Serviços")}<h2>O que<br><i>eu faço</i></h2><ul class="sv">{s}</ul></div></div>','ivory')
page('''<div class="cimg"><img src="img/du-poster.jpg"></div><div class="ct"><div class="lab l">Contato</div><h1>Vamos<br><i>conversar.</i></h1>
<div class="cl"><p><span>Instagram</span>@lindsonalmeida_</p><p><span>Site</span>lindsonalmeida.pages.dev/site/</p></div><div class="sig">LINDSON ALMEIDA<span>Studio · São Luís, Maranhão</span></div></div>''','ivory')
css=open('style.css').read()
open('portfolio.html','w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Lindson Almeida · Portfólio</title><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet"><style>{css}</style></head><body>{"".join(P)}</body></html>')
print(n[0])
