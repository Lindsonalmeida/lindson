# Modelo de aniversário de pessoas · Vereador Leo Pinto (conta Leandro, 03/11/2026)

Pedido do Lindson (03/11): "crie um modelo para aniversário de pessoas" + "crie um modelo que será usado para todos os aniversariantes" + "siga a regra de sempre buscar referências premium". Primeiro aniversariante: **Josef Figueiredo** (foto dele com o Leo num evento).

**REGRA (Lindson, 09/11/2026): aniversário = SÓ STORY, sempre (`"story":true`). Não fazer versão de feed.**

**Um modelo só para todos (versão 2, detalhada):** muda só nome, data, foto, frase e cor. Composição combinada de 3 modelos externos do Designi (Carla Silva, Pr André Vieira, Pedro Sampaio): parede de PARABÉNS, "parabéns" manuscrito, pessoa com contorno de luz, nome em caixas inclinadas, frase grifada. Ver `TEMPLATE.md`. A v1 (simples) foi reprovada.
- **Cor:** `laranja` (principal) ou `azul` (use azul quando a roupa da pessoa for laranja, como a do Josef). No feed, alternar com o post anterior (xadrez).
- **Foto:** a pessoa (de preferência com o Leo) recortada, saindo pela base da arte. Foto de pessoa **não vai para o Git**.
- **Assinatura fixa:** @_leonardopinto com avatar no topo, logo LEO PINTO na base esquerda (branca no azul, letras marinho no laranja), sem placa.
- **Proibido aqui:** balões, estrelas, brilhos, confete, ícones (regras do Leo, 02/11).

## Como fazer um aniversariante novo
1. Peça ao Lindson a foto (uma por mensagem), o nome como deve aparecer e a data.
2. `python3 recortar.py <foto.jpg> <pasta> [x0 y0 x1 y1]` → `<pasta>/recorte.png` (precisa de `rembg`).
3. Na pasta: `avatar.jpg` (**a foto de perfil oficial** do Leo; sem o arquivo, recorte o círculo do @ de uma arte aprovada: `p3-11-12.jpg` em (84,70,127,113)), `logo.png` (= `../instagram-v12-feed/marca/logo_principal.png`), `logo-marinho.png` (`python3 logo_marinho.py <pasta>`), e `dados.json`:
   `{"nome1":"JOSEF","nome2":"FIGUEIREDO","data":"HOJE · 03 DE NOVEMBRO","cor":"azul","chamada":"Parabéns, amigo!","frase":"Que Deus abençoe| sua vida com saúde,| paz e muitas| conquistas.","assinatura":"Conte sempre comigo.","topo":330,"largura":980,"dx":20}`
   (`|` quebra a frase em linhas grifadas)
   (`topo`/`largura`/`dx` ajustam a foto: rostos logo abaixo do nome; nome longo diminui sozinho).
4. `node gerar.js <pasta>` → `<pasta>/aniversario.jpg` (1080×1350).

**Legenda curta (padrão para aniversário):** "Hoje é dia de celebrar a vida do meu amigo <nome>! 🎉 Que Deus abençoe sua caminhada com saúde, paz e muitas conquistas. Feliz aniversário! #tôcomléopinto #SãoJoãoBatista" (sem pedir voto; marcar a pessoa).

Situação: Josef **aprovado pelo Lindson** em 03/11 e publicado nas Aprovações do painel do Leo (arte no privado `dados/clientes-arquivos/leo/aniversarios/`). Para subir um novo: acrescente o item no começo de `APROV` em `painel/leo.html` do privado (1080×1350, qualidade 92) ou no `montar-leo.py`. Sempre mande a arte na conversa antes.

## Modelos B e C (03/11, conta Leandro)
O Lindson: "crie mais dois modelos da arte de parabéns, ele não gostou dessa, e melhore a qualidade da foto". Copiados de modelos EXTERNOS do Designi (capturas em `referencias/`):
- **B · editorial claro** (`aniversario-b.html`): "João Cláudio" + "Vereador Gustavo José": fundo creme, PARABÉNS gigante laranja com 2 ecos em contorno atrás das cabeças, frase grifada, data, pílula marinho com o nome, "Parabéns" manuscrito.
- **C · tipografia em blocos** (`aniversario-c.html`): "Thais Campos" + "Thiago dos Santos": fundo azul, "feliz" manuscrito + ANI/VER/SÁRIO empilhado (SÁRIO amarelo), nome, frase, pílula da data, pessoas grandes à direita sobre um disco amarelo.
- Gerar: `"modelo":"b"` ou `"c"` no dados.json → `node gerar.js <pasta> dados-b.json` → `aniversario-b.jpg`.

**Foto melhor:** antes de recortar, `python3 ../../../../ferramentas/melhorar_foto.py foto.jpg foto-hd.png` (Real-ESRGAN x2 + ajuste leve de cor; modelo em `~/.modelos/real_esrgan_x2.onnx`, baixar de https://huggingface.co/facefusion/models-3.0.0/resolve/main/real_esrgan_x2.onnx). O recorte é feito na foto HD.

**Modelo B aprovado pelo Lindson (03/11) = padrão de aniversário.** Story: acrescente `"story":true` no dados.json → `aniversario-b-story.jpg` (1080×1920 em 2×, áreas seguras do story).
