// Guarda geral: nada fora da tela de acesso, de /painel (com login), /api e /sair. Bloqueia cópias antigas e arquivos do repositório.
// 04/11/2026 (Builder Squad): bloqueia também /membros-arquivos/ (arquivos pagos: só por /api/membros/arquivo) e /produtos/ (fontes e
// entregas dos produtos), menos /produtos/landing/ (páginas de venda). O caminho é decodificado antes de conferir (%2D, // etc.).
export async function onRequest({ request, env, next }) {
  if (!env.CONTAS) env.CONTAS = env.Contas || env.contas;  // vínculo KV aceito em maiúsculas ou não
  const nao = () => new Response('Não encontrado', { status: 404, headers: { 'Cache-Control': 'no-store' } });
  let p; try { p = decodeURIComponent(new URL(request.url).pathname).replace(/\\/g, '/').replace(/\/{2,}/g, '/'); } catch (e) { return nao(); }
  if (/^\/(publico|functions|dados|membros-arquivos)(\/|$)/i.test(p) || /^\/produtos(\/(?!landing(\/|$))|$)/i.test(p) || /\.(md|py|json)$/i.test(p) || p.startsWith('/.') || p.includes('/../')) return nao();
  return next();
}
