# Mova Street · prompts do Gemini para repor as imagens reprovadas na auditoria (conta Leandro, 18/11/2026)
Auditoria completa (peça por peça, com os erros de cada foto): privado `CentralLindsonALmeida/dados/clientes-arquivos/mova-street/AUDITORIA-IMAGENS-18-11.md`.

## Leia antes: como a marca aparece sem montagem
- **Proibido:** colar a logo em perspectiva no vidro, colar o anúncio ou o QR na tela da foto, recortar pessoa para outra cena e juntar fotos (regra do Lindson, 18/11).
- **Vidro traseiro:** a IA gera o carro com o vidro traseiro inteiro coberto por **adesivo perfurado laranja liso, sem letras**. A marca Mova Street entra na arte como **assinatura plana** (logo degradê em PNG transparente, no canto da peça, nunca em cima do vidro).
- **Tela TV Cars:** a IA gera a tela com fundo laranja e no máximo a frase "SUA MARCA AQUI". O **QR real** vai plano na arte, fora da foto, com "Aponte a câmera". QR feito pela IA não funciona e é proibido.
- O Gemini redesenha logos e erra letras (regra de 18/11, conta Pedro), por isso nenhum prompt pede logo nem marca.

## Regras de todos os prompts (já estão escritas dentro de cada um)
Fotografia realista, cinematográfica, de luxo, em São Luís do Maranhão, no fim de tarde ou à noite. O carro é de aplicativo comum (sedã ou hatch compacto prata ou grafite, sem emblemas) e o volante fica à esquerda (Brasil). Passageiro sempre no banco de trás. A tela de 10" fica presa nas duas hastes do encosto do banco da frente, centralizada atrás do encosto e virada para o banco de trás. Sem logotipos, marcas, placas legíveis ou textos, a não ser os indicados. Resolução 4K ou a maior disponível.

**Conferência ao receber:** 8 critérios de `agencia/processos/conferencia-imagem-ia.md`, com zoom. Um erro e a imagem volta com o erro descrito.

**Resolução mínima ao receber:** 16:9 ≥ 2560 px de largura (página e site a 1920); 4:5 ≥ 1080 × 1350; 21:9 ≥ 2160 px.

| Código | Cena | Formato | Substitui (foto antiga) | Onde entra |
|---|---|---|---|---|
| R01 | Tela no encosto, close, sem pessoa | 4:5 + 16:9 | 03 | feed v1 05, feed v2 12, apresentação p3, manual p18, site tela, destaque Funciona 03 |
| R02 | Passageira olhando a tela | 16:9 + 4:5 | 04 | feed v2 03, destaque Funciona 02, apresentação p5, book p21, site passageira |
| R03 | Passageiro aponta o celular para a tela | 4:5 | 05 | feed v2 02, apresentação p6, book p8, estratégia p28, site qr |
| R04 | Carro de aplicativo com vidro laranja na orla à noite | 16:9 + 21:9 | 01 e 08 | capas (book, apresentação, estratégia), proposta, feed v1 01, feed v2 04-06, site hero, bio e og |
| R05 | Close do vidro traseiro adesivado | 4:5 | 02 | feed v1 02, feed v2 10, destaque Funciona 01, apresentação p3, manual p17, site vidro |
| R06 | Aérea da Avenida Litorânea | 16:9 | 06 | feed v2 11, destaque Rua 01, apresentação p8, book p15, site cobertura |
| R07 | Frota de 5 carros de aplicativo | 16:9 | 09 | feed v1 03, manual p1 |
| R08 | Instalação do adesivo | 4:5 | 10 | feed v1 06, destaque Motorista 02, apresentação p12, manual p17 |
| R09 | Instalação da tela | 4:5 | 11 | feed v1 08, apresentação p12, manual p18 |
| R10 | Motorista parceiro com o carro | 4:5 | 14 | feed v1 04, destaque Motorista 01, apresentação p13, book p16, estratégia p25, site motorista |
| R11 | Dono de negócio vendo o resultado | 16:9 | 13 | feed v1 07, feed v2 09, book p8, estratégia p20, destaques Relatório |
| R12 | Cidade à noite vista do banco de trás | 16:9 | 16 e 16b | feed v1 09, feed v2 07, apresentação p9 e p14, book p9 e p23, estratégia p30, site final, destaque Relatório 01 |

