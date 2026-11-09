# Como cada publicação agendada termina (conta Zuleide, 09/11/2026)

Toda tarefa programada que publica um post do @lindsonalmeida_ pelo Windsor faz, depois de publicar:
1. **Confere** no Windsor (`get_data` instagram, `last_3d`) que o post não foi publicado antes.
2. **Atualiza o status:** em `agencia/marca-lindson/agenda-status.json`, no item do post, grava `status: "postado"`, `media_id`, `link` e a data e hora de publicação. Na `AGENDA-WINDSOR.md`, marca "postado".
3. **Republica o painel, só a parte da agenda:** no privado `CentralLindsonALmeida/painel/admin.html`, troca apenas o objeto da agenda dentro de `window.__REDE`, do mesmo jeito do commit f75315b. **Não** rode o `montar-site.py` completo: o admin no ar vem do branch do Leandro (aba "Quadro de atividades"). Depois, commit e push no `main`.
4. **Salva no repositório lindson:** commit e push.
5. **Avisa o Lindson:** 1 linha com o link do post.

O feed é sempre harmônico e em xadrez (regra do Lindson).

**Regra do Lindson (09/11): horários.** Só postar entre **8h e 21h** (fuso de São Luís), com **intervalo de 4 horas** entre posts. Se um post atrasar, **reorganize os seguintes**: o atrasado sai assim que der (dentro da janela) e cada próximo fica 4 h depois do anterior. O que não couber até 21h passa para o dia seguinte a partir das 8h. Mantenha o xadrez das cores.
