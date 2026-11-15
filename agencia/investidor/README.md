# Plano investidor v2 · empresa inteira (conta Lindson, Maquiavel gerente, 15/11/2026)

> v2 (15/11): o Lindson corrigiu: o pitch é para a empresa toda, não só para a pizzaria. Seis frentes (agência, Orégano Turbo, produtos digitais, YouTube e marca pessoal, tecnologia própria, equipe de IA), receita real de R$ 4.800/mês (Jaci 1.500, Leo 2.500, WF 800) como base.

Pedido do Lindson: "quero fazer um plano investidor... deixe pronto pra eu apresentar para prospectos. Crie tudo bem detalhado."

## Arquivos finais (privados, para baixar)
`CentralLindsonALmeida/dados/agencia/investidor/` e `painel/admin-rede/investidor/`:
- `PITCH-DECK-INVESTIDOR.pdf` (17 slides 16:9)
- `PLANO-DE-NEGOCIOS.pdf` (12 páginas A4)
- `ONE-PAGER-INVESTIDOR.pdf` (1 página A4, mandar antes da reunião)
- `PLANO-INVESTIDOR.xlsx` (Consolidado, Premissas em amarelo, Uso do dinheiro, uma aba por unidade, Unit economics, Retorno do investidor, Sensibilidade; tudo fórmula)

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
R$ 100.000 (faixa R$ 80 a 120 mil) em 2 parcelas (R$ 60 mil + R$ 40 mil quando a receita nova somar R$ 10 mil/mês por 2 meses). Revenue share de 10% sobre a receita nova (acima dos R$ 4.800/mês de hoje), a partir do mês 4, até 1,5x (R$ 150 mil), prazo máximo de 60 meses. Projeção, nunca promessa; estrutura final com advogado e contador; conversa privada, sem oferta pública.
