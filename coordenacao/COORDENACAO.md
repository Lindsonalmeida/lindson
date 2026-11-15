# Coordenação das equipes (pedido do Lindson, 15/11/2026; coordenador: conta Leandro)

> "A partir de agora você verá o que tem de cada cliente para fazer no painel e vai dividir o trabalho entre as equipes. Cada projeto será analisado por todos os agentes e dividido em partes, e cada equipe fica com uma parte para otimizar tempo e terminar mais rápido."

## Como funciona
1. **Fonte das tarefas:** o quadro A fazer da Central de Comando (`/painel/comando#afazer`, servidor `dados:admin:afazer`), os cadernos do Lindson (`LISTA-DO-LINDSON.md`), os pendentes do `QUADRO-DA-EQUIPE.md` e as Aprovações reprovadas de cada painel.
2. **Coordenador (Leandro), a cada 2 horas:** lê as fontes, analisa cada projeto novo com os agentes (Maquiavel decide prioridade e dono; o agente do assunto divide em partes), escreve em `coordenacao/fila.json` e avisa no `MENTE-COLETIVA.md`. Também solta itens parados há mais de 24 h em "andamento" e redistribui.
3. **Cada equipe, a cada 2 horas:** roda o prompt de `coordenacao/PROMPT-EQUIPE.md`: pega o próximo item dela, trava na fila, faz, sobe no painel do cliente e fecha.
4. **O Lindson** só aprova no painel do cliente e responde o que estiver "travado" com @Lindson no `MENTE-COLETIVA.md`.

## Quem faz o quê (afinidade)
| Equipe | Clientes e assuntos |
|---|---|
| Zuleide | Orégano Turbo (Reels, YouTube, TikTok, SDR), Passaporte da Bíblia, Pagode Fiado, Samba do Pinto |
| Pedro | Desentupidora SF, tráfego pago (Orégano, Real Time, SF), Projeto Designer, Projeto Influencer |
| Lindson (conta) | Real Time, WF Celulares, Dra. Jaci, curso legislativo, Robô do WhatsApp, grupo de tecnologia |
| Leandro | coordenação, Leo Pinto, Tribuna 98, Raposa e Leão, marca do Lindson |
| qualquer | guias de especialista do Lindson (Google Meu Negócio, SEO, WhatsApp, automação, Meta), VEKTOR, Dublê |
| Lindson (dono) | o que só ele pode fazer (estudar cursos, fotos de produto) |

## Estados na fila
`livre` → `andamento` (com `pegou`) → `feito` / `aguardando aprovação` · `travado` (com `nota` do que falta).
