# Painel da Orégano Turbo na Central (/painel/oregano), montado a partir do painel publicado da Desentupidora SF
# (mesmo sistema: Aprovações com abas Para aprovar · Em ajuste · Aprovados · Postados, CRM, financeiro, notícias, pedidos).
# Trocas pontuais: identidade (carvão, verde, açafrão), dados, CRM de pizzarias e as artes do calendário com legenda.
# As artes ficam em arquivos (painel/oregano/artes/), não embutidas. Conta Leandro, 06/11/2026.
# v4 (conta Zuleide, 08/11/2026): lê também artes/tipo-v4/ e, com USAR_V4 = True (depois que o Lindson aprovar o kit v4),
# troca as peças 'v3:' pela equivalente do kit v4 (campo 'v4' do calendario.json).
# Uso: python3 montar_painel.py [pasta do privado CentralLindsonALmeida]
import json, os, re, sys, shutil, base64, io, glob
USAR_V4 = False   # True quando o Lindson aprovar o kit v4 (../v4/)
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
OP = os.path.join(D, '..', '..')
PRIV = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, '..', '..', '..', '..', '..', 'centrallindsonalmeida')
s = open(os.path.join(PRIV, 'painel', 'sf.html')).read()

def troca(a, b, n=1):
    global s
    assert a in s, 'o painel modelo mudou: ' + a[:70]
    s = s.replace(a, b) if n == 0 else s.replace(a, b, n)

def uri(p, w):
    im = Image.open(p).convert('RGBA'); im.thumbnail((w, w))
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True); return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()

# 1 · identidade
troca('<title>Desentupidora SF · Central</title>', '<title>Orégano Turbo · Central</title>')
for a, b in [('--fundo:#04102B', '--fundo:#121411'), ('--painel:#0A2150', '--painel:#1B1E19'), ('--painel2:#0F2A61', '--painel2:#23271F'),
             ('--linha:#1C3B7A', '--linha:#323829'), ('--amarelo:#FF8A00', '--amarelo:#F2B33D'), ('--texto:#EEF4FF', '--texto:#F3EEE6'), ('--apagado:#A3B7DD', '--apagado:#ABA593')]:
    troca(a, b)
i = s.index('<div class="logo"'); k = s.index('<img src="', i) + 10; f = s.index('"', k)
s = s[:k] + uri(os.path.join(OP, 'identidade', 'kit-mockup', 'simbolo-verde.png'), 200) + s[f:]
s = s.replace('alt="Desentupidora SF" style="width:96px;border-radius:50%"', 'alt="Orégano Turbo" style="width:84px;border-radius:22px;background:#F3EEE6;padding:12px"', 1)
troca('<div class="avatar" title="Desentupidora SF">SF</div>', '<div class="avatar" title="Orégano Turbo">OT</div>')
troca("let cli='sf'", "let cli='oregano'")
troca("const BASE={sf:{nome:'Desentupidora SF'", "const BASE={oregano:{nome:'Orégano Turbo'")
troca("const FRASES={sf:[", "const FRASES={oregano:['Dono de pizzaria decide no WhatsApp. Responda todo contato em até 5 minutos.','Poste as 3 artes do dia: 8h story, 12h feed, 19h feed. Constância vende.','Cada Raio-X vendido é um diagnóstico que pode virar cliente. Faça o follow-up em até 7 dias.','Peça autorização por escrito antes de mostrar número de cliente.'],sf_antigo:[")
troca("const MISSOES={sf:[", "const MISSOES={oregano:[['Postar as 3 artes do dia no horário do calendário',30],['Responder directs e WhatsApp em até 5 minutos',25],['Chamar 5 pizzarias novas pelo app de prospecção',25],['Marcar como postado no painel',10],['Gerar no Gemini as fotos que faltam (lote 2)',10]],sf_antigo:[")

