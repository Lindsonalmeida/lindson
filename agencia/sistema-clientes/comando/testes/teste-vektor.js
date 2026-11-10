// Bateria do VEKTOR (conta Leandro, 10/11/2026): reconhecimento e voz simulados, como o Chrome faz.
// Uso: node teste-vektor.js [/caminho/do/privado]   (antes: python3 ../montar-comando.py --privado <privado>)
// - SpeechRecognition falso: results acumulados com resultIndex crescente (parcial e depois final), uma instância por start().
// - speechSynthesis e <audio> falsos: eventos start/end com duração proporcional ao texto.
// - APIs falsas: fila, equipe, feitas e aprovações em memória (PUT devolve versão nova); /api/vektor desligado (503).
// Confere: intenção e resposta de cada frase, nada de loop, nada de responder a si mesmo, nenhuma frase repetida em 15 s
// e nenhum erro no console. Escreve o resultado em RESULTADO.md, ao lado deste arquivo.
const path = require('path'), fs = require('fs');
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }
const PRIV = process.argv[2] || '/home/user/centrallindsonalmeida';
const BASE = 'https://central.test';
const hoje = (d = 0) => new Date(Date.now() - 3 * 36e5 - d * 864e5).toISOString().slice(0, 10);
const iso = ms => new Date(Date.now() + ms).toISOString();
const DADOS = {
  'admin/ped': { itens: [
    { id: 'p1', cli: 'tribuna', func: 'carrossel', texto: 'carrossel de bastidores', st: 'pronto', conta: 'Zuleide', designada: 'Zuleide', link: '/painel/tribuna/feed/x.jpg', midia: ['/painel/tribuna/feed/x.jpg'], criado: iso(-5 * 36e5), prontoEm: iso(-36e5), atualizado: iso(-36e5) },
    { id: 'p2', cli: 'leo', func: 'reels', texto: 'reels da sessão', st: 'andamento', conta: 'Pedro', designada: 'Pedro', criado: iso(-2 * 36e5), pegoEm: iso(-36e5), atualizado: iso(-36e5) },
    { id: 'p3', cli: 'jaci', func: 'stories', texto: '', st: 'novo', designada: 'Zuleide', criado: iso(-6e5), atualizado: iso(-6e5) }] },
  'admin/eq': { contas: { Zuleide: { estado: 'livre', batida: iso(-6e5) }, Pedro: { estado: 'trabalhando', batida: iso(-3e5), tarefa: 'Reels do Leo' }, Leandro: { estado: 'limite-sessao', ate: iso(3 * 36e5), batida: iso(-9e5) }, Lindson: {} }, hist: [] },
  'admin/feitas': { itens: [{ id: 'f1', data: hoje(), hora: '09:10', cli: 'tribuna', atividade: 'Fotos do perfil', por: 'Lindson' }, { id: 'f2', data: hoje(1), hora: '15:00', cli: 'rt', atividade: 'Agendei duas semanas de conteúdo', por: 'Lindson' }], sementes: ['semente-0911'] }
};
const VERS = {}, PUTS = [];
const INIT = () => {
  window.__ouvir = []; let ativo = null;
  class SR { constructor() { this.lang = ''; this.continuous = false; this.interimResults = false; this.results = []; }
    start() { if (ativo && ativo !== this) throw new Error('InvalidStateError'); ativo = this; window.__rec = this; setTimeout(() => this.onstart && this.onstart(), 5); }
    _fim() { if (ativo === this) ativo = null; window.__rec = ativo; setTimeout(() => this.onend && this.onend(), 5); }
    stop() { this._fim(); } abort() { this._fim(); } }
  window.SpeechRecognition = window.webkitSpeechRecognition = SR;
  // fala do Lindson: um resultado parcial e depois o final, acumulando como o Chrome
  window.__diz = (txt) => { const r = ativo; if (!r) return false; const i = r.results.length, it = (t, fin) => { const x = [{ transcript: t, confidence: .9 }]; x.isFinal = fin; return x; };
    const meio = txt.split(' ').slice(0, Math.max(1, Math.ceil(txt.split(' ').length / 2))).join(' ');
    r.results[i] = it(meio, false); r.onresult && r.onresult({ resultIndex: i, results: r.results });
    setTimeout(() => { if (ativo !== r) return; r.results[i] = it((i ? ' ' : '') + txt, true); r.onresult && r.onresult({ resultIndex: i, results: r.results }); }, 120); return true; };
  try { navigator.mediaDevices.getUserMedia = async () => new MediaStream(); } catch (e) {}
  window.__falando = 0;
  const ss = { speaking: false, pending: false, _u: null, getVoices: () => [], onvoiceschanged: null,
    speak(u) { if (!u.text) return; this.speaking = true; this._u = u; window.__falando++; setTimeout(() => { u.onstart && u.onstart(); this._t = setTimeout(() => { this.speaking = false; window.__falando--; this._u = null; u.onend && u.onend(); }, 150 + u.text.length * 8); }, 10); },
    cancel() { if (this._u) { clearTimeout(this._t); const u = this._u; this._u = null; this.speaking = false; window.__falando--; u.onend && u.onend(); } } };
  Object.defineProperty(window, 'speechSynthesis', { value: ss });
  HTMLMediaElement.prototype.play = function () { if (this.tagName === 'VIDEO') return Promise.resolve(); const a = this; window.__falando++; clearTimeout(a.__t); a.__t = setTimeout(() => { window.__falando--; a.onended && a.onended(); }, 400); a.__on = true; return Promise.resolve(); };
  HTMLMediaElement.prototype.pause = function () { if (this.tagName === 'VIDEO') return; if (this.__t) { clearTimeout(this.__t); this.__t = null; window.__falando--; } };
};
const CASOS = [
  { f: 'Vektor', i: 'chamado' },
  { f: 'bom dia Vektor', i: 'chamado', r: /bom dia|boa tarde|boa noite/i },
  { f: 'Vektor, o que você faz?', i: 'ajuda' },
  { f: 'Vektor, verifique os conteúdos da Doutora Jaci', i: 'ver', r: /pe[cç]a/ },
  { f: 'aprova a primeira', i: 'aprovar', r: /aprov|confirma|posso/i },
  { f: 'sim', i: 'confirmar', r: /aprov/i, put: 'jaci/aprov' },
  { f: 'pede ajuste na segunda: trocar a cor do fundo', i: 'ajuste', r: /trocar a cor do fundo/ },
  { f: 'cancela', i: 'cancelar' },
  { f: 'Vektor, pede ajuste na terceira', i: 'ajuste', r: /mud|ajuste|anoto/i },
  { f: 'deixa o título maior e tira o logo', i: 'ajuste', r: /t[ií]tulo maior/ },
  { f: 'confirma', i: 'confirmar', r: /ajuste/i, put: 'jaci/aprov' },
  { f: 'Vektor, qual o status da Tribuna?', i: 'status', r: /Tribuna 98/ },
  { f: 'e da Jaci?', i: 'status', r: /Jaci/ },
  { f: 'Vektor, o que falta do Leo Pinto', i: 'status', r: /Leo Pinto/ },
  { f: 'Vektor, como está o placar geral', i: 'status', r: /fila|pagantes/i },
  { f: 'Vektor, o que o Pedro está fazendo?', i: 'conta', r: /Pedro.*Reels.*Leo/ },
  { f: 'Vektor, quem está livre?', i: 'equipe', r: /Zuleide/ },
  { f: 'Vektor, quem esgotou?', i: 'equipe', r: /Leandro/ },
  { f: 'Vektor, e a Zuleide?', i: 'conta', r: /Zuleide/ },
  { f: 'Vektor, o que chegou na fila?', i: 'fila', r: /pronto|aberto/i },
  { f: 'Vektor, o que está pronto?', i: 'fila', r: /Carrossel de Tribuna 98/ },
  { f: 'abre o primeiro', i: 'resultado', r: /Carrossel/, esc: true },
  { f: 'aprova', i: 'confirmar', r: /aprov/i, put: 'admin/ped' },
  { f: 'Vektor, feito: Tribuna, refiz as capas dos Reels', i: 'feito', r: /tarefas feitas|lancei|anotado/i, put: 'admin/feitas' },
  { f: 'cancela', i: 'cancelar', r: /anota|desfiz|apaguei|tirei/i, put: 'admin/feitas' },
  { f: 'Vektor, o que eu fiz ontem?', i: 'feitas', r: /Ontem.*agendei/i },
  { f: 'Vektor, o que foi feito para a Tribuna?', i: 'feitas', r: /fotos do perfil/i },
  { f: 'Vektor, o que posta hoje no Instagram?', i: 'agenda' },
  { f: 'Vektor, qual o próximo post?', i: 'agenda' },
  { f: 'Vektor, abre o Recomeço 90', i: 'abrir', r: /Recome/, esc: true },
  { f: 'Vektor, abre os canais dark', i: 'abrir', r: /Canais/, esc: true },
  { f: 'Vektor, faz um carrossel', i: 'pedido', r: /cliente|Carrossel/i },
  { f: 'pra Tribuna', i: 'pedido', r: /Carrossel de Tribuna 98/ },
  { f: 'manda', i: 'confirmar', put: 'admin/ped' },
  { f: 'Vektor, Reels da Real Time sobre o cardápio novo, manda', i: 'pedido', put: 'admin/ped' },
  { f: 'Vektor, fala mais baixo', i: 'baixo' },
  { f: 'Vektor, fala mais alto', i: 'alto' },
  { f: 'Vektor, repete', i: 'repetir', r: /disse|Repetindo|De novo/ },
  { f: 'Vektor, silêncio', i: 'silencio', mudo: true },
  { f: 'Vektor, quem está livre', i: 'equipe', mudo: true },
  { f: 'Vektor, pode falar', i: 'falar' },
  { f: 'Vektor, mostra a fila e quem está livre', is: ['fila', 'equipe'] },
  { f: 'Vektor, blá blá abacaxi azul', i: 'naoEntendi' },
  { f: 'Vektor, xpto zumbido roxo', i: 'naoEntendi', difAnterior: true },
  { f: 'Victor, como tá a real taime?', i: 'status', r: /Real Time/ },
  { eco: true },
  { f: 'Vektor, mostra as aprovações do Léo', i: 'ver', r: /Leo Pinto|pe[cç]a/ },
  { f: 'Vektor, obrigado', i: 'obrigado' },
  { f: 'Vektor, que horas são', i: 'hora', r: /\d/ },
  { pausa: 17000 },
  { f: 'o tempo hoje está bonito lá fora', mudoTotal: true },
  { f: 'Vektor, abre o painel da Jaci', i: 'abrir', r: /painel/i, ultimo: true }
];
(async () => {
  const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required', '--disable-3d-apis'] });
  const pg = await b.newPage({ viewport: { width: 1280, height: 860 }, reducedMotion: 'reduce' });
  const erros = [];
  pg.on('framenavigated', f => { if (f === pg.mainFrame() && process.env.VK_DEBUG) console.log('  navegou', f.url()); });
  pg.on('pageerror', e => erros.push('pageerror: ' + e.message));
  pg.on('console', m => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) erros.push('console: ' + m.text()); });
  await pg.addInitScript(INIT);
  await pg.route(BASE + '/**', async rt => {
    const u = new URL(rt.request().url()), m = rt.request().method();
    if (u.pathname === '/api/vektor') return rt.fulfill(u.searchParams.has('saude') ? { json: { ligado: false } } : { status: 503, json: { erro: 'sem cérebro' } });
    if (u.pathname === '/api/dados') { const k = u.searchParams.get('cli') + '/' + u.searchParams.get('f');
      if (m === 'PUT') { const j = JSON.parse(rt.request().postData()); DADOS[k] = j.dados; VERS[k] = (VERS[k] || 1) + 1; PUTS.push(k); return rt.fulfill({ json: { ok: true, versao: VERS[k] } }); }
      return rt.fulfill({ json: { dados: DADOS[k] || { itens: [] }, versao: VERS[k] || 1 } }); }
    if (u.pathname.startsWith('/api/')) return rt.fulfill({ json: {} });
    let f = path.join(PRIV, decodeURIComponent(u.pathname)); if (u.pathname === '/painel/comando') f = path.join(PRIV, 'painel/comando.html');
    if (fs.existsSync(f) && fs.statSync(f).isFile()) return rt.fulfill({ path: f });
    if (fs.existsSync(f + '.html')) return rt.fulfill({ path: f + '.html' });
    return rt.fulfill({ status: 404, body: '' });
  });
  if (process.env.VK_DEBUG) console.log('abrindo');
  await pg.goto(BASE + '/painel/comando', { waitUntil: 'domcontentloaded' });
  await pg.mouse.click(5, 5);
  await pg.waitForFunction(() => window.__rec && /OUVINDO/.test(document.getElementById('mic-rot').textContent), null, { timeout: 15000 });
  await pg.waitForTimeout(2500); if (process.env.VK_DEBUG) console.log('ouvindo');
  const quieto = async (max = 9000) => { try { return await quieto0(max); } catch (e) { return false; } };
  const quieto0 = async (max) => { const t0 = Date.now(); let ok = 0; while (Date.now() - t0 < max) { const s = await pg.evaluate(() => ({ f: window.__falando, r: !!window.__rec })); ok = s.f <= 0 && s.r ? ok + 1 : 0; if (ok >= 6) return true; await pg.waitForTimeout(150); } if (process.env.VK_DEBUG) console.log('  quieto expirou', JSON.stringify(await pg.evaluate(() => ({ f: window.__falando, r: !!window.__rec, rot: document.getElementById('mic-rot').textContent })))); return false; };
  const linhas = [], falhas = []; let n = 0, okN = 0, ultimaResp = '';
  for (const c of CASOS) {
    if (c.pausa) { await pg.waitForTimeout(c.pausa); continue; }
    await quieto();
    if (c.eco) { // a última fala dele volta pelo microfone (sala com eco): não pode virar resposta
      const st0 = await pg.evaluate(() => ({ l: window.__vk.log.length, f: window.__vk.falas.length, u: (window.__vk.falas.slice(-1)[0] || [])[1] || '' }));
      await pg.evaluate(t => window.__diz(t), st0.u); await pg.waitForTimeout(1500); await quieto();
      const st1 = await pg.evaluate(() => ({ l: window.__vk.log.length, f: window.__vk.falas.length }));
      n++; const ok = st1.l === st0.l && st1.f === st0.f; if (ok) okN++; else falhas.push('eco virou resposta');
      linhas.push(`| ${n} | (eco da própria fala) | — | ${ok ? 'ignorado' : 'RESPONDEU'} | ${ok ? 'ok' : 'FALHA'} |`); continue; }
    const a = await pg.evaluate(() => ({ l: window.__vk.log.length, f: window.__vk.falas.length }));
    const ouviu = await pg.evaluate(t => window.__diz(t), c.f);
    await pg.waitForTimeout(c.ultimo ? 700 : 1300); if (!c.ultimo) await quieto();
    const d = await pg.evaluate(a => ({ log: window.__vk.log.slice(a.l), falas: window.__vk.falas.slice(a.f).map(x => x[1]) }), a);
    const e = d.log.slice(-1)[0] || {};
    const problemas = [];
    if (!ouviu) problemas.push('reconhecimento parado');
    if (c.mudoTotal) { if (d.log.length || d.falas.length) problemas.push('respondeu sem ser chamado'); }
    else {
      if (d.log.length !== 1) problemas.push(`${d.log.length} respostas`);
      if (c.i && e.intent !== c.i) problemas.push(`intenção ${e.intent}`);
      if (c.is && JSON.stringify(e.intents) !== JSON.stringify(c.is)) problemas.push(`intenções ${JSON.stringify(e.intents)}`);
      if (c.r && !c.r.test(e.resp || '')) problemas.push('resposta sem o dado esperado');
      if (c.mudo && d.falas.length) problemas.push('falou no silêncio');
      if (!c.mudo && !c.put && !d.falas.length && e.resp) problemas.push('não falou');
      if (c.difAnterior && e.resp === ultimaResp) problemas.push('repetiu a pergunta');
      if (c.put && !PUTS.includes(c.put)) problemas.push('não gravou ' + c.put);
    }
    if (c.put) PUTS.length = 0;
    if (d.falas.length > 8) problemas.push('falou demais (loop?)');
    ultimaResp = e.resp || ultimaResp;
    n++; if (!problemas.length) okN++; else falhas.push(`${c.f}: ${problemas.join(', ')}`);
    linhas.push(`| ${n} | ${c.f} | ${c.mudoTotal ? '(sem nome, fora da janela)' : (e.intents || [e.intent]).join(' + ')} | ${(c.mudoTotal ? 'calado' : (e.resp || '—')).replace(/\|/g, '/').slice(0, 150)} | ${problemas.length ? 'FALHA: ' + problemas.join(', ') : 'ok'} |`);
    if (process.env.VK_DEBUG) console.log(n, c.f, '→', e.intent, '|', (e.resp || '').slice(0, 90), problemas.join(','));
    if (c.esc) { await pg.keyboard.press('Escape'); await pg.waitForTimeout(200); }
    if (c.ultimo) break;
  }
  // repetição: nenhuma frase igual em 15 s; e nada falado sozinho depois
  const fal = await pg.evaluate(() => window.__vk.falas).catch(() => []);
  const rep = []; fal.forEach(([t, x], i) => fal.slice(0, i).forEach(([t0, x0]) => { if (x0 === x && t - t0 < 15000) rep.push(x); }));
  const fim0 = fal.length; await pg.waitForTimeout(800); const fim1 = await pg.evaluate(() => window.__vk ? window.__vk.falas.length : -1).catch(() => -1);
  await b.close();
  const md = `# Bateria do VEKTOR · resultado\n\nRodada: ${new Date().toISOString().slice(0, 16).replace('T', ' ')} UTC (conta Leandro) · \`node testes/teste-vektor.js\`\n\n` +
    `**${okN} de ${n} certas.** Falas do VEKTOR: ${fal.length} · repetidas em 15 s: ${rep.length}${rep.length ? ' (' + [...new Set(rep)].join(' / ') + ')' : ''} · erros no console: ${erros.length}\n\n` +
    (falhas.length ? '## Falhas\n' + falhas.map(x => '- ' + x).join('\n') + '\n\n' : '') + (erros.length ? '## Console\n' + erros.map(x => '- ' + x).join('\n') + '\n\n' : '') +
    '| # | Frase do Lindson | Intenção | Resposta | Situação |\n|---|---|---|---|---|\n' + linhas.join('\n') + '\n';
  fs.writeFileSync(path.join(__dirname, 'RESULTADO.md'), md);
  console.log(`${okN}/${n} · repetidas ${rep.length} · console ${erros.length}`); falhas.forEach(x => console.log(' -', x)); erros.forEach(x => console.log(' !', x));
  process.exit(falhas.length || rep.length || erros.length ? 1 : 0);
})();
