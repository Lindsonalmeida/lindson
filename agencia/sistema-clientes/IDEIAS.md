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
