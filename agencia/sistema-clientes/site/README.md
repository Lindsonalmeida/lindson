# Central do Cliente no ar (Cloudflare Pages + Functions)

**No ar desde 01/11/2026: https://lindsonalmeida.pages.dev** · repositório privado `Lindsonalmeida/CentralLindsonALmeida` · projeto Cloudflare `lindsonalmeida` (conta Cloudflare do Lindson), KV `centra-contas` ligado como `Contas` (o site aceita `CONTAS` ou `Contas`).

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

**Guarda geral** (`functions/_middleware.js`): bloqueia `/publico/*`, arquivos `.md/.py/.json` e caminhos ocultos. Foi criada em 01/11, depois que uma cópia em `/publico/painel/` abriu sem login no primeiro deploy.

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
1. O Lindson cria o repositório privado **`Lindsonalmeida/CentralLindsonALmeida`** (vazio) e libera o app Claude.
2. Envie para lá `functions/` e **o conteúdo** de `publico/` na raiz (index.html, painel/, _headers, robots.txt). O `publico/` tem os painéis com dados reais, por isso não entra no repositório público.
3. Cloudflare: Workers e Pages → Criar → Pages → Importar repositório → `CentralLindsonALmeida`. **Project name `lindsonalmeida`** (decisão do Lindson, 01/11), branch `main`, framework `None`, comando de build vazio e diretório de saída **vazio** (a raiz). Em 01/11 o site ficou assim no repositório `CentralLindsonALmeida`.
4. Em Armazenamento e bancos de dados → KV, crie o namespace `central-contas`.
5. No projeto Pages → Configurações:
   - Vínculos → Adicionar → Namespace KV: nome da variável `CONTAS`, namespace `central-contas`;
   - Variáveis e segredos: crie `SEGREDO` e `CODIGOS` (tipo Segredo) com os valores de `privado/codigos-acesso.json`.
   Depois, faça um novo deploy.
6. O link fica **https://lindsonalmeida.pages.dev** (endereço único da Central, escolhido pelo Lindson em 01/11). Registre aqui e no `ESTADO-DO-PROJETO.md` quando estiver no ar.

## Testar no computador
Use `npx wrangler@3 pages dev publico --kv CONTAS` com um `.dev.vars` (fora do Git) contendo `SEGREDO=` e `CODIGOS=`. Em 01/11 foram testados 20 casos no servidor e o fluxo completo no navegador, todos certos:
- criar conta: código errado, senha curta, e-mail repetido;
- entrar: senha errada e senha certa;
- cliente: abre o próprio painel e não abre o de outro, o admin nem as contas;
- admin: abre tudo, lista e apaga contas, mas não apaga a própria;
- conta apagada perde o acesso;
- cookie falsificado é recusado;
- sair funciona.

## Ferramentas de gestão (CRM, Financeiro, Notícias): conta Lindson, 01/11/2026
- **Código:** `prototipo/ferramentas.js` (genérico). A configuração de cada cliente fica no `montar-<cliente>.py` (`FERR`: etapas do funil com a mensagem de WhatsApp de cada uma, origens, interesses, categorias do financeiro e temas de notícias). A primeira cliente é a Dra. Jaci.
- **CRM:** funil de pacientes (Novo contato → Conversando → Avaliação marcada → Fez a avaliação → Fez procedimento → Retorno, mais "Não seguiu").
  - Botão **WhatsApp** em cada card, com a mensagem da etapa (regras do CFO). Ao tocar, registra o envio e avança a etapa.
  - Relatório por origem (códigos dos anúncios).
  - O valor do procedimento entra sozinho no Financeiro.
- **Financeiro:**
  - entradas e saídas por mês, a receber e a pagar;
  - meta de faturamento;
  - despesas fixas repetidas no mês seguinte;
  - categorias e últimos 6 meses;
  - planilha CSV.
- **Notícias:** `functions/api/noticias.js` busca no Google Notícias (reserva: Bing) e guarda por 3 horas no KV. Só para quem entrou.
- **Onde ficam os dados:** `functions/api/dados.js` salva no KV (`dados:<cliente>:crm|fin`). Só o próprio cliente ou o admin acessa. Se duas pessoas salvarem ao mesmo tempo, os itens são juntados.

## Envio de fotos (conta Lindson, 01/11/2026)
- **Código:** tela Fotos em `prototipo/fotos.js`; servidor em `functions/api/fotos.js` (lista, envio, exclusão) e `foto.js` (imagem, miniatura, download).
- **Como funciona:** a foto é reduzida no celular para no máximo 2048 px, mais uma miniatura de 480 px, e guardada no KV (`foto:<cliente>:<id>`, `fotot:` para a miniatura). A categoria vai nos metadados.
- **Quem acessa:** o próprio cliente ou o admin.
- **Categorias:** por cliente, em `dados/<cliente>.json` (`fotosCats`).
- **Ordem no montar:** `fotos.js` entra por último, porque encadeia o `__pos` dos outros scripts.
- **Se o volume crescer muito:** passar para o R2 da Cloudflare.

## Dados reais dos clientes
- **Onde ficam:** no repositório privado, em `CentralLindsonALmeida/dados/<cliente>.json`, nunca aqui.
- **Como entram no painel:** o `montar-<cliente>.py` lê esse arquivo (clone o privado em `/home/user/centrallindsonalmeida`, ao lado deste) e o `prototipo/real.js` troca as telas de exemplo pelos dados.
- **O que faltar** aparece como "a medir".
- **Para atualizar:** edite o JSON, rode os scripts de montagem e envie para o privado.

## Novo cliente
1. Crie `../<cliente>/montar-<cliente>.py` a partir do `montar-jaci.py`.
2. Acrescente o cliente nas listas do `montar-site.py`.
3. Gere um código novo e o hash dele em `privado/codigos-acesso.json` e atualize `CODIGOS` na Cloudflare.

## Limites da v1
- Ainda não há recuperação de senha por e-mail: quem esquece pede ao admin, que apaga a conta para a pessoa criar de novo.
- Demandas e agenda do Leo: no claude.ai usam o db do artifact; no site, o servidor da Central (`prototipo/kvdb.js`, chaves `dados:leo:dem` e `dados:leo:ag`). São dois bancos separados.
- A foto do Lindson na tela de acesso só entra se `fotos/principal-*.webp` estiver na máquina que monta o site. Para gerar, use `prototipo/tratar-foto.py` com a foto original (fora do Git). O site montado em 01/11 já tem a foto embutida.
