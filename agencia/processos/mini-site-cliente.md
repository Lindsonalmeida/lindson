# Passo a passo: mini site de cliente

Como entregar um mini site com o nome do cliente no link (ex.: `rafaelimports.pages.dev`), sem o nome Lindson Almeida no endereço, usando GitHub + Cloudflare Pages (grátis).

---

## Parte 1 · Configuração única (faz uma vez só)

### 1. Criar a conta na Cloudflare
1. Acesse **dash.cloudflare.com/sign-up**.
2. Cadastre e-mail e senha e confirme o e-mail que chegar.
3. Se pedir domínio ou plano, pule. Plano: **Free**.

### 2. Ligar a Cloudflare ao GitHub
1. No menu da esquerda: **Workers & Pages** (às vezes dentro de "Compute").
2. **Create** → aba **Pages** → **Connect to Git** (ou "Import an existing Git repository").
3. **Connect GitHub** → faça login no GitHub → **Authorize**.
4. Na tela "Install & Authorize", escolha a conta **Lindsonalmeida** e marque **All repositories** → **Install**.
5. Se tiver organizações (ex.: `rafaelimports`), instale nelas também:
   **github.com/apps/cloudflare-workers-and-pages/installations/select_target** → escolha a organização → **All repositories** → **Install**.

Pronto. Daqui pra frente a Cloudflare enxerga seus repositórios.

---

## Parte 2 · Para cada cliente novo

### Passo 1 · Coletar o material com o cliente
Peça tudo de uma vez, pelo WhatsApp:

- [ ] Logo (arquivo, de preferência PNG)
- [ ] @ do Instagram
- [ ] Números de WhatsApp e para que serve cada um (loja, vendas, suporte…)
- [ ] Endereço completo (rua, número, bairro, ponto de referência)
- [ ] Horário de funcionamento
- [ ] 2 ou 3 vídeos curtos da loja / do serviço (para o fundo)
- [ ] Fotos reais dos produtos ou serviços, **cada uma enviada como arquivo**
- [ ] Os botões que ele quer no site

### Passo 2 · Criar o repositório no GitHub
1. Entre em **github.com/new**.
2. **Repository name:** nome do cliente, sem espaço e sem acento (ex.: `clinicaliliane`).
3. Marque **Public** ou **Private** (os dois funcionam com a Cloudflare).
4. **Create repository** (pode deixar vazio).

### Passo 3 · Pedir o site ao Claude
Mande no chat:
> "Crie o mini site do [cliente] no repositório lindsonalmeida/[nome]. Pode conectar e publicar."

E envie o material do Passo 1. **Fotos: uma por mensagem**, esperando a resposta antes da próxima (imagem colada no meio de outra resposta não fica salva).

O Claude monta o site, testa e publica no repositório.

### Passo 4 · Publicar na Cloudflare
1. **Workers & Pages** → **Create** → aba **Pages** → **Connect to Git**.
2. Escolha o repositório do cliente → **Begin setup**.
3. Preencha:

   | Campo | O que colocar |
   |---|---|
   | Project name | nome do cliente (vira `nome.pages.dev`) |
   | Production branch | `main` |
   | Framework preset | `None` |
   | Build command | (vazio) |
   | Build output directory | (vazio) ou `/` |

4. **Save and Deploy** → espere ~1 minuto.
5. Avise o Claude o link final (ex.: `clinicaliliane.pages.dev`) para ele ajustar os links internos (cards de WhatsApp etc.).

> Se o nome já estiver em uso, a Cloudflare põe letras no fim do link. Troque o Project name (ex.: `clinicalilianeslz`).

### Passo 5 · Testar no celular antes de entregar
- [ ] Abre rápido e o vídeo de fundo roda
- [ ] Cada botão de WhatsApp abre o número certo, com a mensagem pronta
- [ ] Instagram e mapa abrem certo
- [ ] Fotos aparecem (se não, abra o link com `?v=2` no fim para limpar a memória do navegador)
- [ ] Nada com o nome errado ou informação inventada

### Passo 6 · Entregar
1. Mande o link para o cliente e mostre como colocar na bio do Instagram:
   Editar perfil → Links → Adicionar link externo → colar o link.
2. Combine a manutenção mensal (atualizar fotos, produtos, promoções).

---

## Parte 3 · Atualizar um site já entregue
Mande no chat: "Atualize o site do [cliente]: [o que mudar]".
O Claude altera e publica; a Cloudflare atualiza sozinha em ~1 minuto.

---

## Domínio próprio (opcional, cliente premium)
1. O cliente registra o domínio em **registro.br** (~R$ 40/ano, no CPF/CNPJ dele).
2. Na Cloudflare: projeto do cliente → **Custom domains** → **Set up a custom domain** → digite o domínio → siga as instruções (a Cloudflare mostra o que configurar no registro.br).

---

## Problemas comuns
| Problema | Solução |
|---|---|
| Link dá 404 logo depois de publicar | Espere 1–2 min e recarregue |
| Mudança não aparece | Abra o link com `?v=2` (ou outro número) no fim |
| Repositório não aparece na Cloudflare | Instale o app da Cloudflare na conta/organização (Parte 1, item 2.5) |
| Foto enviada não entrou no site | Reenvie como mensagem separada, uma por vez |
| Nome do projeto já existe | Use outro (ex.: acrescente `slz`) |

---

## Clientes ativos
| Cliente | Repositório | Link |
|---|---|---|
| Rafael Imports | rafaelimports/rafadigital | rafaelimports.github.io/rafadigital (migrar para `rafaelimports.pages.dev`) |
