# Instruções do repositório (Lindson Almeida)

## Mini site de cliente (bio)

Sempre que o Lindson pedir um mini site / site bio para um cliente, **antes de começar**, lembre a ele o passo a passo de `agencia/processos/mini-site-cliente.md` e siga-o:

1. Cada cliente tem **o próprio repositório** na conta `Lindsonalmeida` (nome do cliente, sem espaço nem acento, privado). Peça para ele criar o repositório vazio e liberar o acesso do app Claude (All repositories).
2. O site fica no repositório do cliente, **nunca** dentro deste repositório `lindson` (o link não pode ter o nome Lindson).
3. Publicação pela **Cloudflare Pages**: Workers e Pages → Criar → Pages → Importar repositório → Project name = nome do cliente, branch `main`, framework `None`, build vazio. Link final: `nomedocliente.pages.dev`.
4. Links internos absolutos (prévia do WhatsApp, cards) usam o endereço `pages.dev` do cliente.
5. Fotos: pedir uma por mensagem (imagens enviadas no meio de uma resposta não ficam salvas). Nunca usar ilustração no lugar de foto real de produto.
6. Depois de publicar, atualizar a tabela "Clientes ativos" no fim de `agencia/processos/mini-site-cliente.md`.

Clientes ativos hoje: Rafael Imports → repositório `Lindsonalmeida/rafaelimports` → https://rafaelimports.pages.dev

## Copy de vendas (padrão aprovado)

Legendas de post: sempre estilo blog SEO (título com palavra-chave, introdução, subtítulos, exemplo, conclusão, chamada e 3 a 5 hashtags pesquisadas e variadas — tema + nicho + local, nunca o mesmo bloco; até 2.200 caracteres) — modelo em `conteudo/avaliacao-gratuita/LEGENDAS.md`.

Carrosséis: depois da capa, nenhuma tela repete o layout da anterior. Variar composição dentro da identidade (número grande, número de fundo, cor invertida, cartão, problema × solução, faixas, frase de impacto).

Posts estáticos: nunca dois seguidos na mesma composição nem na mesma cor. Alternar entre foto inclinada, celular, palavra gigante, manchete, foto dividida, checklist, conversa e selo — sempre na identidade.

Lead que respondeu "pode mostrar": entregar PDF de proposta na identidade visual DO CLIENTE, seguindo `agencia/processos/proposta-cliente.md` (8 páginas 4:5, sem inventar números).

Toda mensagem de abordagem e copy curta de venda segue `agencia/prospeccao/PADRAO-COPY.md`: **Conexão → Dor → Desejo → Pergunta**, linguagem simples de WhatsApp, entendida numa única leitura. Nunca usar "vi que", "parece que", "gargalo", jargão de marketing ou análise do perfil da pessoa.
