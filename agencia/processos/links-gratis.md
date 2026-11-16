# Links de graça: diretórios do Brasil e do Maranhão (conta Leandro, 16/11/2026)

Objetivo: o mesmo **nome, endereço e telefone (NAP)** em todo lugar, com link para o site. Isso reforça o SEO local (ver `agencia/especialista/seo/README.md`). Nunca comprar link nem usar diretório de spam.

## 1. Diretórios grátis
| # | Diretório | Endereço | Observação |
|---|---|---|---|
| 1 | Perfil da Empresa no Google | business.google.com | Primeiro de todos (`<cliente>/GOOGLE.md`) |
| 2 | Bing Places | bingplaces.com | Dá para importar do Google |
| 3 | Apple Business Connect | businessconnect.apple.com | Aparece no Mapas do iPhone (importante para WF e Rafael) |
| 4 | Facebook (Página) | facebook.com/pages/create | Preencher endereço, telefone e site |
| 5 | LinkedIn Página | linkedin.com/company/setup/new | Empresa com site e descrição |
| 6 | Waze (Waze Ads/Local) | waze.com/business | Só para quem tem endereço que o cliente visita |
| 7 | Foursquare / Swarm | foursquare.com/add-place | Alimenta vários apps de mapa |
| 8 | Apontador | apontador.com.br | Guia brasileiro |
| 9 | Guiamais | guiamais.com.br | Guia brasileiro |
| 10 | TeleListas | telelistas.net | Lista telefônica online |
| 11 | Encontra São Luís / Encontra Maranhão | encontrasaoluis.com.br | Guia local (conferir se segue grátis) |
| 12 | Solutudo | solutudo.com.br | Guia por cidade, tem Zé Doca e São Luís |
| 13 | Cylex Brasil | cylex.com.br | Diretório internacional |
| 14 | Hotfrog Brasil | hotfrog.com.br | Diretório internacional |
| 15 | Yelp | biz.yelp.com | Pouco usado no Brasil, mas indexa bem |
| 16 | Here WeGo | here.com (Map Creator) | Mapas de carro |
| 17 | Instagram e TikTok (bio) | perfil | Link do site + mesmo telefone |
| 18 | Reclame Aqui (empresa) | reclameaqui.com.br | Cadastro grátis; responder sempre |
| 19 | Doctoralia (só Jaci) | doctoralia.com.br | Perfil grátis de profissional de saúde |
| 20 | GetNinjas / Habitissimo (só SF) | getninjas.com.br, habitissimo.com.br | Perfil de prestador |

Confirme se cada um continua grátis antes de cadastrar; pule o que pedir cartão.

## 2. Dados de cada cliente (NAP igual em todo lugar)
| Cliente | Nome | Endereço | Telefone/WhatsApp | Site | Categoria |
|---|---|---|---|---|---|
| Desentupidora SF | Desentupidora SF | Área atendida: São Luís, São José de Ribamar, Paço do Lumiar e Raposa (MA). Endereço [preencher, oculto] | (98) 92010-5710 (o do site no ar; o GOOGLE.md antigo cita (98) 98915-3929: confirmar qual vale) | https://desentupidorasf.pages.dev | Serviço de desentupimento |
| Dra. Jaci Cunha | Dra. Jaci Cunha · Odontologia e Harmonização Orofacial | Av. Militar, nº [preencher], em frente à Praça do Viva, Zé Doca - MA, CEP [preencher] | (98) 98567-2646 | https://drajacicunha.pages.dev | Dentista |
| Real Time | Real Time Full Jobs | [preencher endereço do estúdio], São Luís - MA | (98) 99133-1727 | https://realtimeslz.pages.dev | Locadora de equipamentos audiovisuais |
| WF Celulares | WF Celulares | Loja São Cristóvão: [preencher] · Loja Renascença: [preencher], São Luís - MA | (98) 98827-1882 | https://wfcelulares.pages.dev | Loja de celulares |
| Tribuna 98 | Tribuna 98 | Área atendida: Maranhão (endereço oculto) [preencher se houver redação] | (98) 99105-6523 | https://tribuna98.pages.dev | Agência de notícias |
| Rafael Imports | Rafael Imports | [preencher], São Luís - MA | [preencher] (o do site rafaelimports.pages.dev) | https://rafaelimports.pages.dev | Loja de celulares |

Horário, CNPJ e e-mail: [preencher] com o cliente. Escreva sempre do mesmo jeito (mesma abreviação, mesmo formato de telefone).

## 3. Prompt para a extensão do Claude no Chrome
Cole na extensão, um cliente por vez, já logado na conta da agência:

```
Você vai cadastrar a empresa abaixo em diretórios online grátis. Use EXATAMENTE estes dados, sem mudar nem uma vírgula:
Nome: [Nome]
Endereço: [Endereço] (se estiver "área atendida", marque a opção de esconder endereço / atende no local do cliente)
Telefone e WhatsApp: [Telefone]
Site: [Site]
Categoria: [Categoria]
Horário: [Horário]
Descrição (até 750 caracteres): [colar a descrição do GOOGLE.md do cliente]

Faça nesta ordem: Bing Places, Apple Business Connect, Facebook Página, LinkedIn Página, Foursquare, Apontador, Guiamais, TeleListas, Solutudo, Cylex, Hotfrog, Yelp.
Regras:
1. Antes de criar, pesquise se a empresa já existe no diretório. Se existir, reivindique e corrija em vez de duplicar.
2. Não pague nada, não aceite plano pago nem teste grátis com cartão. Se pedir pagamento, pule.
3. Se pedir verificação por telefone, SMS ou cartão postal, pare e me avise qual diretório e o que precisa.
4. Não invente dados. Campo que não está acima fica em branco.
5. No fim, me devolva uma tabela: diretório | status (feito, já existia, travado) | link da ficha | o que falta.
```

Depois, cole a tabela de volta em `agencia/clientes/<cliente>/LINKS.md`.
