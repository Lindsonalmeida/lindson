"""Kit Instagram + TikTok dos Shorts do Raposa e Leão (conta Leandro, 15/11/2026).
Entrada: shorts-base.json (extraído do dados.js da Central). Saída: kit.json, KIT.md e
/home/user/centrallindsonalmeida/painel/canais/raposa/postagens-instagram-tiktok.html"""
import json, os, re, sys, html, datetime as dt
AQUI = os.path.dirname(os.path.abspath(__file__))
PRIV = sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida'
base = json.load(open(os.path.join(AQUI, 'shorts-base.json'), encoding='utf-8'))
NICHO = ['#filosofia', '#estrategia', '#lideranca', '#desenvolvimentopessoal', '#mentalidade', '#poder', '#psicologia', '#historia']
LOCAL = ['#oprincipe', '#livros', '#leitura', '#dicasdelivros', '#filosofiabrasil']
TT_FIXO = ['#maquiavel', '#filosofiatiktok', '#aprendanotiktok', '#booktokbrasil', '#estrategia', '#poder', '#mentalidade', '#historia']
CTA = ['Salva para lembrar na hora certa e manda para quem precisa ouvir isso.',
       'Manda para aquele amigo que vive caindo nessa.',
       'Salva este post: ele vale mais na próxima decisão difícil.',
       'Compartilha com quem lidera um time ou um negócio.']
VIDA = ['Na sua vida\nPense numa situação desta semana, no trabalho, na família ou no negócio, em que essa regra já apareceu.',
        'Na prática\nMaquiavel não escreveu manual de maldade. Escreveu como o poder funciona, para quem não quer ser pego de surpresa.',
        'Para levar com você\nLeia de novo a frase acima e pense em quem, perto de você, age exatamente assim.',
        'Por que isso importa\nQuem entende a regra decide com calma. Quem ignora só percebe quando o prejuízo já chegou.',
        'Aplicando hoje\nAntes da próxima conversa difícil, lembre desta ideia e veja se ela muda sua jogada.']
INICIO = dt.date(2026, 11, 16); HORAS = ['12h', '19h']
kit = []
for n, s in enumerate(base):
    tit = s['titulo'].replace('#shorts', '').strip()
    corpo = s['legenda'].split('\n\n#')[0].strip()
    linhas = [l for l in corpo.split('\n') if l.strip()]
    fonte = next((l for l in linhas if 'Fonte' in l), '📜 Fonte: Nicolau Maquiavel.')
    texto = [l for l in linhas if 'Fonte' not in l and 'Raposa e Leão:' not in l and not l.startswith('#')]
    yt = [t for t in re.findall(r'#\w+', s['legenda']) if t not in ('#maquiavel', '#shorts')]
    tags = ['#maquiavel'] + yt[:2] + [NICHO[n % len(NICHO)], LOCAL[n % len(LOCAL)]]
    tags = list(dict.fromkeys(tags))[:5]
    ig = (f"{tit.upper()}\n\n{texto[0]}\n\n" +
          (("O que Maquiavel quis dizer\n" + '\n'.join(texto[1:]) + "\n\n") if texto[1:] else '') +
          VIDA[n % len(VIDA)] + "\n\n" +
          f"{fonte}\n\n💬 {s['comentario']}\n{CTA[n % len(CTA)]}\n\n"
          f"🦊🦁 Raposa e Leão: Maquiavel aplicado à vida real. Vídeos longos no YouTube (link na bio).\n\n" + ' '.join(tags))
    ttags = ['#maquiavel'] + yt[:1] + [TT_FIXO[1 + n % 3], TT_FIXO[4 + n % 4]]
    tk = f"{tit} 🦊🦁 {s['comentario']}\n" + ' '.join(dict.fromkeys(ttags))
    slot = n if n < 30 else None
    quando = (f"{(INICIO + dt.timedelta(days=slot // 2)).strftime('%d/%m')} às {HORAS[slot % 2]}" if slot is not None else 'reserva (dia 16+)')
    kit.append({'id': s['id'], 'ordem': n + 1, 'titulo': tit, 'quando': quando, 'dur': s.get('dur'),
                'capa': s['capas'][0]['url'] if s.get('capas') else None,
                'video': (s.get('video') or {}).get('url'), 'app': (s.get('video') or {}).get('app'),
                'instagram': ig[:2200], 'tiktok': tk, 'comentario': s['comentario']})
PERFIL = {
 'bio_instagram': "🦊🦁 Raposa e Leão\nMaquiavel e as leis do poder aplicadas à vida real\n📜 Tudo com a fonte: O Príncipe e Discursos\n▶️ Vídeos completos no YouTube 👇",
 'bio_tiktok': "Maquiavel aplicado à vida real 🦊🦁 Fonte em todo vídeo. Completo no YouTube 👇",
 'nome_perfil': 'Raposa e Leão | Maquiavel', 'arroba': '@raposaeleao (confirmar se está livre; mesmo @ do YouTube)',
 'link_bio': 'Canal do YouTube @RaposaeLeao',
 'destaques': [['Comece aqui', 'Quem foi Maquiavel e o que é o canal (shorts 01 e 02)'],
               ['Temido ou amado', 'Shorts sobre liderança e autoridade (03, 05, 35)'],
               ['Raposa', 'Astúcia, aparência e estratégia (10, 18, 25)'],
               ['Leão', 'Força, disciplina e preparo (14, 27, 36)'],
               ['Negócios', 'Maquiavel na empresa (31, 33, 34)'],
               ['Fontes', 'Capítulos de O Príncipe e dos Discursos citados']],
 'capa_destaque': 'Fundo escuro, ícone dourado simples, mesma paleta da IDENTIDADE.md (sem criar estilo novo)'}
