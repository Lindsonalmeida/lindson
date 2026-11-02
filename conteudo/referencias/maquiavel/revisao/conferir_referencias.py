#!/usr/bin/env python3
"""Segunda conferência: a citação está mesmo no livro/capítulo que o arquivo indica?

Usa revisao/citacoes-dados.json (gerado por conferir_citacoes.py). Para cada citação achada
de forma exata, pega os lugares onde ela aparece no Wikisource/BibIt (que têm livro e capítulo)
e compara com a referência dada no arquivo: primeiro a da mesma linha (ex.: "*Príncipe* XVIII",
"*Discursos* II.17", "III.9"), senão a do título de seção mais próximo acima.
Obras conferidas: Príncipe (capítulo), Discursos (livro.capítulo), Arte da guerra (livro),
História de Florença (livro).
Saída: revisao/referencias-tabela.tsv e resumo na tela.
"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.dirname(AQUI)
ROM = {"I": 1, "V": 5, "X": 10, "L": 50}
LIVRO = {"primo": 1, "secondo": 2, "terzo": 3, "quarto": 4, "quinto": 5, "sesto": 6, "settimo": 7, "ottavo": 8}

def rom(s):
    s = s.upper(); n = 0
    for i, ch in enumerate(s):
        v = ROM[ch]
        n += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return n

def lugares(rotulos):
    """Converte rótulos do Wikisource/BibIt em {(obra, livro, capítulo)}."""
    out = set()
    for r in rotulos:
        m = re.match(r"Il Principe/Capitolo ([IVXL]+)$", r) or re.match(r"Il Principe \(Inglese 1995\) / ([IVXL]+)$", r)
        if m:
            out.add(("P", None, rom(m.group(1)))); continue
        m = re.match(r"Discorsi sopra la prima Deca di Tito Livio/Libro (\w+)/Capitolo (\d+)", r)
        if m:
            out.add(("D", LIVRO[m.group(1)], int(m.group(2)))); continue
        m = re.match(r"Dell'arte della guerra/Libro (\w+)", r)
        if m:
            out.add(("A", LIVRO[m.group(1)], None)); continue
        m = re.match(r"Istorie fiorentine/Libro (\w+)", r)
        if m:
            out.add(("I", LIVRO[m.group(1)], None)); continue
    return out

R_ROM = r"([IVXL]{1,7})"
PADROES = [  # (obra, regex, grupos -> (livro, cap))
    ("P", re.compile(r"Pr[íi]ncipe\*{0,2},?\s+(?:cap\.\s*)?" + R_ROM + r"\b"), lambda m: (None, rom(m.group(1)))),
    ("D", re.compile(r"Discursos\*{0,2},?\s+(I{1,3})\.(\d+)"), lambda m: (rom(m.group(1)), int(m.group(2)))),
    ("A", re.compile(r"Arte da [Gg]uerra\*{0,2},?\s+(?:Livro\s+)?" + R_ROM + r"\b"), lambda m: (rom(m.group(1)), None)),
    ("I", re.compile(r"(?:Hist[óo]ria de Floren[çc]a|Istorie(?: fiorentine)?)\*{0,2},?\s+" + R_ROM + r"\.(\d+)"), lambda m: (rom(m.group(1)), int(m.group(2)))),
]
# referência "solta" (sem nome da obra) vale para a obra do próprio arquivo
SOLTA = {
    "principe.md": ("P", re.compile(r"(?:^|[\s(|*])(?:cap\.\s*)?" + R_ROM + r"(?=[\s,.:;)|*—-])"), lambda m: (None, rom(m.group(1)))),
    "o-principe.md": ("P", re.compile(r"cap\.\s*" + R_ROM + r"\b"), lambda m: (None, rom(m.group(1)))),
    "discursos.md": ("D", re.compile(r"\b(I{1,3})\.(\d{1,2})\b"), lambda m: (rom(m.group(1)), int(m.group(2)))),
    "arte-da-guerra.md": ("A", re.compile(r"Livro\s+" + R_ROM + r"\b"), lambda m: (rom(m.group(1)), None)),
    "historia-de-florenca.md": ("I", re.compile(r"\b([IVX]{1,4})\.(\d{1,2})\b"), lambda m: (rom(m.group(1)), int(m.group(2)))),
}

def refs_linha(linha, arq):
    achou = []
    for ob, rx, f in PADROES:
        for m in rx.finditer(linha):
            try:
                achou.append((m.start(), ob) + f(m))
            except KeyError:
                pass
    base = os.path.basename(arq)
    if not achou and base in SOLTA:
        ob, rx, f = SOLTA[base]
        for m in rx.finditer(linha):
            try:
                v = f(m)
            except KeyError:
                continue
            if v[1] and v[1] > 142 or v[0] and v[0] > 8:
                continue
            achou.append((m.start(), ob) + v)
    return achou

def confere(ref, locs):
    ob, liv, cap = ref
    for o, l, c in locs:
        if o != ob:
            continue
        if ob == "P" and c == cap:
            return True
        if ob == "D" and (l, c) == (liv, cap):
            return True
        if ob in ("A", "I") and l == liv:
            return True
    return False

def principal():
    dados = json.load(open(os.path.join(AQUI, "citacoes-dados.json"), encoding="utf-8"))
    linhas = {}
    out, cont = [], {"conferida": 0, "diferente": 0, "sem referência": 0, "sem lugar": 0}
    for c in dados:
        if not c["resultado"].startswith("exata"):
            continue
        locs = set()
        for r in c["resultado_partes"]:
            locs |= lugares(r.get("todas", []))
        if not locs:
            cont["sem lugar"] += 1; continue
        arq = os.path.join(PASTA, c["arquivo"])
        if arq not in linhas:
            linhas[arq] = open(arq, encoding="utf-8").read().split("\n")
        L = linhas[arq]
        linha = L[c["linha"] - 1]
        q = linha.find(c["citacao"][:30])
        refs = refs_linha(linha, arq)
        obras = {o for o, _, _ in locs}
        refs = [r for r in refs if r[1] in obras]
        if refs:
            # a referência mais próxima da citação (de preferência logo depois dela)
            fimq = q + len(c["citacao"][:30]) if q >= 0 else 0
            depois = [r for r in refs if r[0] >= fimq and r[0] - fimq <= 250]
            refs = sorted(depois, key=lambda r: r[0]) if depois else sorted(refs, key=lambda r: abs(r[0] - q))
            ref = refs[0][1:]
            origem = "linha"
        else:
            ref = None
            for k in range(c["linha"] - 2, -1, -1):
                if L[k].startswith("#"):
                    rr = [r for r in refs_linha(L[k], arq) if r[1] in obras]
                    if rr:
                        ref = rr[0][1:]; origem = "título: " + L[k][:60]
                    break
        if not ref:
            cont["sem referência"] += 1; continue
        ok = confere(ref, locs)
        cont["conferida" if ok else "diferente"] += 1
        if not ok:
            out.append((c["arquivo"], c["linha"], c["citacao"][:90], ref, origem,
                        sorted(locs, key=lambda x: (x[0], x[1] or 0, x[2] or 0))))
    with open(os.path.join(AQUI, "referencias-tabela.tsv"), "w", encoding="utf-8") as fh:
        fh.write("arquivo\tlinha\tcitacao\treferencia_no_arquivo\tde_onde\tonde_esta_no_original\n")
        for a, l, q, ref, orig, locs in out:
            fh.write(f"{a}\t{l}\t{q}\t{ref}\t{orig}\t{locs}\n")
    print(cont)
    for x in out:
        print(x)

if __name__ == "__main__":
    principal()
