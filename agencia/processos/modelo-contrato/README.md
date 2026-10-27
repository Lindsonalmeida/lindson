# Modelo de contrato (padrão aprovado: Dra Jaci Cunha / Apple Black, out/2026)

Usar sempre que o Lindson pedir um contrato de cliente.

1. Dados da CONTRATADA (Lindson Almeida Pinheiro Lopes — ALKANTARA, CNPJ 47.826.006/0001-86): `agencia/contratos/meus-dados.json`, fora do GitHub. Se não existir na sessão, pedir ao Lindson os dados ou o PDF de um contrato anterior.
2. Dados do cliente: `agencia/contratos/<cliente>/dados.json` (exemplo de campos: `plano`, `subtitulo`, `objeto`, `contratante{nome,qualificacao,email,whats,assinatura[]}`, `incluido[]`, `nao_incluido[]`, `gravacoes[]` opcional, `responsabilidade_tecnica` opcional (ex.: CFO/CRO na saúde), `valor`, `tabela`/`desconto` opcionais, `inicio`, `fim`, `vencimento_dia`, `meses`, `arquivo`).
3. `python3 agencia/processos/modelo-contrato/gerar.py agencia/contratos/<cliente>/dados.json` → PDF A4 com rodapé e páginas.

Cláusulas fixas do padrão: objeto; o que está incluído (sem número fixo de publicações, calendário apresentado antes) e o que não está; gravações (opcional); aprovação pelo WhatsApp oficial em 48h com 2 rodadas de ajuste (sem retorno = adiamento, sem acúmulo nem desconto); pagamento pré-pago (serviço só começa após pagamento), multa 2% + juros 1% a.m. pro rata, suspensão após 15 dias; vigência de 3 meses com renovação automática (aviso de 30 dias); reajuste a cada renovação pela tabela ou IPCA anual; obrigações das partes; obrigação de meio (sem garantia de resultado) e isenção por bloqueios das plataformas; multa de 20% das parcelas restantes na rescisão imotivada no 1º período; sem devolução de mês iniciado; direitos autorais (editáveis e estratégias ficam com a contratada), devolução de acessos, portfólio; sem vínculo nem exclusividade; foro São Luís/MA; 2 testemunhas.

Nunca colocar no GitHub dados pessoais (CPF, endereço) do Lindson ou de clientes.
