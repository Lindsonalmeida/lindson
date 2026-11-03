# Prompt para o Claude Design · Identidade do Dublê (conta Pedro, 03/11/2026)

Anexe junto com o prompt: `logo.svg`, `simbolo.svg`, `favicon.svg`, `previa.png`, `previa-app.png` e este `IDENTIDADE.md`. Se quiser mostrar o que o app faz, inclua também 2 ou 3 capturas da tela atual do app (Biblioteca e Voz).

```
Você é um diretor de arte sênior especialista em branding de produtos de IA (voz, vídeo e avatares). Crie a IDENTIDADE VISUAL COMPLETA do app "Dublê" e entregue tudo organizado como um manual de marca (brandbook) visual, em páginas 16:9.

=====================
BRIEFING
=====================
Nome: Dublê (nos arquivos, "duble"). Antes se chamava "Clone Studio".
O que é: um app INTERNO de clone de voz e de imagem da agência do Lindson Almeida (redes sociais, São Luís/MA). Roda no notebook dele, no navegador (Gradio), com uma placa RTX 3050. Ele clona a voz e o rosto do próprio Lindson, de clientes com autorização (um vereador e uma dentista) e de personagens de canais dark do YouTube (narradores, gravuras de Gustave Doré, Maquiavel).
Funções: Biblioteca (cadastro de cada dublê, com termo e vídeo de consentimento), Voz (texto vira fala na voz clonada) e Vídeo (boca sincronizada e gravuras vivas, a próxima etapa).
Público: o Lindson e a equipe dele. É uma ferramenta de trabalho, que ele usa todo dia.
Propósito: fazer conteúdo com a voz e o rosto de quem autorizou, rápido e sem estúdio.
Conceito: todo dublê trabalha com contrato. O símbolo é um círculo partido: a metade cheia é o original (o rosto) e a outra metade são barras de som, o duplo (a voz em eco). Em "dublê", o "d" e o "b" são o espelho um do outro.
Único: "O Dublê é o único estúdio de clone que só grava quem disse sim."
Personalidade: preciso, confiável, moderno e calmo. Arquétipo: o Mago com regra.
Tom de voz: português simples, "você", frases curtas, sem jargão e sem inglês.
Frase de apoio: "Voz e rosto, só com autorização."
Referências copiadas (citar em cada página): ElevenLabs (barras de voz, preto e branco, botão em pílula), Vercel (fundo quase preto, borda de 1 px, fonte Geist), Linear (um único destaque violeta, aba sublinhada), HeyGen (violeta de avatar e vídeo de consentimento), Suno e Runway (palavra em minúsculas e geométrica) e a Central Lindson Almeida (fundo escuro, Manrope e amarelo #F5C518).
O que NÃO quer: estética de "deepfake" ou hacker, neon, gradiente, brilho, robô, rosto de IA genérico, ilustração no lugar de foto real e textos em inglês na interface.

=====================
SISTEMA JÁ APROVADO (anexado): usar como base
=====================
- Símbolo: círculo partido. A metade esquerda é cheia (#F2F1EC) e a direita tem 3 barras arredondadas em Eco (#8B7CFF), com alturas 40/30/16. Fica sobre uma placa #15151C com cantos de 14/64 e borda de 1 px #2A2A35.
- Favicon: a mesma ideia com só 2 barras mais grossas, legível em 16 px.
- Logotipo: símbolo + "dublê" em minúsculas desenhado em traço geométrico de pontas redondas (sem fonte). Só o acento circunflexo vai em Eco.
- Paleta:
  · Grafite   #0B0B10 · fundo (60%)
  · Painel    #15151C · cartões e campos (30%, com a Linha #2A2A35)
  · Papel     #F2F1EC · texto (17,4:1)
  · Apagado   #9C9AAB · texto de apoio (7,1:1)
  · Eco       #8B7CFF · destaque (10%) · texto do botão em Grafite (6,0:1). Branco sobre o Eco é proibido.
  · Selo      #F5C518 · só consentimento e "liberado"
  · Certo #5CC98A · Erro #F0705C
- Tipografia: títulos em Geist SemiBold (espaço -2%), texto em Manrope 400/500/700 e números e selos em Geist Mono 500 maiúsculo. Todas no Google Fonts.
- Interface: modo escuro sempre, cartões com borda de 1 px e sem sombra, um único botão Eco (pílula) por tela, faixa de consentimento amarela e as barras do símbolo animadas enquanto gera.

=====================
ENTREGÁVEIS OBRIGATÓRIOS
=====================
1. CONCEITO: o conceito em 1 parágrafo, a frase do "único" e um moodboard (estúdio de dublagem, sala de gravação, contrato e espelho) com as referências citadas.
2. LOGOTIPO: horizontal, vertical, símbolo e favicon; colorido, 1 cor, positivo (fundo claro) e negativo (fundo escuro); área de proteção, tamanho mínimo (96 px / 16 px) e USOS INCORRETOS.
3. PALETA: as cores acima com a proporção 60/30/10, as combinações aprovadas e a tabela de contraste WCAG AA.
4. TIPOGRAFIA: H1 32, H2 22, H3 18, corpo 15, legenda 13 e selo 12, com pesos e espaçamentos.
5. ELEMENTOS DE APOIO: só as barras de voz (onda, divisor e carregando). Nada de outros grafismos.
6. ICONOGRAFIA: 10 ícones em linha de 1,5 px com pontas redondas (biblioteca, voz, vídeo, rosto, termo, vídeo de consentimento, liberado, bloqueado, baixar, personagem).
7. COMPONENTES DE INTERFACE: botão principal e secundário, campo, menu de escolha, controle deslizante de emoção, abas, selos LIBERADO/BLOQUEADO, faixa de consentimento, tabela da biblioteca e player de áudio com a onda.
8. TELAS (mockups 1440x900 no tema escuro): Biblioteca (cadastro + tabela), Voz (texto, emoção e resultado), Vídeo (rosto + áudio = vídeo) e a tela de bloqueio "Esse dublê está bloqueado: falta o termo".
9. APLICAÇÕES: ícone do atalho na área de trabalho do Windows, aba do navegador com o favicon, marca d'água "Feito com IA · Dublê" para os vídeos, etiqueta do arquivo gerado e o modelo do termo de autorização em A4.
10. TOM DE VOZ: 3 princípios com exemplos de "assim sim / assim não" para os botões, os avisos e os erros.

=====================
CRITÉRIOS DE QUALIDADE
=====================
- Coerência: as barras de voz se repetem no símbolo, no acento, no favicon e na animação.
- Simplicidade: o símbolo é reconhecível em 16 px e em 1 cor.
- Confiança: o consentimento aparece em toda tela onde entra gente real.
- Modernidade: no nível de ElevenLabs, Linear e Vercel, sem copiar a marca de nenhum deles.
- Família: conversa com a Central Lindson Almeida (fundo escuro, Manrope e amarelo só no selo).
- Acessibilidade: AA em todo texto, foco visível e movimento reduzido respeitado.
- Português simples em toda a interface.

=====================
FORMA DE TRABALHO
=====================
1. Parta do sistema anexado. Refine e eleve o acabamento, sem trocar o nome, o símbolo, a paleta nem as fontes. Se enxergar uma melhoria grande, mostre-a separada como "alternativa" e espere a minha aprovação.
2. Em cada página, cite qual referência real foi copiada (nada se cria, tudo se copia).
3. Desenvolva todos os entregáveis de 1 a 10, priorizando as telas (item 8) e os componentes (item 7).
4. Monte o MANUAL DE MARCA completo em páginas 16:9, com capa, sumário e os itens na ordem de 1 a 10.
Se faltar alguma informação, faça suposições razoáveis, diga quais foram e siga em frente.
```
