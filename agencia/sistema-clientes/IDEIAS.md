# Sistema de clientes (multi-cliente com login) · ideias em coleta

> Status: **coletando ideias**. Não construir até o Lindson mandar criar.
> Iniciado em 29/10/2026. O Lindson vai mandando as ideias; cada uma entra aqui, na ordem em que chegou.

## Primeiro cliente
- **Político com mandato: vereador.** O nome e os dados do cliente ficam fora do GitHub (`agencia/contratos/<cliente>/`). Pedir quando for criar.
- Relacionado ao projeto "Meu Vereador", que aparece no organograma do Lindson.

## Ideias recebidas
1. **Sistema único para vários clientes:** o mesmo sistema serve este vereador e os próximos clientes da agência.
2. **Acesso por nível:**
   - **Lindson (admin):** vê e gerencia **todos** os clientes.
   - **Cada cliente:** vê **só o que é dele**.
3. **Tela de login:** cada cliente entra com o próprio login e senha.

## Anotações técnicas (para a hora de construir)
- Separar os dados por cliente (`cliente_id` em tudo) e checar a permissão no servidor, não só na tela.
- Login com senha guardada com hash, e de preferência recuperação de senha por e-mail ou WhatsApp.
- Hospedagem possível: Cloudflare (Pages + Workers + D1), que já está conectada, ou artifact com banco e regras por usuário. Decidir quando chegarem as funções.
- Dados de eleitores e de cidadãos têm dados pessoais: seguir a LGPD (consentimento, finalidade, acesso restrito e registro de quem viu o quê).

4. **Tela de login (29/10):** identidade escura e espacial com movimento, no estilo de banner de filme épico do espaço, aplicado ao marketing.
   - Foto do Lindson passando autoridade, com o texto "Lindson Almeida · Estrategista digital · @lindsonalmeida_".
   - Feito: protótipo em `prototipo/login.html` (monte com `prototipo/montar.sh`).
     - Abertura com letreiro rolando, que pode ser pulada.
     - Campo de estrelas em velocidade de cruzeiro.
     - Foto em órbita.
     - Nome em ouro.
     - Formulário em vidro.
   - Referência que o Lindson achou linda: a tela de entrada do **Estado Alpha** (estadoalpha.com.br/login). Elementos aproveitados no protótipo:
     - minimalismo;
     - grade sutil no fundo;
     - título bem pesado;
     - um único destaque de cor;
     - "Esqueci minha senha" ao lado do rótulo da senha;
     - ícone de olho no campo da senha;
     - botão com seta;
     - "Conexão segura e criptografada" com ponto verde.
5. **Ajuste da tela de login (29/10):**
   - **Sem abertura com letreiro**, porque os clientes achariam chato. O visual deve ser mais sério.
   - O "estilo de filme do espaço" é a **foto** tratada como cartaz de cinema: retrato grande com luz de contorno, aura dourada, horizonte de planeta em luz azul e cores de cinema.
6. **Referência de painel (30/10):** https://efferd.com/view/dashboard-3 (print em `fotos/ref-efferd-dashboard-3.png`, fora do Git).
   - **Menu lateral:**
     - logo e botão principal no topo;
     - grupos com títulos ("Today", "Inbox", "Organization");
     - cartão "Novidades" e "Ajuda" no pé.
   - **Barra superior:** nome da página, ícones de enviar e notificação, e avatar.
   - **Indicadores:** 4 cartões, cada um com número grande e variação (verde ou vermelho, com seta).
   - **Gráficos:**
     - gráfico de área com filtro de período ("Últimos 30 dias");
     - rosca de distribuição por canal;
     - barras empilhadas por dia;
     - linha com rótulos nos pontos.
   - **Estilo:** claro, monocromático, cinza e preto, bordas finas e cantos arredondados, muito respiro.
   - Verde e vermelho só para o que variou.
7. **Login v3 (30/10): sóbrio, premium, amarelo e preto.**
   - **À esquerda, vitrine que desliza para o lado** a cada 7 s. Pausa com o mouse em cima e tem barras de progresso clicáveis.
     1. Cartaz no estilo Star Wars com as 5 fotos recortadas, sem fundo: rosto gigante no céu, figura principal no centro, duas laterais, uma ao fundo, feixe de luz dourado e o nome em ouro.
     2. Rafael Imports (mini site).
     3. Desentupidora SF (mini site).
     4. Passaporte da Bíblia (canal).
     5. Raposa e Leão (canal).
     - Os slides 2 a 5 usam "Conheça um dos nossos clientes/projetos" e só fatos reais.
   - **À direita, o acesso** em preto sólido com um único destaque amarelo.
   - **Fotos recortadas e prints** ficam em `fotos/` e `fotos/casos/` (fora do Git). Monte com `prototipo/montar.sh`.
8. **Cartaz v4 (30/10), a partir das referências que o Lindson mandou** (Fábrica de Cortes, Atração Natural, Bráulio Langer e terapia holística):
   - autoridade vem de **uma foto só**, grande, peito para cima, na frente de uma **parede com o portfólio real** (capas dos canais e sites de clientes) escurecida e em leve rotação;
   - luz e halo amarelos atrás e um arco de luz girando;
   - o nome como assinatura grande embaixo.
   - **Nada de várias cópias da mesma pessoa**: o Lindson achou amador.
9. **Cartaz v5 (30/10): as 5 fotos juntas, cada uma olhando para um lado** (referência: cartaz de esporte do Flamengo).
   - Composição:
     - rostos grandes no alto (69 espelhada e 68);
     - dois corpos sentados nas laterais (71 e 72 espelhada);
     - a foto em pé (70) no centro, na frente.
   - Todas em **duotone amarelo e preto**: uma cor só, que deixa tudo coerente e profissional.
   - Faixas de luz em espiral animadas.
   - A parede do portfólio passa em loop contínuo no fundo.
