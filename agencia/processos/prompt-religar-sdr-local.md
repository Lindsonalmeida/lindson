Responda em português do Brasil, curto. Você roda NESTE PC (Windows). Objetivo: os 3 robôs SDR do WhatsApp (sdr1, sdr2, sdr3) captando agora. Faça tudo sozinho e só me chame para escanear QR.

Pasta do robô: C:\Users\raiss\Downloads\robo-sdr\robo-sdr
(tem robo.js versão nova, config.json já certo: teto 30, inicial 30, fim_de_semana true; sdr2 09:20–17:40 é proposital. npm install já feito.)
NUNCA apague nem mostre token.txt ou .wwebjs_auth.
No PowerShell use npm.cmd (npm.ps1 é bloqueado).

Situação (22/11, 14:48): os robôs ficam travados em "Iniciando o robô…". O sdr1 deu 1 sinal às 14:45 e parou com limite 0. O sdr2 e o sdr3 estão sem sinal desde 13:32 e 13:44. Há Chromes órfãos do robô antigo abertos (about:blank, "Restaurar páginas?") e algo religa robôs sozinho (ligar-sdr*.vbs / iniciar*.cmd, talvez uma tarefa agendada ou a pasta Inicializar).

Faça:
1. Descubra o que religa os robôs sozinho (Get-ScheduledTask, pasta shell:startup, ligar-sdr*.vbs) para não duplicar. Não apague nada: só pause enquanto conserta.
2. Pare todos os node e só os chrome.exe cuja CommandLine contém "wwebjs" (o Chrome normal do usuário fica aberto).
3. Remova as travas SingletonLock/SingletonCookie/SingletonSocket/lockfile dentro de .wwebjs_auth.
4. Rode `node robo.js --numero sdr1` em primeiro plano e LEIA a saída. Se travar em "Iniciando", investigue no robo.js (puppeteer/Chrome, executablePath, headless, sessão corrompida) e corrija. Se pedir QR, me avise: "escaneie o QR do sdr1".
5. Quando o sdr1 estiver ok, abra o sdr2 e depois o sdr3, cada um na sua janela, com 40 s entre eles.
6. Confira em https://lindsonalmeida.pages.dev/api/sdr?robo=1: os 3 precisam estar com "Trabalhando", limite 30 e o "visto" atualizado. Se o limite continuar 0 no domingo, o robo.js rodando é o antigo: confira a versão.
7. Reative a religação automática que você pausou e me responda em até 3 linhas: estado dos 3 e se falta algum QR.

Guia: agencia/processos/time-sdr-whatsapp.md (repo Lindsonalmeida/lindson, branch claude/global-agent-installation-vdyowf).
