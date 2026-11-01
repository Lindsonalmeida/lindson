# Central do Cliente no ar (Cloudflare Pages + Functions)

Montado pela conta Lindson em 01/11/2026. Site da Central do Cliente: tela de acesso com e-mail e código, painel de cada cliente e painel do administrador (Lindson).

## Como funciona o acesso
- O cliente digita o e-mail e o **código de acesso**. O código é conferido **no servidor** (`functions/api/entrar.js`). A página não guarda nenhum código.
- Com o código certo, o servidor grava um cookie assinado (HMAC, HttpOnly, 30 dias) e abre `/painel/<cliente>`.
- `functions/painel/_middleware.js` protege todos os painéis:
  - sem cookie, volta para a tela de acesso;
  - cliente que tenta abrir outro painel volta para o próprio;
  - o **admin** abre todos os painéis.
- `/sair` apaga o cookie.
- Os códigos ficam **só** nas variáveis secretas da Cloudflare:
  - `SEGREDO`: chave das assinaturas;
  - `CODIGOS`: JSON com `HMAC(SEGREDO, código normalizado) → cliente`.
  Os valores estão em `../privado/codigos-acesso.json`, que fica fora do GitHub (peça ao Lindson).

## Painéis no ar
| Endereço | Quem abre | Gerado por |
|---|---|---|
| `/` | todos (tela de acesso) | `prototipo/login.html` |
| `/painel/admin` | só o Lindson | `prototipo/painel.html` + atalhos |
| `/painel/jaci` | Dra. Jaci e admin | `../jaci-cunha/montar-jaci.py` |
| `/painel/leo` | Leo Pinto e admin | `../leo-pinto/montar-leo.py` |

## Montar
```bash
cd agencia/sistema-clientes
python3 jaci-cunha/montar-jaci.py && python3 leo-pinto/montar-leo.py
python3 site/montar-site.py          # gera site/publico/ (fora do Git)
```

## Publicar (repositório privado, nunca o `lindson`, que é público)
1. O Lindson cria o repositório privado **`Lindsonalmeida/central`** (vazio) e libera o app Claude.
2. Envie para lá `functions/` e `publico/`. O `publico/` tem os painéis com dados reais, por isso não entra no repositório público.
3. Cloudflare: Workers e Pages → Criar → Pages → Importar repositório → `central`. Branch `main`, framework `None`, comando de build vazio e diretório de saída `publico`.
4. Em Configurações → Variáveis e segredos, crie `SEGREDO` e `CODIGOS` (tipo Segredo) com os valores de `privado/codigos-acesso.json`. Depois, faça um novo deploy.
5. O link fica `central.pages.dev` (ou o nome que a Cloudflare der). Registre-o aqui e no `ESTADO-DO-PROJETO.md`.

## Testar no computador
Use `npx wrangler@3 pages dev publico` com um `.dev.vars` (fora do Git) contendo `SEGREDO=` e `CODIGOS=`. Em 01/11 foram testados estes casos, todos certos:
- sem cookie;
- código errado (401);
- cliente abrindo o próprio painel e tentando abrir outro;
- admin abrindo tudo;
- cookie falsificado;
- sair.

## Novo cliente
1. Crie `../<cliente>/montar-<cliente>.py` a partir do `montar-jaci.py`.
2. Acrescente o cliente nas listas do `montar-site.py`.
3. Gere um código novo e o hash dele em `privado/codigos-acesso.json` e atualize `CODIGOS` na Cloudflare.

## Limites da v1
- Não há conta nem senha guardada: o acesso é por e-mail + código. Contas e senhas vêm com o D1.
- As demandas e a agenda do painel do Leo só gravam dentro do app no claude.ai. No site, essas telas mostram o conteúdo de exemplo.
- A foto do Lindson na tela de acesso só entra se `fotos/principal-*.webp` estiver na máquina que monta o site.
