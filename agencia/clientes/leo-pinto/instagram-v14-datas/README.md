# Feed v14 · Datas comemorativas do Leo Pinto (15/11 a 01/01) · conta Lindson, 02/11/2026

**Situação (03/11):** **versão 3** (`gerar3.py`, atual): engenharia reversa do Designi e do Behance (`ENGENHARIA-REVERSA.md`, capturas em `referencias/`) aplicada: Anton nos títulos, Leo maior, cartão na frente do peito, cenários reais com véu (obra, sala de Natal, rua, fogos). Fora do painel até o Lindson aprovar. Versão 2 (`gerar2.py`), modelada nas referências que o Lindson mandou em 02/11 (Marcelo Tavares, Mara Costa, Givago, Pedro Henrique e outras campanhas). A 1ª tentativa foi descartada.

**Regras desta versão (decisões do Lindson, 02/11):**
- **Laranja é a cor principal** (partido); fundos alternam laranja e azul em xadrez no feed.
- **Logo aplicada direto no post**, sem balão/placa: versão original no azul e versão com letras marinho no laranja (`assets/logo-marinho.png`, gerada da logo oficial).
- **Pode usar imagem de banco** (gratuita): Natal = luzes desfocadas (Pexels 29754763), Ano Novo = fogos (Pexels 14957414), sempre com véu na cor da marca.
- Do modelo: assinatura fixa (@ com avatar no topo + logo na base esquerda), caixas de cor inclinadas, número gigante atrás do Leo, palavra repetida, cartão de lista e cartão de enquete, Leo sobreposto ao cartão. Sem estrelas, emojis ou adesivos.
- Revisado pelo design-squad (6 correções aplicadas). Prévia do feed na ordem de postagem: `previa-feed.jpg` (as tags de linha editorial aparecem na prévia e no painel, não na arte).
- Gerar: recortes `leo-27`, `leo-02`, `leo-10` (`../instagram-v12-feed/recortar.py`), `assets/avatar.jpg` = foto de perfil v2, `assets/logo.png`; depois `python3 gerar2.py . && node render.js $PWD && python3 feed.py . ../instagram-v13-apresentacao` (o `feed.py` lê `textos.json` com data e linha de cada post).

Plano que continua valendo (posts, linha editorial e alternância foto × só logo):
| Ordem | Data | Linha editorial | Foto ou só logo |
|---|---|---|---|
| 1 | 15/11 Proclamação da República | Mandato que entrega | foto (leo-27, mãos abertas) |
| 2 | 20/11 Consciência Negra | Nossa Baixada | só logo |
| 3 | 11/12 Dia do Engenheiro | Mandato que entrega | foto (leo-02, mão no queixo) |
| 4 | 25/12 Natal | Leo de perto | foto de banco (luzes de Natal) |
| 5 | 31/12 Véspera de Ano Novo | Voz do povo | foto (leo-10, celular) |
| 6 | 01/01 Ano Novo | A cidade que eu sonho | foto de banco (fogos) |

São 6 posts (múltiplo de 3) para a apresentação v13 continuar alinhada na grade. A tag da linha editorial aparece na prévia do feed e no card de aprovação, não na arte publicada.
Aprovações: os 6 posts estão no painel do Leo (Central) com a tag da linha editorial e a legenda.
