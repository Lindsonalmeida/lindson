# Biblioteca do cliente (regra fixa desde 20/11/2026)

**Pedido do Lindson (20/11/2026):** "Organize a biblioteca de cada cliente, no painel de cada cliente, na Central do cliente. Coloque um menu lateral chamado BIBLIOTECA."

**Regra para todas as contas:** todo arquivo novo entra na Biblioteca do cliente. Entregou, subiu para o painel (`painel/<cliente>/` no privado ou nas Aprovações) e rodou o gerador.

## O que o cliente vê
- Menu lateral **Biblioteca** em todos os painéis de cliente (Jaci, Leo, WF, Mova Street, Real Time, SF, Orégano Turbo, Al Kántara, Curso Legislativo, Tribuna 98).
- **Categorias** (só aparecem as que têm itens):
  - Marca;
  - Artes e posts;
  - Carrosséis;
  - Stories;
  - Vídeos e Reels;
  - Capas;
  - Documentos;
  - Site e bio;
  - Referências e pesquisas;
  - Fotos.
- **Cada item mostra:**
  - miniatura;
  - título;
  - data em que entrou;
  - versão;
  - tamanho;
  - situação: aprovado, aguardando ou reprovado.
- **Botões:** Abrir (visualizador com todas as telas, ou o PDF ou a página em outra aba) e Baixar (série pequena e pacote de logos saem em ZIP).
- **Busca e filtros:** busca por nome, tipo ou data; filtro por categoria e por situação.
- **Escondidos por padrão:** reprovado e versão antiga. Cada um volta por um filtro: "Reprovado" e "Versões antigas".
- **Situação ao vivo:** se o cliente aprovar ou pedir ajuste em Aprovações, a Biblioteca segue o que está lá.

## Como rodar o gerador
Os dois repositórios ficam lado a lado: `lindson` e o privado `centrallindsonalmeida`.
```bash
cd agencia/sistema-clientes/site/painel-biblioteca
python3 gerar_biblioteca.py                  # todos os clientes
python3 gerar_biblioteca.py jaci leo         # só esses
python3 gerar_biblioteca.py --seco           # mostra o que faria, sem copiar nada
python3 testar_biblioteca.py                 # conferência com Playwright
python3 testar_biblioteca.py --prints <pasta>  # conferência + prints em 1440 px de Jaci, Leo e Mova
```
Depois, faça commit e push no privado (`painel/<cliente>/biblioteca/`, `painel/biblioteca.js` e os `painel/*.html`).

## De onde vêm os itens
A ordem é esta, e nenhum arquivo entra duas vezes (a conferência é pelo conteúdo, com md5):
1. **Aprovações do painel** (`const APROV` em `painel/<cliente>.html`): título, situação, telas, vídeo, PDF e nota.
2. **Arquivos já servidos** em `painel/<cliente>/`:
   - a série `c1-1` … `c1-6` vira um item só;
   - uma pasta de peças numeradas, ou com mais de 8 imagens, vira um item só;
   - uma pasta de logos vira 1 pacote.
3. **Entregáveis finais** que só existiam em `dados/clientes-arquivos/<x>/` (privado) ou `agencia/clientes/<x>/` (este repositório):
   - o que entra: PDF, logo, vídeo de até 10 MB e imagem de pasta de entrega (`entregas`, `final`, `logos`, `marca`, `identidade`, `brand-book`);
   - eles são **copiados** para `painel/<cliente>/biblioteca/arquivos/`, porque `dados/` não é público.
4. **Links** do site e da bio do cliente.

## O que nunca entra
- Arquivo acima de 24 MB (o deploy da Cloudflare trava em 25 MB). O que não coube aparece como "fora" na saída do gerador.
- Vídeo acima de 10 MB sem versão comprimida.
- `.json`, `.md`, `.py`, `.csv`, `.xlsx` e `.txt`.
- Nome com contrato, CPF, RG, TCLE, comprovante, procuração, senha ou código.
- Pastas de trabalho: referências de terceiros, capturas, banco de imagens, `assets`, fotos soltas, páginas renderizadas de PDF, rascunhos e testes.

## Versões e reprovados
- **Versão:** o gerador lê `v2`, `v3`, `v2.1` e "revisado" no caminho ou no título. Na mesma categoria e com o mesmo nome, só a maior fica como atual; as outras ganham a marca "versão antiga".
- **Reprovado:**
  - vem das Aprovações;
  - um arquivo solto herda a situação da pasta quando todas as Aprovações daquela pasta têm a mesma situação;
  - a lista `reprovado` de cada cliente em `CLIENTES` (gerador) marca à mão o que a `MEMORIA-DO-LINDSON.md` registra como reprovado.

## Cliente novo
1. Acrescente uma linha em `CLIENTES` no `gerar_biblioteca.py`, com:
   - `pastas`: a primeira é o nome do login do cliente;
   - `fontes`;
   - `links`;
   - `reprovado`.
2. Rode o gerador. Ele também põe a aba no painel, pelo `site/painel-feitas/injetar.py`, que o `montar-site.py` e os montadores já chamam.

## Segurança
O manifesto fica em `painel/<cliente>/biblioteca/manifesto.js`, dentro da pasta do cliente. O middleware da Central só deixa abrir:
- o próprio cliente;
- o admin.

O arquivo é `.js` porque a guarda do site bloqueia `.json`.
