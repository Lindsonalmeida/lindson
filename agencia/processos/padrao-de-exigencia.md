# Padrão de exigência da agência (regra fixa, todas as contas, todos os agentes, todo cliente)

Origem: Lindson, 18/11/2026 (conta Leandro, cliente Mova Street): "seja exigente e detalhista" e "fixe todas essas regras de exigência para todas as equipes e no repositório e em qualquer outro lugar que elas aprendam". Nasceu de uma imagem com 8 erros que a equipe mandou sem conferir, de três aberturas de feed reprovadas e de prompts com contradição.

Vale para: as 4 contas (Lindson, Zuleide, Pedro, Leandro), os agentes (`.claude/agents/`), os squads, as rotinas agendadas e qualquer conta nova. Em conflito com uma regra antiga, vale esta.

## 0. Postura
1. **O primeiro crítico é você.** Nada chega ao Lindson como "pronto" sem conferência com zoom: imagem ampliada, PDF aberto na capa e no meio, site aberto no celular e no computador.
2. **Achou erro, diga.** Liste com clareza o que estava errado, corrija e transforme em regra. Nunca defenda uma peça ruim nem esconda limitação (ex.: "o QR da imagem é falso", "a foto repete").
3. **Reprovação vale para trás.** Quando uma técnica ou peça é reprovada, audite todas as peças já entregues que usam a mesma técnica e proponha a troca, sem esperar ele pedir. Exemplo: em 18/11, a reprovação da montagem de fotos levou a auditar todas as peças da Mova.
4. **Revise o próprio texto também.** Prompt, plano, legenda e mensagem passam pela mesma conferência: contradição, geometria impossível, número inventado, promessa, ortografia.
5. **Ele corrige numa frase e espera que você generalize.** Toda correção dele vira regra para todos os clientes (CLAUDE.md, MEMORIA, agentes).

## 1. Antes de criar
1. Pesquisar todas as diretrizes do tema (regra rígida de 16/11).
2. Montar o time: quem lidera e quem revisa (mapa "Quem acionar em cada entrega", no topo do `CLAUDE.md`). O Maquiavel tria antes e confere depois.
3. Persona e mensagem de 1 segundo: o que o cliente vende, para quem, e o que a pessoa tem que entender só de bater o olho.
4. Pesquisa premium de verdade (≥ 8 referências de ≥ 3 países, capturas salvas, `TEMPLATE.md`). Princípios "de memória" não contam como pesquisa.
5. Foco no produto do cliente. Na Mova Street, por exemplo, a protagonista é a tela com o anúncio, não o carro.

## 2. Estética e conteúdo (fixas)
1. **Menos é mais, mas que comunica (luxo clean):** respiro intencional, 1 ideia por peça, tipografia fina e espaçada, cor de destaque só como detalhe, foto herói cinematográfica. Proibido: colagem de mockups, pílulas, cards de UI, notificações, glow espalhado, "cara de vibe code". Respiro sim; vazio de sentido não: cada área da peça tem função. Em 18/11 ele reprovou nos dois sentidos: "poluído/colagem" e "ainda está vazio".
2. **Grade em imagem única:** uma foto só, mesma luz, um elemento herói atravessando, texto mínimo em frase contínua, nada importante nem texto em cima da divisa.
3. **Logo do cliente:** nunca redesenhar o que o dono aprovou. Em fundo escuro, a versão transparente em alta (PNG/SVG), nunca a versão com caixa ou fundo colorido. Só a marca do cliente aparece, nunca o nome de outra marca ou da holding.
4. **Números e promessas:** preço sempre "a partir de" (o valor fecha na conversa); bio sem valores; nenhum número inventado; estimativa do cliente marcada como "estimativa da empresa"; nenhuma promessa de resultado; nenhuma nota interna em material do cliente.
5. **Foto usada uma vez só** e registrada como usada.