# 2 · dados do cliente
i = s.index('window.__DADOS=') + len('window.__DADOS='); j = s.index('};', i) + 1
dados = {"cliente": "oregano", "atualizado": "06/11/2026", "nome": "Orégano Turbo", "seg": "Marketing de vendas só para pizzarias · São Luís/MA",
         "plano": "Operação própria do Lindson: Instagram @oreganoturbo, site e vendas", "inicio": "Novembro/2026",
         "site": "https://lindsonalmeida.pages.dev/oreganoturbo/", "instagram": {"perfil": "@oreganoturbo", "data": "a medir", "periodo": "primeira medição", "visualizacoes": None},
         "kpiCrm": "Diagnósticos marcados", "kpiCrmNota": "no CRM de pizzarias", "metas": [], "semMetas": "Meta aprovada: 2 pizzarias novas por mês; as 5 fundadoras em 60 dias.",
         "entregas": [["Identidade visual v4.1 + manual (19 p.)", "Marca", "06/11", "aprovada"], ["Site principal com planos e formulário", "Site", "06/11", "no ar (prévia)"],
                      ["Kit social v3 (9 posts, 3 stories)", "Posts", "06/11", "aprovado: é o padrão"], ["Calendário de 4 semanas, 3 postagens por dia", "Posts", "06/11", "na aba Aprovações"], ["Kit social v4 + calendário no sistema v4 (comanda PEDIDO Nº)", "Posts", "08/11", "aguardando aprovação"],
                      ["Bio, foto de perfil e capas de destaque", "Perfil", "06/11", "na aba Aprovações"]]}
s = s[:i] + json.dumps(dados, ensure_ascii=False) + s[j:]

# 3 · CRM de pizzarias (ferramentas)
i = s.index('window.__FERR=') + len('window.__FERR='); j = s.index('};', i) + 1
F = json.loads(s[i:j])
F.update({"negocio": "Orégano Turbo", "exEntrada": "Ex.: Plano Fortaleza · Pizzaria do Bairro", "exSaida": "Ex.: Anúncio do Raio-X",
          "origens": ["Instagram @oreganoturbo", "Anúncio do Raio-X (Meta)", "Site (formulário)", "Prospecção pelo app", "Indicação", "WhatsApp direto", "Outro"],
          "interesses": ["Raio-X R$ 297", "Plano Muralha", "Plano Fortaleza", "Plano Cidadela", "Vaga de fundadora", "Ainda não sabe"],
          "catEntradas": ["Raio-X", "Plano Muralha", "Plano Fortaleza", "Plano Cidadela", "Outras entradas"], "catEntradaCRM": "Plano Fortaleza",
          "catSaidas": ["Anúncios (Meta)", "Ferramentas e IA", "Deslocamento e gravação", "Impostos e taxas", "Maquininha e taxas de cartão", "Telefone e internet", "Outras saídas"],
          "noticias": [{"nome": "Pizzarias", "q": "pizzaria OR pizzarias"}, {"nome": "Delivery e iFood", "q": "delivery iFood restaurantes"}, {"nome": "Food service", "q": "food service bares restaurantes Abrasel"},
                       {"nome": "São Luís gastronomia", "q": "São Luís restaurante OR pizzaria"}, {"nome": "Marketing para restaurantes", "q": "marketing restaurante Instagram"}],
          "ideiaPost": "Gancho: \"Saiu uma notícia sobre {tema} e isso mexe com o caixa da sua pizzaria. Te explico em 30 segundos.\"\nNotícia: {titulo}\nFonte: {link}\nFechamento: Manda RAIO-X no direct."})
F["palavras"].update({"pac": "pizzaria", "Pac": "Pizzaria", "pacs": "pizzarias", "aval": "diagnóstico", "Aval": "Diagnóstico", "avals": "diagnósticos", "Avals": "Diagnósticos",
                      "proc": "contrato", "Proc": "Contrato", "procs": "Contratos", "fezProc": "Fecharam contrato", "marcaram": "Marcaram diagnóstico", "tinhaAval": "de quem fez diagnóstico",
                      "negocio": "a Orégano Turbo", "crm": "CRM de pizzarias", "regra": "Conexão, dor, desejo e pergunta. Sem prometer resultado e sem preço antes do diagnóstico, menos o Raio-X R$ 297."})
