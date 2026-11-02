#!/usr/bin/env python3
"""Confere as citações em italiano do acervo Maquiavel no texto original.

O que faz
1. Lê todos os .md de conteudo/referencias/maquiavel/ (e de frente-lindson/), menos a pasta revisao/.
2. Extrai as citações: «...», *"..."*, "*...*", "..." e *itálico* longo; fica só com as que
   estão em italiano (contagem de palavras típicas de italiano x português/espanhol/latim/francês/inglês).
3. Normaliza (acentos, apóstrofos, maiúsculas, espaços, grafias antigas: h, j/i, u/v, y/i, x/s,
   ti+vogal/zi, letras dobradas, et/e, ed/e) e procura cada trecho (as partes separadas por
   "..." ou "(…)" são procuradas uma a uma) nos textos originais de revisao/textos/.
4. Busca exata normalizada; se não achar, busca aproximada (índice de pares de palavras +
   rapidfuzz/difflib) e mostra o trecho real do original.

Saída
- revisao/citacoes-tabela.tsv  (arquivo, linha, citação, obra indicada, resultado, nota, fonte, trecho do original)
- revisao/citacoes-dados.json  (o mesmo, para outros programas)
Uso: python3 revisao/conferir_citacoes.py [arquivo.md ...]
"""
import json, os, re, sys, unicodedata
from collections import Counter, defaultdict

try:
    from rapidfuzz import fuzz
    def parcial(a, b):
        r = fuzz.partial_ratio_alignment(a, b)
        return r.score, r.dest_start, r.dest_end
except ImportError:  # sem rapidfuzz: difflib (mais lento)
    import difflib
    def parcial(a, b):
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        best = (0, 0, len(b))
        for blk in sm.get_matching_blocks():
            s = max(0, blk.b - blk.a); e = min(len(b), s + len(a))
            r = difflib.SequenceMatcher(None, a, b[s:e]).ratio() * 100
            if r > best[0]:
                best = (r, s, e)
        return best

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.dirname(AQUI)
TEXTOS = os.path.join(AQUI, "textos")

# ---------------------------------------------------------------- normalização
def _sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))

def norm_palavra(w):
    w = w.replace("h", "").replace("j", "i").replace("y", "i").replace("v", "u").replace("x", "s")
    w = w.replace("ph", "f")
    w = re.sub(r"ti(?=[aeiou])", "zi", w)
    w = re.sub(r"(.)\1+", r"\1", w)
    if w in ("et", "ed"):
        w = "e"
    return w

TOKEN = re.compile(r"[a-z0-9]+")

def tokens(texto, com_pos=False):
    """Lista de palavras normalizadas (e, se pedido, a posição de cada uma no texto)."""
    t = _sem_acento(texto.lower())
    out, pos = [], []
    for m in TOKEN.finditer(t):
        w = m.group()
        if w.isdigit():
            continue
        n = norm_palavra(w)
        if n:
            out.append(n); pos.append(m.start())
    return (out, pos) if com_pos else out

