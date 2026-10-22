# Esteira de conteúdo: Reels diários

Todo dia de manhã, uma tarefa automática escreve **5 roteiros de Reels de 30 segundos** e grava no app Recomeço 90, aba **Conteúdo** (https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N).

## O teste

Plano em `teste-01-reels.json` (cópia no banco do app: `data/users/me/conteudo/planos`, doc `teste-01`).

- **3 formatos:** Reels falado · Nunca × Em vez disso · Isso parece X, mas é Y
- **10 conteúdos por formato** (30 no total, cada um ligado a uma dor de `agencia/ofertas/dores-e-desejos.md`)
- **10 ganchos por conteúdo** (os mesmos 10 modelos de gancho em todos, para comparar)
- **300 roteiros**, 5 por dia, 60 dias.

**Ordem (k = 0 a 299):** gancho = k ÷ 30; posição = k % 30; formato = posição % 3; conteúdo = posição ÷ 3 (dentro do formato). Os 6 primeiros dias passam pelos 30 conteúdos com o gancho 1; os 6 seguintes, com o gancho 2; e assim por diante.

**Como medir:** 24 horas depois de postar, anotar no app visualizações, envios e salvos. O app ranqueia formatos, ganchos e conteúdos por **envios a cada mil visualizações** (o sinal que mais leva o Reel para quem não segue).

## Regras de cada roteiro

- 30 segundos falados: de 70 a 90 palavras somando gancho, falas e chamada.
- **Gancho (0 a 3s):** o modelo do gancho aplicado ao conteúdo, em versão negativa (o erro, a perda, o mito), sem atacar o cliente.
- **Texto na tela:** até 10 palavras, reforça o gancho.
- **Falas:** 3 ou 4 frases curtas, linguagem de WhatsApp, entendida numa leitura. Sempre entregar a solução.
- **Chamada final:** pedir envio ("manda pra quem...") ou salvamento. No formato Nunca × Em vez disso, a chamada é o último par.
- **Legenda:** padrão blog SEO do repositório (título com palavra-chave, introdução, subtítulos, exemplo, conclusão, chamada, 3 a 5 hashtags variadas: tema + nicho + local), até 2.200 caracteres.
- **Gravação:** uma dica prática de como gravar.
- Público: dono de negócio local. Nunca inventar números, nunca prometer resultado, sem jargão de marketing, sem "vi que", "parece que" (fora do formato Isso parece X, mas é Y) ou "gargalo".

## Campos (documento `data/users/me/conteudo/dias`, id `AAAA-MM-DD`)

`{ "data", "teste", "roteiros": [ { id: "teste-01-k###", k, f, fn, c, cn, g, gn, gancho, tela, fala: [...], cta, legenda, grav, seg: 30 } ] }`