F["etapas"] = [{"id": "novo", "nome": "Novo contato", "botao": "Respondeu", "depois": "conversa", "msg": "Oi, {nome}! Aqui é o Lindson, da Orégano Turbo. Recebi o seu contato sobre {interesse}. Qual o dia mais fraco da sua pizzaria hoje?"},
               {"id": "conversa", "nome": "Conversando", "botao": "Marcou diagnóstico", "msg": "Oi, {nome}! Posso olhar o Instagram, o cardápio e o iFood da sua pizzaria com você numa chamada de 20 minutos. Qual o melhor horário?"},
               {"id": "marcada", "nome": "Diagnóstico marcado", "botao": "Fez diagnóstico", "msg": "Oi, {nome}! Confirmando o nosso diagnóstico {quando}. Se puder, deixa o Instagram da pizzaria aberto."},
               {"id": "compareceu", "nome": "Diagnóstico feito", "botao": "Fechou", "msg": "Oi, {nome}! Obrigado pela conversa. Como combinamos: o próximo passo é o Raio-X ou o plano. Posso te mandar a proposta?"},
               {"id": "fez", "nome": "Cliente", "botao": "Renovação", "depois": "retorno", "msg": "Oi, {nome}! Bem-vindo à Orégano Turbo. Vou marcar a nossa primeira gravação na sua pizzaria. Qual dia da semana fica melhor?"},
               {"id": "retorno", "nome": "Renovação", "depois": "conversa", "msg": "Oi, {nome}! O seu contrato está chegando ao fim. Vamos ver os números juntos e decidir os próximos meses?"},
               {"id": "perdido", "nome": "Não fechou", "depois": "conversa", "msg": "Oi, {nome}! Aqui é o Lindson, da Orégano Turbo. Ainda abrimos vagas de fundadora. Quer conversar de novo sobre a sua pizzaria?"}]
s = s[:i] + json.dumps(F, ensure_ascii=False) + s[j:]
s = s.replace('CRM de chamados', 'CRM de pizzarias')

# 4 · artes do calendário + perfil → APROV (arquivos em painel/oregano/artes/)
cal = json.load(open(os.path.join(D, 'calendario.json')))
leg = {(x['dia'], x['hora']): x['legenda'] for x in (json.load(open(os.path.join(D, 'legendas.json'))) if os.path.exists(os.path.join(D, 'legendas.json')) else [])}
OUT = os.path.join(PRIV, 'painel', 'oregano', 'artes'); os.makedirs(OUT, exist_ok=True)
def arte(r):
    im = r['imagem']
    if im.startswith('v3:'):
        if USAR_V4 and r.get('v4'):
            return [os.path.join(OP, 'social', 'v4', 'pecas', r['v4'][3:])]
        return [os.path.join(OP, 'social', 'v3', 'pecas', im[3:])]
    pre = f"d{r['dia']:02d}-{r['hora']}-"
    for pasta in ['s1-2', 's3-4', 'fotos', 'tipo-v4']:
        fs = sorted(glob.glob(os.path.join(D, 'artes', pasta, pre + '*.jpg')))
        if fs: return fs
    return []
APROV, falta = [], []
for r in cal:
    fs = arte(r)
    if not fs: falta.append(r); continue
    urls = []
    for f in fs:
        nome = os.path.basename(f) if not r['imagem'].startswith('v3:') else f"d{r['dia']:02d}-{r['hora']}-{os.path.basename(f)}"
        shutil.copy(f, os.path.join(OUT, nome)); urls.append('/painel/oregano/artes/' + nome)
    tipo = 'Story' if r['formato'] == 'Story' else ('Carrossel' if len(urls) > 1 else 'Post único')
    item = {"t": tipo, "titulo": f"{r['semana_dia']} {r['data']} · {r['hora']} · {r['manchete']}", "data": f"Postar {r['semana_dia']} {r['data']} às {r['hora']}",
            "linha": r['linha_nome'], "st": "aguardando", "img": urls[0], "legenda": leg.get((r['dia'], r['hora']), r['apoio'])}
    if len(urls) > 1: item["telas"] = urls
    APROV.append(item)
