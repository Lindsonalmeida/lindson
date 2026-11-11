# Robô SDR no WhatsApp (conta Leandro, 11/11/2026)

Pega 20 contatos da aba SDR da Central e envia sozinho pelo WhatsApp Web, com 4 a 9 minutos entre um e outro, no máximo 20 por dia, de segunda a sexta das 9h às 18h, mostrando "digitando…" antes de cada mensagem; para sozinho depois de 3 números sem WhatsApp seguidos. Cada envio vai para a esteira, e quem responder passa sozinho para "Respondeu".
**Risco:** isso vai contra as regras do WhatsApp. Use um chip separado (decisão do Lindson, 11/11/2026).

## Primeira vez (no computador)
1. Instale o Node.js 18 ou mais novo (nodejs.org).
2. Abra o terminal nesta pasta e rode `npm install`.
3. Token: rode no PowerShell (nesta pasta) o comando que gera o token.txt e copie o mesmo valor para o segredo SDR_TOKEN da Cloudflare.

## Rodar um lote
- `npm.cmd start` (Windows) ou `npm start` (Mac).

Na primeira vez aparece um QR code: no celular do chip, abra WhatsApp → Aparelhos conectados → Conectar e escaneie. Das próximas vezes ele entra sozinho.
Deixe o terminal e o computador ligados até aparecer "Fim do lote" (cerca de 1 hora para 20 contatos).
