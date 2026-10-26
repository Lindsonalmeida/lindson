# Modelo da estratégia completa (exemplo: Villa do Vinho). Copie para agencia/propostas/<cliente>/, troque textos e fotos em img/ e rode: python3 montar_estrategia.py
import re
src = open('base.html').read()
head = src[:src.index('<section')]
secs = re.findall(r'<section.*?</section>', src, re.S)
capa, partida, desafio, anuncios, fecho = secs[0], secs[1], secs[2], secs[4], secs[7]

css = '''<style>
.tbl{width:100%;border-collapse:collapse;font-size:25px;line-height:1.3}
.tbl th{font-family:Cinzel;color:var(--gold);text-align:left;font-size:22px;letter-spacing:2px;padding:10px 12px;border-bottom:2px solid var(--gold)}
.tbl td{padding:12px;border-bottom:1px solid rgba(217,178,106,.25);vertical-align:top}
.tbl td:first-child{color:var(--gold);font-weight:700;white-space:nowrap}
.step{display:flex;gap:20px;align-items:flex-start}.step .n{font-family:'Great Vibes';color:var(--gold);font-size:58px;line-height:.9;width:46px;flex:none}
.small p,.small li{font-size:26px;line-height:1.35}
.pill{display:inline-block;border:1.5px solid var(--gold);color:var(--gold);border-radius:30px;padding:4px 16px;font-size:22px;margin:4px 6px 0 0}
.funil div{margin:0 auto;text-align:center;padding:18px;border-radius:14px;font-size:26px}
</style>'''

n = [2]
def pg(eyebrow, titulo, corpo, gold=None):
    n[0] += 1
    t = titulo + (f'<br><span class="gold">{gold}</span>' if gold else '')
    return f'''<section class="pg">
 <div class="top"><span class="num">{n[0]:02d}</span><img class="logo" src="img/logo.png"></div>
 <div class="eyebrow" style="margin-top:6px;font-size:26px">{eyebrow}</div>
 <h2 style="margin-top:10px;font-size:52px">{t}</h2>
 <div class="rule" style="margin:22px 0">✦</div>
 <div class="small">{corpo}</div>
</section>'''

def passos(itens):
    return '<div style="display:flex;flex-direction:column;gap:16px">' + ''.join(
        f'<div class="card step" style="padding:16px 24px"><span class="n">{i+1}</span><p><b class="gold">{a}</b> {b}</p></div>' for i, (a, b) in enumerate(itens)) + '</div>'

def tabela(cab, linhas):
    return '<table class="tbl"><tr>' + ''.join(f'<th>{c}</th>' for c in cab) + '</tr>' + ''.join(
        '<tr>' + ''.join(f'<td>{c}</td>' for c in l) + '</tr>' for l in linhas) + '</table>'

def nota(t): return f'<p class="mut" style="margin-top:22px;text-align:center">{t}</p>'

P = []
P.append(pg('Visão geral', 'Os 4 pilares', None and '' or
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">' + ''.join(
   f'<div class="card"><div class="script" style="font-size:66px">{a}</div><p>{b}</p></div>' for a, b in [
   ('Conteúdo', 'Linhas editoriais que fazem a pessoa desejar a Villa e saber o que comprar.'),
   ('Tráfego', 'Anúncios por produto e por público, só em São Luís, levando ao WhatsApp.'),
   ('Atendimento', 'Roteiro de WhatsApp para a conversa virar visita, reserva e contrato.'),
   ('Medição', 'Cada contato com origem marcada. Toda semana, números claros.')]) + '</div>'
  + nota('Implantação em 3 fases: <b class="gold">base técnica → lançamento → escala</b>.'), 'da máquina de vendas'))

