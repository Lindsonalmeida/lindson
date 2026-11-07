# Painel do Curso de processo legislativo na Central (conta Leandro, 07/11/2026)

Página própria do cliente **curso** na Central, com a identidade **v10 aprovada pelo Lindson em 07/11** (`agencia/clientes/curso-processo-legislativo/identidade/BRANDBOOK-V10.md`). Não usa a identidade do Tribuna 98.

**Endereço (depois de publicar):** https://lindsonalmeida.pages.dev/painel/curso
**Código de acesso:** `CPL-…` (gerado em 07/11; entregue ao Lindson na conversa, não salvo aqui). Falta colar a linha no privado (passo 3).

## Como montar (igual aos outros clientes)
```bash
cd agencia/sistema-clientes
python3 curso-processo-legislativo/montar-curso.py   # gera painel-curso.html
python3 site/montar-site.py                          # gera site/publico/ (fora do Git)
```
- `montar-curso.py`: o modelo da Central (`prototipo/painel.html`) com as cores e a fonte da v10 (Inter Display / Inter), logo em texto e os dados do escopo. Os dados ficam no próprio script (sem foto nem dado pessoal).
- `painel-curso.html`: gerado; fica no Git porque não tem dado pessoal nem foto.

## O que falta para o cliente entrar
1. **Publicar:** com o `site/publico/painel/curso.html`, colar no repositório privado `CentralLindsonALmeida` e fazer push (a Cloudflare publica sozinha). Só com OK do Lindson.
2. **Código:** `site/novo-codigo.py curso CPL` gerou o código. A linha `{ sal, hash, cli: 'curso' }` vai para `CentralLindsonALmeida/functions/_codigos.js` (privado). Não salvar o código em repositório.
3. **Conteúdo a confirmar:** estrutura do curso (aulas), link definitivo da bio, turma de 10 de abril (o post é de 19/03, pode já ter passado), foto de perfil e quem é quem entre os instrutores.
4. **Pendências de arte:** capa v11 (A, B ou C) escolhida pelo Lindson; pesquisa premium ainda parcial (ver `agencia/clientes/tribuna98/curso-processo-legislativo/TEMPLATE.md`).

Registrado em `site/montar-site.py`, `site/admin-sistema.js` e `site/contas.html` (nome "Curso de processo legislativo").
