/* Dublê · tela v2 (conta Pedro, 03/11/2026). Halo de raios copiado do herói do template Sermo (Framer). */
const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const calmo = matchMedia('(prefers-reduced-motion: reduce)').matches;
let ESTADO = {dubles: [], saidas: [], tipos: [], frase: ''}, ABA = 'audios', amp = 0, gerando = false;

/* ---------- halo de raios de voz ---------- */
function halo(cv, {r0, raios, maxL, centroY}) {
  const cx = cv.getContext('2d'), dpr = Math.min(devicePixelRatio || 1, 2);
  const R = Array.from({length: raios}, (_, i) => ({
    a: i / raios * Math.PI * 2 + (Math.random() - .5) * .02,
    L: maxL * (.25 + Math.random() ** 1.6 * .75), f: .4 + Math.random() * 1.2, p: Math.random() * 6.28,
    brilho: Math.random() < .2
  }));
  function tam() { cv.width = cv.clientWidth * dpr; cv.height = cv.clientHeight * dpr; }
  tam(); addEventListener('resize', tam);
  function quadro(t) {
    const w = cv.width, h = cv.height, x0 = w / 2, y0 = h * centroY, k = dpr * Math.min(1, cv.clientWidth / 1100 + .25);
    cx.clearRect(0, 0, w, h);
    const fala = gerando ? .35 + .25 * Math.sin(t / 180) : 0, A = Math.max(amp, fala);
    for (const r of R) {
      const pulso = .72 + .28 * Math.sin(t / 1000 * r.f + r.p);
      const len = r.L * pulso * (1 + A * 1.1) * k, ini = r0 * k * (1 - A * .06);
      const ca = Math.cos(r.a), sa = Math.sin(r.a);
      for (let d = 0; d < len; d += 7 * k) {
        const q = d / len, al = (1 - q) ** 1.2 * (r.brilho ? 1 : .72) * (.75 + A * .25);
        cx.strokeStyle = r.brilho && q < .5 ? `rgba(196,188,255,${al})` : `rgba(139,124,255,${al})`;
        cx.lineWidth = (r.brilho ? 2 : 1.5) * k;
        cx.beginPath(); cx.moveTo(x0 + ca * (ini + d), y0 + sa * (ini + d));
        cx.lineTo(x0 + ca * (ini + d + 3 * k), y0 + sa * (ini + d + 3 * k)); cx.stroke();
      }
    }
    if (!calmo) requestAnimationFrame(quadro);
  }
  requestAnimationFrame(quadro);
}
halo($('#halo'), {r0: 250, raios: 280, maxL: 260, centroY: .36});
halo($('#halo2'), {r0: 150, raios: 150, maxL: 170, centroY: .5});

/* ---------- dados do servidor ---------- */
async function api(url, op = {}) {
  const r = await fetch(url, op); let j = {};
  try { j = await r.json(); } catch (e) {}
  if (!r.ok) throw new Error(j.detail || 'Não deu certo. Tente de novo.');
  return j;
}
async function carrega() {
  ESTADO = await api('/api/estado');
  const q = $('#quem'), atual = q.value;
  q.innerHTML = ESTADO.dubles.length ? ESTADO.dubles.map(d => `<option value="${d.id}">${esc(d.nome)}${d.liberado ? '' : ' (bloqueado)'}</option>`).join('')
    : '<option value="">Cadastre um dublê</option>';
  if (atual) q.value = atual;
  $('#tipo').innerHTML = ESTADO.tipos.map(t => `<option>${esc(t)}</option>`).join('');
  $('#frase').textContent = '“' + ESTADO.frase + '”';
  numeros(); lista();
}
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
const mmss = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

