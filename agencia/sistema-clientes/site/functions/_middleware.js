// Guarda geral: nada fora da tela de acesso, de /painel (com login), /api e /sair. Bloqueia cópias antigas e arquivos do repositório.
export async function onRequest({ request, env, next }) {
  if (!env.CONTAS) env.CONTAS = env.Contas || env.contas;  // vínculo KV aceito em maiúsculas ou não
  const p = new URL(request.url).pathname;
  if (/^\/(publico|functions|dados)(\/|$)/.test(p) || /\.(md|py|json)$/i.test(p) || p.startsWith('/.')) return new Response('Não encontrado', { status: 404, headers: { 'Cache-Control': 'no-store' } });
  return next();
}
