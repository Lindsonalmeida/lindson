# Varredura do painel do Lindson (admin · Minha rede social) · 16/11/2026 (conta Leandro)

Conferidos: 36 artes (`agencia/marca-lindson/artes-aprovadas.json`), 18 posts da agenda (`agenda-status.json`), todos os arquivos de `painel/admin-rede/` e `site/agenda/` (privado), áudio de todos os MP4, teste com Playwright em 390 px e 1440 px.

## Erro → correção
| # | Erro | Correção |
|---|---|---|
| 1-3 | Carrossel "O que responder quando perguntam o preço" (m2), "Perfil sem e com destaques" (m6) e "Checklist do Natal" (m9) com 1 imagem só | As telas 2+ não existem em nenhum branch nem no privado. Título virou "(só a capa · telas 2+ pendentes)" e o card mostra aviso. **Pendente: fazer as telas.** |
| 4-17 | 14 itens "Reels" só com a capa estática, sem vídeo (r1p, r2, r3, r4, s2_r5, s2_r6, s2_r7, s2_r8, m1, m3, m4, m7, m8, m10) | Nenhum vídeo correspondente existe. Card ganhou aviso "Reels sem vídeo: só a capa está pronta". **Pendente: gravar/editar.** |
| 18-23 | Reels 3D 01 a 06 (vídeo único) mostravam só a capa; o vídeo não tocava no painel, só baixava | Card agora mostra o player do vídeo com a capa como pôster (`admin-rede.js`). |
| 24-26 | Agenda L30-04, L30-06, L30-08 sem vídeo, mas a prévia v1 existe em `painel/admin-rede/reels/` | Caminho da prévia anotado em "obs" (voz provisória, não postar essa versão). |
| 27-30 | Agenda L30-05, L30-07, L30-09, L30-10 sem vídeo | Vídeo não existe em lugar nenhum; anotado como pendente de gravação. |
| 31 | Aviso automático: faltava regra que pegasse tipo × arquivos | `avisoArte()` em `admin-rede.js` marca sozinho qualquer carrossel com < 2 telas e Reels sem MP4. |

## Conferido e sem erro
- c2 tem as 4 telas na ordem (a 1ª se chama `c2yp.jpg`, não `c2_1`); c1 (5), s2_c3 (5), s2_c4 (4), destaques (6), stories (10 e 5) completos.
- Nenhum 404 nas imagens e vídeos; todos os MP4 têm áudio; sem rolagem horizontal no celular; legendas preenchidas (só perfil sem legenda, correto).
- Postados não aparecem em "a postar" (a aba exclui o que está na agenda).

## Pendências que dependem do Lindson
- Telas internas de m2, m6 e m9; vídeos dos 14 Reels só com capa e de L30-05/07/09/10.
- a2 e L30-02 estão "agendado" para 10/11 e mostram "Passou do horário": conferir no Instagram se saíram e marcar postado.
- Vídeos soltos sem item: `painel/admin-rede/reels/reels-5-erros-30s*.mp4`.
