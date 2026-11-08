# Perfil do Instagram @oreganoturbo, pronto para colar (Paollo, 06/11/2026)

Substitui a bio da versão 2 de `../../NOME-E-PERFIL.md`. Aquela bio dizia "Mini Raio-X grátis", mas o Raio-X custa R$ 297 (`../../DECISOES-APROVADAS.md`), e "todo dia da semana" soava como promessa.

**Persona:** dono de pizzaria de bairro em São Luís, de 30 a 55 anos. Vive no balcão e no forno, vende bem no sábado e mal de segunda a quarta, e desconfia de agência que fala difícil. Confia em quem fala de pizza, mostra trabalho e responde no zap. Ele entende esta bio numa única leitura? Sim: diz o que é, para quem é, onde fica e qual o próximo passo.

## Para colar
- **@:** `oreganoturbo`
- **Nome do perfil** (29 de 30 caracteres; aparece na busca): `Orégano Turbo | Mkt Pizzarias`
- **Categoria:** Agência de marketing
- **Bio** (137 de 150 caracteres):
  ```
  Marketing de vendas só para pizzarias 🍕
  Foto que dá fome, anúncio no bairro e pedido no zap
  São Luís - MA
  👇 Peça o Raio-X da sua pizzaria
  ```
- **Link da bio:**
  - título: `Chama no zap · Raio-X`;
  - endereço: `https://wa.me/5598985621808?text=Quero%20o%20Raio-X%20da%20minha%20pizzaria`.
  - Quando a página do produto estiver no ar, troque o endereço por ela e mantenha o mesmo título.
- **Botão de contato:** WhatsApp, com o mesmo número.

**Regras:** sem promessa de resultado, sem preço na bio (o preço fica no post fixado e no zap) e sem jargão de marketing.

## Arquivos
| Arquivo | O que é |
|---|---|
| `avatar-1080.png` / `avatar-320.png` | Foto de perfil. O símbolo da folha com seta (v4-16) ficou maior, ocupando cerca de 70% do círculo. Leva um anel de **xadrez de cantina** tomate e creme, um fio carvão e o miolo verde com padrão de ícones bem sutil. |
| `prova-40px.png` | Prova de leitura do avatar a 40 e 64 px e das 6 capas de destaque a 56 px, em fundo claro e escuro. A folha com a seta continua legível a 40 px. |
| `destaque-1-metodo.jpg` … `destaque-6-zap.jpg` | 6 capas de destaque (1080×1920): Método, Raio-X, Planos, Dúvidas, Bastidor e Fale comigo. Cada uma tem cor chapada da paleta v4 (tomate, carvão, creme, verde, tomate, verde: nunca duas iguais lado a lado), ícone em traço gordo dentro de um anel duplo no centro (a área que o Instagram corta em círculo), o nome em Bagel no alto e a linha "pedido nº01…06" da campanha. Embaixo vêm o logo e as faixas de xadrez. |
| `previa-perfil.jpg` | Prévia do perfil no celular: avatar, bio, link, destaques e a grade das 9 primeiras postagens do feed do calendário (dia 1 às 12h até dia 5 às 12h), montada sozinha a partir do `calendario.json`, já com as peças do kit v4. A mais nova fica no canto de cima à esquerda, cortada em 3:4 como o Instagram mostra hoje. Seguidores aparecem como "—" de propósito: não há número inventado. |
| `bio.json` | Textos do perfil, lidos pelo gerador. |
| `gerar_perfil.py`, `render.js`, `montar.py` | Refazer: `python3 gerar_perfil.py && node render.js && node render.js tela && python3 montar.py`. Depois de mudar artes do calendário, rode de novo os dois últimos. O segundo render é necessário porque a tela usa o avatar e as capas já renderizados. |

**Observação sobre a grade:** o Instagram mostra a grade em 3:4, então as laterais dos posts 4:5 ficam cortadas na grade (o post aberto aparece inteiro). Os títulos dos posts do kit estão dentro da área segura, menos as pontas do "COMBO DE TERÇA". Vale conferir isso nos próximos posts.