# ---------------------------------------------------------------- textos-fonte
CABECALHO = re.compile(r"^\s*(?:\d{1,4}\s+)?[A-ZÀÈÉÌÒÙ'’\.\-,;: ]{4,}[A-ZÀÈÉÌÒÙ\.]\s*(?:\d{1,4})?\s*$")
MODERNO = re.compile(r"PREFAZIONE|INTRODUZIONE|PER UN RITRATTO|NOTA EDITORIALE|RASSEGNA|INDICE|SOMMARIO|ATTRIBUZIONI")
OBRAS_MARTELLI = [  # (padrão no cabeçalho corrente da ed. Martelli/Bompiani, rótulo)
    (r"PRINCIPE|^CAPITOLO [IVXL]+$|^CAPITOLI [IVXL\-]+$", "Principe"),
    (r"DISCORSI SOPRA LA PRIMA DECA", "Discorsi"),
    (r"ARTE DELLA GUERRA", "Arte della guerra"),
    (r"ISTORIE FIORENTINE", "Istorie fiorentine"),
    (r"CASTRUCCIO", "Vita di Castruccio"),
    (r"MANDRAGOLA", "Mandragola"), (r"CLIZIA", "Clizia"), (r"ANDRIA", "Andria"),
    (r"FAVOLA|BELFAGOR", "Belfagor"), (r"ASINO", "Asino"), (r"DECENNAL", "Decennali"),
    (r"CAPITOLI PER UNA COMPAGNIA", "Capitoli per una compagnia di piacere"),
    (r"^I ?CAPITOLI", "Capitoli"), (r"CANTI CARNASCIALESCHI", "Canti carnascialeschi"),
    (r"RIME VARIE|SERENATA", "Rime varie"), (r"NOSTRA LINGUA", "Discorso intorno alla nostra lingua"),
    (r"DISCURSUS", "Discursus florentinarum rerum"), (r"LUCCA", "Sommario delle cose di Lucca"),
    (r"FRANCIA", "Ritratto di cose di Francia"), (r"MAGNA", "Ritratto/Rapporto/Discorso della Magna"),
    (r"VALENTINO", "Legazioni / Descrizione del modo tenuto dal Duca Valentino"),
    (r"VALDICHIANA", "Del modo di trattare i popoli della Valdichiana"),
    (r"LEGAZION|COMMISSARI", "Legazioni e commissarie"), (r"LETTERE", "Lettere"),
    (r"EXORTAZIONE", "Esortazione alla penitenza"), (r"PISTORIENS", "De rebus pistoriensibus"),
    (r"ORDINANZA", "Scritti sull'ordinanza"), (r"DANAIO", "Parole da dirle sopra la provvisione del danaio"),
    (r"PISA", "Discorso sopra le cose di Pisa"), (r"SCRITTI POLITICI", "Scritti politici minori"),
    (r"SCRITTI STORICI", "Scritti storici"), (r"TEATRO|SCRITTI LETTERARI", "Scritti letterari"),
]

def ler(p):
    s = open(p, encoding="utf-8", errors="replace").read()
    s = s.replace("¬\n", "").replace("¬ ", "").replace("¬", "")
    return re.sub(r"(\w)[-­]\s*\n\s*(\w)", r"\1\2", s)  # junta palavras partidas por hífen de linha

class Fonte:
    def __init__(self, nome, texto, tipo, rotulos):
        self.nome, self.texto, self.tipo = nome, texto, tipo
        self.tok, self.pos = tokens(texto, True)
        self.rotulos = rotulos          # lista ordenada (posição no texto, rótulo da obra/parte)
        self.junto = " " + " ".join(self.tok) + " "
        # posição (em caracteres de self.junto) -> índice do token
        self.inicio_tok = []
        c = 1
        for w in self.tok:
            self.inicio_tok.append(c); c += len(w) + 1
        self._idx = None

    def rotulo(self, pos_char):
        r = ""
        for p, l in self.rotulos:
            if p > pos_char:
                break
            r = l
        return r

    def indice(self):
        if self._idx is None:
            d = defaultdict(list)
            for i in range(len(self.tok) - 1):
                d[(self.tok[i], self.tok[i + 1])].append(i)
            self._idx = d
        return self._idx

    def tok_de_char(self, c):
        import bisect
        return max(0, bisect.bisect_right(self.inicio_tok, c) - 1)

    def trecho(self, ti, tf, margem=0):
        ti = max(0, ti - margem); tf = min(len(self.tok) - 1, tf + margem)
        a, b = self.pos[ti], self.pos[tf]
        fim = re.match(r"\S*", self.texto[b:]).end()
        return re.sub(r"\s+", " ", self.texto[a:b + fim]).strip()


def carregar_martelli(p):
    """Separa o texto de Maquiavel (com rótulo da obra) dos prefácios/introdução modernos."""
    linhas = ler(p).split("\n")
    mach, mod, rot, atual, c = [], [], [], "moderno", 0
    for l in linhas:
        if CABECALHO.match(l) and re.search(r"[A-Z]{4}", l):
            h = re.sub(r"\d", "", l).strip()
            if MODERNO.search(h):
                atual = "moderno"
            else:
                for pad, lab in OBRAS_MARTELLI:
                    if re.search(pad, h):
                        if lab != atual:
                            atual = lab
                            rot.append((c, atual))
                        break
            continue  # cabeçalho corrente não entra no texto
        if re.fullmatch(r"\s*\d{1,4}\s*", l):
            continue
        if atual == "moderno":
            mod.append(l)
        else:
            mach.append(l); c += len(l) + 1
    return "\n".join(mach), rot, "\n".join(mod)


