# Painel da Desentupidora SF na Central (conta Zuleide, 03/11/2026)

**Endereço:** https://lindsonalmeida.pages.dev/painel/sf (o cliente cria a conta na tela inicial com o código de acesso).

**O que tem:** visão geral, missões do dia, métricas (a medir até a primeira medição), planejamento, relatórios, conteúdos, **Fotos** (antes e depois, equipe, equipamentos), **Aprovações** (vazia até o Lindson aprovar as artes), calendário, entregas, e a área **Gestão**:
- **CRM de chamados:** Novo chamado → Orçamento enviado → Visita agendada → Visita feita → Serviço feito → Manutenção preventiva (180 dias), e "Não fechou". Botão WhatsApp com a mensagem pronta de cada etapa; o valor do serviço entra sozinho no Financeiro.
- **Financeiro:** entradas e saídas por mês, meta, despesas fixas, planilha.
- **Notícias do setor:** desentupimento, saneamento em São Luís, chuvas e alagamentos, caixa de gordura, serviços para casa, marketing para prestador de serviço.

**Identidade:** a do site do cliente (marinho #0a2a6e, royal #1d5fd0, laranja #ff8a00, Montserrat, logo oficial `logo.jpg`).

**Como gerar e publicar:**
```bash
cd agencia/sistema-clientes
python3 desentupidora-sf/montar-sf.py     # lê CentralLindsonALmeida/dados/sf.json (privado)
python3 site/montar-site.py               # gera site/publico/ (fora do Git)
# copie publico/painel/sf.html (e admin.html, contas.html se mudaram) para o repositório privado e faça push: a Cloudflare publica sozinha
```
`painel-sf.html` fica fora do Git (tem dados reais). Dados reais: `CentralLindsonALmeida/dados/sf.json`.

**Aprovações:** em `montar-sf.py`, `MOSTRAR_V1 = True` só depois de o Lindson aprovar as 4 artes (`agencia/clientes/desentupidora-sf/instagram-v1/`). Lê `textos.json` (titulo, data, linha, legenda, arquivo) e `previa-feed.jpg`.

**Código de acesso:** criado por `site/novo-codigo.py sf SFD` e guardado **só como hash PBKDF2** em `CentralLindsonALmeida/functions/_codigos.js` (privado). O código em si foi entregue ao Lindson na conversa e não fica em repositório nenhum. Perdeu o código? Gere outro com o mesmo comando, troque a linha no `_codigos.js` do privado e faça push. Contas já criadas continuam entrando com e-mail e senha.

**Mudanças genéricas feitas para este cliente (valem para todos):**
- `prototipo/ferramentas.js`: palavras da tela configuráveis por cliente (`FERR.palavras`: paciente/cliente, avaliação/visita, procedimento/serviço, regra das mensagens) e exemplos dos lançamentos (`exEntrada`, `exSaida`). Sem `palavras`, tudo fica como na clínica (painel da Jaci conferido igual).
- `prototipo/real.js`: rótulo do 4º número da visão geral (`kpiCrm`, `kpiCrmNota`) e aviso "Ainda sem medição" quando o Instagram ainda não foi medido.
- `site/functions/_lib.js`: além do `CODIGOS` da Cloudflare, confere os códigos extras de `_codigos.js` (aqui no público ele fica vazio).
- `site/admin-sistema.js`, `site/contas.html`, `site/montar-site.py`: Desentupidora SF no painel do administrador e na lista de contas.

**Testado em 03/11** no servidor local da Cloudflare (wrangler): código errado recusado; código certo cria a conta e abre `/painel/sf`; essa conta não abre o painel da Jaci nem o do administrador; entrar com e-mail e senha funciona. Telas conferidas no computador e no celular, sem erro de script e sem rolagem lateral.
