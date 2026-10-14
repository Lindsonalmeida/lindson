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
| `msg` | primeira mensagem de WhatsApp ou direct, na fórmula Prova, Presente e Pergunta do "não" |
| `ideias` | lista com as 2 ideias de vídeo para mandar quando a pessoa disser sim |
| `rot` | os 3 roteiros completos, no padrão de `ENTREGA.md` |
| `convite` | 2 linhas enviadas depois dos roteiros (oferta + pergunta calibrada), no padrão de `ENTREGA.md` |
| `src` | URL de onde vieram os dados |

## Como escrever a mensagem

Fórmula validada pelo Copy Master (Chris Voss + Alex Hormozi + Robert Cialdini): **Prova, Presente e Pergunta do "não"**.

1. **Prova (1 linha):** algo específico e verdadeiro do perfil (serviço, bairro, um post, a bio) + "aqui de São Luís". Mostra que você olhou de verdade.
2. **Presente (1 linha):** já entregue 1 ideia de vídeo concreta, com título entre aspas e o formato. Dar antes de pedir gera reciprocidade e prova competência.
3. **Pergunta do "não" (1 linha):** "Seria um problema eu te mandar mais 2 ideias assim?". É fácil responder "não, pode mandar", e quem responde entra no funil.

Regras: até 300 caracteres; sem "sou o Lindson, faço vídeo e tráfego"; sem preço; sem pedir reunião; sem criticar o perfil; no máximo 1 emoji. Use o primeiro nome do dono ou o nome do negócio.

Exemplo:
"Oi, Fabiana! Vi a aula experimental do studio aí no Vinhais, aqui de São Luís.
Tive uma ideia de Reels pra vocês: "3 sinais de que seu corpo está pedindo pilates", com você demonstrando cada um em 5 segundos.
Seria um problema eu te mandar mais 2 ideias assim?"

Campo extra `ideias`: as 2 ideias que serão enviadas quando a pessoa disser sim (cada uma com título e formato em 1 linha). Cada ideia precisa caber no negócio e no nicho.

### Follow-ups e resposta (o app mostra prontas)

- **Dia 2, sem resposta:** "Oi, [nome]! Separei as outras 2 ideias pra vocês. Mando por aqui ou prefere que eu deixe pra lá?"
- **Dia 5, sem resposta:** "[Nome], vou entender que vídeo pro Instagram não é prioridade agora, tudo certo. Se mudar, me chama aqui. Abraço!"
- **Quando disser sim:** mande as 2 ideias e feche com: "Essas 3 eu gravo num único dia com vocês e coloco anúncio pra quem mora perto. Posso te mostrar em 15 minutos como ficaria? Que dia é melhor, terça ou quinta?"

## Onde gravar

No banco do app Recomeço 90 (https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N):

- Lista do dia: coleção `data/users/me/prospec/dias`, **um documento por nicho**: id `AAAA-MM-DD_<nicho>` (data de São Luís), campos `{ "data": "AAAA-MM-DD", "ni": "<nicho>", "leads": [ ... ] }`. Assim cada documento fica abaixo do limite de 256 KB mesmo com os roteiros.
- Já vistos: coleção `data/users/me/prospec/vistos`, um documento por nicho (id do nicho), campo `ig` com a lista de @ já usados. Acrescente os novos sem apagar os antigos.

Os leads ficam só no banco do app, nunca neste repositório (ele é público).