def carregar_fontes():
    fontes = []
    raw = os.path.join(TEXTOS, "raw")
    def add(nome, arq, tipo, rotulo):
        p = os.path.join(raw, arq)
        if os.path.exists(p):
            fontes.append(Fonte(nome, ler(p), tipo, [(0, rotulo)]))
    p = os.path.join(raw, "martelli-bompiani.txt")
    if os.path.exists(p):
        t, rot, mod = carregar_martelli(p)
        fontes.append(Fonte("Martelli (Tutte le opere, 1971; ed. Bompiani 2018, IA)", t, "primária", rot))
        fontes.append(Fonte("Prefácios modernos da ed. Bompiani 2018 (secundária)", mod, "secundária",
                            [(0, "moderno (prefácio/introdução Bompiani)")]))
    ws = os.path.join(TEXTOS, "wikisource")
    if os.path.isdir(ws):
        for f in sorted(os.listdir(ws)):
            if not f.endswith(".txt"):
                continue
            t = open(os.path.join(ws, f), encoding="utf-8").read()
            rot = [(m.start(), m.group(1).replace("_", " ")) for m in re.finditer(r"^### (.+)$", t, re.M)]
            fontes.append(Fonte("Wikisource " + f[:-4].replace("_", " "), t, "primária", rot or [(0, f)]))
    add("Einaudi/Martelli Il Principe (IA)", "principeilniccolomachiavelli.txt", "primária", "Principe")
    add("Einaudi Discorsi (IA)", "discorsisopralaprimadecadititolivioniccolomachiavelli.txt", "primária", "Discorsi")
    add("Einaudi/Martelli Arte della guerra (IA)", "artedellaguerradellniccolomachiavelli.txt", "primária", "Arte della guerra")
    add("Einaudi Mandragola (IA)", "mandragolaniccolomachiavelli.txt", "primária", "Mandragola")
    add("Einaudi Clizia (IA)", "clizianiccolomachiavelli.txt", "primária", "Clizia")
    add("Einaudi Belfagor (IA)", "favoladibelfagorniccolomachiavelli.txt", "primária", "Belfagor")
    add("Liber Liber Istorie fiorentine (Martelli)", "liberliber-istorie-fiorentine.txt", "primária", "Istorie fiorentine")
    add("Gutenberg 56498 Mandragola/Clizia/Belfagor", "gutenberg56498-mandragola-clizia-belfagor.txt", "primária", "Mandragola/Clizia/Belfagor")
    for i in range(1, 5):
        add(f"Chiappelli, Legazioni vol. {i} (1971-85, IA)", f"chiappelli-legazioni-vol{i}.txt", "primária", "Legazioni e commissarie")
    for v, lab in (("05", "Prose/scritti minori"), ("06", "Legazioni"), ("07", "Legazioni"), ("08", "Lettere familiari")):
        add(f"Opere (Italia 1813) vol. {v} (IA)", f"opere1813-vol{v}.txt", "primária", lab)
    add("Opere complete (Firenze 1843, IA)", "opere-complete-1843.txt", "primária", "Opere complete 1843")
    add("Lettere (IA lettere00mach)", "lettere00mach.txt", "primária", "Lettere")
    for i in (1, 2, 3):
        add(f"Villari, Machiavelli e i suoi tempi vol. {i} (secundária)", f"villari-vol{i}.txt", "secundária", "Villari (cita documentos)")
    return fontes

# ---------------------------------------------------------------- extração das citações
IT = set("""il lo gli la le i un uno una di del dello della dei degli delle de da dal dallo dalla dai dagli dalle
in nel nello nella nei negli nelle con su sul per tra fra che chi cui non piu è e' perche perché ma se come
quando quello quella quelli quelle questo questa questi queste sono essere esser era erano fu furono sia
siano fussi fusse ha hanno aveva avere io tu lui lei noi voi loro mio mia suo sua nostro vostro ogni
alcuno alcuna nessuno niuno debbe debbono puo può sanza senza molto molte molti tanto tanti cosa cose
uomini uomo huomini principe principi stato stati città gente sempre mai ancora adunque dunque però
perciò quale quali li ne ci vi gl' dell' all' nell' sull' coll' altro altri altre ne' de' a' e' co'
volta volte modo fare fatto fatta essendo avendo bisogna bisogno ragione tempo tempi""".split())
PT = set("""o os a as um uma uns umas do dos da das no nos na nas em com para por pelo pela pelos pelas
não que é são foi eram ser estar está ele ela eles elas seu sua seus suas mais muito isso isto este
esta esse essa aquele aquela também quando como mas ou se já até depois antes então porque sobre
nosso nossa você vocês tem têm ter sempre nunca coisa coisas homens homem príncipe estado cidade""".split())
ES = set("""el los las del al y es son fue pero muy por para con sin su sus lo que una uno como más este
esta ese esa aquel hombres hombre príncipe ciudad hay ha han sobre según también""".split())
LA = set("""et est sunt non in ad cum quod qui quae per ex ab nec sed ut atque esse rerum res omnia
nihil enim autem vel nisi tamen""".split())
FR = set("""le la les des du de et est sont pas qui que un une pour par avec dans sur ce cette il ils elle
ne se au aux plus""".split())
EN = set("""the of and to in is are was were that this with for not be by on as it which""".split())

