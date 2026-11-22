# Time de SDR no WhatsApp (3 números) · processo para as equipes

Criado pela conta Pedro em 22/11/2026, a pedido do Lindson ("salve todo o processo nos repositórios para as equipes entenderem"). Código e passo a passo do Lindson: `agencia/prospeccao/robo-sdr/README.md`.

## 1. Como funciona (arquitetura)
```
PC do Lindson (Windows)                Central (Cloudflare Pages)                 KV "CONTAS"
Robô SDR 1  node robo.js --numero sdr1 ─┐                                          sdr:status        (admin / extensão)
Robô SDR 2  node robo.js --numero sdr2 ─┼─ Bearer token ─► /api/sdr ──────────────► sdr:st:sdr1..3   (1 escritor cada: o robô)
Robô SDR 3  node robo.js --numero sdr3 ─┘                  (functions/api/sdr.js)   sdr:robo:sdr1..3 (sinal de vida + pausa)
   cada um: Chrome + WhatsApp Web próprio                  leads: functions/_sdr.js
Admin (navegador) ── aba SDR · Prospecção ──► /api/sdr (cookie de admin)
```
- O robô pede **1 lead por vez** (`?lote=1&numero=sdrN`). A Central devolve só lead livre **daquele número** e grava "reservado para sdrN" por 2 h.
- Dono do lead = `hash(id) % números ativos` (ativo = deu sinal de vida nas últimas 24 h). Assim dois números nunca pegam o mesmo lead, mesmo sem trava atômica no KV.
- Estado do lead = registro mais recente (`em`) entre `sdr:status` e `sdr:st:sdr1..3`. Cada registro guarda `sdr` (qual número enviou).
- Funciona com os 3 no mesmo PC ou em PCs diferentes (mesmo `token.txt`; nunca o mesmo número em dois PCs).

## 2. Adicionar ou remover um número
- **Adicionar (até 3):** chip novo com WhatsApp ativo há alguns dias → rodar `instalar.cmd` de novo e escolher o total de números → abrir o ícone novo e escanear o QR com o celular desse chip. O aquecimento começa sozinho no 1º dia.
- **Mais de 3:** acrescentar `sdr4` em `NUMEROS` (functions/api/sdr.js), na variação `VAR`, no `config.json`, no teste do `robo.js` (`/^sdr[1-3]$/`) e no `instalar.ps1` (pergunta 1–3). Passa pelo Builder e pelo teste.
- **Remover:** Pausar na Central → fechar a janela → apagar os atalhos "Robô SDR N" (Área de Trabalho e `shell:startup`). Depois de 24 h sem sinal, os leads livres dele passam para os outros; os já enviados continuam com o número que enviou.
- **Trocar o chip de um número:** apagar a pasta `.wwebjs_auth/session-sdr-sdrN`, abrir o ícone e escanear o QR do chip novo; zerar o `inicio` dele no `config.json` (volta ao aquecimento).

## 3. Distribuição dos leads
- Automática na Central (seção 1). Ninguém divide lista à mão.
- Maior nota primeiro, só lead com WhatsApp (regra dos apps de SDR: WhatsApp celular + Instagram confirmados).
- Lead preso (robô caiu depois de reservar) volta sozinho para a lista em 2 h.
- O **Modo disparo** manual da aba SDR continua como contingência e grava como "Manual".

## 4. Aquecimento e limites
- Por número (`config.json`): 20/dia na 1ª semana, +10 por semana, até o teto (40). Seg a sex, horários levemente diferentes (09:00–18:00, 09:20–17:40, 09:40–17:20), intervalo aleatório (4–9, 5–10, 5–11 min) e "digitando…".
- 3 números sem WhatsApp seguidos = aquele número para 1 dia. 3 erros seguidos = pausa de 1 h.
- Subir o teto só com o Lindson e depois de 2 semanas sem bloqueio.

