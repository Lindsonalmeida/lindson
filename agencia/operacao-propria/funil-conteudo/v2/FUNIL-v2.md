# Funil de conteúdo v2 · Orégano Turbo (conta Leandro, 23/11/2026)

> **v2 = melhorias pedidas pelo Lindson em 23/11.** A v1 (`../FUNIL.md`) fica como ANTERIOR: persona, etapas topo/meio/fundo, bio, destaques, stories e automação continuam valendo, exceto o que esta página troca. Regras: `../PADRAO.md` (sem promessa, sem número inventado, preço "a partir de").

## O que muda em relação à v1
| # | Melhoria | Resumo |
|---|---|---|
| 1 | Pizzarias Fundadoras | 2 a 3 pizzarias, condição especial em troca de case e depoimento autorizados por escrito |
| 2 | Ritmo | **2 Reels/dia** (60 no mês), cada um reaproveitado em Shorts e TikTok (`CALENDARIO-30-DIAS-v2.md`) |
| 3 | Isca escalável | **Raio-X automático** (formulário → nota + 3 ajustes); o Raio-X em vídeo vira etapa premium |
| 4 | Remarketing | Públicos de quem viu 50%, engajou ou visitou o perfil |
| 5 | Ganchos A/B | 2 ganchos por tema + rotina semanal de repetir o vencedor |
| 6 | Parcerias | Fornecedores locais e collab com pizzarias |
| 7 | Painel de métricas | Aba "Métricas por Reel" + rotina de corte toda segunda |

Os 5 roteiros prontos (`../ROTEIROS-OT31-35.md`) continuam valendo e estão no calendário v2. Na v2 eles viram OT-31 TAXA (26/11), OT-32 RAIO-X (26/11), OT-33 FOTO (27/11), OT-34 CARO (27/11) e OT-35 SUMIU (28/11): mesmo roteiro, só muda a numeração. No OT-32 (Raio-X), a CTA passa a ser "comenta RAIO-X e recebe o link da nota do seu Instagram".

---

## 1. Programa "Pizzarias Fundadoras"
**Para quê:** hoje não existe case real. Sem case, o meio do funil se apoia em exemplo montado. As fundadoras viram a prova do funil.

**Oferta (Hormozi, sem inventar preço novo):**
- **Vagas:** 2 a 3 pizzarias (o número dito em público é o que for real no dia; quando acabar, para de falar).
- **Condição especial:** o preço do plano anual pagando no prazo semestral (decisão 6 de `../../DECISOES-APROVADAS.md`), com o Raio-X em vídeo incluso. Planos a partir de R$ 1.597/mês; o valor fecha na conversa.
- **Em troca:** (a) autorização escrita para mostrar o antes e o depois (perfil, cardápio, fotos, anúncios) e os números do painel; (b) um depoimento em vídeo no 3º mês, **só se a pizzaria quiser e se estiver satisfeita**. Ninguém é obrigado a dizer que deu resultado.
- **Régua:** a mesma do SDR (`../../sdr/PUBLICO-ALVO.md`): delivery ativo, Instagram ativo e sinal de porte.
- **Sem garantia de resultado.** A garantia é só de entrega, nas condições já aprovadas.

**Termo de autorização (simples, conferir com advogado):**
> Eu, [nome], responsável pela [pizzaria], CNPJ [ ], autorizo a Orégano Turbo a usar, em redes sociais, site, anúncios e apresentações comerciais: o nome e a marca da pizzaria; imagens do perfil, cardápio, fotos e anúncios de antes e depois do trabalho; e os números de pedidos e alcance do painel, a partir de [data]. Posso revogar esta autorização a qualquer momento, por escrito, e o material deixa de ser publicado em até 7 dias (o que já foi publicado sai do ar). O depoimento em vídeo é opcional e só será usado se eu aprovar o vídeo final. Não recebo pagamento pelo uso, além da condição de fundadora do contrato nº [ ]. [cidade], [data]. Assinatura: ______

**Roteiro do depoimento (60 a 90 s, celular na vertical, na pizzaria, luz do dia):**
1. "Meu nome é…, sou dono(a) da… há … anos, em [bairro]." (5 s)
2. "Antes, o meu problema era…" (com as palavras dele, sem roteiro decorado) (15 s)
3. "Por que eu topei trabalhar com a Orégano?" (10 s)
4. "O que mudou no dia a dia: …" (o que ele viu de fato; número só se estiver no painel) (20 s)
5. "Para quem está pensando, eu diria…" (10 s)
- Regras: não sugerir frases de resultado; não cortar para mudar o sentido; legenda "depoimento real de cliente fundadora"; ele aprova o corte final.