def lingua(t):
    ws = re.findall(r"[a-zà-öø-ÿ']+", t.lower())
    ws2 = [w.rstrip("'") + ("'" if w.endswith("'") else "") for w in ws]
    c = {k: sum(1 for w in ws2 if w in S or w.rstrip("'") in S) for k, S in
         (("it", IT), ("pt", PT), ("es", ES), ("la", LA), ("fr", FR), ("en", EN))}
    # palavras que só o italiano tem pesam mais
    so_it = sum(1 for w in ws if w in ("il", "che", "gli", "non", "della", "delle", "degli", "nella", "sono",
                                           "perché", "perche", "è", "più", "uno", "debbe", "sanza", "essere", "loro",
                                           "quello", "quelli", "questo", "come", "ogni", "li", "fussi", "fusse",
                                           "di", "e'", "de'", "ne'", "cosa", "cose", "uomini", "huomini"))
    c["it"] += so_it
    return c

def eh_italiano(t, minimo=4):
    ws = re.findall(r"\w+", t)
    if len(ws) < minimo:
        return False
    c = lingua(t)
    outros = max(c["pt"], c["es"], c["la"], c["fr"], c["en"])
    return c["it"] >= 3 and c["it"] > 1.3 * outros

PADROES = [
    ("«»", re.compile(r"«([^»]{3,}?)»")),
    ('*"', re.compile(r'\*"(.+?)"\*')),
    ('*“', re.compile(r"\*“(.+?)”\*")),
    ('"*', re.compile(r'"\*(.+?)\*"')),
    ('"', re.compile(r'(?<![\w*])"([^"\n]{10,}?)"(?![\w*])')),
    ("“", re.compile(r"“([^”\n]{10,}?)”")),
    ("*", re.compile(r"(?<![*\w])\*(?!\*)([^*\n]{25,}?)\*(?![*\w])")),
]
SEPARA = re.compile(r"\s*(?:\[\s*(?:\.\.\.|…)\s*\]|\(\s*(?:\.\.\.|…)\s*\)|\.\.\.|…)\s*")

def limpar(q):
    q = q.replace("**", "").replace("*", "").replace("`", "")
    q = re.sub(r"\[(?!\s*(?:\.\.\.|…))[^\]]*\]", " ", q)  # inserções editoriais [..]
    return re.sub(r"\s+", " ", q).strip(" ,;:")

OBRA_MD = [
    (r"Pr[ií]ncipe|Principe|De principatibus", "Principe"), (r"Discursos|Discorsi", "Discorsi"),
    (r"Arte da [Gg]uerra|[Aa]rte della guerra", "Arte della guerra"),
    (r"Hist[óo]ria de Floren[çc]a|Istorie|\bHF\b", "Istorie fiorentine"),
    (r"Mandr[áa]gora|Mandragola", "Mandragola"), (r"Clizia", "Clizia"), (r"Belfagor", "Belfagor"),
    (r"Castruccio", "Vita di Castruccio"), (r"\bAsno\b|Asino", "Asino"), (r"Decenal|Decennal", "Decennali"),
    (r"Discursus", "Discursus"), (r"carta|lettera|Lettere|Vettori|Guicciardini", "Lettere"),
    (r"[Ll]ega[çz][ãa]o|[Ll]egazion|despacho", "Legazioni"), (r"Andria", "Andria"),
    (r"Capitol[oi] (?:di|dell|della)|Ambi[zç][ãi]o|Ingratid|Occasione|Fortuna \(capitolo", "Capitoli"),
]
PADRAO_ARQ = {"principe.md": "Principe", "o-principe.md": "Principe", "discursos.md": "Discorsi",
              "arte-da-guerra.md": "Arte della guerra", "historia-de-florenca.md": "Istorie fiorentine"}