json.dump({'perfil': PERFIL, 'posts': kit}, open(os.path.join(AQUI, 'kit.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
md = ['# Raposa e Leão · kit Instagram e TikTok (conta Leandro, 15/11/2026)', '',
      'Gerado por `montar_redes.py`. 40 Shorts: 30 na agenda (2 por dia, 16/11 a 30/11, 12h e 19h) e 10 de reserva. Vídeo e capa são os mesmos do YouTube (app de postagem da Central).', '',
      '**Falta (Lindson):** criar/confirmar o @ no Instagram e no TikTok e logar no Metricool ou postar pelo celular.', '',
      '## Perfil', f"- Nome: {PERFIL['nome_perfil']}", f"- @: {PERFIL['arroba']}", '- Bio Instagram:', '```', PERFIL['bio_instagram'], '```',
      f"- Bio TikTok: {PERFIL['bio_tiktok']}", '- Destaques: ' + '; '.join(f'**{a}** ({b})' for a, b in PERFIL['destaques']), '', '## Agenda', '| # | Short | Quando |', '|---|---|---|']
md += [f"| {k['ordem']} | {k['id']} · {k['titulo']} | {k['quando']} |" for k in kit]
md += ['', 'Legendas completas: `kit.json` e página `painel/canais/raposa/postagens-instagram-tiktok.html` (privado).']
open(os.path.join(AQUI, 'KIT.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
E = html.escape
cards = []
for k in kit:
    v = f'<a href="{E(k["video"])}" download>Baixar vídeo</a>' if k['video'] else f'<a href="{E(k["app"] or "#")}" target="_blank">Vídeo no app</a>'
    cards.append(f'''<article><img src="{E(k['capa'] or '')}" alt="" loading="lazy"><div><p class="q">#{k['ordem']} · {E(k['quando'])} · {E(k['dur'] or '')}</p><h2>{E(k['titulo'])}</h2>{v}
<h3>Instagram</h3><pre>{E(k['instagram'])}</pre><button onclick="cp(this)">Copiar Instagram</button>
<h3>TikTok</h3><pre>{E(k['tiktok'])}</pre><button onclick="cp(this)">Copiar TikTok</button></div></article>''')
dest = '\n'.join(f'<li><b>{E(a)}</b>: {E(b)}</li>' for a, b in PERFIL['destaques'])
pg = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Postagens Instagram e TikTok</title>
<style>:root{{--bg:#0e0d0b;--card:#1a1814;--ouro:#c9a24a;--tx:#ece6d8;--mut:#9a927f}}body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 system-ui,sans-serif;padding:16px}}
main{{max-width:980px;margin:auto}}h1{{color:var(--ouro);font-size:24px}}article{{display:flex;gap:16px;background:var(--card);border-radius:12px;padding:14px;margin:14px 0;flex-wrap:wrap}}
article img{{width:150px;border-radius:8px;align-self:flex-start}}article>div{{flex:1;min-width:240px}}pre{{white-space:pre-wrap;background:#0006;padding:10px;border-radius:8px;font:13px/1.45 system-ui}}
.q{{color:var(--ouro);margin:0;font-size:13px}}h2{{margin:4px 0 6px;font-size:18px}}h3{{margin:10px 0 2px;font-size:14px;color:var(--mut)}}a{{color:var(--ouro)}}button{{background:var(--ouro);border:0;border-radius:6px;padding:6px 12px;cursor:pointer}}</style></head>
<body><main><h1>Raposa e Leão · Postagens Instagram e TikTok</h1><p>40 Shorts com legenda própria para cada rede. Agenda: 2 por dia, 16/11 a 30/11 (12h e 19h); #31 a #40 são reserva. <b>Falta o Lindson:</b> criar/confirmar o @ e logar no Metricool ou postar pelo celular.</p>
<h2>Perfil</h2><p><b>Nome:</b> {E(PERFIL['nome_perfil'])} · <b>@:</b> {E(PERFIL['arroba'])}</p><pre>{E(PERFIL['bio_instagram'])}</pre><button onclick="cp(this)">Copiar bio Instagram</button>
<pre>{E(PERFIL['bio_tiktok'])}</pre><button onclick="cp(this)">Copiar bio TikTok</button><h3>Destaques</h3><ul>{dest}</ul>
{''.join(cards)}</main><script>function cp(b){{var t=b.previousElementSibling.textContent;try{{navigator.clipboard.writeText(t);b.textContent='Copiado'}}catch(e){{}}}}</script></body></html>'''
out = os.path.join(PRIV, 'painel', 'canais', 'raposa', 'postagens-instagram-tiktok.html')
open(out, 'w', encoding='utf-8').write(pg); print('ok', len(kit), out, max(len(k['instagram']) for k in kit))
