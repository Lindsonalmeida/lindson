# Leo Pinto · 10 saudações animadas para Stories (conta Leandro, 14/11/2026)
Pedido do Lindson: "crie 10 artes animadas para storys, grafic motion, designer motion, não vídeo... saudações para postar uma por dia. Todas com foto dele do busto pra cima, em alto nível, upscale, premium."

| # | Saudação | Composição | Foto |
|---|---|---|---|
| 01 | Boa semana (segunda) | pilha, royal | a-close-laranja |
| 02 | Bom dia | cruzada, amarelo | d-braços-cruzados-branca |
| 03 | Boa tarde | caixas de cor, laranja | i-mãos-abertas-branca |
| 04 | Boa noite · bom descanso | manuscrito, noite | h-close-amarela |
| 05 | Sextou | eco em contorno, royal | b-punho |
| 06 | Bom sábado | pilha, claro | e-celular |
| 07 | Abençoado domingo | manuscrito, amarelo | c-mãos-juntas-laranja |
| 08 | Fé no dia | cruzada, claro | g-mãos-juntas-amarela |
| 09 | Boa noite (paz) | eco em contorno, noite | j-close-sorrindo |
| 10 | Deus abençoe | caixas de cor, laranja | f-punhos |

- **Identidade:** padrão aprovado v13 v3 (só fontes, logo e cores, mapa de SJB). Regra de situação (`../instagram-v15-saudacoes/TEXTOS.md`).
- **Motion:** tipografia cinética em máscara, caixas que estouram, manuscrito que se escreve, ecos em contorno, mapa desenhado, luz varrendo, foto entrando com zoom lento, logo e assinatura respirando. 8 s, determinístico (`gerar.js`).
- **Som:** `audio.py` (efeitos do `../motion-v1/audio.py` + música Kevin MacLeod, CC BY 4.0, -14 LUFS). Crédito na legenda: "Música: <título> – Kevin MacLeod (incompetech.com), licença CC BY 4.0". Títulos: royal Inspired · amarelo Life of Riley · laranja Carefree · noite Wholesome · claro Easy Lemon.
- **Fotos:** upscale 2x (Real-ESRGAN) + `limpar_recorte.py` (bordas cortadas somem em degradê, sem pedaço solto). Os closes (só rosto) não são usados.
- **Gerar:** `node gerar.js <assets> <saida> [id]` → `python3 audio.py <saida> <pasta-musica>`. Saída final no privado `dados/clientes-arquivos/leo/motion-saudacoes/`.
