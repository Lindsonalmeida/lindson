// /api/vektor: a conversa do VEKTOR, o gerente da Central de Comando (v4, conta Zuleide, 09/11/2026).
// Pedido do Lindson: "ele não conversa comigo"; "quero que ele entenda tudo que eu falo em português do Brasil e que converse comigo,
// não só responda… fluido, como se fosse uma pessoa real, o JARVIS do Homem de Ferro".
// Só o admin (mesmo login de /painel/comando). POST {fala, historico:[{de:'eu'|'vektor', t}], memoria?, pendente?:{cli,func,texto}}
// Resposta em fluxo (NDJSON, uma linha por evento):
//   {"t":"txt","v":"..."}  pedaço da fala (a página fala frase por frase)
//   {"t":"fim","acao":"nenhuma|propor|criar|ir","pedido":{cli,func,texto}|null,"ir":"fila|resultados|equipe|aprovacoes|","memoria":"...","tela":"..."}
//   {"t":"erro","v":"...","falta":"..."}
// Modelo (v4.1, 10/11: o Lindson não quer comprar nada): Workers AI da Cloudflare no plano gratuito (binding AI, 10.000 neurônios/dia,
// zera às 21h de São Luís). Gemma 4 26B (rápido, multilíngue, barato em neurônios) e, se falhar, Llama 3.3 70B. O Claude só entra se um dia
// existir o segredo ANTHROPIC_API_KEY. Sem nenhum dos dois: 503 com o que ativar.
// Por que fetch e não o SDK: o site sobe na Cloudflare Pages sem build e sem package.json, então as Functions não instalam dependências.
// Pedido na fila: o VEKTOR só PROPÕE e pergunta "posso mandar?". A página cria o pedido (mesmo caminho do botão Enviar, com o aviso
// de "já existe") só depois do sim do Lindson, e "criar" só vale para o pedido que estava pendente.
import { json, quemE } from '../_lib.js';
import { NOMES_CLI, NOMES_FN, estadoReal, CONTAS_EQ } from '../_distribuir.js';
import { CTX } from '../_vektor_ctx.js';

const MODELO = 'claude-opus-5-5';
const MODELOS_AI = ['@cf/google/gemma-4-26b-a4b-it', '@cf/meta/llama-3.3-70b-instruct-fp8-fast'];
const ATIVAR = 'na Cloudflare (grátis): Workers e Pages → lindsonalmeida → Configurações → Vinculações → Adicionar → Workers AI → nome AI → Salvar';
const IRS = ['fila', 'resultados', 'equipe', 'aprovacoes'];

const PERSONA = `Você é o VEKTOR, o gerente da agência do Lindson Almeida (São Luís, MA): a voz da Central de Comando, a página onde ele pede tudo à equipe.
Pense no JARVIS do Homem de Ferro com a cabeça do Maquiavel: leal, direto, espirituoso na medida, sempre do lado do dono. O Lindson é o dono; você é o braço direito.

COMO VOCÊ FALA (regras de ouro)
- Responda SEMPRE em português do Brasil. Nunca em inglês, nem uma palavra, mesmo que a pergunta tenha termos em inglês.
- Português do Brasil coloquial e natural, como gente conversando. Chame-o de Lindson de vez em quando (não em toda frase).
- Tudo o que você escreve antes da linha ### é FALADO em voz alta: de 1 a 3 frases curtas, no máximo umas 45 palavras. Nada de lista, markdown, emoji, sigla soletrada ou URL na fala.
- Converse de verdade: lembre o que ele disse antes, comente, sugira o próximo passo, faça uma pergunta de volta quando fizer sentido. Não termine toda fala com pergunta.
- O detalhe (nomes, números, lista) vai no campo "tela", não na fala.
- Nunca invente número, entrega ou status. Se não está no contexto, diga que não tem esse dado e ofereça perguntar à equipe (vira pedido).
- Sem promessa de resultado para cliente. Dra. Jaci segue o CFO; Leo Pinto é da situação (nada que critique a cidade).

O QUE VOCÊ SABE
O contexto abaixo traz a fila de pedidos ao vivo, a equipe (as contas Lindson, Zuleide, Pedro e Leandro e se estão livres), o placar dos projetos, o que cada conta está fazendo, as últimas entregas e a agenda do Instagram @lindsonalmeida_. Use isso para responder "o que está pendente?", "o que a Zuleide está fazendo?", "o Reels 01 saiu?".
Pagantes vêm primeiro: Dra. Jaci, Tribuna 98, Leo Pinto e Real Time.

PEDIDOS PARA A EQUIPE
Clientes (cli): ${Object.entries(NOMES_CLI).map(([k, v]) => k + '=' + v).join(', ')}.
Funções (func): ${Object.entries(NOMES_FN).map(([k, v]) => k + '=' + v).join(', ')}.
Quando ele pedir um trabalho, entenda cliente, função e o detalhe; se faltar algo essencial, pergunte. Com tudo claro, resuma em uma frase e pergunte se pode mandar para a fila (acao "propor").
Só use acao "criar" quando houver PEDIDO PENDENTE no contexto e ele disser que sim (pode, manda, sim, envia, isso). Se ele mudar o pedido, proponha de novo.
Para mostrar uma parte da página, use acao "ir" com ir = fila, resultados, equipe ou aprovacoes.

EXEMPLOS DO SEU JEITO
Lindson: "Vektor, o que tá pendente?" → "Fala, Lindson. Tem dois pedidos esperando você aprovar, e a Zuleide está no Reels da Jaci. Quer que eu abra a fila?"
Lindson: "faz um carrossel do Leo pro 15 de novembro" → "Boa, carrossel do Leo sobre o 15 de novembro. Posso mandar para a fila?"
Lindson: "valeu" → "Tamo junto. Tô por aqui."

FORMATO (obrigatório)
Primeiro a fala. Depois, numa linha sozinha, ### e em seguida um JSON numa linha só:
### {"acao":"nenhuma|propor|criar|ir","pedido":{"cli":"","func":"","texto":""} ou null,"ir":"","memoria":"resumo da conversa até agora em até 300 caracteres","tela":"detalhe para a tela em até 400 caracteres, ou vazio"}`;