A abertura do feed (painel 21:9 em 3 posts) já tem prompt próprio, revisado: `PROMPT-GEMINI-ABERTURA.md` (v4).
Ficam e não precisam de prompt: `fotos-ia/07` (Corolla no Centro Histórico, **versão sem logo**) e `fotos-ia/12` (empresário).

---

## R01 · Tela no encosto, close, sem pessoa (gerar em 4:5 e depois em 16:9)
Fotografia publicitária realista, formato 4:5 vertical (repita depois em 16:9 horizontal), resolução 4K ou a maior disponível. Interior de um sedã compacto de aplicativo, moderno e bem cuidado, à noite em São Luís do Maranhão. A câmera está no banco de trás, no centro, na altura dos olhos de um passageiro sentado, e olha reto para a frente. Lente 35 mm, f/2.

Em primeiro plano e no centro da imagem está a parte de trás do encosto de cabeça do banco do motorista, que fica no lado esquerdo do carro (volante à esquerda, padrão Brasil). Uma tela digital de 10 polegadas, moldura fina de alumínio escovado, presa por um suporte metálico nas duas hastes do encosto de cabeça. A tela fica centralizada na parte de trás do encosto, colada a ele, virada para trás (de frente para a câmera). Ela é do tamanho da largura do encosto e aparece inteira, nítida, sem cortes, sem flutuar.

A tela mostra fundo laranja vibrante e, no centro, a frase em português "SUA MARCA AQUI", em letras brancas grandes e sem serifa. Ortografia correta, sem nenhum outro texto, sem QR code, sem ícones.

A luz laranja da tela ilumina de leve o couro preto do encosto. Ao fundo, desfocados: o motorista sentado no banco dele, com as mãos no volante, e pelo para-brisa as luzes âmbar dos postes da cidade em bokeh. Couro preto, aço escovado, contraste alto, luz baixa, grão fino de filme.

Proibido: tela ao lado do encosto, tela flutuando, tela virada para o lado, banco do motorista vazio, volante à direita, logotipos, marcas de carro, QR code, qualquer texto além de "SUA MARCA AQUI", placas legíveis.

## R02 · Passageira no banco de trás olhando a tela (16:9 e 4:5)
Fotografia publicitária realista e cinematográfica, formato 16:9 horizontal (repita em 4:5), resolução 4K ou a maior disponível. Interior de um sedã compacto de aplicativo à noite em São Luís do Maranhão. Volante do lado esquerdo.

Enquadramento lateral de 3/4: a câmera está no banco de trás do lado esquerdo, virada para a direita e um pouco para a frente. Lente 35 mm, f/2.

À direita da imagem, uma mulher brasileira de 30 anos, cabelo cacheado, blazer azul-marinho e camisa clara, está sentada no banco de trás do lado direito, com o cinto de segurança. Ela olha para a frente, para a tela que está bem diante dela, com expressão interessada e um sorriso leve. As duas mãos estão no colo, segurando um celular apagado.

À esquerda da imagem fica o encosto do banco do carona (banco da frente, lado direito). Uma tela digital de 10 polegadas, moldura fina de alumínio escovado, está presa nas duas hastes desse encosto, centralizada atrás dele e virada para trás, de frente para a passageira. A câmera vê a tela de lado, em ângulo, por isso não se lê nada nela: só o brilho laranja. A luz laranja da tela ilumina o rosto e as mãos da passageira.

Pela janela, a cidade à noite em bokeh (postes âmbar, palmeiras). Couro preto, contraste alto, grão fino de filme.

Proibido: passageira no banco da frente, tela presa na lateral do encosto ou flutuando, tela virada para a câmera, passageira olhando para a janela, mãos ou dedos deformados, logotipos, marcas, textos, placas legíveis.

## R03 · Passageiro aponta o celular para a tela (4:5)
Fotografia publicitária realista, formato 4:5 vertical, resolução 4K ou a maior disponível. Interior de um sedã compacto de aplicativo à noite em São Luís do Maranhão. Volante do lado esquerdo.

