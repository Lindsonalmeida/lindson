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
| `msg` | primeira mensagem, abordagem única para aquele negócio |
| `ideias` | lista com as 2 ideias de vídeo para mandar quando a pessoa disser sim |
| `ent` | a entrega: `{ "tipo": "campanha" \| "roteiros" \| "google", "titulo": ..., "texto": ... }`, com o texto pronto para WhatsApp, no padrão de `ENTREGA.md` |
| `rot` | os 3 roteiros, só quando `ent.tipo` for `roteiros` |
| `convite` | 2 linhas enviadas depois dos roteiros (oferta + pergunta calibrada), no padrão de `ENTREGA.md` |
| `src` | URL de onde vieram os dados |

## Como escrever a mensagem: Conexão, Dor, Desejo
A mensagem tem que ser entendida numa única leitura por um dono de negócio comum. Fale como uma pessoa fala no WhatsApp. Até 280 caracteres, 3 ou 4 linhas curtas:
1. CONEXÃO: saudação simples + quem é. Ex.: "Oi, Dra. Paula! Tudo bem? Sou o Lindson, aqui de São Luís." (varie: "Aqui é o Lindson.", "Meu nome é Lindson.")
2. DOR: uma frase com uma dor real e comum do nicho, dita na língua do dono, que faça ele pensar "isso acontece comigo". Ex.: "O paciente pede orçamento de implante, diz que vai pensar… e não volta mais." / "Sábado lotado e terça vazia: conheço bem essa agenda." / "O cliente chama, pergunta o preço do imóvel… e some."
3. DESEJO: o resultado que ele quer + como o Lindson ajuda, em palavras simples. Ex.: "Eu ajudo clínicas a ter paciente novo chegando toda semana, com anúncio e atendimento no WhatsApp."
4. PERGUNTA de sim: "Posso te mostrar como faria pra vocês?" / "Quer que eu te mostre?" / "Posso te mandar como funciona?"
Use o nome do negócio ou do dono na saudação. Um detalhe do lead só entra se for simples e do negócio (o serviço principal ou o bairro), nunca da vida pessoal.
PROIBIDO: "vi que", "parece que", "gargalo", "desenho de campanha", "plateia", "o que costuma travar", frases de efeito, jargão de marketing, análise do perfil, elogio genérico, citar número de seguidores ou posts, pergunta difícil de responder. Também proibido: preço, link, pedir reunião, prometer número de clientes, criticar o perfil, inventar fatos, mais de 1 emoji. Saúde: sem promessa de resultado. Teste final de cada msg: se o dono precisar ler duas vezes pra entender, reescreva. Varie a dor e a abertura entre os leads do mesmo nicho.

### A entrega (quando disser sim)

O material é escolhido pelo que mais aproxima aquele negócio do objetivo, no padrão de `ENTREGA.md`:

- **campanha:** plano de captação (Meta Ads na era Andromeda e/ou Google), para quem precisa de cliente novo agora.
- **roteiros:** 3 roteiros de vídeo em cascata, para quem precisa ser visto e gerar confiança.
- **google:** plano de Google Meu Negócio + Google Ads, para negócios que o cliente procura na hora da necessidade (urgência, serviço local).

### Follow-ups (o app mostra prontos)

- **Dia 2:** "Oi, [nome]! O plano pra vocês tá pronto aqui. Mando por aqui ou prefere que eu deixe pra lá?"
- **Dia 5:** "[Nome], vou entender que isso não é prioridade agora, tudo certo. Se mudar, me chama aqui. Abraço!"

## Onde gravar

No banco do app Recomeço 90 (https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N):

- Lista do dia: coleção `data/users/me/prospec/dias`, **um documento por nicho**: id `AAAA-MM-DD_<nicho>` (data de São Luís), campos `{ "data": "AAAA-MM-DD", "ni": "<nicho>", "leads": [ ... ] }`. Assim cada documento fica abaixo do limite de 256 KB mesmo com os roteiros.
- Já vistos: coleção `data/users/me/prospec/vistos`, um documento por nicho (id do nicho), campo `ig` com a lista de @ já usados. Acrescente os novos sem apagar os antigos.

Os leads ficam só no banco do app, nunca neste repositório (ele é público).
