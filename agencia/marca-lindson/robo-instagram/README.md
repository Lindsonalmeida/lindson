# Robô do Instagram (posta sozinho no @lindsonalmeida_)

Conta Pedro, 11/11/2026. Mesmo jeito do robô do WhatsApp do Leandro: uma fila no site (`/api/agenda-ig`, no privado `CentralLindsonALmeida`) com um token só do robô, e o robô rodando no seu PC.

**Como funciona:** a cada 15 min o Windows roda o robô. Ele pergunta ao site qual é o próximo post, espera a hora (só entre 8h e 21h, 4 h depois do último), publica pela API oficial do Instagram (post, carrossel, Reels e stories), confere o link e avisa o site. O site guarda tudo no KV: o mesmo post nunca sai duas vezes.

## O que você faz (uma vez só)

### 1. Token da Meta (longa duração)
1. Entre em developers.facebook.com → **Meus apps** → crie um app tipo **Empresa** (ou use o que já tem).
2. O Instagram @lindsonalmeida_ precisa ser **conta profissional** ligada a uma **Página do Facebook**.
3. Abra o **Graph API Explorer** (Ferramentas). Escolha o app, clique em **Gerar token** e marque: `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, `business_management`.
4. Clique no **i** ao lado do token → **Abrir na ferramenta de token de acesso** → **Estender token de acesso**. Copie o token longo (vale 60 dias; repita no fim do prazo e rode o instalador de novo).

### 2. Segredo na Cloudflare
Cloudflare → Workers e Pages → **lindsonalmeida** → Configurações → **Variáveis e segredos** → Adicionar → tipo **Segredo**, nome `IG_ROBO_TOKEN`, valor: uma senha longa sua (24 caracteres ou mais, sem espaço; ex.: gere em um gerador de senhas). Salve e faça um novo deploy (Implantações → Repetir).

### 3. Instalar no PC
Abra o **PowerShell** (sem administrador) e cole:

```powershell
irm https://lindsonalmeida.pages.dev/robo/instalar-robo-instagram.ps1 -OutFile "$env:TEMP\instalar-robo.ps1"; powershell -ExecutionPolicy Bypass -File "$env:TEMP\instalar-robo.ps1"
```

Ele pede o token da Meta e o `IG_ROBO_TOKEN` (guarda criptografados, só o seu usuário do Windows abre), agenda a tarefa **Robo Instagram Lindson** e faz um teste que não publica nada.

- Testar de novo: `powershell -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\RoboInstagram\robo-instagram.ps1" -Teste`
- Registro: `%LOCALAPPDATA%\RoboInstagram\robo.log`
- Parar: Agendador de Tarefas → "Robo Instagram Lindson" → Desabilitar.

O PC precisa estar ligado nas horas dos posts (o robô roda ao ligar e recupera o atrasado dentro da janela).

## Para as contas (Claude)
- Post novo ou mudança na agenda: edite `agenda-status.json`, rode `python3 montar-fila.py` (gera `functions/_agenda_ig.js` no privado) e faça commit e push dos dois repositórios. Status `agendado`/`aprovado` com `urls` e `quando` entra na fila.
- Quem posta de verdade é o KV: `GET /api/agenda-ig` (Bearer `AUTOMACAO_TOKEN`) mostra o status real. Robô atualizado: copie os `.ps1` para `CentralLindsonALmeida/robo/`.
- Rotina do Windsor: ver `COMO-PUBLICAR.md` (consultar e travar na API antes de postar).
