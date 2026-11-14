# Legendas estilo blog SEO (padrão do CLAUDE.md) para a semana 1. Gera semana-1/NN/legenda.txt e LEGENDAS.md.
import json, os
H = os.path.dirname(os.path.abspath(__file__)); R = json.load(open(os.path.join(H, 'roteiros.json')))['reels']
TAGS = {'História da pizza': '#historiadapizza', 'Humor de dono': '#donodepizzaria', 'Raio-X': '#marketingparapizzaria', 'Dados do setor': '#mercadodepizza',
        'Técnica de massa': '#massadepizza', 'Método': '#deliverydepizza', 'Forno': '#fornoalenha', 'Resposta pronta': '#atendimentowhatsapp',
        'Chamada para diagnóstico': '#gestaodepizzaria', 'Gestão': '#gestaodepizzaria', 'Curiosidade': '#pizzanapoletana', 'Ferramenta grátis': '#googlemeunegocio',
        'Bastidor': '#bastidoresdacozinha', 'Insumo': '#pizzaiolo', 'Dia da Pizza': '#diadapizza'}
NICHO = ['#pizzaria', '#pizzariadelivery', '#empreendedorismogastronomico', '#foodservice', '#pizzaiolo']
LOCAL = ['#saoluis', '#saoluisma', '#maranhao', '#pizzariasaoluis', '#slz']
FONTES = {'OT-04': 'Fontes: Apubra via Central do Varejo (40.332 pizzarias) e Apubra + Galunion via O Povo (98% com delivery, 75% usam apps).', 'OT-19': 'Fonte: 50 Top Pizza World 2026 (scattidigusto.it).', 'OT-10': 'Referência de mercado para food service (não é regra fixa: cada pizzaria tem a sua).', 'OT-11': 'Fonte: UNESCO, Lista do Patrimônio Cultural Imaterial (2017).'}
md = ['# Legendas · Reels Orégano Turbo semana 1 (14/11/2026)\n']
for k, r in enumerate(R):
    c = r['cenas']; corpo = [x['narracao'] for x in c[:-2]]
    tags = [TAGS.get(r['linha_editorial'], '#pizzaria'), NICHO[k % 5], LOCAL[k % 5], NICHO[(k + 2) % 5]]
    if r['tipo'] == 'venda': tags.append('#oreganoturbo')
    t = f"""{r['titulo']} 🍕

{corpo[0]} Se você é dono de pizzaria, esse assunto passa pela sua noite toda semana.

▶ O que acontece
{' '.join(corpo[1:3])}

▶ Na prática
{' '.join(corpo[3:])}

▶ Resumo
{c[-1]['narracao']} Pizzaria que cresce cuida do produto e de como ele chega no cliente.

{FONTES.get(r['id'], '')}

👉 {c[-2]['narracao']}
Siga a @oreganoturbo: marketing de vendas só para pizzarias, de São Luís/MA.

{' '.join(tags)}"""
    d = os.path.join(H, 'semana-1', f"{k+1:02d}"); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'legenda.txt'), 'w').write(t)
    md.append(f"## {r['id']} · {r['post']['data']} {r['post']['hora']} · {r['tipo']} · {r['linha_editorial']}\n\n{t}\n")
open(os.path.join(H, 'LEGENDAS.md'), 'w').write('\n'.join(md)); print('ok')
