# Rotina de prospecção diária

Todo dia, 10 leads novos por nicho (100 no total) de negócios da Grande São Luís (São Luís, São José de Ribamar, Paço do Lumiar e Raposa), com análise inicial e mensagem pronta. A lista vai para o app Recomeço 90 (aba Funil → Lista do dia).

## Nichos

| id | Nicho | Buscas sugeridas |
|---|---|---|
| `estetica` | Clínicas de estética e harmonização | clínica estética, harmonização facial, depilação a laser, biomédica esteta |
| `odonto` | Odontologia | clínica odontológica, implante dentário, lente de contato dental, ortodontista |
| `imob` | Imobiliárias e corretores | imobiliária, corretor de imóveis, lançamento imobiliário |
| `planejados` | Móveis planejados e arquitetura | móveis planejados, marcenaria, arquiteta, design de interiores |
| `medicos` | Médicos e clínicas particulares | dermatologista, nutricionista, ginecologista, clínica médica particular |
| `plastica` | Cirurgia plástica e procedimentos | cirurgião plástico, cirurgia plástica, lipo, mamoplastia |
| `academias` | Academias, pilates e funcional | academia, studio de pilates, crossfit, treino funcional |
| `moda` | Boutiques e lojas de moda | boutique, loja de roupas femininas, moda fitness, loja de calçados |
| `beleza` | Salões e barbearias premium | salão de beleza, barbearia, nail designer, studio de cílios |
| `food` | Hamburguerias, restaurantes e delivery | hamburgueria, restaurante, açaí, delivery, confeitaria |

## Como pesquisar

- Use a busca na web (modo extended), por exemplo: `"São Luís" clínica estética instagram.com`, `site:instagram.com hamburgueria "São Luís"`, ou o nome de um bairro (Renascença, Calhau, Cohama, Ponta d'Areia, Turu, Cohab, Olho d'Água, Ponta do Farol, Jardim Eldorado).
- O Instagram não abre diretamente. Os dados vêm dos resultados de busca (bio, seguidores), do site do negócio, do Linktree, do Google e de guias como Solutudo, Apontador e Guia Mais.
- Abra o site ou o link da bio quando houver, para achar WhatsApp e e-mail.

## Regras

- **Nunca invente dados.** Campo não encontrado = `null`. O WhatsApp só entra se aparecer escrito em alguma fonte.
- Só negócios reais e ativos da Grande São Luís. Descarte perfis de outras cidades, franquias nacionais sem perfil local e perfis pessoais sem negócio.
- Não repita o mesmo `@` de dias anteriores (veja a lista de vistos de cada nicho).
- Prefira negócios com sinal de oportunidade: poucos seguidores para o porte, bio sem WhatsApp, sem link, sem Reels, posts parados ou visual amador.

## Campos de cada lead

| Campo | O que é |
|---|---|
| `id` | `<nicho>-<ig>` (ou `<nicho>-<nome-sem-espaco>` se não tiver Instagram) |
| `ni` | id do nicho |
| `n` | nome do negócio |
| `ig` | @ sem a arroba |
| `sg` | seguidores (número) ou `null` |
| `bio` | resumo curto da bio ou da descrição |
| `wa` | WhatsApp só com dígitos, com DDD (ex.: `98988887777`) |
| `tel` | outro telefone, se houver |
| `em` | e-mail |
| `site` | site ou link da bio |
| `bai` | bairro ou cidade |
| `an` | análise inicial em 1 ou 2 frases: o ponto fraco ou a oportunidade que dá para vender |
| `nota` | 1 a 5: quanto este lead tem cara de cliente agora |
| `pl` | plano sugerido: `video`, `trafego`, `alcance`, `presenca` ou `iqv` |
| `msg` | primeira mensagem de WhatsApp ou direct, personalizada |
| `src` | URL de onde vieram os dados |

## Como escrever a mensagem

- Curta (até 4 linhas), em tom de conversa, assinada como Lindson.
- Cite algo específico do perfil (um serviço, o bairro, a bio).
- Aponte uma oportunidade, sem criticar e sem falar de preço.
- Termine com uma pergunta fácil de responder.
- Exemplo: "Oi, [nome]! Sou o Lindson, faço vídeo e tráfego aqui em São Luís. Vi que vocês fazem harmonização no Calhau, mas o perfil quase não tem Reels mostrando resultado. Tenho uma ideia de 3 vídeos que trariam paciente pelo WhatsApp. Posso te mostrar?"

## Onde gravar

No banco do app Recomeço 90 (https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N):

- Lista do dia: coleção `data/users/me/prospec/dias`, documento `AAAA-MM-DD` (data de São Luís), campos `{ "data": "AAAA-MM-DD", "leads": [ ... ] }`.
- Já vistos: coleção `data/users/me/prospec/vistos`, um documento por nicho (id do nicho), campo `ig` com a lista de @ já usados. Acrescente os novos sem apagar os antigos.

Os leads ficam só no banco do app, nunca neste repositório (ele é público).
