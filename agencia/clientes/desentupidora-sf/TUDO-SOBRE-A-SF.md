# Desentupidora SF · tudo num lugar só (14/11/2026, conta Lindson)

Varredura de todas as contas e repositórios: `lindson` (todos os branches), `GruposSF` (site) e `CentralLindsonALmeida` (dados privados).

## O cliente
- Desentupidora em São Luís e Grande Ilha (São Luís, São José de Ribamar, Paço do Lumiar, Raposa).
- Serviços: pia, ralo, vaso sanitário, esgoto, caixa de gordura, calhas.
- Promessas permitidas (só as do site): orçamento grátis por foto/vídeo no WhatsApp, sem quebra-quebra, cabo rotativo, técnicos uniformizados, agendamento no mesmo dia conforme agenda, teste na hora; casas, condomínios, restaurantes e empresas.
- Instagram @desentupidorasf_slz · **WhatsApp atual (98) 92010-5710** (desde 11/11; o antigo (98) 98915-3929 não vale mais).
- Plano (Central): mini site com SEO local + artes para o Instagram. Início: outubro/2026. Sem contrato nem valores registrados.

## Identidade
Marinho `#061a4a`/`#0a2a6e`, royal `#1d5fd0`, céu `#3fa9ff`, laranja `#ff8a00`/`#ff6a00`, branco azulado `#f4f8ff`; Montserrat itálico 900 caixa alta; logo circular "SF" (`GruposSF/img/logo.jpg`). Material do cliente: flyer, `tecnico.jpg`, `caixa-esgoto.jpg` (foto real).

## O que já foi feito
| Data | Conta | Entrega | Onde |
|---|---|---|---|
| 26/10 | Lindson | Mini site com SEO local (11 páginas: início, 6 serviços, 4 cidades), sitemap, Search Console verificado | https://desentupidorasf.pages.dev · repo `GruposSF` |
| 01/11 | Zuleide | Verificação da campanha Meta Ads: sem Pixel, sem UTM, Supermetrics sem Facebook Ads | REGISTRO |
| 03/11 | Zuleide | Painel na Central (CRM de chamados, Financeiro, Notícias, Fotos, Aprovações) com código de acesso | https://lindsonalmeida.pages.dev/painel/sf · `agencia/sistema-clientes/desentupidora-sf/` · privado `dados/sf.json` |
| 03/11 | Zuleide | 4 artes de feed v1 + legendas SEO + 4 linhas editoriais (Socorro rápido, Evite o prejuízo, Bastidores, Fala com a gente). **Aprovadas pelo Lindson** = padrão | `instagram-v1/` · calendário: 10, 13, 17 e 20/11 |
| 03/11 | Zuleide | Google: página inicial indexada; passo a passo + página de copiar | `GOOGLE.md` · https://claude.ai/artifact/CN1KaTtRGTpzCWrKk3AHi7 |
| 03–04/11 | Leandro | Botões Baixar arte/carrossel, aba Em ajuste, Fotos Usadas no painel SF | `prototipo/interacoes.js` |
| 05/11 e 10/11 | Pedro | SF nos stories "Vender sites" e vídeo próprio da SF para marcar (voz do Lindson, "Esse Efe") | `agencia/marca-lindson/stories-sites/` (id 12) |
| 09/11 | Lindson | Pôs saldo e fez a campanha; criou cards e criativos | Central de Comando |
| 10/11 | Leandro | SF entrou nas aprovações, no VEKTOR e no distribuidor | `AUDITORIA-10-11.md` |
| 11/11 | (aba-sdr) | Número novo (98) 92010-5710 no site, artes, Google e painel | commit 7a248dd5 (trazido para este branch em 14/11) |

## O que falta
1. Cliente aprovar as 4 artes no painel (Lindson já aprovou).
2. Google: pedir indexação das outras 10 páginas (cota diária) e criar o Perfil da Empresa (Maps). Falta do cliente: horário, CNPJ/responsável, fotos reais da equipe, veículo e antes/depois.
3. Pixel da Meta + UTM no site e Facebook Ads no Supermetrics (precisa do acesso à conta de anúncios). A campanha de 09/11 roda **sem medição**.
4. Trocar `linkGoogle` em `montar-sf.py` pelo link de avaliação quando o Perfil existir.
5. Vídeo da SF (Pedro, 10/11) aguardando aprovação.

## Observações da varredura
- O repositório `GruposSF` está **público** (o README diz privado). Só tem o site, sem dado sensível.
- O número novo estava só no branch `claude/aba-sdr`; o principal ainda tinha o antigo.
