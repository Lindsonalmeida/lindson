# Brand book premium · pesquisa e template (conta Pedro, 12/11/2026)

Pedido do Lindson (12/11): "crie o branding book de todos, um por cliente, template premium completo" (5 rebrandings: Real Time, WF Celulares, Curso de Processo Legislativo, Leo Pinto, Lindson Almeida) + Orégano Turbo, Dublê e Pagode Fiado (pedidos seguintes, mesmo dia).

## Persona (quem lê o brand book)
1. Dono do negócio ou do mandato, 30 a 55 anos, São Luís e interior do MA.
2. Recebe o PDF no WhatsApp e abre no celular ou na TV da sala de reunião.
3. Dor: cada fornecedor (gráfica, social media, fachada) faz a marca de um jeito.
4. Valoriza: parecer "empresa grande", regras simples, exemplos reais aplicados.
5. Confia quando vê a própria marca já funcionando (posts, site, fachada) e o antes x depois.
Teste: ele mostraria esse PDF para o sócio com orgulho? Sim, se for curto por página, visual e com as peças reais dele.

## Pesquisa (≥ 8 referências, 5 países)
Capturas: não salvas nesta rodada (sessão sem navegador; sites que bloqueiam robô não foram contornados). Referências públicas e conhecidas, listadas com o motivo.

| # | Referência | País | Situação | O que foi copiado |
|---|---|---|---|---|
| 1 | NASA Graphics Standards Manual (Danne & Blackburn, 1975; reedição Standards Manual) | EUA | **ESCOLHIDA** | Número de seção gigante, grade técnica fina, rótulo mono no topo de cada página |
| 2 | Collins · Dropbox Brand Guidelines (brand.dropbox.com) | EUA | **ESCOLHIDA** | Blocos de cor chapada em página cheia, tipografia enorme, paleta como faixas com proporção |
| 3 | Pentagram · Mastercard (Michael Bierut) | EUA / Reino Unido | **ESCOLHIDA** | Página do logo com área de proteção medida pelo próprio símbolo; usos incorretos em grade 3x2 com X |
| 4 | Unimark (Vignelli/Noorda) · NYC Transit Graphics Standards Manual | EUA / Itália | combinada | Tabelas técnicas de cor (HEX/RGB/CMYK) e de letra |
| 5 | Koto · Deliveroo e Bumble (cases no site da Koto) | Reino Unido | combinada | Capítulo de fotografia com regras curtas ao lado das fotos |
| 6 | Tátil Design · Rio 2016 (manual da marca) | Brasil | combinada | Antes x depois e conceito em uma frase antes do desenho |
| 7 | Spotify Design Guidelines | Suécia | descartada | Duotone e cores muito próprias do Spotify; vira cópia de estilo |
| 8 | DesignStudio · Airbnb "Bélo" | Reino Unido | descartada | Apoiado em ilustração; regra do Lindson é foto real |
| 9 | Brand New (UnderConsideration) · críticas de rebranding | EUA | combinada | Formato "o que mudou e por quê" em itens curtos |
| 10 | Templates "Brand Guidelines" do Behance/Envato | vários | descartada | Genéricos, muito espaço vazio ("simplista") |

**As 3 mais impactantes:** 1 NASA (grade e número gigante) · 2 Collins/Dropbox (cor chapada e tipo enorme) · 3 Pentagram/Mastercard (proteção e usos incorretos).

## Template
- `gerar.py` (dados de cada cliente dentro do arquivo) → HTML 1920x1080 por página → PDF via Playwright + prévias e folha de contato.
- `python3 gerar.py <cliente|todos>`; clientes: realtime, wf, curso, leo, lindson, oregano, duble, pagode. Logo do Pagode Fiado: `pagode-fiado/logo.svg` (Caveat Brush + Permanent Marker; títulos em Shrikhand, texto Work Sans).
- Saída (privado, fora do GitHub público): `CentralLindsonALmeida/dados/clientes-arquivos/<cliente>/brand-book/` e `dados/agencia/marca-lindson/brand-book/`.
- Seções: capa, índice, essência, persona, rebranding antes x depois, logo, versões, proteção e tamanho mínimo, usos incorretos, paleta, tipografia, elementos (Leo: página "sem grafismos"), fotografia, tom de voz, aplicações (2 páginas), contracapa.
- Cada livro usa as cores e letras do próprio cliente (nunca o visual de outro).
