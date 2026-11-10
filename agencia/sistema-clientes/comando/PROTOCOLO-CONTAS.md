# Protocolo das contas · Central de Comando (conta Leandro, 09/11/2026 · v2)

O Lindson abre **só** https://lindsonalmeida.pages.dev/painel/comando, a Central de Comando. A voz da página é o **VEKTOR**, o gerente da equipe (holograma que ouve o tempo todo e responde falando). Ele pede, aprova, responde e vê tudo ali. As 4 contas (**Lindson, Zuleide, Pedro, Leandro**) trabalham por uma tarefa agendada de hora em hora, sem ele abrir as contas.

## Configuração (uma vez por conta)
Na tela **05 · Configurar contas**, o botão "Copiar prompt" copia o texto abaixo, já com o nome da conta. O Lindson cola **uma única vez** em cada conta:

```text
Sou o Lindson. Configure esta conta (<CONTA>) UMA VEZ para trabalhar só pela Central de Comando (a página onde eu peço tudo; a voz dela é o VEKTOR, o gerente da equipe).
1. No repositório Lindsonalmeida/lindson (branch claude/global-agent-installation-vdyowf), leia agencia/sistema-clientes/comando/PROTOCOLO-CONTAS.md.
2. Se esta conta ainda não tem a credencial de rede de lindsonalmeida.pages.dev (cabeçalho Authorization: Bearer), peça com request_credential. Nunca escreva o token em arquivo ou na conversa.
3. Crie uma tarefa agendada de hora em hora, com sessão nova a cada disparo e este repositório, chamada "Central · <CONTA>", com este prompt:
"Você é a conta <CONTA>. Faça a RODADA do PROTOCOLO-CONTAS.md: (1) poste 'trabalhando' no quadro da equipe; (2) leia a fila e trate só os pedidos com designada = <CONTA>; (3) leia as respostas do Lindson nas suas perguntas; (4) pegue 1 pedido, faça seguindo o CLAUDE.md, e entregue com 'pronto' (midia + resumo) ou pergunte com 'pergunta' (texto + opcoes); (5) rode o montar-comando.py e faça push; (6) poste 'livre'. Se bater o limite, poste 'limite-sessao' ou 'limite-semana' com o ate do reset."
4. Rode a primeira rodada agora e me diga só "Conta <CONTA> configurada".
```

A tela mostra "● Tarefa ativa" quando a conta bateu o ponto nas últimas 2 h.

## O token
- `/api/automacao` só responde com `Authorization: Bearer <AUTOMACAO_TOKEN>`, um **segredo da Cloudflare** (projeto Pages `lindsonalmeida` → Configurações → Variáveis e segredos, com 24 caracteres ou mais).
- Em cada conta, o token fica como **credencial de rede** do host `lindsonalmeida.pages.dev`; o proxy põe o cabeçalho. **Nunca** em arquivo, commit, conversa ou comando com o valor escrito. Nos exemplos, `$AUT` é só um marcador.
- Sem o token, a rota responde 401.

## A RODADA (a cada hora)
```bash
U=https://lindsonalmeida.pages.dev/api/automacao; H=(-H "Authorization: Bearer $AUT" -H "Content-Type: application/json")
```
1. **Bater o ponto:** `curl -s "${H[@]}" -X POST -d '{"conta":"Pedro","estado":"trabalhando","tarefa":"rodada da fila"}' "$U?fila=equipe"`
2. **Ler a fila:** `curl -s "${H[@]}" "$U?fila=ped"`. A leitura já **redistribui** os pedidos (ver Distribuição). Trate **só** os itens com `"designada":"<sua conta>"`, nos estados `novo` ou `ajuste`, ou que já são seus (`conta` = você, `st` = `andamento`).
3. **Respostas do Lindson:** nos seus pedidos, a última mensagem de `conversa` com `"de":"Lindson"` é a resposta dele. Siga.
4. **Pegar 1 pedido** (o mais antigo; pagantes primeiro): `-d '{"id":"<id>","acao":"pegar","conta":"Pedro"}'` em `$U?fila=ped`. Se der 409, não é seu: pule.
   **Pedido feito na conversa** (o Lindson pediu direto na conta): ponha na fila para nada ser refeito.
   `-d '{"acao":"criar","conta":"Pedro","cli":"jaci","func":"reels","texto":"Reels sobre clareamento","pegar":true}'`
   Com `pegar:true` o pedido já fica com você (`andamento`); sem ele, o distribuidor escolhe a conta. Pedido igual aberto nos últimos 14 dias dá 409 com o existente (use `forcar:true` só se for outro).
5. **Fazer** seguindo o `CLAUDE.md` (memória, persona, pesquisa premium e as regras de cada cliente).
   - **Precisa de algo do Lindson?** Pergunte, com respostas rápidas:
     `-d '{"id":"<id>","acao":"pergunta","conta":"Pedro","texto":"Uso a foto 1 ou a 2?","opcoes":["Foto 1","Foto 2","Pode seguir"]}'`
     O pedido fica "Esperando você" na página. Na próxima rodada, leia a resposta em `conversa`.
   - **Pedido grande** (site, estratégia, leva de Reels): divida.
     `-d '{"id":"<id>","acao":"dividir","conta":"Pedro","partes":[{"texto":"Textos do site"},{"texto":"Fotos e recortes","func":"post"}]}'`
     Cada parte vira um subpedido designado pelo distribuidor. O pedido-mãe continua seu: junte as partes e entregue no fim.
