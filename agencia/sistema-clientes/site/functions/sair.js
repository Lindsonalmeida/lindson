// /sair apaga o cookie e volta para o login.
export const onRequest = ({ request }) => new Response(null, { status: 302, headers: {
  Location: new URL(request.url).origin + '/', 'Set-Cookie': 'central=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax' } });
