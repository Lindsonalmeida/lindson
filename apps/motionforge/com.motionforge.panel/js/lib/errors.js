// Traduz erros técnicos em mensagens claras para quem está no AE.
"use strict";
const { HttpError, CancelledError } = require("./http");

function detail(body) {
  if (!body) return "";
  try {
    const j = JSON.parse(body);
    const d = j.detail || j.error || j.message || j.title;
    if (Array.isArray(d)) return d.map((x) => (x.loc ? x.loc.slice(-1)[0] + ": " : "") + (x.msg || JSON.stringify(x))).join("; ");
    if (d && typeof d === "object") return d.message || JSON.stringify(d);
    return String(d || "").slice(0, 300);
  } catch (e) {
    return String(body).replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim().slice(0, 200);
  }
}

function friendly(e, provider) {
  const who = provider ? ` (${provider})` : "";
  if (!e) return "Erro desconhecido.";
  if (e instanceof CancelledError || e.name === "CancelledError") return "Cancelado.";
  if (e instanceof HttpError || e.name === "HttpError") {
    const d = detail(e.body);
    const low = (d || "").toLowerCase();
    if (e.status === 401) return `Chave de API inválida ou ausente${who}. Confira em Config.`;
    if (e.status === 402 || /balance|credit|exhausted|insufficient|billing|saldo/.test(low)) return `Sem saldo na conta${who}. Recarregue os créditos e tente de novo.`;
    if (e.status === 403) return `Acesso negado${who}: ${d || "a chave não tem permissão para este modelo"}.`;
    if (e.status === 404) return `Modelo ou recurso não encontrado${who}. Confira o ID do modelo.`;
    if (e.status === 405) return `Endereço de API recusado${who} (405).`;
    if (e.status === 413) return "Arquivo grande demais para o provedor.";
    if (e.status === 422 || e.status === 400) return `O modelo recusou os parâmetros${who}: ${d || "confira prompt, duração e imagem"}.`;
    if (e.status === 429) return `Limite de requisições${who}. Aguarde um pouco e tente de novo.`;
    if (e.status >= 500) return `O provedor${who} está instável (${e.status}). Tente de novo em instantes.`;
    return `Erro ${e.status}${who}: ${d}`;
  }
  const code = e.code || "";
  if (code === "ENOTFOUND" || code === "EAI_AGAIN" || code === "ENETUNREACH") return "Sem conexão com a internet (ou o endereço do provedor está errado).";
  if (code === "ECONNREFUSED") return provider === "ComfyUI" ? "ComfyUI não respondeu. Ele está aberto? Confira a URL em Config." : "Conexão recusada pelo servidor.";
  if (code === "ETIMEDOUT") return "Tempo de conexão esgotado. Tente de novo.";
  if (code === "ENOENT" && e.path) return `Programa não encontrado: ${e.path}. Confira o caminho em Config.`;
  return e.message || String(e);
}

module.exports = { friendly, detail };