6. **Entregar:** os arquivos precisam de um link https que abra, como a página no ar, o artifact, `lindsonalmeida.pages.dev/...` ou o raw do GitHub.
   `-d '{"id":"<id>","acao":"pronto","conta":"Pedro","midia":["https://.../tela1.jpg","https://.../tela2.jpg","https://.../video.mp4","https://.../estrategia.pdf"],"link":"https://site-no-ar","resumo":"7 telas + legenda SEO"}'`
   - A página mostra a mídia **ali mesmo**, pelo tipo do arquivo: `.jpg/.png/.webp` na galeria, `.mp4/.webm` no player, `.pdf` no visualizador e qualquer outro link como prévia do site.
   - Aceita até 10 links em `midia` e um resumo de até 300 caracteres.
7. **Registrar:** linha no `REGISTRO-DAS-CONTAS.md` e no `PLACAR-DOS-PROJETOS.md`. Depois rode `python3 agencia/sistema-clientes/comando/montar-comando.py` e faça push nos dois repositórios.
8. **Sair:** `-d '{"conta":"Pedro","estado":"livre"}'` em `$U?fila=equipe`.

**Bateu o limite** (ou a última mensagem da sessão foi de limite): poste o estado com a hora do reset, que vem na mensagem ("resets …"):
`-d '{"conta":"Pedro","estado":"limite-sessao","ate":"2026-11-09T23:00:00-03:00"}'`. Para a semana, use `limite-semana`.
- Os pedidos dessa conta são redistribuídos sozinhos.
- O Lindson também pode marcar pelo botão no quadro da equipe.

## Distribuição (o Lindson não escolhe conta)
`functions/_distribuir.js` roda **em toda leitura da fila** (`GET ?fila=ped`) e quando a página abre. Não precisa de cron. Regras, nesta ordem:
1. **Disponível:** só contas `trabalhando` ou `livre`, com batida de ponto nas últimas 2 h. Nunca uma conta esgotada.
2. **Continuidade:** quem já está trabalhando no mesmo cliente (um pedido em andamento na fila, ou uma linha recente do "Em andamento" do QUADRO).
3. **Especialidade:** quem mais entregou aquela função ou aquele cliente, pelo REGISTRO (o `montar-comando.py` calcula; a página envia para o quadro da equipe).
4. **Menor carga:** menos pedidos abertos.

O pedido mostra o motivo em uma linha, por exemplo "Zuleide: já está trabalhando em Post de Leo Pinto".
- **Redistribui sozinho** quando a designada não pega em 2 h, perde a batida ou bate o limite.
- **Sem ninguém disponível:** o pedido fica "na espera" e mostra quando a primeira conta volta.
- **Só a designada pega:** a API recusa as outras contas com 409.

## Regras do servidor (`functions/api/automacao.js`)
| Rota | Campos |
|---|---|
| `?fila=ped` POST | `id` (4–40), `acao` ∈ pegar · pronto · pergunta · nota · dividir, `conta` ∈ Lindson · Zuleide · Pedro · Leandro |
| criar (v4) | sem `id` obrigatório (o servidor gera; `id` opcional 4–40); `cli` ∈ jaci · tribuna · leo · rt · oregano · marca · outro; `func` ∈ reels · carrossel · post · stories · legenda · data · site · landing · painel · estrategia · proposta · contrato · relatorio; `texto` 1–500; `pegar?` e `forcar?` booleanos. Responde 201 com o item |
| pronto | `midia` até 10 links https, `link` https (opcional), pelo menos um dos dois; `resumo` ≤ 300 |
| pergunta | `texto` ≤ 500, `opcoes` até 6 de ≤ 40 |
| dividir | `partes` de 1 a 6 `{texto ≤ 300, func?}` |
| `?fila=equipe` POST | `estado` ∈ trabalhando · livre · limite-sessao · limite-semana; `ate` ISO nos próximos 8 dias (obrigatório nos limites); `tarefa` ≤ 200 |

- `pronto`, `pergunta` e `dividir` só funcionam para a conta que pegou o pedido.
- Cada gravação soma 1 à versão no KV (`dados:admin:ped` e `dados:admin:eq`). A página grava as mesmas chaves por `/api/dados?f=ped|eq`.
- As rotas antigas `?cli=<cliente>` (aprovações e "postado") não mudaram.

## Limites: o que é verdade
- O Claude **não tem** API de uso por conta.
- Os limites reais são a janela de ~5 h da sessão (na tela, "Hoje") e o limite semanal ("Semana"). Não existem limites diário e mensal.
- O "No mês" da tela conta quantas vezes cada limite foi batido, pelo histórico do quadro da equipe.