## 3. Imagens
1. **Proibido fotomontagem que finge ser foto real:** colar tela, anúncio ou logo em perspectiva numa foto, juntar duas fotos, inserir pessoa recortada dentro de uma cena fotográfica. Continua valendo o recorte de pessoa real sobre o fundo gráfico da arte (padrão aprovado de Leo e Jaci), porque não finge ser uma cena.
2. **Cena inteira gerada por IA, num prompt só:** o Lindson gera no Gemini (regra de 16/11) e a equipe escreve o prompt. Por cima vai só tipografia e logo plana, como assinatura.
3. **Prompt de imagem bem feito:**
   - geometria possível: onde está a câmera, quem está onde, para onde cada pessoa olha, como cada objeto está preso;
   - texto exato, curto e em português, só quando for indispensável;
   - proibições explícitas;
   - formato e resolução (4K ou a maior);
   - divisão em terços quando for grade de 3.
   Antes de entregar, revise o próprio prompt contra os 8 critérios.
4. **Conferência da imagem com zoom:** os 8 critérios de `agencia/processos/conferencia-imagem-ia.md`, registrados no README da peça. Um erro e a imagem não é usada; diga o erro e ajuste o prompt.
5. **Resolução:** não ampliar mais de 1,5×. Imagem pequena é refeita em resolução maior.

## 4. Conferência antes de entregar (o Maquiavel confere; quem fez confere primeiro)
1. Abrir de verdade: todas as artes; o PDF na capa, no meio e no fim; o site no celular (390 px) e no computador (1440 px); o painel logado.
2. Marca certa e versão aprovada mais recente. Nada cortado, nada sobreposto, nada na divisa, sem erro de português.
3. Imagens aprovadas nos 8 critérios.
4. Mensagem entendida em 1 segundo pela persona.
5. Regras do cliente cumpridas (preço, CFO e CRO na Jaci, situação no Leo e outras).
6. Sem dados de exemplo, sem nota interna, sem número inventado.
7. Arquivo no painel do cliente e na aba de clientes, linha em Tarefas feitas, versões reprovadas marcadas como reprovadas.
8. Commit e push confirmados nos dois repositórios. Para site ou painel, conferir no ar depois da publicação, não só localmente.
9. Na resposta ao Lindson: o resultado, o que ele decide e as limitações conhecidas.

## 5. Depois de uma reprovação
1. Registrar na `MEMORIA-DO-LINDSON.md` o que foi reprovado e por quê, com data e conta.
2. Marcar a peça como reprovada no painel; a versão nova recebe nome novo (-v2, -v3).
3. Se a regra vale para todos, pôr nos dois `CLAUDE.md` e nos agentes.
4. Fazer a auditoria retroativa (item 0.3).

## Onde este padrão está fixado
`CLAUDE.md` (lindson e CentralLindsonALmeida), resumo da `MEMORIA-DO-LINDSON.md`, recado no `QUADRO-DA-EQUIPE.md`, `MENTE-COLETIVA.md`, `PROMPT-DA-EQUIPE.md`, `coordenacao/PROMPT-EQUIPE.md` e `COORDENACAO.md`, `agencia/sistema-clientes/comando/PROTOCOLO-CONTAS.md`, todos os agentes de `.claude/agents/`, as skills do privado, o VEKTOR (`functions/api/vektor.js`) e as tarefas agendadas da conta Leandro.

## Anexo · checklist aplicado da Mova Street (cena da tela no encosto, 18/11)
Use como exemplo de como os 8 critérios viram itens concretos para cada cliente:
1. Passageiro no banco de trás (nunca no do motorista nem no do carona).
2. Olhar na tela ou no celular.
3. Celular com o visor virado para o passageiro; se o visor mostrar a tela, o texto tem que estar correto (ou o visor fica só com a cor, sem letras).
4. Tela de 10" presa nas hastes do encosto, centralizada, sem flutuar.
5. Na tela, só: fundo laranja, "SUA MARCA AQUI", "Aponte a câmera" e QR; sem marca real nem erro de ortografia.
6. Rosto e mãos iluminados pela luz laranja da tela (sem luz de teto acesa que mate o clima).
7. Geometria do carro: motorista sentado no próprio banco, volante na frente dele (Brasil: à esquerda), mãos perfeitas.
8. Resolução: largura ≥ 2/3 da final (3240 px pede ≥ 2160 px), sem placa legível.
