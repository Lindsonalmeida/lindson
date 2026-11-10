# Voz do VEKTOR (conta Leandro, 10/11/2026)

O VEKTOR fala com clipes pré-gravados: voz neural masculina pt-BR-AntonioNeural (edge-tts) com efeito leve de IA.
- **Um clipe por fala completa:** nada de juntar pedaços.
- **Frases sem clipe:** respostas livres da conversa caem no speechSynthesis do navegador, com voz masculina pt-BR, `pitch .7` e o mesmo dicionário de pronúncia.

## Arquivos
- `frases.py` → gera `frases.txt` com todas as falas que a página monta: envio por função × cliente × conta, montagem, contagens de 0 a 10 e de 1 a 20, equipe, painéis, tarefas feitas e frases fixas.
- `pronuncia.json`: pares `[como está na tela, como falar]`.
  - Vale só para o TTS; a tela continua normal e a chave do clipe é a frase da tela.
  - Inclui Jaci → Jáci, Zuleide → Zulêide, Reels → Rius, Vektor → Véctor, Dra. → Doutora, SF → Esse Efe, Real Time → Ríal Táime, Tribuna 98 → noventa e oito, PDF → pê dê éfe e SEO → S E O.
  - Os números de 0 a 100 viram palavras.
- `gerar_voz_vektor.py`: gera os mp3 em `CentralLindsonALmeida/painel/comando/voz/` e o `voz.js` (`window.__VOZ = {chave: arquivo}`).
  - A chave é FNV-1a 32 bits da frase normalizada; a página calcula a mesma chave em `vkChave()`.
  - Só refaz o que mudou (texto falado ou variante, controlado em `_gerado.txt`) e apaga clipes que saíram da lista.

## Gerar ou trocar a variante
```bash
cd agencia/sistema-clientes/comando/voz
python3 frases.py
python3 gerar_voz_vektor.py frases.txt /home/user/centrallindsonalmeida/painel/comando/voz D   # D é a padrão
```
**Variantes:**
- **D (padrão, 10/11):** fluida, com brilho de IA e dicção limpa.
- **A:** chorus mais presente.
- **B:** "grave e imponente", com flanger e eco duplo.
- **C:** robótica (filtro de fase).

Para trocar, rode com `A`, `B` ou `C` no lugar de `D`: todos os clipes são refeitos. Depois faça push no privado. Precisa de edge-tts e ffmpeg (usa o `HTTPS_PROXY` do ambiente).
