# Robô SDR no WhatsApp (conta Leandro, 11/11/2026)

Pega 20 contatos da aba SDR da Central e envia sozinho pelo WhatsApp Web, com 2 a 5 minutos entre um e outro. Cada envio vai para a esteira, e quem responder passa sozinho para "Respondeu".
**Risco:** isso vai contra as regras do WhatsApp. Use um chip separado (decisão do Lindson, 11/11/2026).

## Primeira vez (no computador)
1. Instale o Node.js 18 ou mais novo (nodejs.org).
2. Abra o terminal nesta pasta e rode `npm install`.
3. Pegue o token: é o segredo AUTOMACAO_TOKEN da Cloudflare (projeto lindsonalmeida → Configurações → Variáveis e segredos).

## Rodar um lote
- Mac/Linux: `SDR_TOKEN=seu_token npm start`
- Windows (PowerShell): `$env:SDR_TOKEN="seu_token"; npm start`

Na primeira vez aparece um QR code: no celular do chip, abra WhatsApp → Aparelhos conectados → Conectar e escaneie. Das próximas vezes ele entra sozinho.
Deixe o terminal e o computador ligados até aparecer "Fim do lote" (cerca de 1 hora para 20 contatos).