Enquadramento por cima do ombro: a câmera está atrás e um pouco à direita do passageiro, que está sentado no banco de trás do lado direito. Lente 28 mm, f/2,8.

O passageiro é um homem brasileiro de 35 anos, cabelo curto escuro e camisa escura. Ele aparece de costas em 3/4 (orelha, maxilar, ombro e as duas mãos). Ele segura o celular na vertical com as duas mãos, na altura do peito: a câmera traseira do celular aponta para a tela à frente dele e o visor fica virado para ele. Por cima do ombro, o visor do celular mostra só um retângulo laranja (a imagem da tela), sem letras e sem números.

Bem à frente dele, a parte de trás do encosto de cabeça do banco do carona. Uma tela digital de 10 polegadas, moldura de alumínio escovado, está presa nas duas hastes do encosto, centralizada e virada para trás, de frente para o passageiro. A tela mostra fundo laranja e, em branco, "SUA MARCA AQUI". Ela fica levemente desfocada, porque o foco está nas mãos e no celular. A luz laranja da tela ilumina as mãos e o rosto dele.

Ao fundo, pelo para-brisa, a cidade em bokeh. A metade de cima da imagem fica escura e limpa, para texto.

Proibido: passageiro no banco da frente, celular com o visor virado para fora, QR code gerado na tela ou no celular, tela ao lado do encosto, qualquer texto além de "SUA MARCA AQUI", mãos ou dedos deformados, logotipos, marcas.

## R04 · Carro de aplicativo com vidro traseiro laranja na orla de São Luís à noite (16:9 e 21:9)
Fotografia publicitária automotiva realista e cinematográfica, formato 16:9 horizontal (repita em 21:9 panorâmico), resolução 4K ou a maior disponível. Avenida Litorânea de São Luís do Maranhão logo depois do pôr do sol: céu azul-marinho com a última faixa laranja no horizonte, mar escuro à esquerda, palmeiras e postes âmbar, prédios baixos da Ponta d'Areia ao longe.

Um sedã compacto prata, comum de aplicativo, moderno, limpo e sem emblemas, roda na faixa da direita, afastando-se da câmera. Ele é visto em 3/4 traseiro, nítido, no terço direito da imagem. O vidro traseiro inteiro está coberto por um adesivo perfurado laranja vibrante e liso (sem letras, sem desenhos), bem encaixado no formato do vidro. Os vidros laterais ficam escuros e normais. A placa aparece em branco, sem letras.

Rastros de luz laranja e azul dos outros carros passam pela pista da esquerda, que é a contramão, com desfoque de movimento no fundo e no asfalto. O carro principal está nítido e dentro da faixa dele, sem pisar na faixa dupla amarela. O terço esquerdo do céu fica escuro e limpo, para texto. Grão fino de filme, contraste alto.

Proibido: carro de luxo de marca reconhecível, emblemas, logotipos, letras no vidro, adesivo no teto, no para-brisa ou nos vidros laterais, carro sobre a faixa amarela, táxis amarelos, calçadão ondulado de Copacabana, ponte, placas legíveis, qualquer texto.

## R05 · Close do vidro traseiro adesivado (4:5)
Fotografia de produto automotivo premium, realista, formato 4:5 vertical, resolução 4K ou a maior disponível. Close de 3/4 da traseira de um hatch compacto prata, comum de aplicativo, sem emblemas, estacionado à noite numa rua de São Luís depois de uma chuva leve. Lente 85 mm, f/2,8.

O vidro traseiro está coberto por inteiro por um adesivo perfurado laranja vibrante e liso, cortado no formato exato do vidro, bem aplicado, sem bolhas, sem letras e sem desenhos. De perto, vê-se a textura de micro-furos do vinil perfurado. Gotas pequenas de chuva e o reflexo das luzes âmbar da rua aparecem sobre o vinil. A lanterna traseira acesa fica no canto inferior.

O enquadramento deixa o vidro como herói, ocupando metade da imagem, e uma área escura e limpa no alto, para texto. Luz lateral dura, contraste alto, grão fino.

