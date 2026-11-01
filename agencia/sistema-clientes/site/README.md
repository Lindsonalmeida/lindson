# Central do Cliente no ar (Cloudflare Pages + Functions)

Montado pela conta Lindson em 01/11/2026. Site da Central do Cliente: tela de acesso com e-mail e código, painel de cada cliente e painel do administrador (Lindson).

## Como funciona o acesso (um sistema só)
- **Criar conta (só na primeira vez):** nome, e-mail, senha (mínimo de 8 caracteres) e o **código de acesso**. O código diz qual painel é da pessoa e é conferido no servidor (`functions/api/criar.js`).
- **Entrar (das próximas vezes):** e-mail e senha (`functions/api/entrar.js`). A pessoa cai direto no próprio painel.
- **Onde ficam as contas:** no KV `CONTAS` da Cloudflare. A senha é guardada em PBKDF2-SHA256 (100 mil voltas, sal por conta), nunca em texto.
- **Cookie:** assinado (HMAC, HttpOnly, 30 dias).
- **Proteção dos painéis** (`functions/painel/_middleware.js`):
  - quem não entrou volta para a tela de acesso;
  - o cliente só abre o próprio painel;
  - o **admin** (Lindson, código `ADM-…`) abre todos e a página **Contas de acesso** (`/painel/contas`), que mostra quem criou conta e permite apagar uma.
- **Esqueceu a senha:** o admin apaga a conta e a pessoa cria de novo com o mesmo código. A conta apagada perde o acesso na hora.
- **Quem já entrou** e abre o endereço principal vai direto para o painel (`functions/index.js`). `/sair` encerra.
- **Códigos:** ficam só nos segredos da Cloudflare, `SEGREDO` e `CODIGOS` (HMAC de cada código → cliente). Os valores estão em `../privado/codigos-acesso.json`, fora do GitHub.

## Painéis no ar
| Endereço | Quem abre | Gerado por |
|---|---|---|
| `/` | todos (tela de acesso) | `prototipo/login.html` |
| `/painel/admin` | só o Lindson | `prototipo/painel.html` + atalhos |
| `/painel/contas` | só o Lindson | `site/contas.html` |
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
4. Em Armazenamento e bancos de dados → KV, crie o namespace `central-contas`.
5. No projeto Pages → Configurações:
   - Vínculos → Adicionar → Namespace KV: nome da variável `CONTAS`, namespace `central-contas`;
   - Variáveis e segredos: crie `SEGREDO` e `CODIGOS` (tipo Segredo) com os valores de `privado/codigos-acesso.json`.
   Depois, faça um novo deploy.
6. O link fica `central.pages.dev` (ou o nome que a Cloudflare der). Registre-o aqui e no `ESTADO-DO-PROJETO.md`.

## Testar no computador
Use `npx wrangler@3 pages dev publico --kv CONTAS` com um `.dev.vars` (fora do Git) contendo `SEGREDO=` e `CODIGOS=`. Em 01/11 foram testados 20 casos no servidor e o fluxo completo no navegador, todos certos:
- criar conta: código errado, senha curta, e-mail repetido;
- entrar: senha errada e senha certa;
- cliente: abre o próprio painel e não abre o de outro, o admin nem as contas;
- admin: abre tudo, lista e apaga contas, mas não apaga a própria;
- conta apagada perde o acesso;
- cookie falsificado é recusado;
- sair funciona.

## Novo cliente
1. Crie `../<cliente>/montar-<cliente>.py` a partir do `montar-jaci.py`.
2. Acrescente o cliente nas listas do `montar-site.py`.
3. Gere um código novo e o hash dele em `privado/codigos-acesso.json` e atualize `CODIGOS` na Cloudflare.

## Limites da v1
- Ainda não há recuperação de senha por e-mail: quem esquece pede ao admin, que apaga a conta para a pessoa criar de novo.
- As demandas e a agenda do painel do Leo só gravam dentro do app no claude.ai. No site, essas telas mostram o conteúdo de exemplo.
- A foto do Lindson na tela de acesso só entra se `fotos/principal-*.webp` estiver na máquina que monta o site.
