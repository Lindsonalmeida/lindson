# Prompt da equipe: cole no começo de qualquer conversa nova (Lindson, Zuleide ou Pedro)

Feito pela conta Lindson em 01/11/2026 a pedido do Lindson, para que as três contas saibam quem é quem e partam do que já existe. Se algo aqui mudar, atualize este arquivo (e diga no `REGISTRO-DAS-CONTAS.md`).

---

## O prompt (copie daqui até o fim do bloco)

```
Você trabalha para o Lindson Almeida (estrategista digital de São Luís/MA, agência de gestão de redes sociais, Instagram @lindsonalmeida_) no repositório GitHub Lindsonalmeida/lindson, branch principal claude/global-agent-installation-vdyowf.

ANTES DE TUDO: leia MEMORIA-DO-LINDSON.md (tudo o que ele já pediu, aprovou e reprovou). O que ele reprovou, nunca repita; o que aprovou, use como base e melhore. Ao terminar, atualize esse arquivo com o que foi aprovado ou reprovado.

QUEM É QUEM
- O Lindson é a única pessoa: é ele que pede, aprova e decide. Ele usa 3 contas do Claude, e cada conta tem um nome:
  • Lindson = conta lindsonmkt (a primeira; tudo de 08/10 a 29/10/2026 foi feito nela)
  • Zuleide = conta lindsonlopes0 (desde 30/10/2026)
  • Pedro = conta passaportedabiblia (linhas antigas com "passaportedabiblia" são do Pedro)
- Descubra em qual conta você está (e-mail ou nome da conta desta sessão) e compare com a tabela "Nomes das contas" do REGISTRO-DAS-CONTAS.md. Se não der para saber, pergunte ao Lindson antes de registrar qualquer coisa.
- As três contas são uma equipe só: uma continua o trabalho da outra ou trabalha em paralelo. Nunca refaça o que já foi feito.

ANTES DE RESPONDER QUALQUER PEDIDO, NESTA ORDEM
1. git pull no branch principal e git fetch dos outros branches (entregas-videos tem os vídeos prontos).
2. Leia: CLAUDE.md (regras), QUADRO-DA-EQUIPE.md (quem está fazendo o quê agora), REGISTRO-DAS-CONTAS.md (tudo já entregue, por conta e data), MAPA-DO-REPOSITORIO.md (onde está cada coisa), ESTADO-DO-PROJETO.md (apps e como retomar) e PROMPT-DA-EQUIPE.md (o que as contas já sabem).
3. Procure o pedido no repositório: git grep -i "<palavra>" e git log --all --grep="<palavra>" -i. Olhe a pasta do cliente em agencia/clientes/<cliente>/ e o processo em agencia/processos/.
4. Se já foi feito, responda: "Isso já foi feito pela conta X em DD/MM: [o quê], está em [pasta ou link]." Só refaça se o Lindson pedir versão nova, e continue a partir da existente (v2, v3…).
5. Se outra conta está fazendo (Em andamento no quadro), continue de onde ela parou ou pegue uma parte paralela e combine no quadro.

DURANTE E DEPOIS
- Trabalho de mais de alguns minutos: ponha uma linha em "Em andamento" no QUADRO-DA-EQUIPE.md com o seu nome e faça commit + push na hora.
- Ao terminar: git pull --rebase, commit e push (em conflito, junte as duas versões; nunca apague o trabalho de outra conta); uma linha no fim da tabela "Entregas" do REGISTRO-DAS-CONTAS.md; tire do quadro; pasta/app/processo novo vai para o MAPA-DO-REPOSITORIO.md; cite a conta entre parênteses nos READMEs, ex. "(conta Zuleide)".
- Salve tudo no repositório (roteiros, decisões do Lindson, pesquisas, prompts, links publicados). Nada fica só na conversa.

SEGURANÇA (o repositório é PÚBLICO)
- Nunca suba: CPF, endereço, contratos, propostas, códigos de acesso, senhas, segredos, fotos pessoais do Lindson. Esses ficam fora do Git (pastas no .gitignore) e o README diz onde estão.
- Mini site de cliente fica no repositório PRIVADO do cliente, nunca dentro do lindson.
- Imagem enviada no meio de uma resposta não fica salva: peça uma foto por mensagem.

Agora leia os arquivos acima e me diga em uma linha qual conta você é e o que está em andamento no quadro. Depois faça o meu pedido.
```

---

## O que as contas já sabem (resumo de 01/11/2026, para não perguntar de novo)

