# Painel do Vereador Leo Pinto · Central do Lindson (v1, 31/10/2026)

**Publicado:** https://claude.ai/artifact/7TjjwEUN5jASCbytXAvhHk (conta passaportedabiblia). É o painel do cliente `LEO-…` da Central.

**Não é um sistema novo.** É o modelo da Central feito pela outra equipe (`../prototipo/painel.html`, diretrizes em `../IDEIAS.md` itens 6, 16, 17 e 18), montado por `montar-leo.py` com trocas pontuais:
- **Identidade do mandato** (manual do Leo): Montserrat, marinho/royal/sol/laranja/maré e a logo principal oficial (`../../clientes/leo-pinto/instagram-v12-feed/marca/logo_principal.png`).
- **Painel do cliente:** sem o seletor de admin, avatar "LP", frases e missões do Leo que já estavam no modelo.
- **Grupo "Vendas e tráfego" → "Gabinete"** (`gabinete.js`): Demandas da população (banco real), Prestação de contas (ciclo do book Pedimos → Fizemos → Entregamos, com texto pronto do post), Agenda do mandato (banco real) e Campanhas (do modelo).
- **Aprovações** com as 6 artes reais do feed; Conteúdos com pautas do mandato (inclui São João, padroeiro).
- **Bloco de promoção** do Lindson mantido, com o portfólio de `../fotos/casos/`. A foto do Lindson (`../fotos/principal-cine.webp`) fica fora do Git: sem ela, o slide 1 mostra só o nome.
- O que não vem do banco continua marcado como **Dados de exemplo**, como no modelo.

## Dados e LGPD
- Banco do artifact (capacidade `db`, com `user`). Coleções `demandas` (só lê e escreve a partir de Colaborador: regra `{path:"demandas", read:"interact", write:"interact"}`) e `agenda`.
- Nome e contato do cidadão só são gravados com o consentimento marcado. Dê acesso de Colaborador só à equipe do gabinete.
- Próximos passos (README da Central): conferir código `LEO-…` no servidor, registro de quem viu o quê, relatório mensal, integração com WhatsApp do gabinete e Supermetrics/Meta para as métricas.

## Por que não está dentro da Central original
A Central (https://claude.ai/artifact/XjCkj5eULmE2Pg8KptnKcV) está noutra organização do Claude. O convite de editor por e-mail não dá escrita entre organizações, então o painel foi publicado nesta conta. Quando a Central migrar, rode `montar-leo.py` e publique no link dela.

## Editar
1. Mude o modelo (`../prototipo/painel.html`) ou a área Gabinete (`gabinete.js`).
2. `python3 montar-leo.py` gera `painel-leo.html`. Se o modelo mudar num trecho que o script troca, ele avisa qual.
3. Publique `painel-leo.html` no mesmo link, mantendo as capacidades `db` (regra de `demandas`) e `user`.
