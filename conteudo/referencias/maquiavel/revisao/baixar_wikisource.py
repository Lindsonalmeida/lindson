#!/usr/bin/env python3
"""Baixa do it.wikisource.org (páginas /wiki/, sem a API, que dá 429) o texto
completo das obras de Maquiavel, com todas as subpáginas (capítulos, livros, atos).
Saída: revisao/textos/wikisource/<Obra>.txt  (uma linha '### <página>' antes de cada subpágina).
Uso: python3 baixar_wikisource.py [Titolo ...]   (sem argumento = lista padrão)
"""
import html, os, re, sys, time, urllib.parse, urllib.request

BASE = "https://it.wikisource.org/wiki/"
UA = "LindsonMaquiavelReview/1.0 (revisao de citacoes; contato lindson)"
OBRAS = [
    "Il_Principe", "Discorsi_sopra_la_prima_Deca_di_Tito_Livio", "Dell'arte_della_guerra",
    "Istorie_fiorentine", "La_mandragola", "Clizia", "Favola_di_Belfagor_arcidiavolo",
    "La_vita_di_Castruccio_Castracani_da_Lucca", "L'Asino_(Machiavelli)", "Decennali",
    "Lettere_(Machiavelli)", "Rime_varie", "Canti_carnascialeschi_(Machiavelli)",
    "Discorso_intorno_alla_nostra_lingua", "Discorso_delle_cose_fiorentine_dopo_la_morte_di_Lorenzo",
    "Ai_Palleschi", "Del_modo_di_trattare_i_popoli_della_Valdichiana_ribellati",
    "Della_natura_de'_Francesi",
    "Descrizione_del_modo_tenuto_dal_Duca_Valentino_nello_ammazzare_Vitellozzo_Vitelli,_Oliverotto_da_Fermo,_il_Signor_Pagolo_e_il_duca_di_Gravina_Orsini",
    "Discorso_fatto_al_Magistrato_dei_Dieci_sopra_le_cose_di_Pisa",
    "Discorso_sopra_le_cose_della_Magna_e_sopra_l'imperatore",
    "Frammento_sulla_riforma_dello_stato_in_Firenze", "Parole_da_dirle_sopra_la_previsione_del_danaio",
    "Provvedimenti_per_la_riconquista_di_Pisa", "Rapporto_delle_cose_della_Magna",
    "Ritratto_delle_cose_della_Magna", "Ritratto_di_cose_di_Francia",
    "Sommario_delle_cose_della_città_di_Lucca", "Squarcio_di_un_discorso_fatto_ai_Dieci_sopra_le_cose_di_Pisa",
    "I_capitoli", "Dell'ira_e_de'_modi_di_curarla",
]

def get(title):
    url = BASE + urllib.parse.quote(title, safe="/'(),_")
    for tent in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(10 * (tent + 1))
        except Exception:
            time.sleep(10 * (tent + 1))
    return None

def corpo(h):
    i = h.find('id="mw-content-text"')
    j = h.find('<div class="printfooter"')
    return h[i:j] if i >= 0 else h

def texto(h):
    h = corpo(h)
    h = re.sub(r"""\sdata-[\w-]+='[^']*'""", "", h)
    h = re.sub(r'\sdata-[\w-]+="[^"]*"', "", h)
    h = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r'(?s)<span[^>]*class="[^"]*pagenumber[^"]*"[^>]*>.*?</span>', " ", h)
    h = re.sub(r"(?s)<sup[^>]*>.*?</sup>", "", h)
    h = re.sub(r"<br\s*/?>|</p>|</div>|</li>|</h\d>|</tr>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    return re.sub(r"\n\s*\n+", "\n\n", h).strip()

def subpaginas(h, titulo):
    out = []
    for href in re.findall(r'href="(?:https://it\.wikisource\.org)?/wiki/([^"#?]+)"', corpo(h)):
        t = urllib.parse.unquote(href)
        if t.startswith(titulo + "/") and t not in out:
            out.append(t)
    return out

def baixar(titulo, dest):
    visto, fila, partes = set(), [titulo], []
    while fila:
        t = fila.pop(0)
        if t in visto:
            continue
        visto.add(t)
        h = get(t)
        time.sleep(1.2)
        if h is None:
            print("  falhou/404:", t, flush=True)
            continue
        partes.append("### " + t + "\n" + texto(h))
        fila.extend(s for s in subpaginas(h, t) if s not in visto)
        print("  ok", t, flush=True)
    if partes:
        open(dest, "w", encoding="utf-8").write("\n\n".join(partes))
    return len(partes)

if __name__ == "__main__":
    pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "textos", "wikisource")
    os.makedirs(pasta, exist_ok=True)
    for o in (sys.argv[1:] or OBRAS):
        dest = os.path.join(pasta, re.sub(r"[^\w().'-]+", "_", o) + ".txt")
        if os.path.exists(dest) and os.path.getsize(dest) > 1000:
            print("já existe:", o); continue
        print(o, flush=True)
        print(" ->", baixar(o, dest), "páginas", flush=True)
