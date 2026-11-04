# Área de membros dos produtos do Lindson (conta Pedro, 04/11/2026)

Pedido do Lindson (04/11): área de membros estilo Netflix com as fotos dele; todos os produtos na mesma área; só libera o que a pessoa comprou; dentro da área ela compra os outros.

- **Estilo aprovado:** NEXUS · Premium Movie & Series Streaming Platform (Adam Max, dribbble.com/shots/27716502) — "esse estilo é perfeito". Referências que ele mandou: Hubla (ai creator PRO) e Estado α.
- **Protótipo:** `prototipo.html` (abrir com `?tem=kit-mes-pronto,kit-whatsapp-que-fecha` para simular o que a pessoa comprou). Usa as fotos de `agencia/marca-lindson/artes-v1/fotos/` (fora do Git): busto do peito para cima ocupando a arte, **nenhuma foto repetida** (regra dele de 04/11): miniaturas cNN, pôsteres `vb-*` (busto tirado das fotos de corpo inteiro), lista `vc-*` (close espelhado), faixa `vf-c12`.
- **Plataforma recomendada para vender:** Hubla (8,9% + R$ 2,49 por venda; área de membros estilo Netflix com "Outros produtos" para comprar lá dentro). Kiwify (8,99% + R$ 2,49) e Hotmart (9,9% + R$ 2,49) comparadas. Confirmar as taxas na página oficial.
- **Dois caminhos:** (1) usar a área de membros da própria Hubla com estas capas; (2) a área própria (este protótipo) dentro da Central (lindsonalmeida.pages.dev), com o checkout da Hubla e o webhook liberando o produto comprado. Decisão do Lindson.
- **Variações com IA:** o gerador disponível (Figma) só cria a partir de texto e faria outra pessoa; variações com o rosto dele precisam de ferramenta com foto de referência (ex.: Gemini, que ele já usa). Ele sobe na aba Minhas fotos.

## Sistema (área própria dentro da Central · Builder Squad, backend, 04/11/2026)

Caminho escolhido pelo Lindson: **área própria** em https://lindsonalmeida.pages.dev/membros, com o checkout da Hubla e o webhook liberando o que a pessoa comprou. Código no repositório privado `CentralLindsonALmeida` (fonte da verdade, publica sozinho no push da `main`); cópia sem dados em `site/functions/` e `membros/site/` deste repositório. **Ainda não foi para o ar: está no privado sem commit, aguardando revisão.**

### Rotas
| Rota | O que faz | Quem abre |
|---|---|---|
| `/membros/` | Tela de acesso com as abas **Entrar** (e-mail + senha) e **Primeiro acesso** (e-mail + CPF da compra → cria a senha, mínimo 8) | todos (quem já entrou vai direto para a área) |
| `/membros/area` | Área no visual NEXUS aprovado (`prototipo.html`): liberado → página do produto; bloqueado → cadeado e **Comprar** (checkout da Hubla). `?comprar=<slug>` destaca um produto | membro com sessão |
| `/membros/p/<slug>` | Página do produto com os arquivos para baixar (Raio-X e Bio: "em produção / entregue pelo WhatsApp") | só quem comprou aquele produto (os outros voltam para a área com o Comprar) |
| `/membros/sair` | Sai e invalida o cookie | membro |
| `POST /api/hubla` | Webhook da Hubla: `customer.member_added` libera, `customer.member_removed` tira | Hubla (cabeçalho `x-hubla-token`) |
| `POST /api/membros/entrar` · `POST /api/membros/primeiro` | Login e primeiro acesso | todos (erro genérico, espera de 0,8 s e bloqueio de 15 min após 10 erros por e-mail) |
| `GET /api/membros/eu` | `{nome, produtos:[slugs liberados], checkout, contato}` | membro |
| `GET /api/membros/arquivo?p=<slug>&f=<arquivo>` | Baixa o arquivo (só nomes da lista `ARQUIVOS`; `attachment`, `private, no-store`) | quem comprou, ou o admin da agência |
| `GET/POST /api/membros/admin` | Lista membros; `acao`: `liberar`, `remover`, `zerar-senha`, `apagar` | só o admin da agência (cookie `central`) |
| `/painel/membros` | Tela do admin para ver os membros e liberar/tirar produto à mão (venda manual, teste) | só o admin |

Slugs: `kit-mes-pronto`, `kit-whatsapp-que-fecha`, `kit-prospeccao`, `raio-x-do-perfil`, `bio-que-vende`.

