# Letras oficiais do Álbum 01 "Copo Americano" (Pagode Fiado), como foram para o Suno nas versões aprovadas.
# Fonte: Drive "Pagode Fiado/Documentos": album-01-historia.md (00, 03, 04, 07) e PROMPT-SUNO-V4-7 (fórmula vencedora) (01, 02, 05, 06, 08, 09, 10).
# Cada linha: (parte, quem canta ou fala, texto). Gera letras.json.
import json, os
CH = lambda *l: list(l)
def coro(t, quem='Davi', parte='Refrão'): return [(parte, quem, x) for x in t]
SEXTA = ["É sexta de resenha, mesa amarela", "Copo americano, a roda é janela", "Pro que a semana tirou da gente", "Aqui todo mundo é parente"]
MARE = ["Maré tá boa, Lívia, vem comigo", "Te levo na garupa até o Recreio", "Teu pé na água fria, meu coração abrigo", "O verão inteiro cabe nesse passeio"]
TANTA = ["É o tantã do coração", "Tum, tum, chamando teu nome", "Se tu for, me leva na mão", "Que sem teu ritmo esse samba some"]
RECAI = ["É recaída de domingo", "Segunda eu juro que não volto", "Mas o fim de semana é perigo", "E o teu abraço é meu desgosto"]
BILH = ["Bilhete na geladeira", "Foi tudo que restou de nós", "Tua letra tremida e ligeira", "Falou mais alto que a tua voz"]
COPO = ["Copo americano, coração de vidro", "Tu quebrou os dois e saiu sorrindo", "Tô juntando os cacos na mesa de bar", "Esperando o samba te trazer de volta pra cá"]
VISU = ["Visualizou e não voltou", "Leu meu coração e não respondeu", "O status diz \"online\", mas o amor", "Ficou offline no peito meu"]
CAUSO = ["Quem tem pandeiro não anda sozinho", "Quem tem um samba não perde o caminho", "O tempo leva o cabelo e a juventude", "Mas não leva o couro nem a atitude"]
CHORAR = ["Chorar não, sambar", "Quem tem roda não fica no chão", "Se a saudade vier, deixa ela entrar", "Mas ela dança na nossa mão"]
RODA = ["É roda até o sol raiar", "Pandeiro, banjo, cavaco e tantã", "O samba cura o que a vida machucar", "Tristeza fica pra amanhã"]
F = {
'00': dict(titulo='Prólogo: Mesa Sete', cap='Prólogo', historia='Noite de chuva. Davi na mesa sete, sozinho. Seu Tião começa a contar.', linhas=[
  ('Fala', 'Seu Tião', 'Mesa sete de novo, Davi?'), ('Fala', 'Davi', 'Bota mais uma, Seu Tião… e pendura.'),
  ('Fala', 'Seu Tião', 'Esse menino nem sempre foi assim.'), ('Fala', 'Seu Tião', 'Tudo começou numa sexta…')]),
'01': dict(titulo='Sexta de Resenha', cap='Capítulo 1', historia='Uma sexta comum. Ela entra no bar e o Davi erra a letra pela primeira vez na vida.', linhas=[
  ('Verso', 'Davi', 'Sexta-feira, o patrão liberou'), ('Verso', 'Davi', 'Camisa na mochila, chinelo no pé'), ('Verso', 'Davi', 'O Seu Tião já gelou, já gritou'), ('Verso', 'Davi', '"Quem chegar por último paga o café"'),
  ('Pré-refrão', 'Davi', 'O Neguinho no cavaco, a Bia no rebolo'), ('Pré-refrão', 'Davi', 'O Mestre Zé contando causo e pedindo outro bolo')]
  + coro(SEXTA) + [
  ('Verso', 'Davi', 'E no meio do refrão a porta abriu'), ('Verso', 'Davi', 'Vestido de chita, cheiro de chuva'), ('Verso', 'Davi', 'Ela sorriu pro balcão e ninguém viu'), ('Verso', 'Davi', 'Que a minha voz tremeu feito uva na luva'),
  ('Breque', 'Davi', 'Errei a letra, o Neguinho riu'), ('Breque', 'Davi', 'A roda parou e eu nem senti'), ('Breque', 'Davi', 'Seu Tião anotou no caderno, sorriu:'), ('Breque', 'Davi', '"Hoje esse menino não sai daqui"')]
  + coro(SEXTA, 'Todos', 'Refrão final') + coro(SEXTA, 'Todos', 'Refrão final') + coro(SEXTA, 'Todos', 'Refrão final') + [('Fala', 'Juninho', 'Davi… quem é ela?')]),
'02': dict(titulo='Maré Boa', cap='Capítulo 2', historia='A conquista. O primeiro verão de Davi e Lívia.', linhas=[
  ('Verso', 'Davi', 'Descobri teu nome no terceiro sábado'), ('Verso', 'Davi', 'Lívia, que nem flor de beira de estrada'), ('Verso', 'Davi', 'Tu pediu um samba, eu fiquei calado'), ('Verso', 'Davi', 'Cantei olhando o chão, voz desafinada'),
  ('Pré-refrão', 'Davi', 'Tu riu do meu jeito, eu ri do teu riso'), ('Pré-refrão', 'Davi', 'Foi aí que eu soube que eu tava perdido')]
  + coro(MARE) + [
  ('Verso', 'Davi', 'Dividimos milho, cuscuz, picolé'), ('Verso', 'Davi', 'Tu dormiu no meu ombro no ônibus lotado'), ('Verso', 'Davi', 'Eu que nunca tive nada além de fé'), ('Verso', 'Davi', 'Agora tinha alguém pra chamar de "meu lado"'),
  ('Ponte', 'Davi', 'Pendura o meu coração…')] + coro(MARE) + [('Coro', 'Todos', 'Ê, ê, maré tá boa')]
  + coro(MARE, 'Todos', 'Refrão final') + coro(MARE, 'Todos', 'Refrão final')),
'03': dict(titulo='Tantã do Coração', cap='Capítulo 3', historia='O amor firme. O Rafa avisa que todo amor tem dia de festa e dia de dor.', linhas=[
  ('Fala', 'Rafa', 'Tum, tum… escuta. Todo amor tem esse barulho.'),
  ('Verso', 'Davi', 'Tu chegou na minha vida sem pedir licença'), ('Verso', 'Davi', 'Arrumou meu quarto, minha fé, minha agenda'), ('Verso', 'Davi', 'Hoje a casa tem teu cheiro, tua presença'), ('Verso', 'Davi', 'Até meu pandeiro tem fita de renda'),
  ('Pré-refrão', 'Davi', 'E eu, que só sabia cantar a saudade'), ('Pré-refrão', 'Davi', 'Aprendi contigo a cantar a verdade')]
  + coro(TANTA) + [
  ('Fala', 'Rafa', 'Minha avó dizia: amor é batuque.'), ('Fala', 'Rafa', 'Tem dia que é festa… tem dia que é dor.'),
  ('Verso', 'Davi', 'Eu ri do conselho, fiz pouco do truque'), ('Verso', 'Davi', 'Achei que o nosso nunca ia mudar de cor')]
  + coro(TANTA) + coro(TANTA, 'Todos', 'Refrão final')),
'04': dict(titulo='Recaída de Domingo', cap='Capítulo 4', historia='As primeiras brigas. Os dois terminam e voltam toda semana. Dueto de Davi e Bia, que canta como Lívia.', linhas=[
  ('Verso', 'Davi', 'Tu disse que eu vivo mais no bar que em casa'), ('Verso', 'Davi', 'Que meu samba tem mais beijo que a tua boca'),
  ('Verso', 'Lívia (Bia)', 'E tu disse que eu só sei apagar a brasa'), ('Verso', 'Lívia (Bia)', 'Que eu queria um homem e não uma roda louca'),
  ('Pré-refrão', 'Os dois', 'Bateu a porta na sexta, no sábado chorou'), ('Pré-refrão', 'Os dois', 'No domingo de tarde o portão me chamou')]
  + coro(RECAI, 'Os dois') + [
  ('Verso', 'Lívia (Bia)', 'Eu volto porque tu me olha como ninguém'), ('Verso', 'Davi', 'Eu volto porque sem você eu não sou ninguém'),
  ('Ponte', 'Os dois', 'Mas quanto tempo um amor aguenta'), ('Ponte', 'Os dois', 'Viver de voltar?')]
  + coro(RECAI, 'Os dois') + coro(RECAI, 'Os dois', 'Refrão final') + [('Fala', 'Lívia (Bia)', 'Davi… a gente precisa conversar.')]),
'05': dict(titulo='Bilhete na Geladeira', cap='Capítulo 5', historia='O fim. Ela vai embora e deixa só um bilhete.', linhas=[
  ('Verso', 'Davi', 'Cheguei em casa, a luz da cozinha acesa'), ('Verso', 'Davi', 'O café ainda quente, mas tu não tava'), ('Verso', 'Davi', 'Um bilhete preso com ímã de Fortaleza'), ('Verso', 'Davi', 'Três linhas, e a minha vida desmontava'),
  ('Pré-refrão', 'Davi', '"Cuida da planta, paga a luz, me esquece"'), ('Pré-refrão', 'Davi', 'Como se fosse fácil, como se fosse prece')]
  + coro(BILH) + [
  ('Verso', 'Davi', 'A planta eu reguei, a conta eu paguei'), ('Verso', 'Davi', 'Só a terceira parte eu não cumpri'), ('Verso', 'Davi', 'Todo dia eu leio, todo dia eu sei'), ('Verso', 'Davi', 'Que esse ímã segura mais que eu segurei aqui'),
  ('Ponte', 'Davi', 'E no verso do bilhete, bem pequeno'), ('Ponte', 'Davi', 'Tu escreveu "eu te amei"'), ('Ponte', 'Davi', 'No passado, Lívia… no passado'), ('Ponte', 'Davi', 'Foi aí que eu desabei')]
  + coro(BILH, 'Davi', 'Refrão final') + coro(BILH, 'Davi', 'Refrão final') + coro(BILH, 'Davi', 'Refrão final')),
'06': dict(titulo='Copo Americano', cap='Capítulo 6', historia='O Davi afoga a saudade na mesa sete do Seu Tião.', linhas=[
  ('Verso', 'Davi', 'Deixei teu nome escrito no guardanapo'), ('Verso', 'Davi', 'Do bar do Seu Tião, ali na esquina'), ('Verso', 'Davi', 'O garçom já sabe, nem pergunta nada'), ('Verso', 'Davi', 'Traz a gelada e a saudade de brinde'),
  ('Pré-refrão', 'Davi', 'E o cavaco chora junto comigo'), ('Pré-refrão', 'Davi', 'Cada nota é um "volta" que eu não digo')]
  + coro(COPO) + [
  ('Verso', 'Davi', 'Teu batom ficou na borda do meu copo'), ('Verso', 'Davi', 'Teu perfume ainda mora no meu casaco'), ('Verso', 'Davi', 'Os amigos falam "esquece, já deu"'), ('Verso', 'Davi', 'Mas quem esquece é quem nunca viveu'),
  ('Fala', 'Seu Tião', 'Menino… já é a terceira semana.'), ('Ponte', 'Davi', 'Anota, Seu Tião, pendura o meu coração…')]
  + coro(COPO, 'Todos', 'Refrão final') + coro(COPO, 'Todos', 'Refrão final') + coro(COPO, 'Todos', 'Refrão final') + [('Coro', 'Todos', 'Volta pra cá')]),
'07': dict(titulo='Visualizou e Não Voltou', cap='Capítulo 7', historia='Duas da manhã. Ele tenta voltar por mensagem.', linhas=[
  ('Verso', 'Davi', 'Duas da manhã, o celular na mão'), ('Verso', 'Davi', 'Escrevi "saudade", apaguei, voltei'), ('Verso', 'Davi', 'Mandei um áudio tremendo de emoção'), ('Verso', 'Davi', 'Tu ouviu inteiro, eu sei, eu sei'),
  ('Pré-refrão', 'Davi', 'Dois risquinhos azuis no meu peito'), ('Pré-refrão', 'Davi', 'Doeu mais que o adeus mal feito')]
  + coro(VISU) + [
  ('Verso', 'Davi', 'Vi tua foto num lugar que eu não conheço'), ('Verso', 'Davi', 'Teu cabelo novo, sorriso de quem venceu'), ('Verso', 'Davi', 'E eu aqui, Lívia, pagando o preço'), ('Verso', 'Davi', 'De um amor que só eu não esqueceu'),
  ('Ponte', 'Davi', '"Digitando…" apareceu'), ('Ponte', 'Davi', 'E sumiu')]
  + coro(VISU, 'Todos', 'Refrão final')),
'08': dict(titulo='Causo do Mestre Zé', cap='Capítulo 8', historia='O Mestre Zé conta ao Davi o amor que ele mesmo perdeu.', linhas=[
  ('Fala', 'Mestre Zé', 'Senta aqui, menino. Larga esse celular, que eu vou te contar uma coisa.'),
  ('Verso', 'Mestre Zé', 'Eu tinha a tua idade na Vila Isabel'), ('Verso', 'Mestre Zé', 'Pandeiro emprestado, sapato furado'), ('Verso', 'Mestre Zé', 'Amei uma morena de olhar de mel'), ('Verso', 'Mestre Zé', 'Que um dia embarcou e me deixou parado'),
  ('Pré-refrão', 'Mestre Zé', 'Mandou carta três vezes, depois o silêncio'), ('Pré-refrão', 'Mestre Zé', 'E eu fiquei trinta anos pagando esse preço')]
  + coro(CAUSO, 'Mestre Zé') + [
  ('Verso', 'Mestre Zé', 'Guardei as três cartas no forro do violão'), ('Verso', 'Mestre Zé', 'Por isso ele chora melhor que ninguém'), ('Verso', 'Mestre Zé', 'Mas sabe o que eu aprendi, meu irmão?'), ('Verso', 'Mestre Zé', 'A dor vira samba, e o samba faz bem'),
  ('Fala', 'Mestre Zé', 'Não deixa a saudade virar tua casa, menino.'), ('Fala', 'Mestre Zé', 'Ela é visita. Serve o café e manda embora.')]
  + coro(CAUSO, 'Todos', 'Refrão final') + coro(CAUSO, 'Todos', 'Refrão final') + coro(CAUSO, 'Todos', 'Refrão final')),
'09': dict(titulo='Chorar Não, Sambar', cap='Capítulo 9', historia='A Bia sacode o amigo. Chega de mesa sete.', linhas=[
  ('Fala', 'Bia', 'Levanta dessa mesa, Davi. Agora.'),
  ('Verso', 'Bia', 'Três semanas no mesmo copo, no mesmo canto'), ('Verso', 'Bia', 'Teu cavaco empoeirado, tua voz sumida'), ('Verso', 'Bia', 'Tu cantou pra todo mundo a vida inteira, e no entanto'), ('Verso', 'Bia', 'Esqueceu de cantar pra tua própria vida'),
  ('Pré-refrão', 'Bia', 'Eu também já caí, eu também já sangrei'), ('Pré-refrão', 'Bia', 'Foi no rebolo que eu me levantei')]
  + coro(CHORAR, 'Bia') + [
  ('Verso', 'Bia', 'O Seu Tião guardou teu lugar na roda'), ('Verso', 'Bia', 'O Neguinho afinou teu cavaco ontem'), ('Verso', 'Bia', 'O Juninho até parou de se achar na moda'), ('Verso', 'Bia', 'A gente é tua família, não te esconde'),
  ('Ponte', 'Todos', 'Pendura o meu coração na conta…'), ('Ponte', 'Bia', '…que a gente paga junto.')]
  + coro(CHORAR, 'Todos', 'Refrão final') + coro(CHORAR, 'Todos', 'Refrão final') + coro(CHORAR, 'Todos', 'Refrão final')),
'10': dict(titulo='Roda Até o Sol Raiar', cap='Capítulo 10', historia='A virada. O Davi volta a cantar feliz. No último segundo, a porta do bar se abre.', linhas=[
  ('Fala', 'Mestre Zé', 'Agora é todo mundo!'),
  ('Verso', 'Davi', 'Puxa a cadeira, que a noite é criança'), ('Verso', 'Bia', 'Quem chegou tarde entra na dança'), ('Verso', 'Juninho', 'Quem tá sofrendo canta mais alto'), ('Verso', 'Neguinho', 'Quem tá devendo paga no salto'),
  ('Pré-refrão', 'Todos', 'Ninguém vai embora, ninguém vai deitar')]
  + coro(RODA, 'Todos') + [
  ('Verso', 'Davi', 'Eu guardei o bilhete, não vou mentir'), ('Verso', 'Davi', 'Mas tirei da geladeira e botei na carteira'), ('Verso', 'Davi', 'Hoje eu canto sorrindo pra não sumir'), ('Verso', 'Davi', 'Hoje eu sou a roda inteira'),
  ('Ponte', 'Todos', 'Pendura o meu coração na conta, Seu Tião'), ('Ponte', 'Todos', 'Que hoje eu pago cantando'), ('Ponte', 'Todos', 'Pendura o meu coração na conta, Seu Tião'), ('Ponte', 'Todos', 'Que o samba tá me curando')]
  + coro(RODA, 'Todos', 'Refrão final') + coro(RODA, 'Todos', 'Refrão final') + coro(RODA, 'Todos', 'Refrão final')
  + [('Fala', 'Seu Tião', '…Davi. Olha quem chegou.')]),
}
json.dump(F, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'letras.json'), 'w'), ensure_ascii=False, indent=1)
print({k: len(v['linhas']) for k, v in F.items()})
