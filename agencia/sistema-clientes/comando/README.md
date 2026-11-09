# Central de Comando (`/painel/comando`) · conta Leandro, 09/11/2026

Pedido do Lindson (09/11): "quero montar um sistema único, integrado com todas as minhas contas, onde eu peça em um único lugar, visualize resultados, análises, com template de sistema, comandos por voz, visual tecnológico… botões para todas as funções que eu mais preciso."

No ar em **https://lindsonalmeida.pages.dev/painel/comando** (só o admin abre). Atalho em destaque no painel do admin (menu "Visão" e cartão na Visão geral) e em `dados/apps.json`.

## Telas
| Tela | O que faz |
|---|---|
| **Comando** | Microfone gigante (voz em pt-BR no navegador, com campo de texto de reserva), chips de cliente (Jaci, Tribuna 98, Leo e Real Time marcados como pagantes; Orégano, Minha marca, Outro) e 16 botões de função. Toca no cliente e na função, fala ou escreve um detalhe e toca em **Enviar para a equipe**. Antes de mandar, mostra **"Já existe"** se o mesmo cliente e a mesma função têm pedido aberto ou pronto nos últimos 14 dias, e também entregas parecidas do `REGISTRO-DAS-CONTAS.md`. No celular, uma barra "Enviar" aparece em cima das abas quando o pedido está montado. |
| **Fila** | Pedidos com status **novo → com &lt;conta&gt; → pronto → aprovado / ajuste**; conta, datas, link do resultado, **Aprovar** e **Pedir ajuste** (fala ou escreve a nota; o pedido volta para a fila). Atualiza sozinha a cada 45 s. |
| **Resultados e análises** | Placar (barras por projeto), parado esperando o Lindson, aprovações dos clientes ao vivo (`f=aprov` de jaci, tribuna, leo, rt, oregano), pedidos por status, tempo médio até pronto, entregas por conta em 7 dias, o que cada conta está fazendo, últimas 15 entregas e a agenda do @lindsonalmeida_. Nenhum número é inventado: o que não tem dado mostra "—". |

**Voz** (exemplos): "Reels da Jaci sobre clareamento, enviar" (monta e envia) · "carrossel do Leo sobre 15 de novembro" (monta; ele toca em Enviar) · "status" (abre Resultados) · "fila" · "abrir painel do Leo" (vai para `/painel/leo`) · "aprovar Jaci" (abre as aprovações dela). Funciona no Chrome (Android e computador); no iPhone o Safari tem voz a partir do iOS 14.5; sem voz, o campo de texto faz o mesmo.

## Arquivos
- `comando.html`: a página (fonte). Sistema no visual do modelo da Central: menu lateral, cartões de números, `movimento.js`.
- `montar-comando.py`: lê PLACAR, REGISTRO, QUADRO ("Em andamento") e `agencia/marca-lindson/agenda-status.json`; gera no privado `painel/comando/estado.js` (`window.__ESTADO`) e `painel/comando.html`.
- `PROTOCOLO-CONTAS.md`: como as 4 contas leem e marcam a fila.
- `TEMPLATE.md` + `referencias/`: pesquisa premium (11 referências, 4 países).
- `captura-desktop-1440.png`, `captura-celular-390.png`: conferência (fila vazia, sem dado de cliente).

## Dados
- **Fila:** KV `dados:admin:ped`, formato `{dados:{itens:[{id, cli, func, texto, st, conta, link, criado, atualizado, nota, ajustes, prontoEm, notas}]}, versao}`. A página grava por `/api/dados?cli=admin&f=ped` (com versão; em 409 junta e tenta de novo). O `admin.html` não lê essa chave (ele lê o `f=ped` de cada cliente), então a aba atual não muda.
- **Contas:** `/api/automacao?fila=ped` com `Authorization: Bearer <AUTOMACAO_TOKEN>` (segredo da Cloudflare). Ver `PROTOCOLO-CONTAS.md`.

## Toda conta, ao terminar uma entrega
```bash
cd /home/user/lindson && python3 agencia/sistema-clientes/comando/montar-comando.py
cd /home/user/centrallindsonalmeida && git add painel/comando painel/comando.html && git commit -m "Comando: estado atualizado" && git push origin main
```
(Depois de registrar no REGISTRO e no PLACAR, para os Resultados mostrarem a entrega.)

## Proteção
`functions/painel/_middleware.js` (cópia em `site/functions/`): `admin`, `comando`, `contas` e `membros` só abrem para o admin, mesmo se um dia existir um cliente com esse nome. `/painel/comando/estado.js` também fica atrás do login de admin.

## Próximos passos (v2)
- Notificação no celular quando um pedido ficar pronto.
- Contas criarem pedido pela automação (hoje só pegam, entregam e anotam).
