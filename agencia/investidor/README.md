# Plano investidor (conta Lindson, Maquiavel gerente, 15/11/2026)

Pedido do Lindson: "quero fazer um plano investidor... deixe pronto pra eu apresentar para prospectos. Crie tudo bem detalhado."

## Arquivos finais (privados, para baixar)
`CentralLindsonALmeida/dados/agencia/investidor/` e `painel/admin-rede/investidor/`:
- `PITCH-DECK-INVESTIDOR.pdf` (16 slides 16:9)
- `PLANO-DE-NEGOCIOS.pdf` (12 páginas A4)
- `ONE-PAGER-INVESTIDOR.pdf` (1 página A4, mandar antes da reunião)
- `PLANO-INVESTIDOR.xlsx` (Premissas em amarelo, Uso do dinheiro, Projeção 24 meses por cenário, Unit economics, Retorno do investidor por estrutura, Sensibilidade; tudo fórmula)

## Fontes (esta pasta)
- `modelo.py`: premissas e projeção (fonte única dos números dos PDFs).
- `planilha.py`: gera a planilha com fórmulas reais.
- `documentos.py` + `textos.py`: geram deck, plano e one-pager (HTML → PDF pelo Chrome). Fotos e fontes são lidas do privado e das pastas do repositório.
- `ABORDAGEM.md`: WhatsApp, e-mail de follow-up, roteiro de 30 min, 15 objeções.
- `FALTA-DO-LINDSON.md`: dados que faltam.
- `TEMPLATE.md`: persona do investidor e pesquisa premium.

## Como gerar de novo
```
python3 planilha.py <saida>/PLANO-INVESTIDOR.xlsx
python3 documentos.py <saida>
```
Mudou uma premissa? Altere `modelo.py` (PDFs) ou só as células amarelas da planilha.

## O pedido (sugestão, decisão do Lindson)
R$ 70.000 (faixa R$ 50 a 80 mil) em 2 parcelas (R$ 40 mil + R$ 30 mil com 5 pizzarias pagantes). Revenue share de 10% da receita da operação de pizzarias, a partir do mês 4, até 1,5x (R$ 105 mil), prazo máximo de 60 meses. Projeção, nunca promessa; estrutura final com advogado e contador; conversa privada, sem oferta pública.