def obra_indicada(linha, arq):
    achou = []
    for pad, lab in OBRA_MD:
        if re.search(pad, linha) and lab not in achou:
            achou.append(lab)
    if not achou and os.path.basename(arq) in PADRAO_ARQ:
        achou = [PADRAO_ARQ[os.path.basename(arq)]]
    return achou

def extrair(arq):
    cits = []
    em_codigo = False
    for n, linha in enumerate(open(arq, encoding="utf-8"), 1):
        if linha.strip().startswith("```"):
            em_codigo = not em_codigo
        if em_codigo:
            continue
        ocupado = []
        for tipo, rx in PADROES:
            for m in rx.finditer(linha):
                a, b = m.span()
                if any(a < y and b > x for x, y in ocupado):
                    continue
                q = limpar(m.group(1))
                if not eh_italiano(q):
                    continue
                ocupado.append((a, b))
                partes = [p for p in SEPARA.split(q) if len(re.findall(r"\w+", p)) >= 3]
                if not partes:
                    continue
                cits.append({"arquivo": os.path.relpath(arq, PASTA), "linha": n, "tipo": tipo,
                             "citacao": q, "partes": partes, "obra_indicada": obra_indicada(linha, arq),
                             "contexto": linha.strip()[:400],
                             "ja_marcada": bool(re.search(r"n[ãa]o conferid", linha, re.I))})
    return cits

# ---------------------------------------------------------------- busca
def busca_exata(qt, fontes):
    alvo = " " + " ".join(qt) + " "
    achados = []
    for f in fontes:
        i = f.junto.find(alvo)
        if i >= 0:
            ti = f.tok_de_char(i + 1)
            achados.append((f, ti, ti + len(qt) - 1))
    return achados

