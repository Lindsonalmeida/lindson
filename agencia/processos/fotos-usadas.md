# Fotos usadas: nunca repetir foto (regra do Lindson, 04/11/2026, todas as contas)

Pedido: "sempre que usar uma foto em um conteúdo, coloque essa foto em uma aba USADA para não repetir. Priorize as capas para usar fotos; se for carrossel, usar na primeira e última, e no meio pode usar imagens realistas de banco."

## Regras
1. **Cada foto real do cliente vira no máximo um conteúdo.** Antes de escolher uma foto, olhe a aba **Usadas**; se já está lá, escolha outra.
2. **Assim que usar**, a foto sai de "Disponíveis" e entra em **Usadas**, com onde foi usada e a data.
3. **Foto real vai primeiro nas capas** (capa de post, capa de carrossel, capa de Reels, capa de destaque, herói do site).
4. **Carrossel:** foto real só na **primeira e na última** tela. No meio, **imagens realistas de banco** (Unsplash, Pexels, Freepik foto) que combinem com o assunto. Nunca ilustração, e nunca banco no lugar do **produto real** do cliente (regra do mini site continua valendo).
5. Foto de banco também se anota (link de origem) para não repetir a mesma imagem de banco no mesmo cliente.

## Onde fica a aba Usadas
- **Painel do cliente na Central** (aba Fotos → sub-abas **Disponíveis** e **Usadas**). O painel lê `window.FOTOS = {livres:[...], usadas:[{img, nome, onde, data}]}`; modelo em `agencia/sistema-clientes/prototipo/painel.html` e já aplicado nos painéis privados (leo, jaci, rt, sf, admin) em 04/11 (conta Leandro). **Nos painéis no ar** a aba Fotos é a tela real de envio (fotos do servidor): ela ganhou as abas Disponíveis e Usadas, lendo `D.fotosUsadas = {"nome do arquivo": "onde foi usada"}` no painel do cliente (exemplo: `painel/jaci.html`).
- **No repositório:** `agencia/clientes/<cliente>/FOTOS-USADAS.md` (tabela: arquivo · onde foi usada · data · conta). Foto de pessoa/paciente fica no privado `CentralLindsonALmeida/dados/clientes-arquivos/<cliente>/`; no arquivo público vai só o nome e o lugar.

## Rosto sempre inteiro (regra do Lindson, 04/11/2026)
"Não corte imagem do rosto dela, sempre deixe ela bem visível, não queremos imagens cortadas."
- Antes de montar a arte, rode `python3 ferramentas/rosto.py <pasta das fotos> > rostos.json` (acha o rosto com o YuNet, modelo em `~/.modelos/yunet.onnx`).
- A cabeça inteira (com o cabelo) fica dentro da arte, e o texto começa abaixo do queixo. Nunca texto em cima do rosto.
- Foto que já vem com a cabeça cortada no original não entra.
- Exemplo pronto: função `enquadra()` em `agencia/clientes/jaci-cunha/conteudo-nov/gerar.py`.
