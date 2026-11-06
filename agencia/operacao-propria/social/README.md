# Rede social do @oreganoturbo · kit de lançamento (Paollo, sessão paralela da conta Leandro, 06/11/2026)

**Pedido do Lindson (06/11):** "as artes para rede social eu quero mais impactantes e que chamem atenção para as vendas" · "pode parecer uma pizzaria" · "nunca me dê coisas simplistas. eu gosto de coisas impactantes" · "menos espaços em branco, imagens".

**Situação:** v2 campanha entregue, **aguardando aprovação do Lindson**.

## v2 · CAMPANHA (a versão atual, 06/11/2026)
**Direção nova do Lindson**, repassada pela sessão principal: "isso é o que chamo de identidade visual de verdade, impactante, criativa" (Decaf Girl/Misato, HOTWHIZ, Mario hot sauce, McDonald's "Here for the sauce", Drip Riot). As artes viraram **campanha de marca de comida**, com o agente **Rocco** junto do Paollo, seguindo a receita `agencia/processos/direcao-de-arte-campanha-comida.md`:
- cor chapada saturada (cores da identidade v4: tomate, açafrão, verde, carvão, creme);
- sombra dura de flash;
- produto enorme recortado;
- ingredientes voando (calabresa e azeitona recortadas);
- manchete gorda e inclinada, de até 5 palavras;
- zero espaço vazio.

A v1 (antes dessa direção) continua em `artes-v1/`, `previa-feed-v1.jpg` e `gerar-v1.py`.

## O que tem aqui
| Arquivo | O que é |
|---|---|
| `artes/` | 22 peças da v2 em JPG q92, em alta (2160×2700 nos posts e no carrossel, 2160×3840 nos stories) |
| `previa-feed.jpg` | Grade 3×4 como fica no Instagram (o post 12 no canto de cima, à esquerda) |
| `LEGENDAS.md` | Legendas estilo blog SEO dos 12 posts e do carrossel, mais o texto dos stories |
| `TEMPLATE.md` | Persona, pesquisa premium, as 3 referências combinadas, qual peça copia qual, formato do Rocco de cada post e descartadas |
| `referencias/kit/` | Capturas novas (Dribbble e Pinterest) e os recortes `r1` a `r9` das peças usadas |
| `recortes/` | Pizzas, fatias e ingredientes (`ing-*`) recortados das fotos CC; `descartes.png` (Frans Hals, domínio público) |
| `gerar.py` → `pecas.html` → `render.js` | Gerador. Para refazer: `python3 gerar.py && node render.js`. Para uma peça só: `node render.js post-03` |

## Os 12 posts (ordem de postagem)
Nunca há dois iguais lado a lado, nem na mesma cor, na sequência e na grade.

| # | Arte | Formato (Rocco/biblioteca) | Cor dominante |
|---|---|---|---|
| 01 | Sua pizza merece **FILA** | 4 · palavra gigante atrás do produto + texto em círculo | tomate |
| 02 | Terça. Seu delivery está **ON** | Chave de interface com a pizza de bolinha | verde |
| 03 | **TERÇA VAZIA** é dinheiro **NO LIXO** | 1 · produto voando com ingredientes | açafrão |
| 04 | O cardápio da terça vazia | 8 · cartaz da paleta em faixas ("paga igual") | faixas |
| 05 | Penso, logo **PEÇO.** | 9 · produto fora do lugar (Descartes com a fatia) | tomate |
| 06 | Vagas de **FUNDADORA** | Cartaz retrô, pizza enorme e selo "SÓ 5" | creme e xadrez verde |
| 07 | **MENOS APP. MAIS ZAP.** | 3 · mão puxando a fatia + celular com o pedido | verde |
| 08 | O mesmo forno. Outro perfil. | Antes × depois de perfil, sem números | carvão / açafrão |
| 09 | **SEGUNDA, 8H.** | Relatório em close (exemplo ilustrativo) | açafrão |
| 10 | **QUANTOS PEDIDOS NA TERÇA?** | 5 · grade de 4 cores com a comida | 4 cores |
| 11 | **4 PASSOS.** Toda semana. | 7 · pizza vista de cima com setas | verde |
| 12 | **RAIO-X** da sua pizzaria · R$ 297 | Pizza enorme meio foto, meio raio-x | carvão |

## Carrossel (7 telas): "5 erros que deixam a sua pizzaria sem pedido na terça"
1. **Capa:** 5 gigante com a fatia.
2. **Foto escura:** tira a fome × dá fome.
3. **Só posta promoção:** parede de "PROMOÇÃO".
4. **Bio sem link:** celular.
5. **Respondeu 1 hora depois:** conversa.
6. **Só aparece no sábado:** gráfico com fatias.
7. **Chamada para o Raio-X.**

Nenhuma tela repete o layout da anterior.

## Stories (3)
1. **Enquete:** "A sua terça é…", forno cheio × forno parado.
2. **Caixinha:** "Me pergunta sobre vender mais pizza".
3. **Raio-X:** "Passa no RAIO-X?", R$ 297.

Em cada um, a figurinha nativa vai por cima do cartão.

## Regras seguidas
- Nada de promessa de resultado (decisão do Lindson, 05/11). Números só no relatório e na conversa, marcados **"exemplo ilustrativo · não é promessa"**; antes/depois marcado "simulação, sem números".
- Preço só o aprovado (`../DECISOES-APROVADAS.md`): Raio-X R$ 297, abatido no 1º mês se fechar em 7 dias. Fundadoras: "preço do plano anual no prazo semestral", valores na conversa.
- Sem "ROAS", "funil", "gargalo". Sem citar percentual do aplicativo (dito "uma parte de cada pedido").
- Logo da Orégano Turbo em todas as peças.

## Créditos das fotos
Fotos de pizza, forno e caixa: Wikimedia Commons, licenças CC0 / CC BY / CC BY-SA, autores e links em `../identidade/fotos-v3/CREDITOS.md` e `../identidade/fotos-v4/CREDITOS.md` (recortes e cunhas de fatia feitos a partir delas: obra derivada, mesma licença). Retrato de René Descartes: Frans Hals, c. 1649, domínio público (https://commons.wikimedia.org/wiki/File:Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg). Quando houver fotos reais das fundadoras (com autorização), elas substituem as de banco.
