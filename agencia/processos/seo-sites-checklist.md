# Checklist de SEO técnico dos sites (Cloudflare Pages)

Criado em 16/11/2026 (conta Leandro), depois da auditoria de 16/11. Vale para todo site novo ou alterado.

## Checklist
- [ ] Título com até 60 caracteres, com a palavra-chave e a cidade.
- [ ] Descrição com até 155 caracteres, sem promessa de resultado.
- [ ] `<link rel="canonical">` com o endereço próprio da página (a bio aponta para `/bio/`, não para `/`).
- [ ] Um H1 por página.
- [ ] Alt descritivo em toda imagem (inclusive as decorativas).
- [ ] `sitemap.xml` com todas as páginas e `robots.txt` com a linha `Sitemap:`.
- [ ] JSON-LD do tipo certo: LocalBusiness/Store/MobilePhoneStore (loja), Dentist/MedicalProcedure (clínica), NewsMediaOrganization/ProfilePage (jornal), Service + FAQPage (serviço).
- [ ] Nunca inventar dado (horário, 24h, número de clientes, avaliações). Telefone e endereço só os que já estão no site.
- [ ] Se o site tem `gerar.py`, editar o gerador e rodar; nunca o HTML na mão.
- [ ] Push na `main` (`git -c push.negotiate=true push`) e conferir no ar com `curl`.

Como medir: script de auditoria que lê cada `index.html` e conta caracteres do `<title>` e da descrição, canonical, H1, imagens sem alt e JSON-LD.

## Antes e depois (16/11/2026)
| Site | Antes | Depois |
|---|---|---|
| drajacicunha.pages.dev | títulos 59 a 72, descrições até 186, 10 imagens sem alt na home | títulos 53 a 60, descrições 73 a 150, 0 sem alt (pelo `gerar.py`) |
| realtimeslz.pages.dev | títulos 60 a 82, descrições 170 a 239, 1 imagem sem alt na bio | títulos 50 a 60, descrições 127 a 146, 0 sem alt |
| tribuna98.pages.dev | títulos até 72, bio sem JSON-LD e com canonical na home | títulos 44 a 59, bio com ProfilePage + NewsMediaOrganization e canonical `/bio/`; Thiago com TH conferido |
| oreganoturbo.pages.dev | título 62, descrição 166, 2 imagens sem alt, bio com título de 21 | título 52, descrição 137, 0 sem alt, bio com 60 |
| rafaelimports.pages.dev | título 14, sem canonical, sem JSON-LD, 2 sem alt, sem sitemap e robots | título 60, canonical, MobilePhoneStore, 0 sem alt na home, sitemap e robots |
| wfcelulares.pages.dev | sem JSON-LD, sem sitemap e robots | Store/LocalBusiness com as unidades São Cristóvão e Renascença, sitemap e robots, título 49 com palavra-chave primeiro |
| desentupidorasf.pages.dev | 11 páginas, 1 descrição com 159 | 19 páginas: 8 de bairro (Cohama, Turu, Calhau, Cohab, Renascença, Centro, Vinhais, Anjo da Guarda) com texto próprio, no sitemap e ligadas na página de São Luís; descrições até 147 |

Pendências: endereço completo (rua e número) da Rafael Imports e das lojas da WF não está no site, por isso o JSON-LD leva só bairro e cidade. As páginas internas `os/` e `artes/` da Rafael Imports são cartões de WhatsApp e ficaram fora do sitemap.
