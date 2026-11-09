// Service worker da Central de Comando (v4, conta Zuleide, 09/11/2026). Fonte: agencia/sistema-clientes/comando/v4/app/sw.js (repositório lindson).
// Só mostra os avisos ("pedido pronto", "a conta pergunta") e abre a página no toque. Não guarda cache e não intercepta nenhum pedido.
// O evento "push" já fica pronto para quando houver Web Push (precisa de chaves VAPID, um segredo que ainda não existe).
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('push', e => {
  let d = {}; try { d = e.data ? e.data.json() : {}; } catch (_) { d = { titulo: e.data ? e.data.text() : '' }; }
  e.waitUntil(self.registration.showNotification(d.titulo || 'Central de Comando', { body: d.corpo || 'Chegou algo para você na fila.', tag: d.tag || 'comando', icon: '/painel/comando/icone-192.png', badge: '/painel/comando/selo-96.png', data: { url: '/painel/comando#fila' } }));
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  const url = (e.notification.data && e.notification.data.url) || '/painel/comando#fila';
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(lista => {
    const aba = lista.find(w => new URL(w.url).pathname.startsWith('/painel/comando'));
    if (aba) { aba.postMessage({ ir: 'fila', tag: e.notification.tag || '' }); return aba.focus(); }
    return self.clients.openWindow(url);
  }));
});