## 5. Variações da mensagem
- A mensagem de cada lead está em `functions/_sdr.js` (padrão `agencia/prospeccao/PADRAO-COPY.md`: Conexão → Dor → Desejo → Pergunta).
- A Central troca só a saudação e a pergunta, por número: SDR 1 = original; SDR 2 = "Tudo certo? Aqui é o Lindson." + "Quer que eu te mostre como faria pra vocês?"; SDR 3 = "Olá," + "Meu nome é Lindson." + "Posso te mandar como funciona pra vocês?". Dor e desejo não mudam.
- Variação nova: editar `VAR` em `functions/api/sdr.js` e rodar o teste (confere o PADRAO-COPY: sem "vi que", "parece que", "gargalo", até 300 caracteres).

## 6. Como pausar
- Um número: Central → SDR · Prospecção → Time de SDR → **Pausar** no cartão dele (vale em até 2 min). **Ligar** volta.
- Tudo de uma vez: Pausar nos 3 cartões, ou fechar as janelas no PC.

## 7. Erros comuns
| Erro | Causa | Solução |
|---|---|---|
| `MODULE_NOT_FOUND ... robo.js` ao ligar o PC | o `iniciar.cmd` foi **copiado** para `shell:startup` e procurou o robô lá | apagar o arquivo do `shell:startup` e rodar o `instalar.cmd` (ele apaga as cópias e cria **atalhos** que apontam para a pasta certa com caminho absoluto) |
| "Falta o arquivo token.txt" | pasta nova sem token | rodar o `instalar.cmd` e colar o token, ou copiar o `token.txt` da pasta antiga |
| "Central fora do ar: Sem acesso" | token errado | conferir o `token.txt` (o mesmo segredo SDR_TOKEN da Cloudflare) |
| "A página do WhatsApp recarregou" (detached Frame) | WhatsApp Web recarregou | nada: o robô religa sozinho em 1 min (exit 2 + laço do cmd) |
| QR aparece de novo todo dia | sessão apagada ou número desconectado no celular | escanear de novo; não usar o mesmo número em outro PC/navegador |
| Cartão "Desligado" na Central | janela fechada, PC desligado ou sem internet | abrir o ícone Robô SDR N |
| "Sem leads livres para este número" | lista acabou | pôr leads novos (seção 8) |
| "3 números sem WhatsApp seguidos" | lista com números ruins | conferir a pesquisa de leads; o número volta sozinho em 1 dia |
| Número bloqueado pelo WhatsApp | volume ou denúncias | Pausar o número, não religar no mesmo dia; avisar o Lindson; voltar com limite inicial |
| Dois robôs abrindo juntos travam o PC | 3 Chromes ao mesmo tempo | os atalhos já esperam 0/40/80 s; não abrir os 3 ícones de uma vez |

## 8. Como colocar leads novos
1. Pesquisa de leads no padrão (WhatsApp celular + Instagram confirmados, nota ≥ 80, mensagem no PADRAO-COPY, passa pelo Maquiavel e Copy squad).
2. Acrescentar os objetos em `CentralLindsonALmeida/functions/_sdr.js` (`id` único, `nome`, `ig`, `wa` com 55+DDD, `nicho`, `cidade`, `nota`, `motivo`, `msg`, `fonte`).
3. `node --check functions/_sdr.js`, commit e push no `main` do privado: a Cloudflare publica e os robôs pegam no próximo ciclo (até 1 h).

## 9. Quem faz o quê
| Quem | Faz |
|---|---|
| Lindson | chips, instalar no PC, escanear o QR, pausar/ligar, aprovar subir o teto |
| Conta Pedro | robô e `/api/sdr` (código, testes, README, este processo) |
| Conta Leandro (coordenação) | põe "leads novos" na fila `coordenacao/fila.json` quando a lista acabar |
| Equipe de prospecção (Maquiavel → Copy squad, Hormozi) | pesquisa de leads e mensagens no PADRAO-COPY |
| Builder squad + Jim Manico | revisão de qualquer mudança em `/api/sdr` (segurança e testes) |

## Funil de follow-up (Lindson, 22/11/2026)
Só para quem não respondeu: **D+3** contato humanizado; **D+6** terceiro contato; **D+9** último contato com apelo e oferta de **organizar o Instagram de graça** (bio, destaques, primeira impressão) para provar a qualidade. Mensagens em `CentralLindsonALmeida/functions/_sdr_fluxo.js` (FOLLOW), adaptadas ao nicho (escritório, barbearia, clínica). Quem aceitar o presente vai para o Lindson.