def busca_aprox(qt, fontes, maxcand=6):
    """Melhor alinhamento aproximado em CADA fonte: lista de (score, fonte, tok_ini, tok_fim)."""
    q = " ".join(qt)
    pares = [(qt[i], qt[i + 1]) for i in range(len(qt) - 1)] or [(qt[0], qt[0])]
    res = []
    for f in fontes:
        idx = f.indice()
        votos = Counter()
        for k, par in enumerate(pares):
            lst = idx.get(par)
            if not lst or len(lst) > 3000:
                continue
            for p in lst:
                votos[(p - k) // 4] += 1
        melhor = (0, None, 0, 0)
        for bloco, v in votos.most_common(maxcand):
            if v < max(1, len(pares) // 6):
                break
            ini = max(0, bloco * 4 - 8); fim = min(len(f.tok), bloco * 4 + len(qt) + 12)
            janela = " ".join(f.tok[ini:fim])
            sc, ds, de = parcial(q, janela)
            if sc > melhor[0]:
                ti = f.tok_de_char(f.inicio_tok[ini] + ds)
                tf = f.tok_de_char(f.inicio_tok[ini] + max(ds, de - 1))
                melhor = (sc, f, ti, tf)
        if melhor[1] is not None:
            res.append(melhor)
    return sorted(res, key=lambda r: -r[0])

def _sim(a, b):
    import difflib
    return difflib.SequenceMatcher(None, a, b).ratio()

def diferencas(qt, ot):
    """Compara palavra a palavra (já normalizadas). Devolve (n_reais, lista de diferenças).
    Diferença 'de grafia' = só separação de palavras ou letras parecidas (prudenza/prudenzia, dala/da la);
    diferença 'real' = palavra trocada, faltando ou sobrando."""
    import difflib
    sm = difflib.SequenceMatcher(None, qt, ot, autojunk=False)
    ops = sm.get_opcodes()
    # palavras do original que sobram só nas pontas = alinhamento largo demais, não é erro
    while ops and ops[0][0] == "insert":
        ops = ops[1:]
    while ops and ops[-1][0] == "insert":
        ops = ops[:-1]
    reais, lista = 0, []
    for op, i1, i2, j1, j2 in ops:
        if op == "equal":
            continue
        a, b = " ".join(qt[i1:i2]), " ".join(ot[j1:j2])
        curtas = op == "replace" and i2 - i1 == 1 and j2 - j1 == 1 and len(a) <= 2 and len(b) <= 2
        if curtas or op == "replace" and (a.replace(" ", "") == b.replace(" ", "") or
                                (_sim(a.replace(" ", ""), b.replace(" ", "")) >= 0.75 and abs((i2 - i1) - (j2 - j1)) <= 1)):
            lista.append(("grafia", a, b))
        else:
            reais += max(i2 - i1, j2 - j1)
            lista.append(("real", a, b))
    return reais, lista

def conferir(cits, fontes):
    prim = [f for f in fontes if f.tipo == "primária"]
    sec = [f for f in fontes if f.tipo != "primária"]
    for c in cits:
        res_partes = []
        for parte in c["partes"]:
            qt = tokens(parte)
            if len(qt) < 3:
                continue
            ach = busca_exata(qt, prim)
            if ach:
                f, ti, tf = ach[0]
                res_partes.append({"parte": parte, "res": "exata", "score": 100, "fonte": f.nome,
                                   "obra": f.rotulo(f.pos[ti]), "original": f.trecho(ti, tf),
                                   "todas": sorted({a[0].rotulo(a[0].pos[a[1]]) for a in ach})})
                continue
            cands = busca_aprox(qt, prim)
            if (not cands or cands[0][0] < 75) and sec:
                cands = sorted(cands + busca_aprox(qt, sec), key=lambda r: -r[0])
            if not cands:
                res_partes.append({"parte": parte, "res": "não encontrada", "score": 0})
                continue
            # entre as fontes com bom alinhamento, fica a de menos diferenças reais
            avals = []
            for sc, f, ti, tf in cands:
                if sc < 75 and avals:
                    continue
                n, lst = diferencas(qt, f.tok[ti:tf + 1])
                avals.append((n, -sc, f, ti, tf, lst, sc))
            avals.sort(key=lambda r: (r[0], r[1]))
            n, _, f, ti, tf, lst, sc = avals[0]
            obra = f.rotulo(f.pos[ti])
            if sc < 75:
                res = "não encontrada"
            elif n == 0:
                res = "aproximada (só grafia)"
            else:
                res = "aproximada (divergente)"
            if f.tipo != "primária" and sc >= 75:
                res += " [só em texto secundário]"
            res_partes.append({"parte": parte, "res": res, "score": round(sc, 1), "fonte": f.nome,
                               "obra": obra, "original": f.trecho(ti, tf, 0), "n_reais": n,
                               "difs": [d for d in lst if d[0] == "real"][:12]})
        c["resultado_partes"] = res_partes
        ordem = {"exata": 0, "aproximada (só grafia)": 1, "aproximada (divergente)": 2}
        if not res_partes:
            c["resultado"] = "curta demais"
        else:
            piores = sorted(res_partes, key=lambda r: (ordem.get(r["res"], 3), -r["score"]))
            c["resultado"] = piores[-1]["res"]
            c["score_min"] = min(r["score"] for r in res_partes)
        obras = {r.get("obra", "") for r in res_partes}
        c["obra_encontrada"] = "; ".join(sorted(o for o in obras if o))
    return cits

def principal(args):
    if args:
        arqs = args
    else:
        arqs = []
        for raiz, dirs, fs in os.walk(PASTA):
            if os.path.relpath(raiz, PASTA).startswith("revisao"):
                continue
            arqs += [os.path.join(raiz, f) for f in sorted(fs) if f.endswith(".md")]
    cits = []
    for a in arqs:
        cits += extrair(a)
    print(f"{len(cits)} citações em italiano em {len(arqs)} arquivos", file=sys.stderr)
    fontes = carregar_fontes()
    print(f"{len(fontes)} textos-fonte, {sum(len(f.tok) for f in fontes):,} palavras", file=sys.stderr)
    conferir(cits, fontes)
    with open(os.path.join(AQUI, "citacoes-dados.json"), "w", encoding="utf-8") as fh:
        json.dump(cits, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(AQUI, "citacoes-tabela.tsv"), "w", encoding="utf-8") as fh:
        fh.write("arquivo\tlinha\tcitacao\tobra_indicada\tresultado\tsemelhanca\tobra_encontrada\tfonte\ttrecho_original\n")
        for c in cits:
            rp = c["resultado_partes"]
            fh.write("\t".join(str(x).replace("\t", " ") for x in (
                c["arquivo"], c["linha"], c["citacao"], ", ".join(c["obra_indicada"]), c["resultado"],
                c.get("score_min", ""), c["obra_encontrada"], "; ".join(sorted({r.get("fonte", "") for r in rp})),
                " (…) ".join(r.get("original", "") for r in rp if r["res"] != "exata"))) + "\n")
    cont = Counter(c["resultado"] for c in cits)
    for k, v in cont.most_common():
        print(f"{k}: {v}", file=sys.stderr)

if __name__ == "__main__":
    principal(sys.argv[1:])
