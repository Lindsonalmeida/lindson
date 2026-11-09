# Criativos de tráfego dos produtos da Hubla (conta Leandro, 09/11/2026)

Pedido do Lindson (09/11): "crie 5 criativos para cada produto meu, dos produtos cadastrados no hubla e coloque no repositorio para subir nas campanhas de trafego" + "faça no estilo infoprodutor do behance".

**6 produtos x 5 = 30 criativos**, 1080x1350 (4:5, serve feed e, com margem, Stories/Reels):
Bio que Vende · Kit Mês Pronto · Kit WhatsApp que Fecha · Kit Prospecção · Raio-X do Perfil · Pack de Capas de Destaque.

## Onde está
- Textos de cada criativo, texto principal e título do anúncio: `criativos.json`.
- Gerador: `node gerar.js <recortes> <saida> [slug]` (Playwright). Recortes: `python3 recortar_lote.py <pasta> [n]` (BiRefNet; as fotos ficam no privado).
- **Artes prontas para subir:** `CentralLindsonALmeida/produtos/criativos-trafego/<produto>/<produto>-0N.jpg`.

## Os 5 ângulos (um layout cada, cor alternando: nunca dois seguidos iguais)
1. **Especialista:** palavra gigante em ouro atrás, o Lindson recortado com luz âmbar, capa do produto em 3D, manchete com caixa e botão.
2. **Dor:** "?" gigante vazado, recorte à esquerda, a dor do cliente em pergunta.
3. **O que vem dentro:** capa em 3D + entregáveis em cartões numerados (sem foto nova).
4. **Número:** o número do produto (15 min, 30 roteiros, 20 respostas, 100/10 nichos, 11 pontos, 36 capas) gigante + recorte.
5. **Virada:** cartão ANTES riscado x cartão DEPOIS em destaque.

## Regras seguidas
- Sem preço na arte (só no checkout), sem promessa de resultado, sem número inventado: os números são o conteúdo do produto (`copy.json` das landings).
- Foto usada uma só vez: 23 fotos diferentes do Lindson, uma por criativo (os 6 do ângulo 3 e o 5 do Pack não usam foto).
- O corte de baixo do recorte sai pela base da arte (nunca aparece).
- Marca do Lindson: só preto `#0A0A0A` e amarelo `#F5C518`, Anton + Manrope (+ JetBrains Mono nos rótulos).

## Situação
Aguardando aprovação do Lindson. Depois de aprovado: subir no Gerenciador de Anúncios (pela extensão do Chrome) com o `texto` e o `headline` de cada produto e o link do checkout da Hubla.
