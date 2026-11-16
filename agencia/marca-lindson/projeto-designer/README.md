# Projeto Designer do Lindson (conta Leandro, 16/11/2026)

Pedido do Lindson: "faça logo você agora" (fila cad-designer-26 Behance e 29 Vender identidade visual). Pinterest (27) ficou com a equipe Pedro e LinkedIn (28) com a equipe Zuleide: **usem o nome e as imagens daqui**.

## Nome do projeto (as contas vão ter este nome)
1. **Lindson Almeida Studio** (@lindsonalmeidastudio): RECOMENDADO. Usa a autoridade que já existe (Instagram @lindsonalmeida_, site lindsonalmeida.pages.dev, brand book da marca). Quem compra identidade visual em São Luís compra de uma pessoa em quem confia: o nome dele na frente passa isso. 'Studio' diz que é serviço de design, não perfil pessoal. Funciona igual no Behance, Pinterest e LinkedIn.
2. **Âmbar Estúdio de Marca** (@ambar.estudio): Vem da luz âmbar da marca do Lindson (preto + #F5C518). Nome curto, premium, fácil de falar. Contra: começa do zero em autoridade e 'âmbar' é palavra comum, chance maior de o @ estar ocupado.
3. **Forja Branding** (@forja.branding): Ideia de construir marca forte, ligada ao universo 'Estado Próprio' (pedra, fortaleza). Soa de estúdio grande. Contra: separa o estúdio do rosto do Lindson, que é o que mais vende hoje.

**Recomendado: Lindson Almeida Studio (@lindsonalmeidastudio).** Disponibilidade do @: não deu para checar daqui (Behance, Pinterest e LinkedIn bloqueiam robô); o Lindson confere na hora de criar. Se estiver ocupado: `lindsonalmeida.studio` ou `studiolindsonalmeida`.
Para trocar o nome em tudo: mude `STUDIO`/`HANDLE` em `gerador/conteudo.py` e rode `python3 gerador/gerar.py <saida> <páginas dos brand books> <site/img>` e `python3 gerador/landing.py <privado>/site/identidade`.

## Persona (quem compra identidade visual)
1. Quem: dono(a) de negócio local de São Luís/MA e interior (clínica, loja, restaurante, escritório, profissional liberal, criador de curso), 28 a 50 anos, fatura com o boca a boca e já tem Instagram.
2. Rotina: atende o dia inteiro, posta quando dá, faz arte no Canva ou com sobrinho; decide pelo celular, à noite, pelo WhatsApp.
3. Dor: a marca parece amadora perto do concorrente, cada post sai de um jeito, tem vergonha de mandar o perfil para cliente maior; quer cobrar mais e não consegue.
4. Valoriza: ver trabalho real de gente da região, processo claro, prazo cumprido, alguém que entende de venda, não só de 'desenho'.
5. Confia quando: vê cases completos (antes e depois, aplicações reais), fala com o próprio designer no WhatsApp e recebe proposta organizada. Está no Instagram, Google e WhatsApp; empresas maiores e online olham Behance e LinkedIn.
Teste: essa pessoa compraria disso? Sim, se a peça mostrar o case pronto e aplicado, sem jargão e com caminho direto para o WhatsApp.

## Passo a passo para criar as contas (o Lindson faz, ~20 min)
1. **Behance:** behance.net → Sign up (com conta Adobe, e-mail dele) → nome de exibição "Lindson Almeida Studio" → URL `lindsonalmeidastudio` → Edit profile: cole os campos de `BEHANCE.md` → "Create a project" para cada pasta de `behance/` (capa = `00-capa-808x632.jpg`, módulos 01 a 10 em ordem, título/descrição/tags/ferramentas do `TEXTO.md`) → Publicar.
2. **Pinterest empresa:** business.pinterest.com → Criar conta empresarial → nome "Lindson Almeida Studio | Identidade Visual", usuário `lindsonalmeidastudio` → reivindicar o site lindsonalmeida.pages.dev. Pastas e pins: equipe Pedro.
3. **LinkedIn:** (a) perfil pessoal "Lindson Almeida" (o link já existe no site: linkedin.com/in/lindson-almeida-64953b281); (b) Para empresas → Criar página → Pequena empresa → nome "Lindson Almeida Studio", URL `lindsonalmeidastudio`. Textos e posts: equipe Zuleide.

## Arquivos
- `BEHANCE.md` + `behance/<case>/` (6 cases: capa 808x632, intro, 8 módulos 1400 px, créditos, TEXTO.md)
- `OFERTA.md` (pacotes, etapas, mensagens, anúncio, briefing) + `oferta/` (proposta PDF, carrossel de anúncio)
- Página de venda: privado `site/identidade/index.html` (+ `briefing.html`) → https://lindsonalmeida.pages.dev/site/identidade/ depois do deploy
- Esteira interna com preços de negociação: só no privado `dados/agencia/projeto-designer/ESTEIRA-INTERNA.md` (+ PDF)
- `TEMPLATE.md`: pesquisa premium
- Painel: privado `painel/admin-rede/projeto-designer/index.html`
