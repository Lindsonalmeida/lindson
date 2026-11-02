#!/usr/bin/env python3
"""Baixa da Biblioteca Italiana (BibIt) os textos de Maquiavel em XML/TEI e converte em texto.
Il Principe = ed. Inglese (Einaudi 1995); os demais = ed. Martelli (Sansoni 1971).
Saída: revisao/textos/bibit/<id>.txt (linhas '### Obra / título da divisão')."""
import html, os, re, urllib.request
IDS = {'bibit000214': 'Il Principe (Inglese 1995)', 'bibit000305': 'Istorie fiorentine', 'bibit000747': 'Discorsi',
       'bibit001126': 'Mandragola', 'bibit000181': 'Clizia', 'bibit000170': 'Asino', 'bibit000535': 'Arte della guerra',
       'bibit000245': 'Capitoli', 'bibit001186': 'Decennali', 'bibit000554': 'Vita di Castruccio',
       'bibit000555': 'Belfagor', 'bibit001565': 'Discorso intorno alla nostra lingua'}
URL = "http://backend.bibliotecaitaliana.it/wp-json/muruca-core/v1/xml/"
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "textos", "bibit")
os.makedirs(out, exist_ok=True)
for i, t in IDS.items():
    s = urllib.request.urlopen(URL + i, timeout=120).read().decode("utf-8")
    s = s[s.find("<text>"):]
    s = re.sub(r"(?s)<note.*?</note>", " ", s)
    s = re.sub(r"(?s)<head[^>]*>(.*?)</head>",
               lambda m: "\n### " + t + " / " + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n", s)
    s = re.sub(r"<lb\s*/>|</p>|</l>|</sp>|</div\d?>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    open(os.path.join(out, i + ".txt"), "w", encoding="utf-8").write("### " + t + "\n" + s)
    print(i, t, len(s))
