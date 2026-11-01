// Área "Agenda cheia" do painel da Clínica Dra. Jaci Cunha (entra no modelo prototipo/painel.html pelo montar-jaci.py).
// Vem da estratégia premium de out/2026 (agencia/clientes/jaci-cunha/estrategia-resumo.md): funil de avaliações,
// plano de 90 dias (marcações salvas neste aparelho) e pautas com os ganchos prontos. Conta Lindson, 01/11/2026.
(() => {
const V = window.__V, T = window.__T;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const CHAVE = 'jaci-plano90';
let feitos = {};
try { feitos = JSON.parse(localStorage.getItem(CHAVE) || '{}'); } catch (e) {}
const salva = () => { try { localStorage.setItem(CHAVE, JSON.stringify(feitos)); } catch (e) {} };

const FUNIL = [
  ['Conteúdo orgânico', '4 reels por semana aquecem a cidade.'],
  ['Remarketing', 'Quem viu 50% dos vídeos recebe prova e "agende sua avaliação".'],
  ['WhatsApp', 'Resposta em até 5 minutos, 3 perguntas e 2 horários.'],
  ['Avaliação', 'Confirmada na véspera.'],
  ['Procedimento', 'E o próximo retorno já marcado na saída.']];
const CODIGOS = [['[BTX01]', 'Botox não é pra congelar o rosto', 'Estética · Zé Doca + 40 km'], ['[BIO01]', 'Flacidez depois dos 35: o que dá pra fazer?', 'Estética e cidades vizinhas'],
  ['[LAB01]', 'Lábio natural, do seu jeito', 'Estética · Zé Doca + 40 km'], ['[ODO01]', 'Faz quanto tempo que você não vai ao dentista?', 'Odontologia · 25 km']];
const PLANO = [
  ['Novembro · semanas 1 e 2 · Base', ['Bio nova com CRO 8514 e chamada para a avaliação', 'Destaques: Avaliação, Procedimentos, Dúvidas, A Clínica, Pacientes, Como chegar', 'Perfil da Empresa no Google com 20+ fotos reais', 'Mini site com o chat de avaliação no link da bio', 'WhatsApp com etiquetas e resposta rápida', 'Códigos nos anúncios ([BTX01], [BIO01], [LAB01], [ODO01])']],
  ['Novembro · semanas 3 e 4 · Campanhas', ['Campanhas A (estética), B (odontologia) e C (remarketing) no ar', '4 reels por semana com os ganchos novos', 'Tema do mês: "quem quer estar bem nas festas começa agora"']],
  ['Dezembro · Retorno e prova', ['Retornos de botox marcados', 'Collab com perfis da região', 'Depoimentos autorizados (TCLE)', 'Pedir avaliação no Google depois de cada atendimento']],
  ['Janeiro · Escala', ['Aumentar a verba do que trouxe avaliação', 'Campanha regional (cidades vizinhas)', 'Plano anual para quem fez procedimento']]];
const GANCHOS = ['Botox deixa a cara parada? Vou te contar a verdade.', 'O que acontece na sua primeira avaliação aqui.', '3 perguntas para fazer antes de qualquer procedimento.',
  'Bioestimulador ou preenchimento? A diferença em 30 segundos.', 'Por que eu digo não para alguns pedidos de paciente.', 'Um dia comigo na clínica.',
  'Natural não é fazer pouco, é fazer certo pra você.', 'Você sorri de boca fechada nas fotos? Esse vídeo é pra você.'];
const LINHAS = [['Bastidores e acolhimento', 30, 'Reels e stories com a Dra. e a equipe'], ['Dúvidas respondidas', 25, 'Reels com rosto + carrossel curto'],
  ['Histórias de pacientes', 15, 'Depoimento autorizado, sem promessa'], ['Parcerias e Zé Doca', 15, 'Collab com perfis da região'], ['Autoridade e segurança', 15, 'Formação, materiais, biossegurança']];

const IG = (window.__DADOS || {}).instagram || {};
const n = v => typeof v === 'number' ? v.toLocaleString('pt-BR') : (v || 'a medir');
V.funil = () => `<div class="grade g4">${[['Seguidores', n(IG.seguidores), 'Instagram · ' + (IG.data || '')], ['Visualizações (30 dias)', n(IG.visualizacoes), IG.periodo || ''], ['Conversas por código', 'a medir', 'quando as campanhas entrarem'], ['Avaliações agendadas', 'a medir', 'etiqueta no WhatsApp']]
    .map(([r, v, n]) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var up"><span>${n}</span></div></div>`).join('')}</div>
  <div class="grade g21"><div class="card"><h3>O caminho da paciente</h3><p class="sub">Do vídeo até o procedimento. Se a conversa é barata mas ninguém agenda, o problema é o atendimento, não o anúncio.</p>
  <div class="lista">${FUNIL.map(([t, d], i) => `<div class="item"><div style="min-width:0"><div class="t">${i + 1}. ${t}</div><div class="d">${d}</div></div></div>`).join('')}</div></div>
  <div class="card"><h3>Códigos dos anúncios</h3><p class="sub">Cada anúncio abre o WhatsApp com um código. Assim a gente sabe de onde veio cada paciente.</p>
  <div class="lista">${CODIGOS.map(([c, t, p]) => `<div class="item"><div style="min-width:0"><div class="t">${c} ${esc(t)}</div><div class="d">${p}</div></div></div>`).join('')}</div></div></div>
  <div class="card"><h3>Relatório da semana</h3><p class="sub">O que a gente mede toda semana (os números entram quando as campanhas começarem).</p><div class="tab"><table><thead><tr><th>Número</th><th>O que mostra</th></tr></thead><tbody>
  ${[['Conversas por código', 'De qual anúncio veio cada paciente'], ['Custo por conversa', 'Quanto custa cada contato'], ['% que agendou', 'Força do atendimento'], ['% que compareceu', 'Força da confirmação'], ['% que fez procedimento', 'Força da avaliação'], ['% que voltou no 6º mês', 'Recorrência'], ['Avaliações no Google', 'Confiança da cidade']]
    .map(([a, b]) => `<tr><td>${a}</td><td>${b}</td></tr>`).join('')}</tbody></table></div></div>`;

V.plano90 = () => {
  const tot = PLANO.reduce((a, f) => a + f[1].length, 0), ok = Object.values(feitos).filter(Boolean).length;
  return `<div class="card"><h3>Plano de 90 dias</h3><p class="sub">Da estratégia de vendas aprovada. Marque o que já foi feito (fica salvo neste aparelho). ${ok} de ${tot} concluídos.</p><div class="barra"><i style="width:${ok / tot * 100}%"></i></div></div>
  <div class="grade g2">${PLANO.map(([f, l], i) => `<div class="card"><h3>${f}</h3><div class="lista">${l.map((t, j) => { const k = i + '-' + j; return `<label class="missao ${feitos[k] ? 'feita' : ''}"><input type="checkbox" data-p90="${k}" ${feitos[k] ? 'checked' : ''}><span class="t">${esc(t)}</span></label>`; }).join('')}</div></div>`).join('')}</div>`;
};

V.pautas = () => `<div class="grade g2"><div class="card"><h3>Ganchos de reels prontos</h3><p class="sub">Os 3 primeiros segundos sempre com o rosto da Dra. e a frase na tela.</p>
  <div class="lista">${GANCHOS.map((g, i) => `<div class="item"><div style="min-width:0"><div class="t">"${esc(g)}"</div></div><div class="fim"><button class="btn" type="button" data-copia="${i}">Copiar</button></div></div>`).join('')}</div></div>
  <div class="card"><h3>Linhas editoriais</h3><p class="sub">Ritmo: 4 reels + 1 carrossel por semana e stories todos os dias. Toda legenda termina com "chame no WhatsApp para sua avaliação".</p>
  <div class="lista">${LINHAS.map(([n, p, f]) => `<div><div style="display:flex;justify-content:space-between"><span>${n}</span><b>${p}%</b></div><div class="barra"><i style="width:${p * 3}%"></i></div><div class="d" style="font-size:12px;color:var(--apagado);margin-top:4px">${f}</div></div>`).join('')}</div></div></div>
  <div class="card"><h3>Regras do CFO</h3><p class="sub" style="margin:0">Pode: selfie da Dra., conteúdo educativo e bastidor, antes e depois de casos próprios com TCLE, depoimento autorizado. Não pode: preço, promoção, desconto, sorteio, "consulta grátis", promessa de resultado, procedimento sendo feito, sangue ou tecido. Em toda peça: CRO 8514.</p></div>`;

T.funil = 'Agenda cheia'; T.plano90 = 'Plano de 90 dias'; T.pautas = 'Pautas e ganchos';

window.__pos = view => {
  const m = document.getElementById('conteudo');
  if (!m) return;
  m.querySelectorAll('[data-p90]').forEach(c => c.onchange = () => { feitos[c.dataset.p90] = c.checked; salva(); if (c.checked) window.__toast('Feito! Plano atualizado.'); window.__render(); });
  m.querySelectorAll('[data-copia]').forEach(b => b.onclick = () => { try { navigator.clipboard.writeText(GANCHOS[+b.dataset.copia]); } catch (e) {} window.__toast('Gancho copiado.'); });
};
})();
