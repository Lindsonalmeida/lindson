# TikTok Orégano Turbo: gera LEGENDAS-TIKTOK.md dos 21 Reels aprovados e sobe no painel /painel/oregano (Aprovações).
# Idempotente; edita só o APROV do oregano.html publicado (não roda montador). Conta Zuleide, 15/11/2026.
import json, os, re, sys
T = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(T, '..', 'reels')
PRIV = sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida'
leg = open(os.path.join(R, 'LEGENDAS.md')).read()
TAGS = {'História da pizza': '#historiadapizza #pizzatok #donodepizzaria #saoluis',
 'Humor de dono': '#humordedono #donodepizzaria #pizzaria #saoluisma',
 'Raio-X': '#marketingparapizzaria #donodepizzaria #deliverydepizza #saoluis',
 'Dados do setor': '#mercadodepizza #donodepizzaria #empreendedorismo #nordeste',
 'Técnica de massa': '#massadepizza #pizzaiolo #pizzatok #donodepizzaria',
 'Método': '#marketingparapizzaria #vendasnodelivery #donodepizzaria #saoluis',
 'Forno': '#fornodepizza #pizzaiolo #pizzatok #donodepizzaria',
 'Resposta pronta': '#atendimentoaocliente #ifood #donodepizzaria #deliverydepizza',
 'Chamada para diagnóstico': '#marketingparapizzaria #donodepizzaria #pizzaria #saoluisma',
 'Gestão': '#gestaodepizzaria #cmv #donodepizzaria #empreendedorismo',
 'Curiosidade': '#curiosidades #pizzatok #pizzanapolitana #pizzaria',
 'Ferramenta grátis': '#googlemeunegocio #marketinglocal #donodepizzaria #saoluis',
 'Bastidor': '#bastidores #conteudoparapizzaria #pizzatok #donodepizzaria',
 'Insumo': '#queijoparapizza #pizzaiolo #pizzatok #donodepizzaria',
 'Dia da Pizza': '#diadapizza #datascomemorativas #donodepizzaria #pizzaria'}
HORA = {'12:10': '12h (almoço do dono)', '19:10': '19h (antes do pico)', '23:40': '23h40 (fechamento do forno)'}
SOM = {'Humor de dono': 'som em alta de "POV" no TikTok (volume baixo sob a voz)', 'Curiosidade': 'som em alta de "você sabia" (volume baixo)'}
out = ['# Legendas TikTok · 21 Reels Orégano Turbo (15/11/2026, conta Zuleide)', '',
 'Mesmos mp4 aprovados (`../reels/semana-1/`). Legenda curta: gancho + "comenta PALAVRA" ou link da bio. Sem preço e sem promessa. Som: o original do vídeo (voz Antonio + trilha); trend só onde indicado. Horário: o mesmo bloco do Reels (8h-21h preferido; 23h40 segue o calendário aprovado).', '']
items = []
for m in re.finditer(r'## (OT-\d\d) · (\S+) (\S+) · (.+?)\n\n\*\*Título Shorts:\*\* (.+?)\n(.*?)(?=\n## OT|\Z)', leg, re.S):
    id_, dia, hora, linha, tit, corpo = m.groups()
    pal = re.search(r'Comenta (\S+) que', corpo).group(1)
    cap = f'{tit} 🍕 Comenta {pal} que eu te mando o material. Raio-X da sua pizzaria no link da bio.'
    if len(cap) > 150: cap = f'{tit} 🍕 Comenta {pal} que eu te mando o material.'
    if len(cap) > 150: cap = f'{tit} 🍕 Comenta {pal}!'
    full = cap + '\n\n' + TAGS.get(linha, '#donodepizzaria #pizzaria #saoluis')
    som = SOM.get(linha, 'som original do vídeo')
    out += [f'## {id_} · {dia} · {linha}', '', '```', full, '```', '', f'- Caracteres da legenda: {len(cap)}', f'- Horário sugerido: {dia} às {HORA.get(hora, hora)}', f'- Som: {som}', '']
    items.append({'t': 'TikTok', 'tt': 1, 'titulo': f'TikTok · {id_} · {tit}', 'data': f'Postar {dia} · {HORA.get(hora, hora)}', 'linha': linha,
      'st': 'pendente', 'por': 'aguardando o Lindson', 'img': f'/painel/oregano/reels/{id_}-capa-p.jpg', 'video': f'/painel/oregano/reels/{id_}.mp4', 'legenda': full})
assert len(items) == 21, len(items)
open(os.path.join(T, 'LEGENDAS-TIKTOK.md'), 'w').write('\n'.join(out))
perfil = open(os.path.join(T, 'PERFIL.md')).read().split('## Para colar', 1)[1].strip()
items.insert(0, {'t': 'TikTok', 'tt': 1, 'titulo': 'TikTok · kit do perfil', 'data': 'Kit do perfil · 15/11 · conta Zuleide', 'linha': 'Perfil TikTok',
  'st': 'pendente', 'por': 'aguardando o Lindson', 'img': '/painel/oregano/tiktok/avatar-1080.png', 'baixar': '/painel/oregano/tiktok/avatar-1080.png', 'legenda': perfil})
os.makedirs(os.path.join(PRIV, 'painel/oregano/tiktok'), exist_ok=True)
import shutil; shutil.copy(os.path.join(T, '..', 'social/perfil/avatar-1080.png'), os.path.join(PRIV, 'painel/oregano/tiktok/avatar-1080.png'))
p = os.path.join(PRIV, 'painel', 'oregano.html'); s = open(p).read()
s = re.sub(r'\{"t": "TikTok", "tt": 1, .*?\},(?=\{)', '', s)
i = s.index('const APROV=') + len('const APROV=') + 1
s = s[:i] + ','.join(json.dumps(x, ensure_ascii=False) for x in items) + ',' + s[i:]
open(p, 'w').write(s); print(len(items), 'itens TikTok no painel')