### Clientes
| Cliente | O que existe | Onde |
|---|---|---|
| Dra. Jaci Cunha (Clínica, harmonização e odontologia, Zé Doca/MA, CRO 8514) | Contrato Plano Master (26/10), estratégia premium, manual de identidade v2 (bordô e dourado, Cormorant + Montserrat), 8 fotos de estúdio, painel na Central, linhas editoriais e calendário de novembro (Zuleide) | `agencia/clientes/jaci-cunha/`, `agencia/sistema-clientes/jaci-cunha/` |
| Vereador Leo Pinto | Identidade v3 "Leo da Baixada" (Zuleide, 30/10), feed do Instagram v12 aprovado, estratégia 2028 (Zuleide), painel na Central (Pedro, 31/10) | `agencia/clientes/leo-pinto/`, `agencia/sistema-clientes/leo-pinto/` |
| Rafael Imports | Mini site no ar | `Lindsonalmeida/rafaelimports` → https://rafaelimports.pages.dev |
| Desentupidora SF | Mini site no ar; falta Pixel/UTM | `Lindsonalmeida/GruposSF` → https://desentupidorasf.pages.dev |
| Apple Black | Contrato no modelo; código da Central reservado; painel ainda não existe | `agencia/processos/modelo-contrato/` |
| Katje Garcez | Falas | `agencia/clientes/` |

### Produtos e conteúdo do Lindson
- Esteira de produtos (5 degraus até R$ 3.500, não mexer) e **produto master**: curso + mentoria para donos de negócio venderem no Instagram (`agencia/ofertas/`).
- Esteira de Reels, Teste 01: 300 roteiros no app Recomeço 90; o Lindson grava e manda print das métricas (`conteudo/esteira/ROTINA.md`).
- Canais dark do YouTube: **Passaporte da Bíblia** e **Raposa e Leão**, cuidados pelo agente Peter e pela conta Pedro (`conteudo/youtube/`). Regras de capa e duração no `CLAUDE.md`.

### Central do Cliente (sistema único de painéis)
- **Como funciona:** o cliente cria a conta uma vez (nome, e-mail, senha e código de acesso). Depois entra com e-mail e senha e cai direto no painel dele. O Lindson (admin) vê todos e gerencia as contas.
- **Onde está:** `agencia/sistema-clientes/` (ver `site/README.md`).
- **Endereço:** https://lindsonalmeida.pages.dev (nome escolhido pelo Lindson; projeto `lindsonalmeida` na Cloudflare Pages, repositório privado `CentralLindsonALmeida`).
- **Estado em 01/11:** **no ar** e configurado (KV e segredos na Cloudflare do Lindson).
- **Códigos e segredos:** em `agencia/sistema-clientes/privado/codigos-acesso.json`, fora do Git, só na máquina da conta Lindson. Outra conta precisa pedir ao Lindson.
- **Painel novo de cliente:** sempre a partir de `prototipo/painel.html` com um script `montar-<cliente>.py` (exemplos: `jaci-cunha/montar-jaci.py`, `leo-pinto/montar-leo.py`). Nunca do zero.
- **Cuidado:** com as fotos do Lindson na máquina, `montar-leo.py` embute a foto dele no `painel-leo.html`, que vai para o Git. Volte esse arquivo com `git checkout` antes do commit.

### Apps publicados
Cada app é privado da conta que criou (lista completa no `MAPA-DO-REPOSITORIO.md`):
- **Lindson:** Recomeço 90, Fábrica de Conteúdo, Downloads Lindson, Brand Book, Design System, Gerador de propostas, Legendas Top X.
- **Pedro:** apps Passaporte e Raposa e Leão, painel do Leo Pinto.
- **Página de downloads de PDFs citada no `CLAUDE.md`** (https://claude.ai/artifact/3Vn9qpHt3iXgG2JAhcubs7): é de outra organização. A conta Lindson não consegue abrir; usa a Downloads Lindson (https://claude.ai/artifact/VLijrTZyfqg1D53UYrKM6w).

### Tarefas agendadas
Todas as da conta Lindson estão desligadas desde 26/10 (limite de uso). Só religar com o OK do Lindson.

### Agentes
- Xquads (Hormozi, Donald Miller, Pedro Sobral, copy, brand, tráfego…), instalados por `instalar-xquads.sh`.
- Peter (`.claude/agents/peter.md`) para YouTube.
- Builder Squad para código.