function conta(el, fim) {
  const ini = +el.textContent.replace(',', '.') || 0, t0 = performance.now();
  const passo = t => { const q = Math.min(1, (t - t0) / 900), v = ini + (fim - ini) * (1 - (1 - q) ** 3);
    el.textContent = Number.isInteger(fim) ? Math.round(v) : v.toFixed(1).replace('.', ','); if (q < 1) requestAnimationFrame(passo); };
  requestAnimationFrame(passo);
}
function numeros() {
  const n = ESTADO.dubles.length, lib = ESTADO.dubles.filter(d => d.liberado).length;
  conta($('#n-dubles'), n); conta($('#n-lib'), lib); conta($('#n-seg'), ESTADO.segundos || 0); conta($('#n-aud'), ESTADO.saidas.length);
  // gráfico 1: uma barra por dublê (as mais altas = liberados), com mínimo de 18 barras de fundo
  const g1 = $('#g1'), barras = Math.max(18, n);
  g1.innerHTML = Array.from({length: barras}, (_, i) => {
    const d = ESTADO.dubles[i], h = d ? (d.liberado ? 92 : 58) : 10 + 22 * Math.abs(Math.sin(i * 1.7));
    return `<i class="${d && d.liberado ? 'forte' : ''}" style="height:${h}%"></i>`;
  }).join('');
  // gráfico 2: 40 quadradinhos, acesos = liberados, meio = bloqueados
  $('#g2').innerHTML = Array.from({length: 40}, (_, i) => `<i class="${i < lib ? 'on' : i < n ? 'meio' : ''}"></i>`).join('');
  $('#g3').style.width = Math.min(96, 6 + (ESTADO.segundos || 0) / 6) + '%';
}

/* ---------- lista do console (abas) ---------- */
function lista() {
  const ul = $('#lista');
  if (ABA === 'audios') {
    ul.innerHTML = ESTADO.saidas.length ? ESTADO.saidas.slice(0, 6).map(s => `<li><span class="nome">${esc(s.dublê)} · ${esc(s.arquivo.slice(-19, -4))}</span><small>${mmss(s.duracao)}</small><button class="seta" data-ouvir="${esc(s.arquivo)}" aria-label="Ouvir">→</button></li>`).join('')
      : '<li class="vazio">Nenhum áudio ainda. Escreva um texto acima e toque na seta.</li>';
  } else if (ABA === 'dubles') {
    ul.innerHTML = ESTADO.dubles.length ? ESTADO.dubles.map(d => `<li><span class="nome">${esc(d.nome)}<span class="motivo">${esc(d.tipo)} · ${esc(d.motivo)}</span></span><span class="selo ${d.liberado ? 'lib' : 'blo'}">${d.liberado ? 'Liberado' : 'Bloqueado'}</span><button class="seta" data-usar="${d.id}" aria-label="Usar esta voz">→</button></li>`).join('')
      : '<li class="vazio">Biblioteca vazia. Cadastre o primeiro dublê lá embaixo.</li>';
  } else {
    ul.innerHTML = ['Boca sincronizada no vídeo base (MuseTalk 1.5, roda na RTX 3050)', 'Gravuras vivas para os canais dark (LivePortrait)', 'Corpo e gestos na nuvem (Modal), só quando precisar']
      .map(t => `<li><span class="nome">${t}</span><small>em breve</small></li>`).join('');
  }
}
$$('.aba').forEach(b => b.onclick = () => {
  $$('.aba').forEach(x => { x.classList.toggle('ativa', x === b); x.setAttribute('aria-selected', x === b); });
  ABA = b.dataset.aba; lista();
});
$('#lista').onclick = e => {
  const o = e.target.closest('[data-ouvir]'), u = e.target.closest('[data-usar]');
  if (o) abreAudio(o.dataset.ouvir, true);
  if (u) { $('#quem').value = u.dataset.usar; $('#texto').focus(); }
};
$('#emocao').oninput = e => $('#emocao-v').textContent = (+e.target.value).toFixed(2).replace('.', ',');

/* ---------- aviso flutuante ---------- */
function voo(titulo, sub, tipo = '') {
  const v = $('#voo'); v.hidden = false; v.className = 'aviso-voo ' + tipo;
  $('#voo-t').textContent = titulo; $('#voo-s').textContent = sub;
  clearTimeout(voo.t); if (tipo) voo.t = setTimeout(() => v.hidden = true, 7000);
}

