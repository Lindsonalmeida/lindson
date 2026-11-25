# Gera PLANO.md a partir do conteudo.py (conta Leandro, 25/11/2026)
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from conteudo import *
L = ['# Plano de Comunicação de Autoridade · Lindson Almeida, CEO · v1', '',
     '> Conta Leandro, 25/11/2026 · situação: **aguardando avaliação do Lindson** · PDF: `Plano de Autoridade - Lindson Almeida CEO v1.pdf` (26 p. 16:9, visual Al Kántara v2.1)', '',
     f'**Tese:** {TESE}', '', '## 1. Posicionamento', '', '### Personas']
L += [f'- **{n}:** {t}' for n, t in PERSONAS]
L += ['', '### Título por público', '| Público | Como se apresenta |', '|---|---|'] + [f'| {a} | {c} |' for a, b, c in TITULOS]
L += ['', '### Arquitetura', '- Nível 1, a pessoa: **Lindson Almeida**, fundador e CEO (autoridade e voz).', '- Nível 2, a casa: **Al Kántara Group** (Labs · Barzakh · Media · Ventures).',
      '- Prática pessoal, fora da vitrine do grupo: **Lindson Almeida · Estratégia Política** (mandatos e pré-campanha; dossiê e painel pela Labs, peças pela Barzakh; sem partido; um mandato por cidade).', '',
      '### De → para', '| Hoje | A partir de dezembro |', '|---|---|'] + [f'| {a} | {b} |' for a, b in DE_PARA]
L += ['', '### Prova de autoridade (só dado real)', '| Nº | O quê | Fonte |', '|---|---|---|'] + [f'| {n} | {t} | {f} |' for n, t, f in PROVAS]
L += ['', '## 2. Narrativa do fundador, manifesto e one-liner', ''] + [f'- **{a}:** {b}' for a, b in NARRATIVA]
L += ['', '**Manifesto**', ''] + [f'> {l}' for l in MANIFESTO] + ['', f'**One-liner:** {ONE_LINER}', '', f'**Assinatura do grupo:** {ASSINATURA}']
L += ['', '## 3. Auditoria dos pontos de contato', '| Ponto | O que derruba hoje | O que fazer |', '|---|---|---|'] + [f'| {a} | {b} | {c} |' for a, b, c in AUDITORIA]
L += ['', '## 4. O novo perfil', '', '### Instagram @lindsonalmeida_'] + [f'- **Bio {n}** (nome: {nm}):\n\n```\n{b}\n```' for n, nm, b in BIO_IG]
L += ['', '**Destaques:** ' + ' · '.join(f'{n} ({t})' for n, t in DESTAQUES), '', '### Os 9 primeiros posts (ordem de postagem)', '| # | Formato | Linha | Gancho | O que mostra |', '|---|---|---|---|---|']
L += [f'| {i+1} | {f} | {l} | {g} | {d} |' for i, (f, l, g, d) in enumerate(NOVE)] + ['', 'Fixar 9, 3 e 1. Reels gravados com a voz dele (nunca Antonio, nunca miniaturas 3D).']
L += ['', '### LinkedIn', f'- **Título:** {LINKEDIN_TIT}', f'- **Sobre:** {LINKEDIN_SOBRE}', '- URL /in/lindsonalmeida · página da empresa Al Kántara Group · datas de experiência: o Lindson preenche.']
L += ['', '### Padrão visual CEO premium', '- Cores: ' + ' · '.join(f'{n} {h} ({p})' for n, h, p in VISUAL_CORES)] + [f'- **{n}:** {t}' for n, t in COMPOSICOES] + ['- **Nunca:** ' + '; '.join(NUNCA)]
L += ['', '### Fotos: lote de 8 (Gemini; anexar 1 a 3 fotos do rosto)', f'**Bloco base (colar junto de cada cena):** {FOTO_BASE}', ''] + [f'{i+1}. **{n}:** {t}' for i, (n, t) in enumerate(FOTOS)]
L += ['', 'Conferir cada foto nos 8 critérios (`agencia/processos/conferencia-imagem-ia.md`) e registrar em `FOTOS-USADAS.md` como "lote CEO".']
L += ['', '## 5. Linhas editoriais e calendário'] + [f'- **{n} ({p})** · {o} · {f}: ' + '; '.join(x) for n, p, o, f, x in LINHAS]
L += ['', '| Dia | Formato · linha · pauta |', '|---|---|'] + [f'| {i+1} | {c} |' for i, c in enumerate(CAL)] + ['', '\\* só com autorização do cliente. Ritmo: 4 posts/semana, stories diários, LinkedIn 2×/semana.']
L += ['', '## 6. Receber os vereadores', '| Tempo | Etapa | Como |', '|---|---|---|'] + [f'| {a} | {b} | {c} |' for a, b, c in REUNIAO]
L += ['', '**Nunca dizer:** ' + '; '.join(NUNCA_DIZER), '', '### Kit de autoridade'] + [f'{i+1}. **{n}:** {t}' for i, (n, t) in enumerate(KIT)]
L += ['', '## 7. Plano de 90 dias'] + [f'- **{m} · {n}:** ' + '; '.join(it) for m, n, it in PLANO90]
L += ['', '| Eixo | Indicador | Meta |', '|---|---|---|'] + [f'| {a} | {b} | {c} |' for a, b, c in METAS]
L += ['', '## Time de agentes (o que cada um mudou)'] + [f'- **{n}** ({p}): {t}' for n, p, t in TIME]
L += ['', '## Decisões do Lindson'] + [f'{i+1}. **{n}:** {t}' for i, (n, t) in enumerate(DECISOES)]
L += ['', '## Limitações'] + [f'- {x}' for x in LIMITES]
L += ['', '## Como gerar de novo', '`python3 gerador/gerar.py && node gerador/render.js && python3 gerador/markdown.py` (precisa de `shapely`; fontes e logos vêm de `agencia/marca-holding/v2/`).']
open(os.path.dirname(H) + '/PLANO.md', 'w').write('\n'.join(L) + '\n')
