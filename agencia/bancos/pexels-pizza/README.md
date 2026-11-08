# Banco de fotos de pizza · Pexels (300 fotos, 17 categorias)

- **Origem:** galeria "Fotos profissionais de pizzas", montada pelo Claude da outra conta em 08/11/2026 (https://claude.ai/artifact/1zT13Yi5gTQesfZvHwtY7h). Salva aqui pela conta Zuleide.
- **Licença Pexels:**
  - uso gratuito, inclusive comercial;
  - crédito opcional (nós damos o link da página);
  - proibido revender a foto sem alteração;
  - proibido sugerir que as pessoas retratadas endossam algo.
- **Arquivos:**
  - `catalogo.json`: categoria, ID, link em alta (`alta`) e página (`pagina`) de cada foto;
  - `previas/<categoria>.jpg`: folha de prévia com o ID embaixo de cada foto, para escolher.
- **Como usar uma foto:**
  1. Escolha pelo ID na prévia.
  2. Baixe em alta: `curl -o alta/<id>.jpg "<alta>?auto=compress&cs=tinysrgb&w=2000"`.
  3. Registre o uso no `FOTOS-USADAS.md` do projeto.
  4. Coloque o link da página nos créditos.
- **Fora do Git:** `miniaturas/` e `alta/` (pesados). Para recriar, use os links do catálogo.
- **Regras:**
  - foto de banco não substitui a foto real do cliente;
  - na arte do cliente, a foto real da pizzaria dele vem primeiro;
  - foto usada não se repete.
