# Modelo de aniversário de pessoas · Vereador Leo Pinto (conta Leandro, 03/11/2026)

Pedido do Lindson (03/11): "crie um modelo para aniversário de pessoas" + "crie um modelo que será usado para todos os aniversariantes" + "siga a regra de sempre buscar referências premium". Primeiro aniversariante: **Josef Figueiredo** (foto dele com o Leo num evento).

**Um modelo só para todos:** muda só nome, data, foto, frase e cor. Template escolhido e descartados em `TEMPLATE.md`.
- **Cor:** `laranja` (principal) ou `azul` (use azul quando a roupa da pessoa for laranja, como a do Josef). No feed, alternar com o post anterior (xadrez).
- **Foto:** a pessoa (de preferência com o Leo) recortada, saindo pela base da arte. Foto de pessoa **não vai para o Git**.
- **Assinatura fixa:** @_leonardopinto com avatar no topo, logo LEO PINTO na base esquerda (branca no azul, letras marinho no laranja), sem placa.
- **Proibido aqui:** balões, estrelas, brilhos, confete, ícones (regras do Leo, 02/11).

## Como fazer um aniversariante novo
1. Peça ao Lindson a foto (uma por mensagem), o nome como deve aparecer e a data.
2. `python3 recortar.py <foto.jpg> <pasta> [x0 y0 x1 y1]` → `<pasta>/recorte.png` (precisa de `rembg`).
3. Na pasta: `avatar.jpg` (foto de perfil do Leo), `logo.png` (= `../instagram-v12-feed/marca/logo_principal.png`), `logo-marinho.png` (`python3 logo_marinho.py <pasta>`), e `dados.json`:
   `{"nome1":"JOSEF","nome2":"FIGUEIREDO","data":"HOJE","cor":"azul","chamada":"Parabéns, amigo!","frase":"Que Deus abençoe sua vida com saúde, paz e muitas conquistas. Conte sempre comigo.","topo":470,"largura":900,"dx":0}`
   (`topo`/`largura`/`dx` ajustam a foto: rostos logo abaixo do nome; nome longo diminui sozinho).
4. `node gerar.js <pasta>` → `<pasta>/aniversario.jpg` (1080×1350).

**Legenda curta (padrão para aniversário):** "Hoje é dia de celebrar a vida do meu amigo <nome>! 🎉 Que Deus abençoe sua caminhada com saúde, paz e muitas conquistas. Feliz aniversário! #tôcomléopinto #SãoJoãoBatista" (sem pedir voto; marcar a pessoa).

Situação: Josef feito em 03/11, aguardando o OK do Lindson (aprovação da criação); depois sobe para as Aprovações do painel do Leo.