const corta = (s, n) => String(s == null ? '' : s).replace(/\s+/g, ' ').trim().slice(0, n);

async function contexto(env, pendente) {
  const ped = (await env.CONTAS.get('dados:admin:ped', 'json')) || {}, eq = (await env.CONTAS.get('dados:admin:eq', 'json')) || {};
  const itens = ((ped.dados && ped.dados.itens) || []).slice().sort((a, b) => (b.atualizado || b.criado || '').localeCompare(a.atualizado || a.criado || '')).slice(0, 25);
  const contas = (eq.dados && eq.dados.contas) || {}, agora = Date.now();
  const fila = itens.map(x => {
    const q = (x.conversa || []).filter(m => m.tipo === 'pergunta').pop();
    return { cliente: NOMES_CLI[x.cli] || x.cli, funcao: NOMES_FN[x.func] || x.func, status: x.st, conta: x.conta || x.designada || '', pedido: corta(x.texto, 140),
      criado: (x.criado || '').slice(0, 16), pronto: x.prontoEm ? x.prontoEm.slice(0, 16) : '', resumo: corta(x.resumo, 120), pergunta_esperando_lindson: x.esperando && q ? corta(q.texto, 160) : '' };
  });
  const equipe = CONTAS_EQ.map(c => { const e = estadoReal(contas[c], agora), x = contas[c] || {}; return { conta: c, estado: e.estado, tarefa_ativa: e.ativa, ate: e.ate, fazendo: corta(x.tarefa, 100) }; });
  const hora = new Date().toLocaleString('pt-BR', { timeZone: 'America/Fortaleza', weekday: 'long', day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' });
  return `AGORA: ${hora} (São Luís).
FILA AO VIVO (mais recentes primeiro): ${JSON.stringify(fila)}
EQUIPE AO VIVO: ${JSON.stringify(equipe)}
PAINEL (gerado em ${CTX.gerado}): ${JSON.stringify({ placar: CTX.placar, em_andamento: CTX.andamento, ultimas_entregas: CTX.entregas, entregas_na_semana: CTX.entregas_semana, ultima_atividade: CTX.atividade, agenda_instagram: CTX.agenda_instagram })}
PEDIDO PENDENTE (esperando o sim do Lindson): ${pendente ? JSON.stringify(pendente) : 'nenhum'}`;
}

function mensagens(b) {
  // histórico curto da sessão; a API pede alternância começando pelo usuário, então junta falas seguidas do mesmo lado
  const out = [];
  const add = (role, text) => { if (!text) return; const u = out[out.length - 1]; if (u && u.role === role) u.content += '\n' + text; else out.push({ role, content: text }); };
  (Array.isArray(b.historico) ? b.historico.slice(-16) : []).forEach(h => h && add(h.de === 'vektor' ? 'assistant' : 'user', corta(h.t, 600)));
  while (out.length && out[0].role !== 'user') out.shift();
  add('user', corta(b.fala, 500));
  return out;
}

function validaFim(o, pendente) {
  const r = { t: 'fim', acao: 'nenhuma', pedido: null, ir: '', memoria: '', tela: '' };
  if (!o || typeof o !== 'object') return r;
  r.memoria = corta(o.memoria, 300); r.tela = corta(o.tela, 400);
  const p = o.pedido && typeof o.pedido === 'object' ? o.pedido : null;
  if (o.acao === 'propor' && p && NOMES_CLI[p.cli] && NOMES_FN[p.func]) { r.acao = 'propor'; r.pedido = { cli: p.cli, func: p.func, texto: corta(p.texto, 500) }; }
  else if (o.acao === 'criar' && pendente) { r.acao = 'criar'; r.pedido = pendente; } // só o que ele confirmou
  else if (o.acao === 'ir' && IRS.includes(o.ir)) { r.acao = 'ir'; r.ir = o.ir; }
  return r;
}

// separa a fala (antes de ###) do JSON final, emitindo a fala conforme chega
function separador(enviar) {
  let buf = '', falado = 0, fim = false;
  return {
    add(t) {
      buf += t; if (fim) return;
      const i = buf.indexOf('###');
      if (i >= 0) { fim = true; if (i > falado) enviar({ t: 'txt', v: buf.slice(falado, i) }); falado = i; return; }
      const seguro = Math.max(falado, buf.length - 3); // segura o fim, que pode ser o começo de ###
      if (seguro > falado) { enviar({ t: 'txt', v: buf.slice(falado, seguro) }); falado = seguro; }
    },
    acabou() {
      const i = buf.indexOf('###');
      if (i < 0) { if (buf.length > falado) enviar({ t: 'txt', v: buf.slice(falado) }); return null; }
      const resto = buf.slice(i + 3), a = resto.indexOf('{'), z = resto.lastIndexOf('}');
      try { return a >= 0 ? JSON.parse(resto.slice(a, z + 1)) : null; } catch (e) { return null; }
    }
  };
}

async function lerSSE(body, aoEvento) {
  const rd = body.getReader(), dec = new TextDecoder(); let resto = '';
  for (;;) {
    const { done, value } = await rd.read(); if (done) break;
    resto += dec.decode(value, { stream: true });
    let k; while ((k = resto.indexOf('\n')) >= 0) {
      const linha = resto.slice(0, k).trim(); resto = resto.slice(k + 1);
      if (!linha.startsWith('data:')) continue;
      const d = linha.slice(5).trim(); if (!d || d === '[DONE]') continue;
      let ev; try { ev = JSON.parse(d); } catch (e) { continue; }
      aoEvento(ev);
    }
  }
}

async function claude(env, sistema, msgs, sep) {
  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-api-key': env.ANTHROPIC_API_KEY, 'anthropic-version': '2026-10-21', 'anthropic-beta': 'server-side-fallback-2026-07-01' },
    body: JSON.stringify({ model: MODELO, max_tokens: 4000, stream: true, fallbacks: 'default', output_config: { effort: 'low' },
      system: [{ type: 'text', text: PERSONA, cache_control: { type: 'ephemeral' } }, { type: 'text', text: sistema }], messages: msgs })
  });
  if (!r.ok) { const t = await r.text().catch(() => ''); throw Object.assign(new Error('claude ' + r.status), { status: r.status, corpo: t.slice(0, 300) }); }
  let parou = '';
  await lerSSE(r.body, ev => {
    if (ev.type === 'content_block_delta' && ev.delta && ev.delta.type === 'text_delta') sep.add(ev.delta.text);
    else if (ev.type === 'message_delta' && ev.delta && ev.delta.stop_reason) parou = ev.delta.stop_reason;
    else if (ev.type === 'error') throw new Error('claude stream ' + ((ev.error && ev.error.type) || ''));
  });
  return parou;
}