P.append(pg('Fase 1 · Semanas 1 e 2', 'Base técnica', passos([
  ('Gerenciador de Negócios.', 'Página, Instagram, conta de anúncios e WhatsApp da Villa ligados num só lugar, no nome da Villa.'),
  ('Pixel e conjunto de dados.', 'Instalados na página de links e no cardápio, para medir quem visitou e criar públicos.'),
  ('WhatsApp Business organizado.', 'Catálogo com eventos, menus e adega, mensagens rápidas e etiquetas por produto.'),
  ('Links rastreados.', 'Cada campanha abre o WhatsApp com uma mensagem pronta e um código (ex.: EV-CORP). Assim sabemos de onde veio cada contato.'),
  ('Públicos salvos.', 'Seguidores, quem engajou em 30, 90 e 365 dias, quem viu vídeos e quem já chamou no WhatsApp.'),
  ('Google Meu Negócio.', 'Fotos, horários, cardápio e respostas às avaliações, para quem busca "restaurante para evento" no Google.')]),
  'que mede tudo'))

P.append(pg('Fase 1 · Perfil que vende', 'O Instagram como', passos([
  ('Bio com caminho.', 'Uma linha por produto + "Orçamento de eventos no link 👇". O link abre uma página com botões: Eventos, Reservar mesa, Adega, Cardápio.'),
  ('Destaques organizados.', 'Eventos (com 10/20/30 convidados), Salões, Executivo, Jantar, Adega, Depoimentos, Como chegar.'),
  ('3 posts fixados.', 'Vídeo dos salões, menu executivo e o depoimento de um evento real.'),
  ('Toda legenda pede uma ação.', '"Chama no WhatsApp", "reserve pelo link", "manda EVENTO no direct".'),
  ('Resposta automática no direct.', 'Quem manda EVENTO, MESA ou VINHO recebe o link certo na hora.')]),
  'vitrine e balcão'))

P.append(pg('Conteúdo', 'Linhas editoriais', tabela(['Linha', 'O que mostra', 'Formatos'], [
  ('Eventos<br>que encantam', 'Salões montados, festas reais, "10, 20, 30 convidados", antes e depois', 'Reels, carrossel'),
  ('A mesa<br>da Villa', 'Executivo de R$79,90, pratos do jantar, especiais da casa', 'Reels curtos, foto'),
  ('A adega', 'Vinho da semana, harmonização, espumante para datas', 'Reels com o sommelier, carrossel'),
  ('Gente e<br>bastidores', 'Equipe, cozinha, montagem, música de sexta', 'Stories, Reels'),
  ('Prova<br>social', 'Depoimentos de noivos, empresas e clientes da mesa', 'Reels, repost'),
  ('Oferta', 'Datas livres, kits, confraternização com tudo incluso', 'Stories, anúncio')]) +
  nota('Cada linha conversa com um produto. <b class="gold">Nenhum post fica sem dono.</b>'), 'com objetivo de venda'))

P.append(pg('Conteúdo · Como cada vídeo é feito', 'Roteiro de Reels', passos([
  ('0 a 3 segundos: gancho.', '"Quanto custa um casamento para 30 pessoas em São Luís?" / "Esse é o almoço mais pedido da Mário Andreazza."'),
  ('3 a 15 segundos: mostrar.', 'O salão montado, o prato saindo, a taça sendo servida. Imagem real, sem enrolação.'),
  ('15 a 25 segundos: provar.', 'Cliente falando, mesa cheia, detalhe que só a Villa tem.'),
  ('Final: chamar.', '"Chama no WhatsApp e pergunta a data." Texto na tela + legenda + link.')]) +
  '<div class="card" style="margin-top:18px"><p><b class="gold">Ganchos prontos:</b> "3 erros ao escolher o lugar da festa da empresa" · "O que vem no menu de R$79,90" · "O vinho que eu levaria para o Natal" · "Casamento íntimo existe, e é assim"</p></div>',
  'que vende'))

P.append(pg('Conteúdo · Rotina', 'A semana da Villa', tabela(['Dia', 'Feed', 'Stories'], [
  ('Segunda', 'Bastidor de evento montado', 'Enquete: qual evento você faria aqui?'),
  ('Terça', 'Executivo da semana', 'Cardápio do dia + reservar'),
  ('Quarta', 'Vinho da semana (adega)', 'Caixinha: dúvidas sobre vinho'),
  ('Quinta', 'Depoimento ou evento real', 'Datas livres do mês'),
  ('Sexta', 'Música ao vivo sem couvert', 'A noite ao vivo'),
  ('Sáb/Dom', 'Clima do jantar / carrossel', 'Repost de clientes')]) +
  nota('Ritmo: <b class="gold">5 posts no feed e stories todos os dias</b>. O post que mais funcionar vira anúncio.'), 'cada dia vende algo'))

