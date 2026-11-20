# Barzakh · método das cenas de mockup (conta Zuleide, sessão Barzakh, 20/11/2026)

Faz parte de `../APRESENTAR.md` (seção 2). Os prompts estão em `PROMPTS.md`.

## A regra em uma linha
**Cada imagem nasce inteira de um processo só.** O logo de um objeto ou é a textura de um render 3D (trilho A) ou nasce dentro da cena do Gemini e passa na sobreposição com o SVG (trilho C, se o Lindson aprovar). A cena do Gemini sem logo (trilho B) só recebe tipografia e logo **plano** numa área vazia. Nunca: colar PNG em perspectiva, juntar fotos, recortar pessoa para dentro da cena, corrigir logo por clonagem, foto do Lindson (decisão de 20/11).

## Trilho A · render 3D com a textura oficial (padrão)
- Base: `agencia/marca-lindson/projeto-designer/v3/gerador/` (`texturas.py` → `cenas.js` → `mockups.py`, three@0.169.0 + Playwright).
- Logos oficiais: Barzakh `projeto-designer/v3/marca/logos/png/ouro/` e `svg/`; clientes nas pastas `identidade` de cada um (Real Time `rt-full-jobs/identidade/v1/marca/`, WF `wf-celulares/identidade/logo-b/`, Orégano `operacao-propria/identidade/kit-mockup/`).
- Objetos novos a modelar: ecobag, camiseta dobrada, boné, copo térmico, caneca, avental, caderno espiral, crachá com cordão, tag com barbante, papel de seda com padrão, caixa de presente, pouch com válvula, copo de papel com luva, caixa de pizza, sacola kraft, marmita com cinta.
- Luz: 1 key light suave a 45°, gobo de janela, sombra de contato, chão de concreto (Barzakh, WF, Real Time) ou papel ou linho (Orégano, Jaci), grão leve. **A mesma luz em todas as cenas de um case.**
- Saída: 2160×2880 (feed 3:4), 2800 px de largura (Behance), 2000×3000 (Pinterest).
- Teste de realismo: a mesma cena no Blender Cycles (`pip install bpy`, headless). Ficar com o que estiver mais perto das refs 01 e 02 numa comparação lado a lado.

## Trilho B · cena do Gemini sem logo (regra aprovada)
1. Conversa nova no Gemini; modo de imagem (Nano Banana).
2. Cole o **texto de abertura** de `PROMPTS.md` uma vez.
3. Cole **1 prompt por mensagem**; peça a maior resolução; baixe e mande **1 arquivo por mensagem**.
4. Nós conferimos os 8 critérios (`agencia/processos/conferencia-imagem-ia.md`) com zoom e anotamos em `CONFERENCIA.md` nesta pasta. Um erro = não usa.

## Trilho C · Gemini com o logo anexado (TESTE, só com OK do Lindson)
1. Anexe **só** o PNG oficial indicado no prompt (fundo transparente, em alta).
2. A superfície do logo fica **de frente** para a câmera (sem curva forte, sem dobra sobre o logo).
3. Aprovação: abrimos a imagem a 100%, sobrepomos o SVG oficial com 50% de opacidade e comparamos letra por letra, proporção e espaçamento. **Qualquer diferença = descarta** (não se corrige por cima). Registro em `CONFERENCIA.md`.
4. Pode ser usado só como imagem-herói (1 por case), marcada "imagem gerada por IA".

## Mensagem de autorização ao cliente (Conexão → Dor → Desejo → Pergunta, até 280 caracteres)
> Oi, [nome]! A marca da [empresa] ficou entre os trabalhos que mais gosto. Quero mostrar no portfólio do estúdio (Instagram e Behance) só a marca e as aplicações, sem dado seu nem de cliente. Posso publicar?

Guardar o "sim" (print) no privado `dados/clientes-arquivos/<cliente>/autorizacao-portfolio.png` e marcar na tabela 3b do `APRESENTAR.md`.
