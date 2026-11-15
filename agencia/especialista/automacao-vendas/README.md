# Especialista em automação de vendas

Conta Leandro, 15/11/2026 (fila `cad2-marca-13`). Base que já existe: apps de SDR com botão WhatsApp que registra o envio e avança a cadência (`CLAUDE.md`), Robô do WhatsApp e a fila da Central (`/api/automacao`). Regra do Lindson: "automatizar: ele só toca em enviar/aprovar"; nada pago sem ele pedir (usar o gratuito).

## 1. O que o especialista sabe
- **Funil:** atrair → captar o contato → conversar → proposta → fechar → pós-venda. Automação tira o trabalho repetido de cada etapa, não a conversa humana na hora de fechar.
- **CRM simples:** cada contato tem etapa, data do último contato e próxima ação. Pode ser planilha, o app SDR da Central ou um CRM grátis.
- **Peças comuns:**
  - formulário/anúncio de cadastro → CRM ([Anúncios de cadastro da Meta](https://www.facebook.com/business/help/1481110642115637));
  - clique para WhatsApp com mensagem pronta;
  - resposta automática e menu no WhatsApp;
  - lembrete de follow-up;
  - mensagem de confirmação de agendamento;
  - pedido de avaliação no pós-venda.
- **WhatsApp automatizado de verdade exige a API oficial** (Cloud API, modelos de mensagem aprovados e opt-in). Fontes: [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api), [Modelos de mensagem](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates), [Política de opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in). Ferramentas "piratas" que controlam o WhatsApp comum arriscam banimento do número.
- **Ferramentas grátis/de baixo custo:** Cloudflare Workers (já usado na Central), Google Sheets + Apps Script ([documentação](https://developers.google.com/apps-script)), Meta Business Suite (respostas automáticas no Instagram/Messenger: [ajuda](https://www.facebook.com/business/help/1468289100139469)).

## 2. Trilha de 7 dias (1 h por dia)
| Dia | Estudo | Prática |
|---|---|---|
| 1 | Desenhar o funil de um cliente | Funil da SF em 6 caixas, com onde o contato se perde |
| 2 | App SDR da Central e o botão WhatsApp | Rodar uma cadência de 5 leads do começo ao fim |
| 3 | [Respostas automáticas no Business Suite](https://www.facebook.com/business/help/1468289100139469) | Configurar resposta automática de direct de um cliente |
| 4 | [Anúncios de cadastro](https://www.facebook.com/business/help/1481110642115637) | Desenhar formulário de 3 perguntas para Jaci |
| 5 | [Cloud API: começar](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started) | Listar o que o Robô do WhatsApp já faz e o que falta |
| 6 | [Apps Script](https://developers.google.com/apps-script) | Planilha que avisa follow-up vencido |
| 7 | Revisão | Escrever o relatório "horas economizadas e etapas medidas" |

## 3. Checklist de execução (por cliente)
1. Mapear o funil e as mensagens de cada etapa (copy no padrão `PADRAO-COPY.md`).
2. Uma entrada única de contatos (CRM/planilha) com etapa e próxima ação.
3. Captação: link WhatsApp com texto pronto em anúncio, site e bio; formulário quando fizer sentido.
4. Resposta automática fora do horário + menu simples (até 4 opções).
5. Cadência de follow-up: dia 0, 1, 3, 7 (o app registra sozinho ao tocar em enviar).
6. Confirmação e lembrete de agendamento (D-1).
7. Pós-venda: avaliação no Google + oferta de retorno.
8. Painel semanal: contatos novos por etapa e taxa de passagem entre etapas.
9. Revisão mensal: mensagem que menos converte é reescrita.

## 4. Como vender
- **Oferta:** "Seu atendimento funcionando sozinho": funil desenhado, respostas automáticas, cadência de retorno e painel com os números. Encaixa como complemento dos planos Presença e Instagram que Vende (`esteira-de-produtos.md`). Implantação avulsa: preço a definir com o Lindson.
- **Sem promessa** de vendas; prometer só o que se entrega (respostas configuradas, painel, rotina).
- **Mensagem:**
  > Oi, Seu João! Tudo bem? Aqui é o Lindson, de São Luís.
  > O cliente pede orçamento, você responde depois… e ele já fechou com outro.
  > Eu deixo seu WhatsApp respondendo na hora e lembrando você de quem precisa de retorno.
  > Quer que eu te mostre como funciona?

## 5. Erros comuns e regras
- Robô que não deixa falar com humano; disparo sem opt-in; ferramenta não oficial no WhatsApp; automatizar antes de ter a mensagem que funciona.
- **Saúde:** automação não dá orientação clínica; confirmação de consulta sem detalhe do procedimento.
- **Eleitoral:** proibido disparo em massa e robô de propaganda eleitoral (Resolução TSE nº 23.610/2019 e alterações: [TSE](https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019)).
- **LGPD:** base legal para guardar contato, opção de sair em toda cadência, dados do CRM fora do repositório público. Fonte: [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).

## 6. Aplicar já nos clientes
| Cliente | Próxima ação | Quem |
|---|---|---|
| Orégano Turbo | Resposta automática no Instagram/WhatsApp com link do cardápio e horário | Zuleide |
| Desentupidora SF | Cadência de retorno para orçamento não fechado (dia 1 e 3) | Pedro |
| Dra. Jaci | Mensagem de confirmação D-1 e de pós-consulta (avaliação) no Robô do WhatsApp | conta Lindson |
| Real Time | Formulário de reserva de equipamento → planilha → aviso no WhatsApp | conta Lindson |
| WF Celulares | Aviso automático "seu aparelho está pronto" | conta Lindson |
| Tribuna 98 / Leo | Resposta automática de direct (anunciantes / pedidos de bairro) | Leandro |