**No funil:** o meio ganha a linha "Diário da fundadora" (bastidor semanal autorizado) a partir da 1ª assinatura. Até lá, o calendário v2 usa os temas FUNDADORA (vagas e troca).

## 2. Ritmo: 2 Reels/dia + Shorts + TikTok
- 60 Reels no mês, 12:10 e 20:10 (dentro da janela 8h-21h). Conta: 42 de conteúdo e 18 de venda (70/30).
- Mais tempo por vídeo para subir a qualidade: vídeo real de pizza, Seu Turbo animado e edição no padrão aprovado (SFX, trilha, -14 LUFS).
- Cada Reel sai também como **Shorts** (YouTube @oreganoturbo, +2 h) e **TikTok** (+4 h), com o gancho B. Mesma identidade nos 3 canais (regra de 15/11).
- Calendário: `CALENDARIO-30-DIAS-v2.md` (+ `calendario-v2.json`).

## 3. Isca escalável: Raio-X automático
**O quê:** página `oreganoturbo.pages.dev/raio-x` (repo `Lindsonalmeida/oreganoturbo`, Cloudflare Pages) com um formulário de 10 perguntas que devolve na hora uma **nota de 0 a 100 do Instagram da pizzaria** e os **3 ajustes mais importantes**, em ordem. Feito pelo Webdesigner + Builder no visual v4 da Orégano.

**Perguntas (sim/não ou múltipla escolha; o @ é obrigatório):**
| # | Pergunta | Peso |
|---|---|---|
| 1 | @ do Instagram, nome, cidade e WhatsApp | (cadastro) |
| 2 | A bio diz o que vocês vendem, o bairro e como pedir? | 12 |
| 3 | Tem link na bio que abre o WhatsApp ou o cardápio direto? | 14 |
| 4 | As fotos das pizzas são feitas com luz natural, de perto? | 12 |
| 5 | Quantos Reels por semana? (0 / 1-2 / 3+) | 12 |
| 6 | Os stories mostram preço e como pedir? | 10 |
| 7 | Os destaques têm cardápio, entrega e avaliações? | 8 |
| 8 | Em quanto tempo respondem o WhatsApp? (até 5 min / até 30 / mais) | 12 |
| 9 | O Google Meu Negócio tem fotos e horário atualizados? | 10 |
| 10 | Vocês sabem quantos pedidos vieram do Instagram no mês? | 10 |

**Lógica da nota:** soma dos pesos (sim = peso cheio; resposta do meio = metade; não = 0), de 0 a 100. É **autoavaliação**: a página diz isso ("nota baseada nas suas respostas"). Faixas: até 49 "o perfil está travando pedidos"; 50 a 74 "tem base, falta caminho até o pedido"; 75 ou mais "pronto para anúncio".
**Os 3 ajustes:** as 3 perguntas de maior peso que ficaram com 0 (ou metade), cada uma com 1 frase do que fazer e o Reel da Orégano que ensina (ex.: link na bio → OT "3 erros de bio").

**Ligação com o SDR:** ao enviar, a página faz `POST /api/sdr-oregano` com @, WhatsApp, nota, respostas e origem (palavra do Reel ou `?ref=`). O lead entra no SDR VIRTÙ na etapa "Novo" com a nota, e a cadência D+3/D+6/D+9 já usa a nota na mensagem. A tela final tem o botão WhatsApp: "Quero o Raio-X em vídeo do meu perfil".

**Escada:** Raio-X automático (grátis, ilimitado) → **Raio-X em vídeo** (etapa premium: grátis só para quem passa na régua do SDR; para os outros, a partir de R$ 297, abatido no 1º mês se fechar em 7 dias) → plano.

## 4. Remarketing (Pedro Sobral) · estrutura e verba como HIPÓTESE
| Público (Meta, 30 dias) | Anúncio | Objetivo |
|---|---|---|
| R1: viu 50% de qualquer Reel | Reel "Nota do seu Instagram em 2 minutos" → página do Raio-X automático | Cadastro (lead) |
| R2: engajou com o perfil (comentou, salvou, mandou DM) | Reel do Raio-X em vídeo/fundadoras → WhatsApp | Mensagens |
| R3: visitou o perfil e não mandou mensagem | Reel "Por que só pizzaria" + depoimento (quando existir) → WhatsApp | Mensagens |
| Exclusão | Quem já está no SDR (lista de clientes enviada) e clientes ativos | — |