P.append(pg('Tráfego · Estrutura', 'O funil da Villa',
  '<div class="funil" style="display:flex;flex-direction:column;gap:14px">'
  '<div style="width:100%;background:rgba(179,18,28,.35)"><b>DESCOBRIR</b> · quem ainda não segue: vídeos dos salões, do executivo e da adega para a cidade</div>'
  '<div style="width:86%;background:rgba(179,18,28,.55)"><b>CONSIDERAR</b> · quem viu 50% dos vídeos ou engajou: depoimentos, pacotes, "como funciona"</div>'
  '<div style="width:72%;background:var(--red)"><b>COMPRAR</b> · quem visitou o link ou chamou e não fechou: datas livres, oferta, "chama agora"</div></div>'
  + nota('A maior parte da verba começa no <b class="gold">COMPRAR</b> e no <b class="gold">CONSIDERAR</b>: os 43 mil já conhecem a casa. Depois a gente amplia a cidade.'),
  'descobrir → considerar → comprar'))

P.append(pg('Tráfego · Campanhas', 'As 6 campanhas', tabela(['Campanha', 'Para quem', 'Destino'], [
  ('C1 Confrater-<br>nização', 'Empresários, gestores e RH em Renascença, Calhau, Cohama, Ponta d\'Areia e Centro', 'WhatsApp · EV-CORP'),
  ('C2 Casamento<br>e 15 anos', 'Noivos e pais na Grande São Luís, quem segue cerimonial e decoração', 'WhatsApp · EV-CAS'),
  ('C3 Aniversários', 'Quem segue ou engajou com a Villa + público parecido', 'WhatsApp · EV-ANI'),
  ('C4 Executivo', 'Raio de 3 a 5 km da Mário Andreazza, dias úteis, 10h às 13h', 'Rota / WhatsApp'),
  ('C5 Jantar e<br>sexta ao vivo', 'Cidade toda, quinta a sábado, 16h às 21h', 'Reserva · MESA'),
  ('C6 Adega', 'Interesse em vinho e gastronomia; Natal e Réveillon', 'WhatsApp · VINHO')]) +
  nota('Mais uma campanha sempre ligada: <b class="gold">remarketing</b> para quem já viu, curtiu ou chamou.'), 'uma para cada produto'))

P.append(pg('Tráfego · Públicos', 'Quem vai ver', passos([
  ('Quentes (prioridade).', 'Seguidores, engajados de 30 a 365 dias, quem viu 50% dos vídeos, quem visitou o link, lista de clientes e contatos do WhatsApp.'),
  ('Parecidos.', 'Público semelhante a quem já chamou para orçamento de evento, que é o mais valioso.'),
  ('Por lugar.', 'Raio por bairro para executivo e empresas. Cidade toda para jantar, casamento e adega.'),
  ('Por momento de vida.', 'Recém-noivos, pais de adolescentes, formandos e cargos de gestão, quando a plataforma oferecer.'),
  ('Exclusões.', 'Quem já fechou não recebe anúncio de venda, recebe de retorno.')]),
  'a pessoa certa, na hora certa'))

P.append(anuncios.replace('<span class="num">04</span>', '<span class="num">12</span>').replace('E os próximos 90 dias', 'Criativos e 90 dias'))
n[0] = 12

P.append(pg('Tráfego · Testes', 'Como os anúncios', passos([
  ('3 criativos por campanha.', 'Vídeo do lugar, depoimento e oferta direta, cada um com ganchos diferentes.'),
  ('3 dias de leitura.', 'Nada é julgado antes de 3 dias rodando.'),
  ('Corte.', 'O criativo que traz conversa muito mais cara que a média sai e entra um novo.'),
  ('Escala.', 'O que traz conversa boa ganha verba aos poucos, cerca de 20% a cada 2 ou 3 dias.'),
  ('Renovação.', 'Criativos novos a cada 2 semanas para o público não cansar.')]),
  'melhoram toda semana'))