Proibido: degradê azul, letras ou logo no vidro, trinca ou risco no vidro, emblema ou lanterna de marca reconhecível, limpador de para-brisa cortando o adesivo, placa legível.

## R06 · Aérea da Avenida Litorânea (16:9)
Fotografia aérea realista feita de drone, formato 16:9 horizontal, resolução 4K ou a maior disponível. Avenida Litorânea de São Luís do Maranhão no fim de tarde dourado: mar e faixa de areia à esquerda, pista dupla com canteiro de coqueiros, prédios residenciais baixos e médios à direita. O trânsito é o do Brasil, com mão à direita: na pista da direita os carros se afastam da câmera e mostram as lanternas; na da esquerda vêm de frente. Táxis brancos e carros comuns.

O drone está atrás e acima, a uns 40 metros, olhando para a frente com ângulo de 45°. No centro, na pista da direita, um sedã compacto prata de aplicativo se afasta da câmera e tem o **vidro traseiro** (só o vidro de trás, não o teto) coberto por um adesivo laranja vibrante e liso, sem letras. É o único ponto laranja forte da cena. O teto do carro é prata, igual à lataria.

A faixa de cima da imagem (céu dourado) fica limpa, para texto. Cores naturais, contraste alto, nitidez extrema.

Proibido: laranja no teto, táxis amarelos, calçadão de ondas de Copacabana, morros do Rio de Janeiro, logotipos, outdoors com texto, placas legíveis, letreiros.

## R07 · Frota de 5 carros de aplicativo (16:9)
Fotografia publicitária realista, formato 16:9 horizontal, resolução 4K ou a maior disponível. Cinco carros comuns de aplicativo (três sedãs compactos e dois hatches, prata e grafite, modernos e sem emblemas) estão estacionados lado a lado, de traseira para a câmera, num estacionamento coberto de concreto escuro, à noite. A luz de estúdio dramática vem de cima e o piso molhado reflete os carros.

Em todos os cinco, só o **vidro traseiro** está coberto por adesivo perfurado laranja vibrante e liso, sem letras, cortado no formato de cada vidro. Os vidros laterais ficam escuros e normais. As placas aparecem em branco. A câmera está centralizada, na altura de 1,2 m, com lente 35 mm. A faixa de cima, o teto escuro, fica livre para texto.

Proibido: carros de luxo de marca reconhecível (Audi, Mercedes, BMW), SUVs grandes, emblemas, logotipos, laranja nos vidros laterais ou no teto, letras, placas legíveis.

## R08 · Instalação do adesivo (4:5)
Fotografia realista de bastidor, formato 4:5 vertical, resolução 4K ou a maior disponível. Oficina de comunicação visual limpa e moderna em São Luís, com luz suave de teto. **Um único técnico**, de luvas pretas e camiseta escura, aplica o adesivo perfurado laranja no vidro traseiro de um hatch prata comum, sem emblemas.

O adesivo já está cortado no formato do vidro e metade dele já está colada no vidro. Com a mão direita, o técnico passa uma espátula azul de feltro sobre o adesivo, do centro para a borda. Com a mão esquerda, ele segura a parte do adesivo que ainda não foi colada, um pouco afastada do vidro. Close nas duas mãos e no vidro. Lente 50 mm, f/2,8. Rosto do técnico fora do quadro ou desfocado.

São só duas mãos, de uma pessoa, com 5 dedos cada. O adesivo fica todo sobre o vidro, nunca sobre a lataria. Laranja liso, sem letras.

Proibido: três mãos ou braços, segunda pessoa, adesivo solto no ar, adesivo sobre a lataria, degradê azul, letras, logotipos, marcas.

## R09 · Instalação da tela (4:5)
Fotografia realista de bastidor, formato 4:5 vertical, resolução 4K ou a maior disponível. Um técnico brasileiro de 35 anos, de luvas pretas e camisa escura, está sentado no banco de trás de um sedã compacto de aplicativo, com a porta traseira aberta, dentro de uma oficina limpa com luz suave. O banco está montado no carro, não fora dele.

