# Identidade v2 · Leo da Baixada (mandato)

- `manual.html` → fonte do manual (12 páginas 4:5). Renderizar com Playwright.
- `leo-pinto-manual-identidade-v2.pdf` → manual do sistema de marca: capa, conceito, monograma com grade, logo em versões, cores, regras de uso, paleta HEX/RGB/CMYK, tipografia, 12 ícones, grafismos regionais, slogan e fotografia.
- `monograma.svg` → símbolo (L + sol + duas águas).
- Fotos: usa os recortes de `../v1/leo-*.png`.

## Pendente: mockups fotográficos
Bandeira, boné azul, camiseta amarela, crachá, placa do gabinete, faixa de evento e capa das redes.
`gerar-mockups.py` gera as fotos-base pelo Qwen-Image (Hugging Face). Em 30/10/2026 a cota ZeroGPU deu erro:
o token do segredo de rede não chegou ao Hugging Face (`whoami` respondeu "Invalid username") e o
`invoke` do conector MCP está desligado (gradio=none). Depois de gerar as fotos, aplicar o logo por cima
de cada uma e adicionar as páginas de aplicações ao manual.
