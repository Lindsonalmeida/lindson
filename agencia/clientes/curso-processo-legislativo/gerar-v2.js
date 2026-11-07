// Identidade v2 "Sinal" (pedido do Lindson, 07/11: mais impacto e atual). Gera capas-v2/ (9 capas 1080x1920) e identidade/direcoes-v2.png.
// Uso: node gerar-v2.js   (Node + Playwright). Referências e escolhas: TEMPLATE-V2.md
const { chromium } = require('playwright');
const path = require('path');
const BASE = `
:root{--bg:#0F0F10;--paper:#F2F1EC;--sinal:#FF4A1C;--mute:#8C8A84}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#666}
.c{width:1080px;height:1920px;position:relative;overflow:hidden;background:var(--bg);color:var(--paper);font-family:'Inter Display','Inter',Arial,sans-serif}
.p{background:var(--paper);color:var(--bg)}
.s{background:var(--sinal);color:var(--bg)}
.mono{font-family:'JetBrains Mono',monospace;font-size:24px;letter-spacing:.04em;text-transform:uppercase}
.bar{position:absolute;left:72px;right:72px;top:72px;display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid currentColor;padding-bottom:22px}
.logo{font-family:'Inter Display','Inter',sans-serif;font-weight:900;font-size:44px;line-height:.9;letter-spacing:-.03em;text-transform:uppercase}
.foot{position:absolute;left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;border-top:3px solid currentColor;padding-top:22px}
.h{position:absolute;left:72px;right:72px;font-weight:900;text-transform:uppercase;letter-spacing:-.045em;line-height:.86}
.sn{color:var(--sinal)}
.s .sn,.p .sn{color:var(--bg)}
.k{position:absolute;left:72px}
`;
const BAR = (n) => `<div class="bar"><div class="logo">Processo<br>Legislativo</div><div class="mono">Curso · ${n}/09</div></div>`;
const FOOT = `<div class="foot mono"><span>@curso_processo_legislativo_</span><span>Reels · curso</span></div>`;
const W = (cls, inner) => `<section class="c ${cls}">${inner}</section>`;
const CAPAS = [
  ['capa-01-urgencia', W('s', BAR('01') +
    '<div class="h" style="top:430px;font-size:230px">Urgência</div>' +
    '<div class="h" style="top:700px;font-size:110px;letter-spacing:-.03em">o que muda<br>na votação?</div>' + FOOT)],
  ['capa-02-pode-votar', W('', BAR('02') +
    '<div class="h sn" style="top:330px;font-size:1100px;left:0;right:0;text-align:center;line-height:1">?</div>' +
    '<div class="h" style="top:1240px;font-size:128px">Pode votar<br>sem quórum?</div>' + FOOT)],
  ['capa-03-projeto-tramitar', W('p', BAR('03') +
    '<div class="k mono" style="top:360px;color:var(--mute)">Problema</div>' +
    '<div class="h" style="top:420px;font-size:150px">Projeto<br>tramita<br>sem parecer?</div>' +
    '<div style="position:absolute;left:0;right:0;top:1040px;bottom:0;background:var(--bg);color:var(--paper)"></div>' +
    '<div class="k mono sn" style="top:1110px">Solução</div>' +
    '<div class="h" style="top:1170px;font-size:124px;color:var(--paper)">Veja a regra<br>da <span class="sn">sua casa.</span></div>' + FOOT)],
  ['capa-04-devido-processo', W('', BAR('04') +
    '<div class="h sn" style="top:430px;font-size:262px;left:72px;right:72px;text-align:left">Devido</div>' +
    '<div class="h" style="top:730px;font-size:178px;left:72px;right:72px;text-align:left">processo</div>' +
    '<div class="h" style="top:960px;font-size:130px;left:72px;right:72px;color:var(--mute)">O que é o devido processo legislativo?</div>' + FOOT)],
  ['capa-05-sessao-secreta', W('s', BAR('05') +
    '<div style="position:absolute;left:120px;right:72px;top:470px;height:900px;background:var(--bg);box-shadow:-22px 22px 0 var(--paper)"></div>' +
    '<div class="k mono" style="top:560px;left:170px;color:var(--sinal)">Caso prático</div>' +
    '<div class="h" style="top:640px;left:170px;right:120px;font-size:130px;color:var(--paper)">Sessão secreta pode acontecer?</div>' + FOOT)],
  ['capa-06-principio', W('', BAR('06') +
    '<div style="position:absolute;left:0;right:0;top:470px;height:340px;background:var(--sinal)"></div>' +
    '<div class="k mono" style="top:520px;color:var(--bg)">Princípio</div>' +
    '<div style="position:absolute;left:0;right:0;top:810px;height:520px;background:var(--paper)"></div>' +
    '<div class="h" style="top:880px;font-size:132px;color:var(--bg)">Publicidade</div>' +
    '<div class="h" style="top:1030px;font-size:66px;color:var(--bg);letter-spacing:-.02em;text-transform:none;font-weight:700">O que é o princípio da publicidade?</div>' + FOOT)],
  ['capa-07-medida-provisoria', W('', BAR('07') +
    '<div style="position:absolute;left:150px;top:470px;width:780px;height:780px;border-radius:50%;border:56px solid var(--sinal);display:flex;align-items:center;justify-content:center;font-family:\'Inter Display\',sans-serif;font-weight:900;font-size:290px;color:var(--sinal);letter-spacing:-.05em">MP</div>' +
    '<div class="h" style="top:1320px;font-size:128px">Medida<br><span class="sn">provisória</span>?</div>' + FOOT)],
  ['capa-08-quorum', W('', BAR('08') +
    '<div style="position:absolute;left:72px;top:440px;width:18px;height:880px;background:var(--sinal)"></div>' +
    '<div class="k mono" style="top:440px;left:130px;color:var(--mute)">Quórum</div>' +
    '<div class="h" style="top:520px;left:130px;right:72px;font-size:150px;text-transform:none;letter-spacing:-.04em;font-weight:800;line-height:.95">Quórum é o número mínimo para a votação valer.</div>' +
    '<div class="h sn" style="top:1400px;left:130px;font-size:90px">O que é quórum?</div>' + FOOT)],
  ['capa-09-quem-propoe', W('', BAR('09') +
    '<div class="h sn" style="top:440px;font-size:760px;left:0;right:0;text-align:center;letter-spacing:-.06em;line-height:.9">PL</div>' +
    '<div class="h" style="top:1270px;font-size:124px">Quem pode<br>propor um<br>projeto de lei?</div>' + FOOT)],
];
const BOARD = `<section style="width:1600px;height:900px;display:flex;font-family:'Inter Display',Inter,sans-serif">
 <div style="width:800px;height:900px;background:#0F0F10;color:#F2F1EC;padding:64px;position:relative">
  <div class="mono" style="font-family:'JetBrains Mono';font-size:22px;color:#8C8A84;letter-spacing:.06em">DIREÇÃO C · SINAL · preto + laranja</div>
  <div style="font-weight:900;font-size:100px;line-height:.86;letter-spacing:-.045em;margin-top:40px;text-transform:uppercase">Processo<br>Legislativo</div>
  <div style="font-weight:900;font-size:120px;line-height:.86;letter-spacing:-.045em;margin-top:40px;color:#FF4A1C;text-transform:uppercase">Urgência</div>
  <div style="display:flex;gap:16px;margin-top:60px"><div style="width:140px;height:140px;background:#0F0F10;border:2px solid #F2F1EC"></div><div style="width:140px;height:140px;background:#F2F1EC"></div><div style="width:140px;height:140px;background:#FF4A1C"></div><div style="width:140px;height:140px;background:#8C8A84"></div></div>
  <div style="font-size:24px;line-height:1.5;margin-top:36px">Preto #0F0F10 · papel #F2F1EC · sinal #FF4A1C · cinza #8C8A84<br>Títulos: Inter Display 900, caixa alta, entrelinha curta<br>Rótulos e números: JetBrains Mono</div>
 </div>
 <div style="width:800px;height:900px;background:#FF4A1C;color:#0F0F10;padding:64px;position:relative">
  <div style="font-family:'JetBrains Mono';font-size:22px;letter-spacing:.06em">DIREÇÃO C · VARIANTE · sinal dominante</div>
  <div style="font-weight:900;font-size:100px;line-height:.86;letter-spacing:-.045em;margin-top:40px;text-transform:uppercase">Pode votar<br>sem quórum?</div>
  <div style="font-weight:900;font-size:300px;line-height:.9;letter-spacing:-.06em;margin-top:30px">?</div>
  <div style="font-size:24px;line-height:1.5;margin-top:36px">Mesma gramática, fundo laranja para peças de destaque. Usar com moderação: no máximo uma peça de cada três.</div>
 </div></section>`;
(async () => {
  const dir = __dirname;
  const FONTS = '';
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.setContent(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${BASE}</style></head><body>${CAPAS.map(c => c[1]).join('')}</body></html>`, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const secs = await page.$$('section.c');
  for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: path.join(dir, 'capas-v2', CAPAS[i][0] + '.png') });
  const b = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 });
  await b.setContent(`<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">${BOARD}</body></html>`, { waitUntil: 'load' });
  await b.evaluate(() => document.fonts.ready);
  await (await b.$('section')).screenshot({ path: path.join(dir, 'identidade', 'direcoes-v2.png') });
  await browser.close();
  console.log('ok', secs.length);
})().catch(e => { console.error('FALHOU', e.message); process.exit(1); });
