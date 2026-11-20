"""Põe a aba Tarefas feitas (feitas.js), a pasta Postados (postados.js, 15/11/2026) e a Biblioteca (../painel-biblioteca/biblioteca.js, 20/11/2026) em todos os painéis de cliente de uma pasta painel/ (idempotente). Conta Zuleide, 15/11/2026.
  python3 injetar.py <pasta painel>   (montar-site.py chama sozinho para publico/painel)"""
import os, shutil, sys
TAG = '<script src="/painel/feitas.js"></script>'
TAG2 = '<script src="/painel/postados.js"></script>'
def injetar(pasta, _de_novo=False):
    for js in ('feitas.js', 'postados.js'): shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), js), os.path.join(pasta, js))
    feitos = []
    for f in sorted(os.listdir(pasta)):
        p = os.path.join(pasta, f)
        if not f.endswith('.html') or f in ('admin.html', 'comando.html'): continue
        s = open(p).read()
        if 'id="menu"' not in s: continue
        if TAG in s:  # já tem feitas: só garante o postados (painel com aba de conteúdos) e o window.__T
            n = s
            if 'window.__T' not in n and 'window.__V = V;' in n: n = n.replace('window.__V = V;', 'window.__V = V; window.__T = T;', 1)
            if TAG2 not in n and any(k in n for k in ('data-v="aprovacoes"', 'data-v="aprovar"', 'data-v="postagens"')): n = n.replace(TAG, TAG + '\n' + TAG2, 1)
            if n != s: open(p, 'w').write(n); feitos.append(f)
            continue
        if 'window.__V' not in s:  # painel antigo (ex.: tribuna): expõe V, T e render para o feitas.js
            if 'const V = {' not in s or 'const T = {' not in s or 'function render() {' not in s: continue
            s = s.replace('const V = {', 'const V = window.__V = {', 1).replace('const T = {', 'const T = window.__T = {', 1).replace("addEventListener('hashchange', render);", "window.__render = render; addEventListener('hashchange', render);", 1)
        tags = TAG + ('\n' + TAG2 if any(k in s for k in ('data-v="aprovacoes"', 'data-v="aprovar"', 'data-v="postagens"')) else '')
        i = s.rfind('</body>'); s = s[:i] + tags + '\n' + s[i:] if i > -1 else s + '\n' + TAG + '\n'
        open(p, 'w').write(s); feitos.append(f)
    if feitos and not _de_novo: injetar(pasta, True)  # 2ª passada: painel recém-montado às vezes só ganha o postados.js na segunda (visto na Mova, 20/11/2026)
    return feitos + biblioteca(pasta)

def biblioteca(pasta):
    """Menu lateral "Biblioteca" em todo painel de cliente (pedido do Lindson, 20/11/2026; Builder Squad, conta Lindson).
    O manifesto de cada cliente sai do ../painel-biblioteca/gerar_biblioteca.py (painel/<cliente>/biblioteca/manifesto.js)."""
    js = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'painel-biblioteca', 'biblioteca.js')
    if not os.path.exists(js): return []
    shutil.copy(js, os.path.join(pasta, 'biblioteca.js')); feitos = []
    for f in sorted(os.listdir(pasta)):
        p = os.path.join(pasta, f)
        if not f.endswith('.html') or f in ('admin.html', 'comando.html'): continue
        s = open(p).read()
        if 'id="menu"' not in s or 'window.__V' not in s or '/painel/biblioteca.js' in s: continue
        tag = f'<script src="/painel/biblioteca.js" data-cli="{f[:-5]}"></script>'
        i = s.rfind('</body>'); s = s[:i] + tag + '\n' + s[i:] if i > -1 else s + '\n' + tag + '\n'
        open(p, 'w').write(s); feitos.append(f + ' (biblioteca)')
    return feitos
if __name__ == '__main__': print(injetar(sys.argv[1]))
