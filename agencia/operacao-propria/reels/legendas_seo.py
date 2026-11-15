"""Legendas SEO dos 21 Reels (padrão CLAUDE.md: título com palavra-chave, intro, subtítulos, exemplo, conclusão,
CTA de vendas da Orégano e 3-5 hashtags tema+nicho+local). Gera LEGENDAS.md e semana-1/NN/legenda-seo.txt. Conta Zuleide, 15/11/2026."""
import json, os, re
D = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(D, 'roteiros.json')))['reels']
TEMA = {'História da pizza': ['#historiadapizza', '#pizzanapolitana'], 'Humor de dono': ['#donodepizzaria', '#vidadeempreendedor'],
        'Raio-X': ['#diagnosticodepizzaria', '#marketingparapizzaria'], 'Dados do setor': ['#mercadodepizza', '#foodservice'],
        'Técnica de massa': ['#massadepizza', '#pizzaiolo'], 'Método': ['#vendasnowhatsapp', '#marketingdevendas'],
        'Atendimento': ['#atendimentoaocliente', '#deliverydepizza'], 'Gestão': ['#gestaodepizzaria', '#cmv'],
        'Canal próprio': ['#pedidodireto', '#delivery'], 'Bastidores': ['#bastidores', '#fotodecomida'], 'Relatório': ['#gestaodepizzaria', '#relatorio'], 'Bastidor': ['#bastidores', '#fotodecomida'], 'Chamada para diagnóstico': ['#diagnosticodepizzaria', '#consultoria'], 'Curiosidade': ['#curiosidadesdapizza', '#pizzalovers'], 'Dia da Pizza': ['#diadapizza', '#datacomemorativa'], 'Ferramenta grátis': ['#googlemeunegocio', '#marketinglocal'], 'Forno': ['#fornoalenha', '#pizzaiolo'], 'Insumo': ['#mussarela', '#insumos'], 'Resposta pronta': ['#atendimentoaocliente', '#whatsappbusiness']}
LOCAL = ['#saoluis', '#saoluisma', '#pizzariasaoluis', '#maranhao', '#slz']
NICHO = ['#pizzaria', '#pizzarias', '#donodepizzaria', '#empreendedorismogastronomico', '#pizza']
CTA = ('Quer saber o que trava a venda na SUA pizzaria? Peça o Raio-X da Orégano Turbo: chame no WhatsApp pelo link da bio '
       '(oreganoturbo.pages.dev) e a gente olha o seu Instagram, o cardápio e o caminho até o pedido com você.\n'
       'Orégano Turbo: marketing de vendas só para pizzarias, de São Luís/MA.')
fr = lambda t: [x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if x.strip()]
out = ['# Legendas SEO · Reels Orégano Turbo semana 1 (v2, 15/11/2026, conta Zuleide)\n', 'Gerado por `legendas_seo.py`. Aprovadas pelo Lindson em 15/11 (vídeos).\n']
for k, r in enumerate(R):
    fs = [f for f in fr(' '.join(r['blocos_voz'])) if 'Comenta' not in f and 'Marca quem' not in f]
    m = max(2, len(fs) // 2)
    tags = (TEMA.get(r['linha_editorial'], ['#marketingparapizzaria'])[:2] + [NICHO[k % 5], LOCAL[k % 5]])
    t = (f"{r['titulo']} 🍕\n\n{fs[0]} Se você é dono de pizzaria, isso mexe com o seu caixa toda semana.\n\n"
         f"▶ O que acontece\n{' '.join(fs[1:m])}\n\n▶ Na prática, na sua pizzaria\n{' '.join(fs[m:-1]) or fs[-1]}\n\n"
         f"▶ Conclusão\n{fs[-1]} Pizzaria que cresce cuida do produto e de como ele chega no cliente.\n\n"
         f"🎁 Comenta {r['cta_palavra']} que eu te mando: {r['entrega_no_video'].replace('Te mando ', '')}\n\n👉 {CTA}\n\n{' '.join(tags)}")
    assert len(t) <= 2200
    open(os.path.join(D, 'semana-1', r['id'][3:], 'legenda-seo.txt'), 'w').write(t)
    out.append(f"\n## {r['id']} · {r['post']['data']} {r['post']['hora']} · {r['linha_editorial']}\n\n**Título Shorts:** {r['titulo']}\n\n{t}\n")
open(os.path.join(D, 'LEGENDAS.md'), 'w').write('\n'.join(out))
print('ok', len(R))