- **Verba (hipótese, dentro dos R$ 30/dia aprovados):** R$ 15 para impulsionar o Reel de topo vencedor (público frio de donos de restaurante/pizzaria no Nordeste) e R$ 15 para o remarketing (R1 R$ 7, R2 R$ 5, R3 R$ 3). Os públicos de remarketing precisam de volume para rodar: abaixo de uns 1.000 usuários, junte R1+R2+R3 num público só.
- **Corte:** a regra da decisão 19 continua (sobe só com custo por diagnóstico abaixo de R$ 150). O número real vem do relatório de segunda; nada estimado vai como fato.

## 5. Testes de gancho A/B
- Cada tema do calendário v2 tem **Gancho A** (Instagram) e **Gancho B** (TikTok/Shorts). Mesmo vídeo; muda só a frase da tela no 1º segundo e a 1ª fala.
- **Toda segunda (15 min):** comparar retenção aos 3 s e compartilhamentos de A × B por tema, com pelo menos 48 h no ar. O vencedor vira o gancho padrão daquele tipo; o formato (POV, pergunta, número, choque) que ganhar 2 semanas seguidas ganha +1 Reel na semana seguinte, tirando do formato que perdeu.
- Registro na aba de métricas (seção 7), coluna "gancho vencedor".

## 6. Parcerias
**Fornecedores locais (São Luís primeiro):** farinha e insumos (distribuidora de farinha, queijo, embutidos), fornos e equipamentos (venda e manutenção de forno a lenha/elétrico), embalagens (caixa de pizza personalizada, sacola térmica), delivery (motoboys/cooperativas, apps regionais), cardápio digital e sistema de pedidos, bebidas (distribuidora local).
- **O que propor:** Reel collab (os 2 perfis no mesmo post) com conteúdo útil para o dono (ex.: "a farinha certa para massa que não encolhe", "caixa que chega quente"), sem pagamento dos dois lados, e indicação mútua só quando fizer sentido.
- **Collab com pizzarias:** Reels de bastidor em pizzarias da cidade (fora da concorrência direta de um cliente com exclusividade de bairro), com o dono como protagonista. Vira prova social do nicho e porta para o SDR.

**Mensagem de convite (PADRAO-COPY: Conexão → Dor → Desejo → Pergunta):**
> Oi, [nome]! Aqui é o Lindson, da Orégano Turbo, a gente faz marketing só para pizzaria. Dono de pizzaria vive perguntando sobre [farinha/forno/caixa] e quase ninguém explica direito. Pensei num Reel junto: você ensina, a gente grava e edita, e sai nos dois perfis. Topa conversar?

**Para pizzaria:**
> Oi, [nome]! Sou o Lindson, da Orégano Turbo, a gente só trabalha com pizzaria. Tô gravando bastidores de pizzarias de São Luís pra mostrar quem faz pizza de verdade. A gente grava em 1 hora e você usa o vídeo no seu perfil também. Posso te mandar como funciona?

## 7. Painel de métricas · aba "Métricas por Reel"
**Onde:** nova aba em `/painel/oregano` (Builder: dados no KV, mesma API do SDR), com cópia em planilha CSV para download. Até a aba ficar pronta: planilha `metricas-reels.csv` no privado `painel/oregano/funil/`.
**Colunas (1 linha por Reel):** id · data · tema · etapa · gancho A · gancho B · visualizações IG · retenção 3 s · salvamentos · compartilhamentos · comentários com a palavra (RAIO-X etc.) · visitas ao perfil · cadastros no Raio-X automático (pelo `?ref=` do Reel) · conversas no WhatsApp · Raio-X em vídeo pedidos · vendas (plano fechado com origem no Reel) · visualizações Shorts · visualizações TikTok · gancho vencedor · decisão (repetir/cortar/testar).
**Fonte:** Instagram e YouTube pelo Windsor; TikTok manual; cadastros, conversas e vendas pelo SDR VIRTÙ (origem gravada no lead). Sem dado, a célula fica "falta" (nunca estimada).
**Rotina de corte toda segunda (30 min, Social media + Maquiavel):**
1. Ordenar os Reels da semana por compartilhamentos + comentários com palavra-chave.
2. **Repetir:** os 2 melhores viram tema de nova versão na semana seguinte e vão para o impulsionamento.
3. **Cortar:** o tipo de tema que ficar 2 semanas seguidas entre os 3 piores sai do calendário.
4. **Testar:** 1 formato novo por semana, no lugar do cortado.
5. Escrever as 3 linhas (repetir/cortar/testar) no painel e no relatório de segunda.

## O que o Lindson decide
1. Quantas fundadoras (2 ou 3) e se a condição é a da decisão 6 (anual no prazo semestral).
2. Liberar o Webdesigner/Builder para publicar a página `/raio-x` no oreganoturbo.pages.dev.
3. Ferramenta da resposta automática no direct (ManyChat ou a da Meta) e liberar os R$ 30/dia.