/* ---------- gerar voz ---------- */
$('#gerar').onclick = async () => {
  if (gerando) return;
  const id = $('#quem').value, texto = $('#texto').value;
  if (!id) return voo('Escolha um dublê na Biblioteca.', 'Cadastre o primeiro em "Novo dublê".', 'erro');
  if (!texto.trim()) return voo('Escreva o texto.', 'Frases curtas e números por extenso.', 'erro');
  gerando = true; $('#gerar').classList.add('girando'); voo('Gerando a voz…', 'Carregando o modelo de voz');
  const vigia = setInterval(async () => {
    try { const p = await api('/api/progresso'); if (p.ativo) voo('Gerando a voz…', p.total ? `${p.texto || 'Frase'} · ${Math.round(p.feito / p.total * 100)}%` : p.texto); } catch (e) {}
  }, 900);
  try {
    const r = await api('/api/voz', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({id, texto, emocao: +$('#emocao').value, humano: $('#humano').checked})});
    voo('Pronto: ' + r.duracao.toFixed(1).replace('.', ',') + ' s de voz', 'Feito com IA: avise o público quando parecer real.', 'ok');
    await carrega(); abreAudio(r.arquivo, true);
  } catch (e) { voo(e.message, 'Nada foi gerado.', 'erro'); }
  finally { clearInterval(vigia); gerando = false; $('#gerar').classList.remove('girando'); }
};

/* ---------- player com onda (a onda e o halo reagem à voz) ---------- */
const audio = new Audio(); let ctxA, analisador, picos = [];
async function abreAudio(arquivo, tocar) {
  const url = '/api/saidas/' + encodeURIComponent(arquivo);
  $('#resultado').hidden = false; $('#baixar').href = url; audio.src = url;
  try {
    ctxA = ctxA || new AudioContext();
    if (!analisador) { const fonte = ctxA.createMediaElementSource(audio); analisador = ctxA.createAnalyser(); analisador.fftSize = 256; fonte.connect(analisador); analisador.connect(ctxA.destination); }
    const buf = await ctxA.decodeAudioData(await (await fetch(url)).arrayBuffer()), dados = buf.getChannelData(0), n = 120, bloco = Math.floor(dados.length / n);
    picos = Array.from({length: n}, (_, i) => { let m = 0; for (let j = i * bloco; j < (i + 1) * bloco; j += 16) m = Math.max(m, Math.abs(dados[j])); return m; });
  } catch (e) { picos = []; }
  desenhaOnda(); if (tocar) { ctxA && ctxA.resume(); audio.play().catch(() => {}); }
}
function desenhaOnda() {
  const cv = $('#onda'), dpr = devicePixelRatio || 1, w = cv.clientWidth * dpr, h = 56 * dpr, c = cv.getContext('2d');
  cv.width = w; cv.height = h; c.clearRect(0, 0, w, h);
  const q = audio.duration ? audio.currentTime / audio.duration : 0, n = picos.length || 1, bw = w / n;
  picos.forEach((p, i) => { const a = Math.max(2 * dpr, p * h * .92);
    c.fillStyle = i / n < q ? '#8B7CFF' : '#3a3948'; c.beginPath(); c.roundRect(i * bw + bw * .2, (h - a) / 2, bw * .6, a, 2 * dpr); c.fill(); });
  $('#tempo').textContent = mmss(audio.currentTime || 0) + ' / ' + mmss(audio.duration || 0);
}
$('#tocar').onclick = () => { ctxA && ctxA.resume(); audio.paused ? audio.play() : audio.pause(); };
$('#onda').onclick = e => { if (audio.duration) { const r = e.target.getBoundingClientRect(); audio.currentTime = (e.clientX - r.left) / r.width * audio.duration; } };
audio.onplay = () => $('#tocar').innerHTML = '<svg viewBox="0 0 20 20"><path d="M5 4h3v12H5zM12 4h3v12h-3z" fill="currentColor"/></svg>';
audio.onpause = audio.onended = () => $('#tocar').innerHTML = '<svg viewBox="0 0 20 20"><path d="M6 4l10 6-10 6z" fill="currentColor"/></svg>';
(function laco() {
  if (analisador && !audio.paused) { const d = new Uint8Array(analisador.frequencyBinCount); analisador.getByteFrequencyData(d);
    amp = amp * .7 + (d.reduce((a, b) => a + b, 0) / d.length / 140) * .3; desenhaOnda(); }
  else amp *= .92;
  requestAnimationFrame(laco);
})();

