// Pizzaria Brasa Viva · exemplo demonstrativo (sem dependências)
(function () {
  var NUMERO = '5598900000000'; // número fictício do exemplo
  var wa = function (msg) { return 'https://wa.me/' + NUMERO + '?text=' + encodeURIComponent(msg); };

  // todos os botões de WhatsApp com mensagem pronta
  document.querySelectorAll('.js-wa').forEach(function (a) {
    a.href = wa(a.dataset.msg || 'Oi, Brasa Viva! Quero fazer um pedido');
    a.target = '_blank'; a.rel = 'noopener';
  });

  // topo sólido + botão flutuante depois do herói
  var topo = document.getElementById('topo');
  var flut = document.querySelector('.flutuante');
  var pizza = document.getElementById('pizzaHeroi');
  var reduz = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function rolar() {
    var y = window.scrollY;
    topo.classList.toggle('solido', y > 40);
    var fimHeroi = document.querySelector('.heroi').offsetHeight * 0.7;
    var perto = document.querySelector('.rodape').getBoundingClientRect().top < window.innerHeight * 0.7;
    flut.classList.toggle('mostra', y > fimHeroi && !perto);
    if (pizza && !reduz && y < 1400) pizza.style.transform = 'rotate(' + (y * 0.12) + 'deg) scale(' + (1 + Math.min(y, 600) / 6000) + ')';
  }
  window.addEventListener('scroll', rolar, { passive: true }); rolar();

  // aberto agora? (horário de São Luís = UTC-3)
  var agora = new Date(Date.now() + (new Date().getTimezoneOffset() - 180) * 60000);
  var dia = agora.getDay(), min = agora.getHours() * 60 + agora.getMinutes();
  var fecha = (dia === 5 || dia === 6) ? 23 * 60 + 30 : 23 * 60;
  var aberto = dia !== 1 && min >= 18 * 60 && min < fecha;
  var av = document.getElementById('aovivo');
  if (dia === 1) { av.classList.add('fechado'); av.innerHTML = '<i></i><b>Hoje fechado</b> · volta terça, 18h'; }
  else if (!aberto) { av.classList.add('fechado'); av.innerHTML = '<i></i><b>Abre às 18h</b> · até ' + (fecha > 1380 ? '23h30' : '23h'); }
  else { av.innerHTML = '<i></i><b>Aberto agora</b> · até ' + (fecha > 1380 ? '23h30' : '23h'); }
  var hoje = document.querySelector('#horario li[data-dia="' + dia + '"]');
  if (hoje) hoje.classList.add('hoje');

  // abas do cardápio
  var abas = document.querySelectorAll('.abas button');
  abas.forEach(function (b) {
    b.addEventListener('click', function () {
      abas.forEach(function (x) { x.setAttribute('aria-selected', x === b); });
      document.querySelectorAll('.lista').forEach(function (l) { l.hidden = l.dataset.lista !== b.dataset.aba; });
    });
  });

  // montador de pedido -> mensagem pronta
  var estado = { sabor: 'Pepperoni', tamanho: 'G · 8 fatias' };
  document.querySelectorAll('[data-campo]').forEach(function (grupo) {
    grupo.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        grupo.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
        estado[grupo.dataset.campo] = b.textContent.trim(); monta();
      });
    });
  });
  var borda = document.getElementById('borda'), bairro = document.getElementById('bairro');
  borda.addEventListener('change', monta); bairro.addEventListener('change', monta);
  function monta() {
    var t = estado.tamanho.split(' ')[0];
    var msg = 'Oi, Brasa Viva! 🍕\nQuero 1 pizza ' + estado.sabor + ' (' + t + ')' +
      (borda.checked ? ' com borda de catupiry' : '') + '.\nEntrega no bairro ' + bairro.value + '.\nQual o valor com a entrega?';
    document.getElementById('previa').textContent = msg;
    document.getElementById('enviarPedido').href = wa(msg);
  }
  monta();

  // revelação na rolagem
  if (!('IntersectionObserver' in window)) { document.documentElement.classList.add('semjs'); return; }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visivel'); io.unobserve(e.target); } });
  }, { threshold: 0.15 });
  document.querySelectorAll('.revela').forEach(function (el, i) { el.style.transitionDelay = (i % 3) * 90 + 'ms'; io.observe(el); });

  var cel = document.querySelector('.celular');
  new IntersectionObserver(function (es) { if (es[0].isIntersecting) cel.classList.add('vivo'); }, { threshold: 0.4 }).observe(cel);

  // manifesto acende palavra por palavra
  var m = document.getElementById('manifesto');
  var quentes = ['lenha', 'descansou', 'verdade.', 'mesa.'];
  m.innerHTML = m.textContent.trim().split(/\s+/).map(function (w) {
    return '<span class="p' + (quentes.indexOf(w.toLowerCase()) > -1 ? ' quente' : '') + '">' + w + '</span>';
  }).join(' ');
  var palavras = m.querySelectorAll('.p');
  function acende() {
    var r = m.getBoundingClientRect(), h = window.innerHeight;
    var prog = Math.min(1, Math.max(0, (h * 0.85 - r.top) / (r.height + h * 0.35)));
    var n = Math.round(prog * palavras.length);
    palavras.forEach(function (p, i) { p.classList.toggle('acesa', i < n); });
  }
  if (reduz) palavras.forEach(function (p) { p.classList.add('acesa'); });
  else { window.addEventListener('scroll', acende, { passive: true }); acende(); }
})();
