# Tela do Dublê v2: template copiado (conta Pedro, 03/11/2026)

> Pedido do Lindson (03/11): "pesquise em sites de templates, e escolha o mais impactante, bonito, tecnológico e impressionante que existe, melhore o nosso. A identidade visual eu gostei, o template não."
> Regra do repositório: nada se cria, tudo se copia. Copiamos a **composição**; cores, logo e fontes são do Dublê (`IDENTIDADE.md`).

## Escolhido: Sermo (Framer Marketplace)
- Página: https://www.framer.com/marketplace/templates/sermo/ · ao vivo: https://sermo-ai.framer.website/
- Template "dark, motion-first" feito para agentes de voz com IA. Capturas em `referencias/sermo-*.png`.
- **Por que ganhou:** é o único que junta impacto (halo de raios de voz atrás de um título gigante) e cara de app de verdade (console com caixa de texto, abas em pílula e lista). Os outros são só página de venda.

## O que foi copiado → onde está no Dublê
| Sermo | Dublê (`web/`) |
|---|---|
| Menu em 3 pílulas flutuantes (logo · links · botão branco) | `.topo` |
| Halo de raios tracejados atrás do título | `#halo` (canvas). No Dublê ele **pulsa com a voz** enquanto gera e enquanto toca |
| Selo "Introducing" + título gigante em 2 linhas + 2 botões | `.heroi-txt` |
| "Sermo Console": Welcome back, caixa com botão redondo, abas em pílula, lista com setas | `.console` (Olá, Lindson · gerar voz · Áudios / Biblioteca / Vídeo) |
| Aviso flutuante com barras no canto | `.aviso-voo` (gerando / pronto / erro) |
| 3 cartões de números com gráfico (barras, pontos, progresso) | `.cartoes`, com números **reais** da biblioteca |
| Título em duas cores + 3 colunas com ícone | `.trava` (Só entra quem autorizou) |
| "Composer": passos 01–05 ao lado de painel de vidro | `.composer` (cadastro do dublê em 5 passos, com gravação pelo microfone) |
| Laranja do Sermo | Violeta Eco #8B7CFF; amarelo da Central só no consentimento |

## Comparados e descartados
| Template | Onde | Por que não |
|---|---|---|
| Volta Studio | framer.com/community/marketplace/templates/volta-studio | Bonito, mas genérico de SaaS (gradiente laranja/roxo) |
| VoxAI | framer.com/marketplace/templates/voxai | Rosto de robô e letra gigante: impacto, mas sem tela de app e com ilustração |
| Sonix | marketplace.framer.com/marketplace/templates/sonix | Página bloqueada para robô; não deu para conferir |
| Mucer (Cansaas, Contra) | contra.com/p/oqkE6ZYL-ai-audio-dashboard-design-for-mucer | Ótima organização de estúdio (menu lateral + histórico com ondas), visual menos impressionante. Fica como referência para a aba Vídeo |
| Echo (Wix), Voice AI (EpicPxls) | wix.com / epicpxls.com | Fora do padrão (Wix) ou pago sem prévia |

## Tela
Prévias: `tela-v2-1.png` (início), `tela-v2-3.png` (console com áudio), `tela-v2-4.png` (números), `tela-v2-6.png` (novo dublê), `tela-v2-celular.png`.
