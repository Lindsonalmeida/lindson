# REGRAS DO DOSSIÊ · valem para TODAS as contas, agentes e rotinas (Lindson, 25/11/2026)

Pedido do Lindson: "crie as regras do dossiê, pra todos". Estas são as regras obrigatórias. O detalhe de cada uma está em `QUALIDADE.md` (nesta pasta), o estilo em `../dossie-politico.md` e o gerador em `README.md`. Se uma regra for quebrada, o dossiê não sai.

## A. Padrão (nunca mudar)
1. **Não mude o padrão** (Lindson, 25/11). O modelo é o do Francisco Messias / Fubá / Campaner / Alcemir: 26 páginas 16:9, sempre na mesma ordem e com o mesmo layout. Copie o gerador de um dossiê pronto; nunca crie do zero.
2. **Uma cor de destaque só: a do partido do político**, sobre grafite e creme. Anton + Archivo + IBM Plex Mono. Título em 2 linhas, com a 2ª linha na cor do partido.
3. **Foto na capa é obrigatória** (Lindson, 25/11: "todos precisam vir com a foto na capa"):
   - foto real e pública, com no mínimo 1000 px de altura, rosto nítido, recortada com rembg e com crédito;
   - sem essa foto, peça à extensão antes de gerar o PDF;
   - capa só com números ou foto inventada não valem.
4. Nome do arquivo: **"Dossiê - Nome do vereador"** (PDF, .md e zip). Versão refeita: **"Dossiê - Nome v2"**. A versão antiga fica marcada.

## B. Pesquisa (antes do PDF)
5. A pesquisa é feita pela **extensão do Lindson**, com o **prompt oficial** `agencia/prospeccao/vereador/PROMPT-DOSSIE-MODELO.md`:
   - blocos 0–12, LACUNAS, FONTES, checklist e arquivos obrigatórios;
   - um bloco "JÁ TEMOS" tirado da base do SDR (`functions/_sdr.js`) e do TSE;
   - cada vereador ganha o seu `PROMPT-DOSSIE-<NOME>.md`.
6. **Pesquisa parcial não vira PDF final.** Para cada item ❌, a extensão precisa mostrar 3 caminhos tentados. Se voltar parcial, faça um prompt de complemento só com o que falta.
7. **O zip precisa trazer:**
   - a pesquisa .md;
   - a foto oficial com ≥1000 px;
   - 3 a 5 fotos em ação;
   - prints (Instagram, os 3 melhores posts, Câmara, TSE, matérias);
   - instagram-12-posts.csv.

## C. Conteúdo (um erro = não entrega)
8. **Nenhum número inventado.** Todo número tem fonte e data, e toda conta mostra a fórmula no rodapé (ex.: "1,10% = 40 ÷ 3.626").
9. Deixe claro o que é dado e o que é opinião:
   - nota por canal = **"avaliação da equipe"**, com o critério;
   - inferência = **"leitura da equipe"**;
   - votos em 2028 = **"simulação · não é previsão"**;
   - mapa = **"esquemático · sem escala"**.
10. **Passivos:** cada item com fonte, lado e situação. Escreva "sem condenação definitiva" quando for o caso.
    - **Processo de homônimo ou com identidade não confirmada nunca é atribuído ao político.**
    - **Parentesco não confirmado não é afirmado.**
11. **Patrimônio:** mostre a evolução com o aviso de que "declarações ao TSE usam critérios variados; isso não indica irregularidade por si só". Não publique endereço nem placa.
12. **Instagram:** separe os posts próprios das collabs, porque as collabs inflam a média. Curtidas ocultas viram "piso". Engajamento = interações ÷ seguidores, com a conta à vista.
13. **Dado que falta:** a página sai no modelo **"dado a levantar"** e entra na lista de lacunas. Nunca preencha com suposição.
14. **Tom:** o político é **lead e cliente potencial**. O texto é um diagnóstico respeitoso que abre conversa, nunca um ataque.
15. Sem promessa de voto ou de resultado, sem preço e sem nota interna.
16. **CTA final:** WhatsApp (98) 98562-1808 (link wa.me com mensagem pronta) e "LINDSON ALMEIDA · ESTRATEGISTA DE COMUNICAÇÃO POLÍTICA · @LINDSONALMEIDA_".

## D. Conferência e entrega (definição de pronto)
17. **Abra com zoom** a capa, o meio (págs. 6, 10, 13, 15 e 18) e o fim. Confira:
    - nada cortado, sobreposto ou vazio sem sentido;
    - título com no máximo 2 linhas;
    - números grandes sem quebrar linha.
18. **Confira cada número grande contra a pesquisa:** capa, resumo, votos, Instagram e contas. Confira também a cor, o nome, a cidade, a data e o "NN/26" em todas as páginas.
19. Entregue com a **lista honesta** de lacunas e dos defeitos que sobraram. Nunca diga que usou agentes ou skills que não usou.
20. **Salvar:**
    - no privado `dados/clientes-arquivos/<politico>/`, com material/, gerador, PDF e prévia;
    - commit;
    - na `MEMORIA-DO-LINDSON.md`, o que for aprovado ou reprovado;
    - na `MENTE-COLETIVA.md`, 1 linha.

## E. Reprovações que viraram regra
- 25/11: dossiê **sem foto na capa** → reprovado (regra 3).
- 25/11: **"não mude o padrão"** → nada de layout, ordem ou estilo novo (regra 1).
- 24/11: dossiê fora do estilo Messias → reprovado. Todos no mesmo estilo (regra 1).