/* ---------- novo dublê: passos (Composer) ---------- */
const NOMES = ['Quem é', 'Amostra de voz', 'Termo assinado', 'Vídeo de consentimento', 'Fonte e vídeo base'];
let passo = 0;
function vaiPara(p) {
  passo = Math.max(0, Math.min(4, p));
  $$('#passos li').forEach((li, i) => { li.classList.toggle('ativo', i === passo); });
  $$('.etapa').forEach((e, i) => e.classList.toggle('ativa', i === passo));
  $('#passo-t').textContent = NOMES[passo]; $('#passo-n').textContent = `${passo + 1} de 5`;
  $('#voltar').style.visibility = passo ? 'visible' : 'hidden';
  $('#seguir').hidden = passo === 4; $('#salvar').hidden = passo !== 4;
}
$$('#passos li').forEach(li => li.onclick = () => vaiPara(+li.dataset.p));
$('#seguir').onclick = () => { if (passo === 0 && !$('#form').nome.value.trim()) { msg('Dê um nome ao dublê.', 'erro'); return; } msg(''); $$('#passos li')[passo].classList.add('feito'); vaiPara(passo + 1); };
$('#voltar').onclick = () => vaiPara(passo - 1);
$$('.arquivo input').forEach(i => i.onchange = () => {
  const l = i.closest('.arquivo'); l.classList.toggle('cheio', !!i.files.length);
  l.querySelector('span').textContent = i.files.length ? i.files[0].name : 'Escolher arquivo';
});
function msg(t, tipo = '') { const m = $('#msg'); m.textContent = t; m.className = 'msg ' + tipo; }

$('#form').onsubmit = async e => {
  e.preventDefault();
  const f = e.target, fd = new FormData(f);
  for (const [k, v] of [...fd]) if (v instanceof File && !v.size) fd.delete(k);
  if (gravado) fd.set('amostra', gravado, 'amostra-gravada.webm');
  try {
    const r = await api('/api/dubles', {method: 'POST', body: fd});
    msg(r.aviso, r.liberado ? 'ok' : 'erro'); await carrega();
    if (r.liberado) { $('#quem').value = r.id; }
  } catch (err) { msg(err.message, 'erro'); vaiPara(err.message.includes('amostra') ? 1 : 0); }
};

/* gravar a amostra direto do microfone */
let gravado = null, rec = null;
$('#gravar').onclick = async () => {
  const b = $('#gravar');
  if (rec && rec.state === 'recording') { rec.stop(); return; }
  try {
    const s = await navigator.mediaDevices.getUserMedia({audio: true}), partes = [];
    rec = new MediaRecorder(s); rec.ondataavailable = e => partes.push(e.data);
    rec.onstop = () => { gravado = new Blob(partes, {type: rec.mimeType}); s.getTracks().forEach(t => t.stop());
      b.textContent = '✓ Gravado · gravar de novo'; const l = b.previousElementSibling; l.classList.add('cheio'); l.querySelector('span').textContent = 'Amostra gravada no microfone'; };
    rec.start(); b.textContent = '■ Parar gravação';
  } catch (e) { msg('Não consegui usar o microfone. Libere no navegador ou envie um arquivo.', 'erro'); }
};

vaiPara(0);
carrega().catch(e => voo('O servidor do Dublê não respondeu.', 'Abra pelo abrir.bat.', 'erro'));
