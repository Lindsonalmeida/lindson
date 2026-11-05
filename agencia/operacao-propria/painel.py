# Página "Assessoria para pizzarias" na Central (só o admin abre: fica em /painel/). Conta Leandro, 05/11/2026.
# Pedido do Lindson: "suba tudo no sistema". Junta os documentos da operação própria e da análise da franquia Alpha
# (Markdown do repositório, mostrado com marked) e a planilha de projeção para baixar.
# Uso: python3 painel.py <pasta painel de saída>   (o montar-site.py chama sozinho; ou direto no privado: python3 painel.py /home/user/centrallindsonalmeida/painel)
import sys, os, json, shutil
AQUI = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(AQUI, '..', 'ofertas', 'franquia-alpha')
DOCS = [  # (id, título no menu, grupo, arquivo)
    ('operacao', 'Plano da operação', 'Assessoria para pizzarias', os.path.join(AQUI, 'README.md')),
    ('precos', 'Preços dos planos', 'Assessoria para pizzarias', os.path.join(AQUI, 'PRECOS-PIZZARIAS.md')),
    ('pagamentos', 'Pagamento antecipado (MRR e TCV)', 'Assessoria para pizzarias', os.path.join(AQUI, 'PAGAMENTOS.md')),
    ('promessa', 'Promessa irresistível', 'Assessoria para pizzarias', os.path.join(AQUI, 'PROMESSA.md')),
    ('estrategia', 'Marketing, tráfego, vendas e Instagram', 'Assessoria para pizzarias', os.path.join(AQUI, 'ESTRATEGIA-MARKETING.md')),
    ('nome', 'Nome e perfil do Instagram', 'Assessoria para pizzarias', os.path.join(AQUI, 'NOME-E-PERFIL.md')),
    ('maquiavel', 'Análise do Maquiavel', 'Franquia Alpha (estudo)', os.path.join(FR, 'ANALISE-MAQUIAVEL.md')),
    ('planilha-alpha', 'A planilha deles, refeita', 'Franquia Alpha (estudo)', os.path.join(FR, 'ANALISE-PLANILHA.md')),
    ('modelo', 'O modelo do site deles', 'Franquia Alpha (estudo)', os.path.join(FR, 'MODELO-ALPHA.md')),
    ('planos-proprios', 'Planos próprios (1ª versão)', 'Franquia Alpha (estudo)', os.path.join(FR, 'PLANOS-PROPRIOS.md')),
]
def montar(painel):
    os.makedirs(os.path.join(painel, 'pizzarias'), exist_ok=True)
    shutil.copy(os.path.join(AQUI, 'PROJECAO-PROPRIA.xlsx'), os.path.join(painel, 'pizzarias', 'projecao-propria.xlsx'))
    docs = [{'id': i, 't': t, 'g': g, 'md': open(f).read()} for i, t, g, f in DOCS if os.path.exists(f)]
    dados = json.dumps(docs, ensure_ascii=False).replace('</', '<\\/')
    html = '''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Assessoria para pizzarias · Central</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<style>
:root{--fundo:#0A0A0A;--card:#141414;--linha:#262626;--texto:#EDEDED;--apagado:#9A9A9A;--amarelo:#F5C518}
*{box-sizing:border-box}body{margin:0;background:var(--fundo);color:var(--texto);font:15px/1.6 Inter,system-ui,sans-serif}
.lay{display:grid;grid-template-columns:290px 1fr;min-height:100vh}
aside{border-right:1px solid var(--linha);padding:22px 16px;position:sticky;top:0;height:100vh;overflow:auto}
aside h1{font-size:17px;margin:0 0 4px}aside p{color:var(--apagado);font-size:12.5px;margin:0 0 18px}
aside h4{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--apagado);margin:18px 8px 6px}
aside a{display:block;color:var(--texto);text-decoration:none;padding:9px 10px;border-radius:10px;font-size:14px}
aside a:hover{background:#1c1c1c}aside a[aria-current]{background:rgba(245,197,24,.12);color:var(--amarelo);font-weight:700}
.baixar{display:block;margin-top:18px;background:var(--amarelo);color:#0A0A0A!important;font-weight:800;text-align:center}
main{padding:34px clamp(18px,4vw,56px);max-width:1060px}
main h1{font-size:30px;line-height:1.15;margin:0 0 14px}main h2{font-size:22px;margin:34px 0 10px;color:var(--amarelo)}main h3{font-size:17px;margin:24px 0 8px}
main a{color:var(--amarelo)}main code{background:#1d1d1d;padding:1px 6px;border-radius:6px;font-size:.92em}
main pre{background:#141414;border:1px solid var(--linha);padding:14px;border-radius:12px;overflow:auto}
main blockquote{margin:14px 0;padding:10px 16px;border-left:3px solid var(--amarelo);background:#141414;border-radius:0 10px 10px 0}
main table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px;display:block;overflow-x:auto}
main th,main td{border:1px solid var(--linha);padding:8px 10px;text-align:left;vertical-align:top}main th{background:#181818}
.volta{position:fixed;left:12px;bottom:12px;background:var(--amarelo);color:#0A0A0A;font:700 13px system-ui;padding:9px 14px;border-radius:99px;text-decoration:none}
@media(max-width:800px){.lay{grid-template-columns:1fr}aside{position:static;height:auto;border-right:0;border-bottom:1px solid var(--linha)}}
</style></head><body><div class="lay"><aside><h1>Assessoria para pizzarias</h1><p>Operação própria · preços · pagamentos · promessa · marketing · nome. E o estudo da franquia Alpha.</p>
<nav id="menu"></nav><a class="baixar" href="/painel/pizzarias/projecao-propria.xlsx" download>Baixar a planilha de projeção (Excel)</a></aside><main id="doc"></main></div>
<a class="volta" href="/painel/admin">← Central</a>
<script>
const DOCS=''' + dados + ''';
const menu=document.getElementById('menu'),doc=document.getElementById('doc');let g='';
menu.innerHTML=DOCS.map(d=>{const h=d.g!==g?`<h4>${g=d.g}</h4>`:'';return h+`<a href="#${d.id}" data-id="${d.id}">${d.t}</a>`}).join('');
function mostra(){const id=(location.hash||'#'+DOCS[0].id).slice(1),d=DOCS.find(x=>x.id===id)||DOCS[0];
 doc.innerHTML=window.marked?marked.parse(d.md):'<pre>'+d.md.replace(/[&<]/g,c=>c==='&'?'&amp;':'&lt;')+'</pre>';
 menu.querySelectorAll('a').forEach(a=>a.toggleAttribute('aria-current',a.dataset.id===d.id));scrollTo(0,0)}
addEventListener('hashchange',mostra);mostra();
</script></body></html>'''
    open(os.path.join(painel, 'pizzarias.html'), 'w').write(html)
    return len(docs)
if __name__ == '__main__':
    print('pizzarias.html', montar(sys.argv[1]), 'documentos')
