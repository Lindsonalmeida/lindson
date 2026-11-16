# Tweet + notícia v1 · carrossel no formato @oneyaraujo (conta Leandro, 16/11/2026)
Guia do formato: privado `dados/agencia/referencias/carrossel-tweet-noticia/` (5 referências). Busca prévia (`git grep tweet/noticia` nos dois repositórios): nada neste formato antes, nada repetido.

- 24 carrosséis de 5 telas (1080x1350, Playwright): `<linha>/NN/01..05.png`. Prévia das capas: `previa-grade.jpg`. Legendas blog SEO: `LEGENDAS.md`.
- Estrutura: tela 1 alerta + fato; 2 card da manchete (link da fonte); 3-4 narrativa e virada para o dono de negócio; 5 lição + ponte "Instagram que vende" (sem preço). Fundo alterna branco/preto (xadrez também entre carrosséis).
- Perfil do tweet: Lindson Almeida @lindsonalmeida_, avatar oficial (`linkedin/artes/foto-perfil-800.jpg`, o mesmo de todos os canais). Sem selo de verificado (o perfil não tem).
- Imagens: foto de capa (og:image) da própria matéria, com "Fonte: veículo · data · imagem: reprodução" queimado (uso jornalístico/comentário, como no formato de referência). Nenhum número ou citação fora do que está na matéria.
- Linha "Produtos do Rubla": TRAVADA. "Rubla" não existe em nenhum branch dos dois repositórios, nem na memória/quadro. Falta o Lindson dizer quais são os produtos.
- Gerar de novo: scripts `gerador/` (conteudo.py = textos e fontes; render.py; docs.py).

## Pesquisa premium das referências
Formato copiado: @oneyaraujo (5 capturas no privado). Linguagem visual do "print de tweet" do X/Twitter (Inter, cabeçalho avatar+nome+@, mídia com cantos de 34 px). Ponte final no preto e amarelo da marca do Lindson.

