# Modelo de contrato (gestão de redes sociais / serviços da agência)

Usar sempre que o Lindson pedir um contrato de cliente.

1. Dados do Lindson (contratado): `agencia/contratos/meus-dados.json` (fora do GitHub, porque tem CPF/endereço). Campos: `contratado_qualificacao`, `contratado_nome`, `contratado_doc`. Se o arquivo não existir na sessão, pedir os dados ao Lindson.
2. Dados do cliente: criar `agencia/contratos/<cliente>/dados.json` com `plano`, `cliente_qualificacao` (nome, nacionalidade, estado civil, profissão, CPF, endereço, e-mail, WhatsApp), `cliente_nome`, `cliente_doc`, `cliente_instagram`, `escopo` (lista de [entrega, quantidade]), `valor` (ex.: "R$ 2.000,00 (dois mil reais)"), `forma_pagamento`, `dia_vencimento`, `data_inicio`, `data_assinatura`, `arquivo`.
3. Rodar `python3 agencia/processos/modelo-contrato/gerar.py agencia/contratos/<cliente>/dados.json`.

Cláusulas fixas: objeto com tabela de escopo, obrigações das partes, aprovação em 2 dias úteis (silêncio = aprovado), verba de anúncio paga pelo cliente direto à Meta, multa 2% + juros 1%/mês e suspensão após 5 dias de atraso, reajuste anual IPCA, prazo indeterminado mês a mês com aviso de 30 dias, direitos de imagem e portfólio, sem garantia de resultado, LGPD, foro São Luís – MA.
Nunca colocar dados pessoais de clientes ou do Lindson no GitHub.
