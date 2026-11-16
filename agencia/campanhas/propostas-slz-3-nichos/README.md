# Propostas premium SLZ: advogado, barbeiro, dentista (conta Leandro, 16/11/2026)

Pedido do Lindson (16/11): proposta premium em PDF para cada nicho de São Luís, com as fotos dele, 8 serviços (tráfego Meta e Google, GMN, conteúdo, sistemas, sites, site bio, métricas, estratégia de vendas validada). Regra extra (16/11): nada de fundo vazio; toda página com imagem, camadas, mockups e vídeo (QR para vídeos/demos).

- `proposta-advogado.pdf`, `proposta-barbeiro.pdf`, `proposta-dentista.pdf` (14 páginas 4:5 cada) · `folha.jpg` (3 capas)
- Gerar: `cd gerador && python3 gerar.py` (precisa de `fotos/c*.jpg` e `fotos/*-rec.png`, que ficam fora do Git: copiar de `CentralLindsonALmeida/membros/img/` e recortar com rembg + `limpar_recorte.py`)
- **Preços:** dicionário `PRECOS` no topo do `gerar.py`. **Textos:** `gerador/conteudo.py`. Alinhados com `agencia/campanhas/vendas-slz-3-nichos/ESTRATEGIA-DE-VENDAS.md`.
- "4x" só como meta do projeto, nunca garantia. Sem número inventado (painel é ilustração com "—"), sem depoimento falso. Advogado: Provimento 205/2021. Dentista: CFO 196/2019.
- Pesquisa: `TEMPLATE.md` + `referencias/`.
- Situação: aguardando aprovação do Lindson. Cópia no privado: `painel/admin-rede/propostas-slz/`.

## Persona (5 linhas por nicho)
**Advogado:** 30 a 50 anos, escritório pequeno em São Luís (família, previdenciário, trabalhista). Rotina de audiência e prazo, sem tempo para Instagram. Dor: depende de indicação, mês fraco sem aviso. Valoriza sobriedade, ética e não se expor. Confia em quem conhece a OAB e mostra trabalho real; está no Instagram e no LinkedIn.
**Barbeiro:** 22 a 40 anos, dono de barbearia de 2 a 4 cadeiras no bairro. Corta o dia inteiro, responde WhatsApp entre um cliente e outro. Dor: terça e quarta vazias, cliente que some, barbearia nova na esquina. Valoriza estilo, agenda cheia e coisa prática. Confia em quem mostra antes e depois e fala a língua dele; vive no Instagram.
**Dentista:** 28 a 50 anos, dona(o) de clínica particular (implante, lente, alinhador). Agenda corrida, recepção sobrecarregada. Dor: orçamento parado, dependência de convênio e indicação, rede com preço baixo. Valoriza imagem premium e segurança ética (CFO). Confia em cases reais de clínica; está no Instagram e no Google.

## Fotos usadas
Capas: c09 (advogado), c12 (barbeiro), c14 (dentista). Recortes da carta: c15, c10, c08 (rembg + limpar_recorte.py). Registrado em `agencia/marca-lindson/FOTOS-USADAS.md`.
