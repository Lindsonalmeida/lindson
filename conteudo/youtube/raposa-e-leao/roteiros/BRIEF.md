# Brief do roteirista · vídeo longo do Raposa e Leão (motor Pintura Viva, identidade Raposa)

Leia antes:
- `/home/user/lindson/.claude/agents/peter.md`: TODAS as regras de monetização e retenção, inclusive as seções dos dois vídeos do Peter Jordan (canal dark e 8 mil horas).
- `/home/user/lindson/conteudo/youtube/raposa-e-leao/img/acervo/MAPA.md`: imagens disponíveis.
- `/home/user/lindson/conteudo/youtube/raposa-e-leao/IDENTIDADE.md`.
- Para tom e formato, o roteiro `longo-09` em `/home/user/lindson/conteudo/youtube/passaporte/roteiros/longo-09.json`. É outro canal, mas é o mesmo motor e o mesmo padrão de conversa.

## Entrega
Um objeto JSON em `/home/user/lindson/conteudo/youtube/raposa-e-leao/roteiros/<id>.json` com os campos abaixo.

**Identificação**
- `id`, `canal: "raposa"`, `formato: "longo"`.
- `titulo`: 5 a 8 palavras, com palavra-chave de busca (Maquiavel, O Príncipe, poder, Médici etc.) e carga de contradição ou negativa. Nada de clickbait que o vídeo não entrega.

**`legenda`** (descrição do YouTube), nesta ordem:
1. 2 parágrafos curtos com palavras-chave.
2. `⏱️ Capítulos\n{CAPITULOS}`
3. `📜 Fonte: Nicolau Maquiavel, <obra e capítulos exatos>.`
4. `🦊🦁 Raposa e Leão: Maquiavel e as leis do poder aplicadas à vida real.`
5. `▶️ Playlist recomendada: <nome da playlist da série>`
6. 3 a 5 hashtags variadas.

**Comentário e tela**
- `comentario`: pergunta fixada ligada à lição, mais "Continue na playlist <nome> ⬇️".
- `titulo_tela: {"sup":"RAPOSA E LEÃO","txt":"<2-5 palavras>","dur":3.2}`.
- `capa: {"A":"<até 3 palavras>","B":"<até 3 palavras diferentes>","gravA":"<arquivo>","gravB":"<arquivo>"}`. As thumbnails são claras, com pouquíssimo texto, cores quentes ou ciano e sem vermelho. Escolha imagens luminosas, com rosto ou figura forte.

**`cenas`**: 85 a 100 cenas, cada uma `{"gravura":"<caminho relativo a raposa-e-leao/img/, ex.: acervo/xxx.jpg, hist/hannibal.jpg, cesar.jpg>","mov":"in|out|esq|dir|cima","txt":"narração"}`. Campos opcionais:
- `"cap":{"sup":"LIÇÃO 1","txt":"título do capítulo"}`: 6 a 9 capítulos.
- `"verso":"citação curta e fiel de Maquiavel em paráfrase","ref":"O PRÍNCIPE, CAP. XVIII"`: 8 a 14 no vídeo.
- `"cta":"html curto com <b>"`: só no meio e na última cena. Na última, use também `"selo":"RAPOSA<br>E LEÃO"`.
- `"interage":{"tipo":"comenta|checkin|segue|salva|manda","txt":"balão de até 6 palavras"}`.

## Regras: retenção e monetização acima de tudo
1. **Duração de 16 a 20 minutos:** 2.400 a 2.900 palavras de narração no total, com 15 a 45 palavras por `txt`. Passa de 8 minutos e libera anúncio no meio do vídeo.
2. **Gancho nos primeiros 7 s** (1ª cena) com contradição ou pergunta forte.
3. **Loops abertos:** abra 2 ou 3 promessas no começo ("no fim eu te mostro…"), feche cada uma de forma explícita mais adiante, abra outras e deixe a maior para o final. Faça uma quebra de padrão a cada 1 ou 2 minutos.
4. **Conversa com o ouvinte:** 7 a 9 cenas com `interage`, cada fala única e ligada ao que a pessoa acabou de aprender.
   - Check-in ("tá comigo até aqui?").
   - Pergunta para comentar aplicando a lição na vida dela (trabalho, família, negócios).
   - Seguir o canal só depois de entregar valor.
   - Salvar e mandar para alguém.
   - Tom humano, de WhatsApp.
5. **Corredor de sessão:** na metade, `cta` convidando a seguir o canal e a assistir a playlist da série. Na última cena, indique o próximo vídeo da playlist e termine com "Até a próxima lição, raposa." (ou variação).
6. **Fidelidade:**
   - Só fatos e citações reais de Maquiavel (O Príncipe, Discursos, A Arte da Guerra, História de Florença, cartas), com capítulo correto.
   - Datas históricas só se forem consenso.
   - Nada de número inventado.
   - Quando houver debate entre historiadores, diga isso.
7. **Ética:** a aplicação prática é para se proteger e liderar melhor. Nunca ensinar a manipular ou prejudicar pessoas.
8. **Linguagem:** simples, com "você". Nunca usar "vi que", "parece que", "gargalo".
9. **Imagens:** só arquivos do MAPA.md. Nunca a mesma em cenas seguidas, varie o `mov` e use pelo menos 25 imagens diferentes.
10. **Antes de terminar:** valide o JSON, confira se toda gravura existe em `/home/user/lindson/conteudo/youtube/raposa-e-leao/img/` e conte as palavras. Responda só com o caminho do arquivo, o nº de cenas, o nº de palavras e o título.
