# Robô SDR do WhatsApp · time de 3 números (conta Leandro 11/11/2026; time de SDR: conta Pedro 22/11/2026)

O robô pega leads da aba **SDR · Prospecção** da Central e manda a primeira mensagem pelo WhatsApp Web, sozinho. Agora são até **3 números** (sdr1 = o número que já funcionava, sdr2 e sdr3 = chips novos). Cada número recebe **só os leads dele**: dois números nunca falam com a mesma pessoa.
**Risco:** automação no WhatsApp Web vai contra as regras do WhatsApp. Use chips separados (decisão do Lindson, 11/11/2026). Processo completo para as equipes: `agencia/processos/time-sdr-whatsapp.md`.

## Passo a passo do Lindson (no PC Windows)
1. **Baixar e atualizar:** baixe o `robo-sdr.zip` em https://lindsonalmeida.pages.dev/painel/admin-arquivos/robo-sdr.zip (entre como admin) e descompacte na pasta ONDE ESTÁ a sua pasta `robo-sdr` (ex.: se ela é `C:\robo-sdr`, descompacte em `C:\`), aceitando substituir os arquivos (o `token.txt` e a sessão do WhatsApp continuam lá). Se for a primeira vez, descompacte numa pasta fixa, ex.: `C:\robo-sdr`. Precisa do Node.js (nodejs.org, botão LTS) e do Google Chrome.
2. **Rodar o instalador:** dois cliques em `instalar.cmd`. Ele pergunta quantos números vão trabalhar neste PC (1, 2 ou 3), apaga os ícones e cópias antigas (inclusive o `iniciar.cmd` copiado no Inicializar, que dava erro MODULE_NOT_FOUND) e cria, para cada número, o ícone **Robô SDR N** na Área de Trabalho e o atalho que liga com o Windows.
3. **Escanear o QR de cada número:** abra **um ícone por vez**. Na janela aparece um QR com o nome do número ("SDR 2"). No celular DO CHIP CERTO: WhatsApp → Aparelhos conectados → Conectar → escaneie. Espere aparecer "WhatsApp conectado" e só então abra o próximo. O SDR 1 já entra sozinho (usa a sessão antiga).
4. **Pausar:** na Central, aba **SDR · Prospecção → Time de SDR**, cada número tem o botão **Pausar/Ligar** próprio (para em até 2 minutos). Para desligar de vez no PC, feche a janela do Robô SDR N.

## Como cada número trabalha (config.json)
| | SDR 1 | SDR 2 | SDR 3 |
|---|---|---|---|
| Horário (seg a sex) | 09:00–18:00 | 09:20–17:40 | 09:40–17:20 |
| Intervalo entre envios | 4–9 min | 5–10 min | 5–11 min |
| Limite por dia | 20 na 1ª semana, +10 por semana, até o teto (40) | igual | igual |
| Mensagem | versão 1 | versão 2 (saudação e pergunta diferentes) | versão 3 |
- "Digitando…" antes de cada mensagem (`digitando: true`). O `inicio` é gravado sozinho no 1º dia do número (conta o aquecimento).
- 3 números sem WhatsApp seguidos = pausa de 1 dia (lista ruim derruba o chip). Página do WhatsApp recarregou ("detached Frame") = o robô sai com código 2 e o laço do `iniciar-sdrN.cmd` religa em 1 minuto.
- Quem responder vai sozinho para **Respondeu** na esteira (só leads que aquele número enviou).
- Números em PCs diferentes: rode o instalador em cada PC e escolha só os números daquele PC (a pergunta "algum número já roda em outro PC?"). Copie o mesmo `token.txt`. Nunca abra o mesmo número em dois PCs.

## Arquivos
- `robo.js`: o robô (`node robo.js --numero sdr2`). Sessão por número em `.wwebjs_auth/session-sdr-sdrN` (o sdr1 reaproveita `session-sdr`).
- `config.json`: nome, horário, intervalo, limites e aquecimento de cada número.
- `instalar.cmd` / `instalar.ps1`: instalador único. Gera `iniciar-sdrN.cmd` e `ligar-sdrN.vbs` com **caminho absoluto** (funcionam mesmo copiados) e põe **atalhos** (nunca cópias) na Área de Trabalho e no Inicializar.
- `iniciar.cmd`: modo manual (`iniciar.cmd sdr2`); se for copiado para fora da pasta, avisa em vez de dar MODULE_NOT_FOUND.
- `testes/api-sdr.test.mjs`: teste da distribuição com KV falso (`node testes/api-sdr.test.mjs`). Não manda WhatsApp.
- Fora do Git (`.gitignore`): `token.txt`, `.wwebjs_auth/`, `enviados-sdrN.json`, os `iniciar-sdrN.cmd` gerados.

## Central (/api/sdr, privado CentralLindsonALmeida)
- Lote: `GET /api/sdr?lote=1&numero=sdrN` devolve 1 lead livre **deste número**, já marcado "reservado para sdrN" por 2 h, com a mensagem na variação do número.
- Sem repetir lead: o KV da Cloudflare não tem trava atômica, então cada lead tem **dono fixo** (`hash(id) % números ativos`); só o dono recebe. Cada robô grava só na chave dele (`sdr:st:sdrN`), então dois robôs nunca sobrescrevem um ao outro. Estado do lead = registro mais recente entre `sdr:status` (admin) e `sdr:st:sdr1..3`.
- Sinal de vida e pausa por número: `sdr:robo:sdrN` (o `sdr:robo` antigo é lido como sdr1).
- Token: o mesmo de sempre (segredos SDR_TOKEN / AUTOMACAO_TOKEN na Cloudflare). Nada novo.

## O que os especialistas apontaram (22/11/2026)
- **Builder Chief:** uma porta só (`/api/sdr`), contrato documentado no topo do arquivo, rota mínima (sem Durable Object), limite de 2 tentativas automáticas antes de escalar (o robô pausa 1 h após 3 erros e para 1 dia após 3 sem WhatsApp).
- **Backend Engineer:** contrato antes do código; `numero` validado (só sdr1–3), autorização no servidor, idempotência (enviar 2x o mesmo lead só regrava o mesmo estado), reserva com prazo (lead preso volta sozinho em 2 h), observabilidade pelo sinal de vida.
- **Automation & Integration Engineer:** KV não é atômico → partição determinística + um escritor por chave; timeout de 30 s em cada chamada; chamadas do robô em fila (o aviso de "respondeu" não grava junto com o envio); contingência manual mantida (Modo disparo na Central).
- **QA Engineer:** 11 testes de risco (sem token, número inválido, 3 robôs intercalados sem repetição, reserva, número que enviou, pausa por número, compatibilidade do sdr:robo antigo, admin volta lead, variações no padrão, lead sem WhatsApp) e a aba SDR no Playwright (1440 e 390 px, sem erro de JS).
- **Jim Manico (segurança):** todo pedido autenticado (cookie do admin ou Bearer comparado em tempo constante); entrada validada (numero na lista, id existente, etapa na lista, textos cortados em 80/30 caracteres, números limitados a 500); sinal de vida só com token do robô (403 para outros); saída escapada no painel (`esc()`); token só no `token.txt` do PC, fora do Git e fora do zip.
- **Riscos que ficam:** bloqueio do chip pelo WhatsApp (mitigado com aquecimento, horários e mensagens diferentes, nunca zerado); se um número fica 24 h sem sinal, a divisão muda e os leads livres dele passam para os outros (os já reservados ou enviados não mudam); o KV pode demorar até 60 s para espalhar entre regiões (com os 3 no mesmo PC isso não acontece).
