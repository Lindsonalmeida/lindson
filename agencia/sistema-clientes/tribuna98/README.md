# Painel do Tribuna 98 na Central (conta Leandro, 07/11/2026)

Página própria do cliente **Tribuna 98** na Central, com a identidade do próprio Tribuna (azul royal e amarelo da logo). Não é a identidade do curso.

**Endereço (depois de publicar):** https://lindsonalmeida.pages.dev/painel/tribuna
**Código de acesso:** `TRB-…` (gerado em 07/11; entregue ao Lindson na conversa, não salvo aqui). Falta colar a linha no privado (passo 3).

## Como montar (igual aos outros clientes)
```bash
cd agencia/sistema-clientes
python3 tribuna98/montar-tribuna.py   # gera painel-tribuna.html
python3 site/montar-site.py           # gera site/publico/ (fora do Git)
```
- `montar-tribuna.py`: o modelo da Central com a identidade do Tribuna. Os números são os de 03/11 (prints de 07/11 a confirmar). Sem foto dos sócios.
- Nomes de pessoas: não usar nomes de sócios no painel até o Lindson confirmar (regra da trava, `TRAVA-MAQUIAVEL.md`, item 6).

## O que falta para o cliente entrar
1. **Publicar:** com o `site/publico/painel/tribuna.html`, colar no repositório privado `CentralLindsonALmeida` e fazer push. Só com OK do Lindson.
2. **Código:** `site/novo-codigo.py tribuna TRB` gerou o código. A linha `{ sal, hash, cli: 'tribuna' }` vai para `CentralLindsonALmeida/functions/_codigos.js` (privado).
3. **Pendências:** prints de 07/11 e Insights (item 8), decisão do site principal (item 4), pesquisa premium do painel ainda parcial.

Registrado em `site/montar-site.py`, `site/admin-sistema.js` e `site/contas.html` (nome "Tribuna 98").
