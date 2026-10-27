# Gera o contrato em PDF: python3 gerar.py dados.json  (dados.json fica em agencia/contratos/<cliente>/, fora do GitHub)
import json, sys, os, subprocess, html
d = json.load(open(sys.argv[1], encoding='utf-8'))
me = json.load(open(os.path.join(os.path.dirname(__file__), '..', '..', 'contratos', 'meus-dados.json'), encoding='utf-8'))
s = open(os.path.join(os.path.dirname(__file__), 'contrato.html'), encoding='utf-8').read()
d.update({k: v for k, v in me.items() if k not in d})
d['escopo_linhas'] = ''.join(f'<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td></tr>' for a, b in d['escopo'])
for k, v in d.items():
    if isinstance(v, str): s = s.replace('{{' + k + '}}', v if k == 'escopo_linhas' else html.escape(v))
assert '{{' not in s, 'faltou preencher: ' + s[s.index('{{'):s.index('}}', s.index('{{')) + 2]
out = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), d.get('arquivo', 'contrato') + '.pdf')
h = out[:-4] + '.html'; open(h, 'w', encoding='utf-8').write(s)
subprocess.run(['node', '-e', f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{h}');await p.pdf({{path:'{out}',format:'A4',printBackground:true}});await b.close()}})()"], check=True)
print(out)
