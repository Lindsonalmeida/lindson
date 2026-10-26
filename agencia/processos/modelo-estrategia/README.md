# Modelo: estratégia completa para o cliente (padrão aprovado, out/2026)

Exemplo aprovado: **Villa do Vinho Bistrô** (19 páginas). PDF final fica em `agencia/propostas/<cliente>/` (fora do GitHub).

## Como usar
1. Copie `base.html` e `montar_estrategia.py` para `agencia/propostas/<cliente>/`.
2. Coloque em `img/` o logo (`logo.png`) e as fotos reais do cliente (recortadas dos prints do Instagram).
3. Troque cores e letras em `base.html` (`:root`) pelas da identidade **do cliente**.
4. Troque os textos (capa, ponto de partida, desafio, anúncios, fecho em `base.html`; demais páginas em `montar_estrategia.py`).
5. Rode `python3 montar_estrategia.py` e gere o PDF:
```bash
node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+process.cwd()+'/estrategia-completa.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.pdf({path:'estrategia.pdf',width:'1080px',height:'1350px',printBackground:true});await b.close()})()"
```
6. Confira se nenhuma página passa de 1350 px de altura.

## Estrutura (19 páginas, 4:5)
1. Capa (slogan/resultado do cliente) · 2. Ponto de partida (forças reais) · 3. O desafio (sem criticar o perfil)
4. Os 4 pilares: conteúdo, tráfego, atendimento, medição + 3 fases
5. Fase 1, base técnica: Gerenciador de Negócios, Pixel, WhatsApp Business, links rastreados com código, públicos salvos, Google Meu Negócio
6. Fase 1, perfil que vende: bio, destaques, fixados, CTA, resposta automática
7. Linhas editoriais (tabela linha × o que mostra × formatos)
8. Roteiro de Reels (gancho → mostrar → provar → chamar) + ganchos prontos
9. A semana do cliente (feed + stories por dia)
10. Funil de tráfego (descobrir → considerar → comprar)
11. Campanhas por produto (público, bairro/horário, destino + código)
12. Públicos (quentes, parecidos, por lugar, por momento de vida, exclusões)
13. Criativos (3 mockups de celular) + 90 dias
14. Testes de anúncio (3 criativos, 3 dias, corte, escala ~20%, renovação)
15. Roteiro do WhatsApp (6 passos até o contrato)
16. Calendário de 90 dias
17. Relatório semanal
18. Quem faz o quê ("Vocês servem. Eu vendo.")
19. Próximo passo (uma ação: QUERO COMEÇAR + 15 minutos de conversa)

## Regras
- **Sem preços nem planos** nesta etapa: valores só na conversa depois.
- Identidade do cliente; fotos reais; sem inventar números; sem prometer vendas.
- Linguagem simples, sem "vi que", "parece que", "gargalo".
- Construída com os agentes Xquads: Hormozi Offers (oferta e urgência), Pedro Sobral (tráfego, calendário, relatório), Donald Miller (mensagem e textos).
