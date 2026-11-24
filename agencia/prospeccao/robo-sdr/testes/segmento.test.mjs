// Respostas do SDR separadas por segmento: política × varejo (Lindson, 24/11/2026). Uso: node testes/segmento.test.mjs [/caminho/Central]
import assert from 'node:assert/strict';
const CENTRAL = process.argv[2] || '/home/user/centrallindsonalmeida';
const F = await import(CENTRAL + '/functions/_sdr_fluxo.js');
const { CONTATOS } = await import(CENTRAL + '/functions/_sdr.js');
const VAREJO = /loja|produto|estoque|cliente|delivery|promo|faturamento|faturar|venda|vender|negócio local|agenda enche/i;
const POL = /mandato|vereador|eleitor|2028|gabinete/i;
const falas = ['sim', 'oi tudo bem', 'quanto custa?', 'já tenho alguém que faz marketing', 'não tenho interesse', 'agora não, depois', 'quem é você?', 'o que vocês fazem?'];
const leads = { politica: ['vereador', 'Vereador Alcemir Costa', 'deputado estadual'], varejo: ['loja de iPhone', 'hamburgueria', 'loja de celular'] };
let n = 0;
for (const [seg, lista] of Object.entries(leads)) for (const nicho of lista) for (const f of falas) for (let s = 0; s < 6; s++) {
  for (const passo of ['aberto', 'q1', 'q2']) {
    const r = F.proximo({ passo, msgs: [], nRobo: 0 }, f, { semente: s, nicho });
    for (const t of r.responder) { if (seg === 'politica') assert.ok(!VAREJO.test(t), `política recebeu varejo: [${nicho}] "${f}" → ${t}`); else assert.ok(!POL.test(t), `varejo recebeu política: [${nicho}] "${f}" → ${t}`); n++; }
  }
}
for (const nicho of leads.politica) { for (const fu of F.FOLLOW) { const t = fu.msg('Alcemir', nicho); assert.ok(!VAREJO.test(t) && /Vereador/.test(t), t); } assert.ok(!VAREJO.test(F.textoDepois('Alcemir', nicho))); n += 4; }
for (const nicho of leads.varejo) { for (const fu of F.FOLLOW) assert.ok(!POL.test(fu.msg('Ana', nicho))); n += 3; }
assert.equal(F.segmento('', 'Gabinete do Ver. João'), 'politica'); assert.equal(F.segmento('', 'Fulano'), 'neutro'); assert.equal(F.segmento('loja de celular', 'iCell'), 'varejo');
assert.equal(F.proximo({ passo: 'aberto', msgs: [] }, 'oi', { nicho: '' }).revisao, true);
const errados = CONTATOS.filter(c => F.segmento(c.nome, c.ig, c.msg || '') === 'politica' && F.nichoDe(c.nicho) !== 'politica');
assert.equal(errados.length, 0, 'leads políticos com nicho errado: ' + errados.map(c => c.id));
console.log('ok', n, 'respostas sem cruzar segmento;', CONTATOS.filter(c => F.nichoDe(c.nicho) === 'politica').length, 'leads de política na fila');