PERFIL = os.path.join(OP, 'social', 'perfil')
if os.path.exists(os.path.join(PERFIL, 'previa-perfil.jpg')):
    bio = open(os.path.join(PERFIL, 'BIO.md')).read() if os.path.exists(os.path.join(PERFIL, 'BIO.md')) else ''
    shutil.copy(os.path.join(PERFIL, 'previa-perfil.jpg'), os.path.join(OUT, 'perfil-previa.jpg'))
    APROV.insert(0, {"t": "Perfil", "titulo": "Perfil do Instagram · bio, foto e destaques", "data": "Fazer antes da 1ª postagem", "linha": "Perfil", "st": "aguardando",
                     "img": "/painel/oregano/artes/perfil-previa.jpg", "legenda": bio})
    extra = [('avatar-1080.jpg', 'Perfil', 'Foto de perfil @oreganoturbo', 'Subir como foto de perfil (1080×1080)')]
    extra += [(os.path.basename(f), 'Destaque', 'Capa de destaque · ' + os.path.basename(f)[11:-4].replace('-', ' ').title(), 'Subir nas capas dos destaques') for f in sorted(glob.glob(os.path.join(PERFIL, 'destaque-*.jpg')))]
    for k, (arq, t, tit, quando) in enumerate(extra, 1):
        shutil.copy(os.path.join(PERFIL, arq), os.path.join(OUT, 'perfil-' + arq))
        APROV.insert(k, {"t": t, "titulo": tit, "data": quando, "linha": "Perfil", "st": "aguardando", "img": "/painel/oregano/artes/perfil-" + arq, "legenda": ""})
i = s.index('const APROV=') + len('const APROV='); j = s.index('];', i) + 1
s = s[:i] + json.dumps(APROV, ensure_ascii=False) + s[j:]
s = s.replace('Desentupidora SF', 'Orégano Turbo')
# prévia do feed (posts de feed na ordem de postagem, o mais novo no topo, como no Instagram)
feed = [x for x in APROV if x['t'] in ('Post único', 'Carrossel')][:18][::-1]
W = 360; g = Image.new('RGB', (3 * W + 4, ((len(feed) + 2) // 3) * int(W * 1.25) + 4), '#121411')
for k, x in enumerate(feed):
    im = Image.open(os.path.join(OUT, os.path.basename(x['img']))).convert('RGB'); im = im.resize((W, int(W * 1.25)))
    g.paste(im, ((k % 3) * (W + 2), (k // 3) * (int(W * 1.25) + 2)))
g.save(os.path.join(OUT, 'previa-feed.jpg'), quality=80)
k = s.index('Como o seu feed fica'); a = s.index('<img src="', k) + 10; b = s.index('"', a)
s = s[:a] + '/painel/oregano/artes/previa-feed.jpg' + s[b:]
for a_, b_ in [('#0A2A6E', '#1E5B3B'), ('#04102B', '#121411'), ('#1D5FD0', '#2E7A4E'), ('#030C22', '#0E100C'), ('#061639', '#181B16')]:
    s = s.replace(a_, b_)
# Gestão: link da Assessoria para pizzarias (saiu dos cartões do admin), conta Leandro 11/11/2026
_c = s.index('Campanhas</a>', s.index('<h4>Gestão</h4>')) + len('Campanhas</a>')
s = s[:_c] + '\n      <a href="/painel/pizzarias.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 17 17 7M9 7h8v8"/></svg>Assessoria para pizzarias</a>' + s[_c:]
open(os.path.join(PRIV, 'painel', 'oregano.html'), 'w').write(s)
print(len(APROV), 'itens no painel ·', len(falta), 'esperando foto:', ', '.join(f"d{r['dia']} {r['hora']} ({r['imagem']})" for r in falta))
