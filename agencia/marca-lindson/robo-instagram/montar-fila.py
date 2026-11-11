#!/usr/bin/env python3
"""Gera functions/_agenda_ig.js (repo privado CentralLindsonALmeida) a partir de agenda-status.json.
Uso: python3 montar-fila.py [/caminho/centrallindsonalmeida]   (conta Pedro, 11/11/2026)"""
import json, sys, pathlib
aqui = pathlib.Path(__file__).resolve().parent
agenda = json.loads((aqui.parent / 'agenda-status.json').read_text(encoding='utf-8'))
destino = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida') / 'functions' / '_agenda_ig.js'
campos = ['id', 'seq', 'titulo', 'formato', 'cor', 'urls', 'capa', 'legenda', 'quando', 'status', 'media_id', 'link', 'stories']
posts = [{k: p[k] for k in campos if p.get(k) not in (None, '', [])} for p in agenda['posts']]
destino.write_text('// Gerado por lindson/agencia/marca-lindson/robo-instagram/montar-fila.py. Nao editar a mao.\n'
                   'export const IG_USER = "17841443356770777";\nexport const POSTS = '
                   + json.dumps(posts, ensure_ascii=False, indent=0) + ';\n', encoding='utf-8')
print(f'{len(posts)} posts -> {destino}')