## Fontes das notícias
| Carrossel | Título | Fonte |
|---|---|---|
| Marketing e IA 01 | A Meta quer fazer seu anúncio sozinha | Sobre a Meta · 06/10/2026 · https://about.fb.com/br/news/2026/10/advertising-week-new-york-2026-novas-capacidades-de-ia-para-guiar-campanhas-e-alcancar-clientes/ |
| Marketing e IA 02 | Robô no seu WhatsApp: socorro ou risco? | Estado de Minas · 23/06/2026 · https://www.em.com.br/mundo-corporativo/2026/06/7447151-meta-lanca-ia-e-amplia-anuncios-no-instagram.html |
| Marketing e IA 03 | ChatGPT virou provador de roupa | Times Brasil | CNBC · 02/10/2026 · https://timesbrasil.com.br/empresas-e-negocios/tecnologia-e-inovacao/chatgpt-vira-provador-virtual-e-mostra-como-roupas-podem-ficar-em-voce/ |
| Marketing e IA 04 | O Google colocou anúncio dentro da resposta da IA | Tecnoblog · 20/05/2026 · https://tecnoblog.net/noticias/google-vai-exibir-anuncios-nas-respostas-com-ia-na-busca/ |
| Negócios 01 | Black Friday: vender muito e lucrar nada | Times Brasil | CNBC · 06/11/2026 · https://timesbrasil.com.br/brasil/pequenas-empresas-precisam-proteger-margens-e-negociar-fornecedores-na-black-friday-diz-sergio-all/ |
| Negócios 02 | A IA vai às compras pelo seu cliente | Fast Company Brasil · 10/05/2026 · https://fastcompanybrasil.com/money/google-e-openai-correm-para-lancar-ias-com-autonomia-para-fazer-compras/ |
| Negócios 03 | O cliente parou de pesquisar no Google | Olhar Digital · 24/03/2026 · https://olhardigital.com.br/2026/03/24/inteligencia-artificial/chatgpt-vai-ajudar-usuarios-a-pesquisar-e-comparar-produtos-sem-sair-da-plataforma/ |
| Negócios 04 | WhatsApp não salvou o caixa | Movimento Econômico · 17/04/2026 · https://movimentoeconomico.com.br/empreendedorismo/2026/04/17/whatsapp-nao-salva-o-caixa-meis-faturam-12-menos-em-2026/ |
| São Luís 01 | São Luís vai contratar no fim do ano | Imirante · 29/10/2026 · https://m.imirante.com/noticias/sao-luis/2026/10/29/comercio-maranhao-deve-abrir-1000-vagas-formais |
| São Luís 02 | Lisboa agora chega direto em São Luís | Movimento Econômico · 27/10/2026 · https://movimentoeconomico.com.br/economia/2026/10/27/chega-ao-maranhao-primeiro-voo-internacional-direto-de-lisboa/ |
| São Luís 03 | Afroturismo no Quilombo Liberdade | Imirante · 29/10/2026 · https://m.imirante.com/entretenimento/sao-luis/amp/2026/10/29/seminario-gratuito-debate-afroturismo-memoria-quilombo-liberdade-luis |
| São Luís 04 | Feira do Empreendedor em São Luís | Imirante · 24/07/2026 · https://m.imirante.com/noticias/sao-luis/2026/07/24/feira-do-empreendedor-2026-reune-mais-de-200-horas-de-capacitacao-e-palestra-gratuita-com-roberta-miranda |
| Assessor político 01 | Quase um conteúdo de IA por hora | Diário do Grande ABC · 06/10/2026 · https://www.dgabc.com.br/Noticia/4351247/nas-eleicoes-2026-quase-um-conteudo-eleitoral-com-ia-circulou-por-hora |
| Assessor político 02 | O que o TSE liberou e proibiu na IA | Migalhas · 11/05/2026 · https://www.migalhas.com.br/quentes/455672/ia-nas-campanhas-eleitorais-2026-veja-o-que-tse-autoriza-ou-proibe |
| Assessor político 03 | 72 horas de silêncio para a IA | Congresso em Foco · 19/08/2026 · https://www.congressoemfoco.com.br/artigo/121395/eleicoes-2026-ia-e-redes-sociais-mudam-o-jogo-para-candidatos |
| Assessor político 04 | O TSE se antecipou à IA | CNN Brasil · 17/01/2026 · https://www.cnnbrasil.com.br/eleicoes/uso-de-ia-e-riscos-da-desinformacao-pautam-regras-para-eleicoes-de-2026/ |
| Dono de grupo de tecnologia (Al Kántara) 01 | Itaú compra startup de IA por R$ 2,9 bi | Eu Quero Investir · 26/10/2026 · https://euqueroinvestir.com/acoes/itau-compra-startup-brasileira-de-ia-por-r-29-bilhoes |
| Dono de grupo de tecnologia (Al Kántara) 02 | Solo Network compra fábrica de data center | Baguete · 04/11/2026 · https://www.baguete.com.br/noticias/solo-network-adquire-planeje-tecnologia |
| Dono de grupo de tecnologia (Al Kántara) 03 | Comprou a empresa só pelo time | Startups · 09/09/2026 · https://startups.com.br/negocios/inteligencia-artificial/em-acqui-hire-strattum-adquire-tropicalia-que-encerra-atividades/ |
| Dono de grupo de tecnologia (Al Kántara) 04 | A IA virou critério de compra de empresa | Startups · 03/08/2026 · https://startups.com.br/exclusivo/com-regua-mais-alta-mas-caem-no-1o-semestre-de-2026/ |
| Dono de agência de design 01 | Depois de 10 anos, a agência mudou de nome | Portal Nosso Meio · 23/07/2026 · https://nossomeio.com.br/fkd-influencers-evolui-para-fkd-creators-e-reposiciona-a-marca-para-a-nova-fase-da-creator-economy/ |
| Dono de agência de design 02 | Rebranding de agência de Fortaleza | Portal Nosso Meio · 20/03/2026 · https://nossomeio.com.br/pronto-apresenta-rebranding-e-reforca-nova-fase-de-crescimento/ |
| Dono de agência de design 03 | 15 anos e uma marca nova | Portal Nosso Meio · 18/05/2026 · https://nossomeio.com.br/impulsione-celebra-15-anos-com-redesign-da-marca-e-reforco-do-posicionamento-estrategico/ |
| Dono de agência de design 04 | Jotacom virou Jota | Portal Nosso Meio · 27/07/2026 · https://nossomeio.com.br/jotacom-vira-jota-e-reforca-modelo-que-integra-publicidade-e-reputacao-com-criatividade-e-foco-no-negocio/ |