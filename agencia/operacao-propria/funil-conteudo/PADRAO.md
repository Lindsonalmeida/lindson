# Padrão de exigência aplicado à Orégano Turbo (conta Leandro, 23/11/2026)

Pedido do Lindson (23/11): "verifique os novos padrões de exigência para criarmos conteúdos da Orégano Turbo". Fontes: `REGRAS-GERAIS.md`, `agencia/processos/padrao-de-exigencia.md`, `agencia/processos/conferencia-imagem-ia.md`, `MEMORIA-DO-LINDSON.md` (resumo D e reprovados), `CLAUDE.md` dos dois repositórios. Time: Paollo + Rocco (visual), Social media (gancho e legenda), Copy squad, Donald Miller (mensagem), Hormozi (isca), Pedro Sobral (tráfego), Maquiavel (conferência).

## 1. Decisões que mandam (não discutir de novo)
- **Só Reels**, 3 por dia, **70% conteúdo / 30% venda**, foco em **donos de pizzaria**. Meta: "a página mais acessada por donos de pizzaria" (14/11).
- **Voz Antonio +4%** aprovada **só na Orégano** (na marca do Lindson é reprovada).
- **Mascote Seu Turbo** aprovado para os vídeos (15/11): `agencia/operacao-propria/mascote/` (rig, `demo/fazer.py`).
- Nicho só pizzaria, sem franquia, **sem garantia de resultado** (a promessa "se não se pagar, o mês é por nossa conta" foi RETIRADA em 05/11; não usar em bio, Reels nem anúncio).
- Preço em material público: **"a partir de"**. Raio-X da Pizzaria a partir de R$ 297 (abatido no 1º mês se fechar em 7 dias). Bio sem valor.
- Mesma identidade em Instagram, YouTube, TikTok, site e painel (avatar e cores do Instagram aprovado).

## 2. Referências aprovadas (copiar a composição, não criar do zero)
| O quê | Onde | Fala do Lindson |
|---|---|---|
| Kit social v3 (Paollo) | `agencia/operacao-propria/social/v3/` | "AGORA SIM, ESSE É O PADRÃO" (06/11) |
| Sistema v4 (comanda, tomate/verde/creme/carvão, Bagel) | `agencia/operacao-propria/social/v4/` | base dos Reels (08/11) |
| 21 Reels semana 1 | `agencia/operacao-propria/reels/` (`PLANO-SEMANA-1.md`, `roteiros.json`, `motor/`) | "os vídeos da Orégano estão aprovados" (15/11) |
| Criativos de tráfego v2 | `agencia/operacao-propria/criativos-trafego/pecas-v2/` (branch `claude/elegant-goodall-6s5brw`) | "perfeito, isso sim é premium" (15/11): pizza grande e de perto, várias fotos, fundo escuro, cor só em detalhe |
| Nível premium da casa | `agencia/marca-holding/v2/` (Al Kántara v2) | "quero esse padrão pra tudo" (16/11) |

## 3. Proibido (já reprovado, nunca repetir)
- Material do Claude do Google (pranchas e posts v4 a v6 das branches `cassandra/oregano-turbo-*`).
- Criativos v1: "mais fome, menos cor", fundo sem nada, pizza pequena.
- Kit YouTube v1 preto com perfil novo.
- **Reels em miniaturas 3D com bonecos** e **foto parada com zoom fingindo vídeo** (21/11). Pizza real = vídeo real (banco de vídeo, gravação na pizzaria ou Cinema IA com cena inteira gerada).
- Fotomontagem que finge foto real (tela colada em perspectiva, pessoa recortada numa cena). Por cima da cena só tipografia e logo vetorial.
- Colagem de mockups, pílulas, cards de UI falsos, notificações inventadas, glow espalhado ("cara de vibe code"). Tela de celular só se for **gravação real**.
- Nome clichê (Forno Ligado, Fornada…), número sem fonte, "vou dobrar seu faturamento", escassez falsa.
- Foto repetida (espelhar ou recolorir conta como repetição): `social/FOTOS-USADAS.md`.

## 4. Pronto = os 11 itens de `REGRAS-GERAIS.md`, na prática da Orégano
1. Diretrizes pesquisadas (este arquivo + MEMORIA + MENTE).
2. Persona e mensagem de 1 segundo no topo do roteiro.
3. Composição copiada do kit v3 / Reels aprovados, citada no roteiro.
4. Agentes lidos e contribuição anotada (Paollo, Rocco, Social media, Copy).
5. Vídeo **assistido inteiro com áudio**: gancho na tela no 1º segundo, 20 a 35 s, narração sem travar, SFX nos cortes, trilha com crédito, -14 LUFS.
6. Imagem de IA nos 8 critérios (`conferencia-imagem-ia.md`), ampliação ≤ 1,5×, foto registrada como usada; "imagem gerada por IA" na legenda.
7. Logo original, sem erro de português, pronúncia conferida no Whisper.
8. Sem promessa, número só com fonte, exemplo marcado "ilustrativo".
9. No painel `/painel/oregano` (Aprovações, "aguardando") + Biblioteca (`gerar_biblioteca.py oregano`) + Tarefas feitas.
10. Commit nos dois repositórios, REGISTRO, MENTE, MEMORIA, PLACAR.
11. Resposta ao Lindson em até 5 linhas.

**Nota mínima 9** no crivo (Paollo, Social media, Copy, Maquiavel). Abaixo de 9 vai como rascunho, com o motivo.

## 5. Checklist de 30 segundos antes de subir cada Reel
- [ ] Gancho negativo/curioso em até 5 palavras na tela no 1º segundo.
- [ ] Uma ideia só; fala com o DONO, não com o cliente final.
- [ ] CTA "comenta PALAVRA" com algo concreto para entregar.
- [ ] Pizza grande, de perto, em movimento real; cor só em detalhe.
- [ ] Legenda SEO (título com palavra-chave, subtítulos, chamada, 3 a 5 hashtags variadas).
- [ ] Nada da lista "Proibido".