P.append(pg('Atendimento', 'Roteiro do WhatsApp', passos([
  ('Boas-vindas em até 5 minutos.', '"Oi! Que bom falar com você. É para qual ocasião?"'),
  ('2 perguntas.', 'Qual o evento e quantas pessoas? Qual a data?'),
  ('Mostrar o espaço certo.', 'Vídeo do salão para aquele tamanho de festa + opções de menu.'),
  ('Convite para visita com degustação.', 'Quem visita fecha muito mais. A meta da conversa é a visita.'),
  ('Proposta no mesmo dia.', 'PDF na identidade da Villa, com validade.'),
  ('Retorno em 1, 3 e 7 dias.', 'Mensagens prontas para quem sumiu. Ninguém fica sem resposta.')]),
  'da 1ª mensagem ao contrato'))

P.append(pg('Calendário', 'Os próximos 90 dias', tabela(['Quando', 'Foco'], [
  ('Novembro<br>1ª e 2ª semana', 'Base técnica + C1 Confraternização no ar + perfil reorganizado'),
  ('Novembro<br>3ª e 4ª semana', 'Remarketing ligado + Black Friday da adega + executivo'),
  ('Dezembro', 'Confraternizações acontecendo (filmar tudo) + Natal com kits de vinho + Réveillon com espumante + formaturas'),
  ('Janeiro', 'Férias e turistas no almoço e jantar + C2 Casamento e 15 anos do ano + aniversários de verão')]) +
  nota('Todo evento de dezembro vira conteúdo e depoimento para vender os eventos de 2027.'), 'nov · dez · jan'))

P.append(pg('Medição', 'O relatório', tabela(['Número', 'O que mostra'], [
  ('Conversas', 'Quantas pessoas chamaram no WhatsApp, por produto'),
  ('Custo por conversa', 'Quanto custou cada contato'),
  ('Orçamentos', 'Quantos pediram orçamento de evento'),
  ('Visitas', 'Quantos foram conhecer os salões'),
  ('Fechados', 'Quantos eventos fecharam e o valor (a equipe informa)'),
  ('Alcance na cidade', 'Quantas pessoas novas viram a Villa'),
  ('Melhor post', 'O que funcionou e o que vem na próxima semana')]) +
  nota('Uma página, toda semana, <b class="gold">em português claro</b>.'), 'que cabe numa leitura'))

P.append(pg('Parceria', 'Quem faz o quê', '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">'
  '<div class="card"><div class="tag">Eu faço</div><ul style="list-style:none;margin-top:12px">'
  + ''.join(f'<li>✓ {x}</li>' for x in ['Base técnica e rastreio', 'Linhas editoriais e calendário', 'Roteiros e edição', 'Campanhas e públicos', 'Testes e otimização', 'Roteiro de WhatsApp', 'Relatório semanal']) +
  '</ul></div><div class="card"><div class="tag">Vocês fazem</div><ul style="list-style:none;margin-top:12px">'
  + ''.join(f'<li>✓ {x}</li>' for x in ['Liberar acessos', 'Responder rápido no WhatsApp', 'Marcar a origem do contato', 'Avisar quando fechar', 'Abrir espaço para gravar', 'Servir bem, como sempre']) +
  '</ul></div></div>' + nota('Vocês servem. <b class="gold">Eu vendo.</b>'), 'cada um no seu forte'))

fecho = fecho.replace('e eu marco 15 minutos para mostrar como isso funciona na Villa.', 'e eu marco 15 minutos para mostrar como isso funciona na Villa.')
html = head.replace('</style></head>', '</style>' + css + '</head>') + capa + partida + desafio + ''.join(P) + fecho + '</body></html>'
open('estrategia-completa.html', 'w').write(html)
print(html.count('<section'), 'páginas')
