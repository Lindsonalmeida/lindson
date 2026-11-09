# Protocolo das contas · fila da Central de Comando (conta Leandro, 09/11/2026)

Vale para as 4 contas: **Lindson, Zuleide, Pedro, Leandro**. O Lindson pede em `/painel/comando`; as contas pegam, fazem e entregam pela fila. Um pedido fica com **uma conta só**: o servidor recusa (409) a segunda que tentar pegar.

## O token
- O endereço `/api/automacao` só responde com o cabeçalho `Authorization: Bearer <AUTOMACAO_TOKEN>`.
- O `AUTOMACAO_TOKEN` é um **segredo da Cloudflare** (projeto Pages `lindsonalmeida` → Configurações → Variáveis e segredos), com 24 caracteres ou mais.
- Na sessão de cada conta ele fica como **credencial de rede** do host `lindsonalmeida.pages.dev` (o proxy põe o cabeçalho sozinho). **Nunca** no repositório, num arquivo, na conversa ou num comando com o valor escrito. Nos exemplos abaixo, `$AUT` é só um marcador: com a credencial de rede salva, o cabeçalho pode ir com um valor qualquer (o proxy troca).
- Sem o token configurado, a rota responde 401 e a conta segue o trabalho normal (quadro e registro).

## Ao abrir a conversa e a cada hora
1. **Ler a fila**
   ```bash
   curl -s -H "Authorization: Bearer $AUT" "https://lindsonalmeida.pages.dev/api/automacao?fila=ped"
   ```
   Resposta: `{ itens:[{id, cli, func, texto, st, conta, link, criado, nota, ...}], versao }`.
   Pegue o mais antigo com `st` = `novo`, ou `ajuste` que seja seu (o `ajuste` volta para a conta que fez). Pagantes primeiro (jaci, tribuna, leo, rt).
2. **Pegar** (antes de começar; se der 409, outra conta pegou: escolha outro)
   ```bash
   curl -s -X POST -H "Authorization: Bearer $AUT" -H "Content-Type: application/json" \
     -d '{"id":"<id>","acao":"pegar","conta":"Leandro"}' "https://lindsonalmeida.pages.dev/api/automacao?fila=ped"
   ```
3. **Fazer** seguindo o `CLAUDE.md` (memória, persona, pesquisa premium, regras de cada cliente). Linha no `QUADRO-DA-EQUIPE.md` se demorar.
4. **Recado no pedido** (opcional, ex.: "falta a foto X do cliente")
   ```bash
   -d '{"id":"<id>","acao":"nota","conta":"Leandro","texto":"..."}'
   ```
5. **Marcar pronto** com o link do resultado (https: artifact, página no ar, painel do cliente, arquivo no GitHub). Só a conta que pegou consegue.
   ```bash
   -d '{"id":"<id>","acao":"pronto","conta":"Leandro","link":"https://..."}'
   ```
6. **Registrar e atualizar a Central:** linha no `REGISTRO-DAS-CONTAS.md`, placar no `PLACAR-DOS-PROJETOS.md`, depois `python3 agencia/sistema-clientes/comando/montar-comando.py` e push no privado (README desta pasta).

O Lindson aprova ou pede ajuste na tela Fila. Ajuste volta com `st: "ajuste"` e a `nota` dele.

## Regras do servidor (`functions/api/automacao.js`)
| Campo | Regra |
|---|---|
| `id` | 4 a 40 letras, números ou hífen; tem que existir |
| `acao` | `pegar`, `pronto` ou `nota` |
| `conta` | `Lindson`, `Zuleide`, `Pedro` ou `Leandro` |
| `link` | obrigatório no `pronto`; começa com `https://`; até 500 caracteres |
| `texto` | obrigatório na `nota`; até 500 caracteres |
| `versao` | opcional; se mandar e a fila mudou, 409 (leia de novo) |
- `pegar`: só com `st` `novo` (ou `ajuste` da mesma conta) → `andamento`. Senão 409 com quem está.
- `pronto`: só com `st` `andamento` e a mesma conta → `pronto`, grava `link` e `prontoEm`.
- Cada gravação soma 1 à versão do KV (`dados:admin:ped`), a mesma que a página usa.
- As rotas antigas `?cli=<cliente>` (aprovações e "postado") não mudaram.

## Tarefa agendada (opcional)
Uma tarefa de hora em hora pode rodar os passos 1 e 2 e avisar a conta. Só ligar com o OK do Lindson.
