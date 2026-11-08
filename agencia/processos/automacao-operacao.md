# Automação da operação (pedido do Lindson, 08/11/2026)

"A partir de hoje eu quero automatizar toda a nossa operação, sem eu precisar passar o dia pedindo coisas. Quero dizer o que fazer uma única vez, e você automatizar tudo e fazer sozinho. Me diga o que precisa."

## O que já é automático (sem o Lindson)
- Consultar o repositório antes de qualquer ação (regra de 07/11, `consultar-antes.md`).
- Commit e push de cada etapa, com registro no quadro, na memória e na trava.
- Sessões remotas em paralelo para trabalhos longos (identidade, painel, site).
- Pesquisa e montagem de peças (capas, artes, painéis) a partir dos modelos aprovados.

## O que depende de ligação (conector) que ainda não existe aqui
| Operação | O que precisa | Situação hoje |
|---|---|---|
| Postar e agendar no Instagram (feed, story, Reels) | Conta de negócio do Meta com acesso de publicação (conector ou agendador) | **Não conectado** |
| WhatsApp (SDR, respostas, lista de envio) | WhatsApp Business API ou número conectado | **Não conectado** |
| E-mail e campanhas | Brevo | Conectado |
| Vídeos com avatar e narração | HeyGen | Conectado |
| Site e deploy | GitHub + Cloudflare Pages (já funciona por push) | Funciona |
| Google Meu Negócio e Search Console | Acesso da conta Google do cliente | **Não conectado** |
| Venda de low ticket (Hubla) | Acesso à Hubla | **Não conectado** |
| Relatório semanal | Dados de Insights (Instagram, Analytics) | Depende do Instagram e do Analytics |

## Rotinas que eu posso agendar (quando você confirmar)
- Relatório semanal de status (segunda, por Maquiavel) com placar, travas e próxima decisão.
- Checagem diária do quadro: o que ficou parado há mais de 24 h, e qual sessão precisa de decisão.
- Conferência das sessões remotas e alerta quando uma parar.

## O que eu preciso do Lindson (uma vez)
1. **Conectar o Instagram** dos clientes (Leo, Tribuna 98, curso, Orégano, Jaci, Real Time) pelo conector do Meta, ou dizer qual agendador você usa.
2. **Conectar o WhatsApp Business** (número e API) para as respostas e a lista de envio.
3. **Dar acesso** ao Google Meu Negócio dos clientes e ao Search Console.
4. **Confirmar as rotinas** acima (relatório semanal e checagem diária).
5. **Aprovar uma vez** o modelo de postagem: quais peças saem sozinhas (já aprovadas, como o modelo B de aniversário) e quais passam por você antes (anúncio, promessa, preço).

## Limites que continuam
- Gasto de dinheiro (anúncio, assinatura, faturamento) só com o seu OK.
- Dado pessoal de paciente, aluno ou cliente não vai para o repositório público.
- Nada de promessa de resultado ou número inventado.
- Peça nova continua sendo mostrada para aprovação.

## Real Time · postagem automática (08/11/2026, conta Leandro)
- Tarefa agendada `trig_01PunAiAegefs281sWBJd77w`: 9h58, 13h58 e 17h58 (Fortaleza), a partir de 11/11. Lê `realtimeslz.pages.dev/posts/fila.json` (15 posts), confere a aba Aprovados por `/api/automacao?cli=rt`, posta 1 por vez via Windsor e marca como postado.
- Pendente: o conector Windsor.ai precisa ser ligado à tarefa em claude.ai (Rotinas → tarefa → Conectores); a API não deixou anexar.
- Os 2 stories aprovados (enquete e caixa de pergunta) ficam de fora: figurinha só pelo app.
