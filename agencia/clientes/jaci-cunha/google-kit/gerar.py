# Gera kit.html (páginas 4:5, 1080x1350) na identidade da Jaci; PDF: node pdf.js kit.html Kit-Google-Dra-Jaci.pdf
import os, html
from conteudo import *
D = os.path.dirname(os.path.abspath(__file__))
e = html.escape
pg = []
def page(body, cls='', n=True):
    pg.append(f'<section class="pg {cls}">{body}<footer><span>DRA. JACI CUNHA · CRO-MA 8514</span><span>PERFIL NO GOOGLE</span>{f"<b>{len(pg)+1:02d}</b>" if n else ""}</footer></section>')
def head(k, t, s=''):
    return f'<div class="k">{k}</div><h1>{t}</h1>' + (f'<p class="lead">{s}</p>' if s else '')

pg.append(f'''<section class="pg capa"><img class="mono" src="monograma.jpg">
<div class="ct"><div class="k d">KIT PRONTO · NOVEMBRO 2026</div><h1 class="big">Sua clínica<br><em>no Google</em></h1>
<p class="lead w">Tudo para o Perfil da Empresa no Google da Dra. Jaci Cunha: a ficha preenchida, 8 posts, perguntas e respostas, respostas às avaliações e a rotina do mês.</p></div>
<div class="assin">DRA. JACI CUNHA<small>HARMONIZAÇÃO OROFACIAL E ODONTOLOGIA · ZÉ DOCA (MA)</small></div></section>''')

page(head('01 · POR QUE ISSO IMPORTA', 'Quem procura, <em>encontra você</em>',
          'Quando alguém digita "harmonização perto de mim" ou "dentista em Zé Doca", o Google mostra primeiro as fichas do Maps. É ali que a paciente vê o endereço, as fotos, as avaliações e toca em "Ligar" ou "Rotas".')
     + '<div class="tres"><div><b>Relevância</b><span>A ficha combina com o que a pessoa buscou: categoria certa, serviços e descrição.</span></div><div><b>Distância</b><span>Quem está perto da clínica vê primeiro. Endereço exato e verificado.</span></div><div><b>Destaque</b><span>Avaliações, fotos reais, posts e site ativo. É o que este kit cuida.</span></div></div>'
     + '<p class="nota">Ninguém compra posição no Maps. O nosso trabalho é deixar a ficha completa e viva; o resto é o Google que decide.</p>')

page(head('02 · A FICHA', 'Campos prontos para copiar') + '<table>' + ''.join(f'<tr><th>{e(a)}</th><td>{e(b)}</td></tr>' for a, b in FICHA) + '</table>'
     + f'<div class="box"><div class="k">DESCRIÇÃO · {len(DESCRICAO)} DE 750 CARACTERES</div><p>{e(DESCRICAO)}</p></div>')

page(head('03 · O QUE FALTA DA CLÍNICA', 'Cinco coisas para <em>publicar</em>', 'A ficha só vai ao ar depois da verificação, feita pela dona da clínica (o Google escolhe: vídeo, ligação ou mensagem).')
     + '<ol class="check">' + ''.join(f'<li>{e(x)}</li>' for x in FALTA) + '</ol>'
     + '<div class="box"><div class="k">VÍDEO DE VERIFICAÇÃO (O MAIS COMUM)</div><p>Um vídeo contínuo de 30 a 60 s: a rua e a Praça do Viva, a fachada com a placa, a porta abrindo, a recepção e um documento ou ferramenta de trabalho da clínica. Sem cortes e sem mostrar pacientes.</p></div>')

for i in (0, 4):
    page(head('04 · POSTS DO PERFIL' if i == 0 else '04 · POSTS DO PERFIL (CONT.)', '8 semanas de posts' if i == 0 else 'Semanas 5 a 8', '1 post por semana, com uma foto real nova (nunca a mesma do Instagram). Botão indicado em cada um.' if i == 0 else '')
         + '<div class="posts">' + ''.join(f'<div class="post"><div class="num">{i+j+1:02d}</div><b>{e(t)}</b><p>{e(x)}</p><span class="bt">Botão: {e(bt)}</span></div>' for j, (t, x, bt) in enumerate(POSTS[i:i+4])) + '</div>')

page(head('05 · PERGUNTAS E RESPOSTAS', 'As dúvidas de quem <em>ainda não veio</em>', 'Cadastre como perguntas da própria clínica e responda; elas aparecem na ficha.')
     + '<div class="qa">' + ''.join(f'<div><b>{e(q)}</b><span>{e(a)}</span></div>' for q, a in PERGUNTAS) + '</div>')

page(head('06 · RESPOSTAS ÀS AVALIAÇÕES', 'Toda avaliação <em>tem resposta</em>')
     + '<div class="resp">' + ''.join(f'<div><div class="k">{e(t)}</div><p>{e(x)}</p></div>' for t, x in RESPOSTAS) + '</div>'
     + f'<p class="nota">{e(REGRA_RESPOSTA)}</p>')

page(head('07 · PEDIR AVALIAÇÃO', 'Uma mensagem, <em>no mesmo dia</em>')
     + f'<div class="zap"><div class="bolha">{e(PEDIDO)}</div></div><p class="nota">{e(PEDIDO_REGRA)}</p>'
     + '<div class="box"><div class="k">O LINK</div><p>Depois da verificação: Perfil da Empresa → "Pedir avaliações" → copiar o link curto e colocar no lugar de {link}. Com ele fazemos também o cartão com QR code para o balcão.</p></div>')

page(head('08 · A ROTINA', 'O que manter <em>todo mês</em>') + '<table>' + ''.join(f'<tr><th>{e(a)}</th><td>{e(b)}</td></tr>' for a, b in ROTINA) + '</table>'
     + '<div class="fim"><img src="monograma.jpg"><div><b>Dra. Jaci Cunha</b><span>Cirurgiã-dentista · CRO-MA 8514<br>Av. Militar, em frente à Praça do Viva · Zé Doca (MA)<br>(98) 98567-2646 · drajacicunha.pages.dev</span></div></div>')

css = open(os.path.join(D, 'kit.css')).read()
open(os.path.join(D, 'kit.html'), 'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Kit Google · Dra. Jaci Cunha</title>'
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
    f'<style>{css}</style></head><body>{"".join(pg)}</body></html>')
print(len(pg), 'páginas')