Ele encaixa uma tela digital de 10 polegadas (moldura fina de alumínio escovado, tela apagada e preta) num suporte metálico preso nas duas hastes do encosto de cabeça do banco do motorista. A tela fica centralizada na parte de trás do encosto, virada para o banco de trás. Uma mão segura a tela pela borda e a outra aperta o parafuso do suporte com uma chave. Ao lado, no banco, uma maleta de ferramentas organizada. Foco nas mãos e no suporte. Lente 50 mm.

Proibido: banco fora do carro, tela na lateral do encosto, tela acesa com texto, mais de duas mãos, dedos deformados, logotipos, marcas.

## R10 · Motorista parceiro com o carro (4:5)
Retrato publicitário realista, formato 4:5 vertical, resolução 4K ou a maior disponível. Avenida de São Luís do Maranhão no fim de tarde dourado, com palmeiras e prédios desfocados ao fundo. Um motorista de aplicativo brasileiro de 38 anos, barba curta, camisa polo azul-marinho, sorri de forma natural e olha para a câmera. Ele segura a chave do carro com as duas mãos na altura da cintura.

Ele está de pé na calçada, ao lado da **traseira** do carro: um sedã compacto prata, comum, sem emblemas, estacionado junto ao meio-fio, visto em 3/4 traseiro atrás dele, à direita da imagem. O **vidro traseiro** do carro está coberto por um adesivo perfurado laranja vibrante e liso, sem letras, bem visível. O para-brisa e os vidros laterais ficam normais. Lente 85 mm, f/2, fundo desfocado.

Proibido: adesivo no para-brisa ou nos vidros laterais, carro de frente, carro parado no meio da pista, letras ou logo no vidro, logotipos, placas legíveis, mãos deformadas.

## R11 · Dono de negócio vendo o resultado (16:9)
Fotografia publicitária realista, formato 16:9 horizontal, resolução 4K ou a maior disponível. Um empresário brasileiro de 42 anos, camisa social clara com mangas dobradas, está atrás do balcão da sua loja (ótica ou cafeteria moderna) em São Luís, no começo da noite, com luz quente. Ele está à esquerda da imagem, olha o celular que segura com a mão direita e sorri satisfeito. A tela do celular está virada para ele: vemos só a parte de trás do aparelho e um leve brilho laranja no rosto dele.

À direita, pela vitrine, a rua desfocada ao entardecer, com um carro prata de aplicativo passando. O vidro traseiro do carro tem adesivo laranja liso e aparece em bokeh. A metade direita de cima da imagem fica limpa, para texto. Lente 50 mm, f/2.

Proibido: tablet ou celular com a tela virada para a câmera, gráficos, mapas, números, letras na tela, letreiros legíveis na loja, logotipos, marcas, mãos deformadas.
(O relatório com cliques, tela ligada e mapa entra na arte como gráfico plano e real, fora da foto, marcado "tela ilustrativa".)

## R12 · Cidade à noite vista do banco de trás (16:9)
Fotografia cinematográfica realista, formato 16:9 horizontal, resolução 4K ou a maior disponível. Interior de um sedã compacto de aplicativo andando à noite por uma avenida de São Luís do Maranhão. A câmera está no banco de trás, no centro, e olha para a frente, entre os dois bancos dianteiros. Lente 28 mm, f/2.

O motorista está sentado no banco da esquerda (volante à esquerda), visto de costas e desfocado, com as duas mãos no volante. O banco do carona está vazio. No centro, pelo para-brisa, a avenida com postes âmbar, palmeiras e luzes dos carros em bokeh suave. O painel é escuro e discreto, sem marcas. A metade de cima da imagem (teto escuro e céu) fica limpa, para texto. Luz baixa, contraste alto, grão fino de filme.

Proibido: carro andando sem motorista, volante à direita, painel de marca reconhecível (Tesla e outras), telas do painel com texto, logotipos, placas legíveis, qualquer texto.

---
## Se sair errado
Mande a imagem mesmo assim. A equipe confere os 8 critérios com zoom e devolve o prompt corrigido, dizendo o erro (como no `PROMPT-GEMINI-ABERTURA.md`).