### Onde fica cada coisa (privado `CentralLindsonALmeida`)
- `functions/_membros.js`: configuração (**MAPA_HUBLA**, **CHECKOUT**, **CONTATO**, lista de arquivos) e as funções comuns (sessão `lm_membro`, tentativas, gravação conferida).
- `functions/api/hubla.js`, `functions/api/membros/*.js`, `functions/membros/_middleware.js`, `functions/membros/sair.js`, `functions/membros/p/[slug].js`.
- `functions/_middleware.js` (guarda geral): agora também dá 404 em `/membros-arquivos/*` e em `/produtos/*` (entregas e fontes dos produtos estavam abertas a quem soubesse o endereço), menos `/produtos/landing/*`. Confere o caminho decodificado (`%2D`, `//`, maiúsculas).
- `membros/index.html` (tela de acesso), `membros/area.html` (área), `membros/img/` (21 JPGs otimizados, todos abaixo de 160 KB).
- `membros-arquivos/<slug>/`: os arquivos pagos (cópia das `entrega/` de `produtos/`). Ao atualizar um PDF, copie de novo para cá.
- `painel/membros.html` (gerado de `site/membros.html` pelo `montar-site.py`).

### KV (vínculo `CONTAS`, o mesmo da Central)
- `membro:<email>` → `{ nome, email, docHash:{sal,hash}, tel4, produtos:{slug:{ativo, desde, ate, at, v, sub, origem}}, senha:{sal,hash}, sv, criado, primeiroAcesso }`. CPF só em PBKDF2 (100 mil voltas, sal próprio), telefone só os 4 últimos dígitos, senha em PBKDF2. `sv` muda quando a pessoa sai ou o admin zera a senha, e derruba as sessões antigas.
- `hubla:idem:<sha256 do x-hubla-idempotency>` → evento já processado (30 dias).
- `membro-tent:<entrar|primeiro>:<hmac do e-mail>` → tentativas erradas (15 min).
- Evento fora de ordem: um "concedido" mais velho (mesma assinatura com `version` menor, ou `modifiedAt` anterior) não desfaz um "removido" mais novo.
- Log: só o tipo do evento e o slug (nada pessoal).

### O que o Lindson faz (uma vez)
1. **Segredo do webhook:** Hubla → Integrações → Webhooks → criar integração e copiar o **Hubla Token**. Cloudflare → Workers e Pages → projeto `lindsonalmeida` → Configurações → **Variáveis e segredos** → Adicionar → nome `HUBLA_TOKEN`, tipo **Segredo**, valor = o token (Produção). Sem ele o webhook responde 503 e nada é liberado.
2. **Webhook na Hubla:** URL `https://lindsonalmeida.pages.dev/api/hubla`, eventos **Acesso concedido** e **Acesso removido** (só esses dois), nos 5 produtos.
3. **IDs e links:** no privado, `functions/_membros.js`, troque os `PREENCHER-ID-HUBLA-...` do **MAPA_HUBLA** pelo ID de cada produto na Hubla e os `https://pay.hub.la/PREENCHER-...` do **CHECKOUT** pelos links de venda. Opcional: **CONTATO** = link do WhatsApp para o botão "Falar com o Lindson". Enquanto um checkout tiver `PREENCHER`, o botão daquele produto mostra "Em breve".
4. **Na Hubla, desligar a área de membros dela** para esses produtos (ou deixar só como reserva) e, na mensagem de compra aprovada, mandar o link `https://lindsonalmeida.pages.dev/membros/#primeiro` ("entre com o e-mail e o CPF da compra").
5. **Publicar:** revisar e fazer commit/push no privado (o Cloudflare publica sozinho). Depois, fazer uma compra de teste (ou "Enviar teste" no webhook da Hubla e liberar à mão em `/painel/membros`) e conferir o primeiro acesso.

Notas: quem comprar com outro e-mail tem outro cadastro (libere à mão no admin). Esqueceu a senha: o admin clica **Zerar senha** em `/painel/membros` e a pessoa faz o Primeiro acesso de novo. Pedido de exclusão (LGPD): **Apagar** no admin. Se o `_membros.js` for preenchido no privado, não copie o do público por cima (igual ao `_codigos.js`).

### Testes
`node agencia/sistema-clientes/membros/testes/testar-membros.mjs /home/user/centrallindsonalmeida` roda as Functions com KV falso: **44 de 44 certos em 04/11** (webhook: token errado, sem token, concedido, repetido, produto sem mapa, outro tipo, JSON inválido, removido, concedido atrasado, recompra, dois webhooks ao mesmo tempo; primeiro acesso: CPF errado, e-mail sem compra, senha curta, certo, repetido; login, bloqueio após 10 erros, cookie falso, cookie da agência; downloads permitido/negado/sem sessão/nome fora da lista; páginas; guardas; admin e logins da agência intactos; nenhum CPF, telefone ou senha em texto no KV). Também testado com `npx wrangler@3 pages dev . --kv CONTAS --binding SEGREDO=... HUBLA_TOKEN=...` no privado (estático bloqueado, `ASSETS` servindo o PDF de 2 MB, fluxo no navegador em computador e celular).