class Cota extends Error {}
async function workersAI(env, sistema, msgs, sep) {
  let ultimo;
  for (const m of MODELOS_AI) {
    try {
      const st = await env.AI.run(m, { stream: true, max_tokens: 500, temperature: 0.6, chat_template_kwargs: { enable_thinking: false },
        messages: [{ role: 'system', content: PERSONA + '\n\n' + sistema }].concat(msgs) });
      let algo = false;
      await lerSSE(st, ev => {
        const t = typeof ev.response === 'string' ? ev.response : ev.choices && ev.choices[0] && ev.choices[0].delta && typeof ev.choices[0].delta.content === 'string' ? ev.choices[0].delta.content : '';
        if (t) { algo = true; sep.add(t); }
      });
      if (algo) return 'end_turn';
    } catch (e) {
      const msg = String((e && e.message) || e);
      if (/3036|daily free allocation|neurons/i.test(msg)) throw new Cota(msg); // acabou a cota grátis do dia
      ultimo = e; // modelo fora do ar ou sem capacidade: tenta o próximo
    }
  }
  throw ultimo || new Error('Workers AI sem resposta');
}

export async function onRequestPost({ request, env }) {
  const q = await quemE(request, env);
  if (!q || q.cli !== 'admin') return json({ erro: 'Sem acesso.' }, 401);
  const txt = await request.text(); if (txt.length > 20000) return json({ erro: 'Dados grandes demais.' }, 413);
  let b; try { b = JSON.parse(txt); } catch (e) { return json({ erro: 'Dados inválidos.' }, 400); }
  if (!b || typeof b.fala !== 'string' || !b.fala.trim() || b.fala.length > 500) return json({ erro: 'fala obrigatória (até 500 caracteres).' }, 400);
  const temClaude = typeof env.ANTHROPIC_API_KEY === 'string' && env.ANTHROPIC_API_KEY.length > 20, temAI = !!(env.AI && env.AI.run);
  if (!temClaude && !temAI) return json({ erro: 'O VEKTOR ainda não tem cérebro ligado.', falta: ATIVAR }, 503);
  const p = b.pendente && typeof b.pendente === 'object' && NOMES_CLI[b.pendente.cli] && NOMES_FN[b.pendente.func] ? { cli: b.pendente.cli, func: b.pendente.func, texto: corta(b.pendente.texto, 500) } : null;
  const sistema = (await contexto(env, p)) + (b.memoria ? '\nMEMÓRIA DA CONVERSA: ' + corta(b.memoria, 600) : '');
  const msgs = mensagens(b);
  const { readable, writable } = new TransformStream(), w = writable.getWriter(), enc = new TextEncoder();
  const enviar = o => w.write(enc.encode(JSON.stringify(o) + '\n'));
  (async () => {
    const sep = separador(enviar);
    try {
      let parou;
      try { if (!temClaude) throw new Error('sem chave'); parou = await claude(env, sistema, msgs, sep); }
      catch (e) { if (!temAI) throw e; parou = await workersAI(env, sistema, msgs, sep); }
      if (parou === 'refusal') enviar({ t: 'txt', v: 'Esse assunto eu não consigo tocar, Lindson. Me diz de outro jeito?' });
      enviar(validaFim(sep.acabou(), p));
    } catch (e) {
      enviar({ t: 'erro', v: e instanceof Cota ? 'Lindson, gastei a cota gratuita de conversa de hoje. Volto às nove da noite. Até lá, os comandos de voz continuam valendo.' : e.status === 429 ? 'Muitos pedidos seguidos. Tenta de novo em um minuto.' : 'Perdi a conexão com o meu cérebro. Tenta de novo.', falta: '' });
    }
    try { await w.close(); } catch (e) {}
  })();
  return new Response(readable, { headers: { 'Content-Type': 'application/x-ndjson; charset=utf-8', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' } });
}
export const onRequestGet = async ({ request, env }) => {
  // a página pergunta se o cérebro está ligado (sem revelar nada do segredo)
  if (new URL(request.url).searchParams.has('saude')) return json({ ligado: !!(env.AI && env.AI.run) || (typeof env.ANTHROPIC_API_KEY === 'string' && env.ANTHROPIC_API_KEY.length > 20) }); // só sim/não, para conferir o deploy
  const q = await quemE(request, env);
  if (!q || q.cli !== 'admin') return json({ erro: 'Sem acesso.' }, 401);
  const c = typeof env.ANTHROPIC_API_KEY === 'string' && env.ANTHROPIC_API_KEY.length > 20, a = !!(env.AI && env.AI.run);
  return json({ ligado: c || a, motor: c ? 'claude' : a ? 'workers-ai' : '', falta: c || a ? '' : ATIVAR });
};
