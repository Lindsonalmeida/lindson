"""Monta o site publicável da Central do Cliente em site/publico/ (Cloudflare Pages + Functions). Conta Lindson, 01/11/2026.
  python3 montar-site.py
Um sistema só: cria a conta uma vez (nome, e-mail, senha e código), depois entra com e-mail e senha e cai no próprio painel; o admin vê todos.
Gera: publico/index.html (tela de acesso), publico/painel/{admin,contas,jaci,leo}.html, publico/_headers.
Antes, gere os painéis: python3 ../jaci-cunha/montar-jaci.py e python3 ../leo-pinto/montar-leo.py.
O acesso é conferido no servidor (functions/). Os códigos ficam só nas variáveis da Cloudflare (ver README)."""
import base64, os, re, shutil
D = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(D, '..'); OUT = os.path.join(D, 'publico')
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(os.path.join(OUT, 'painel'))
webp = lambda p: 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
FOTOS = os.path.join(SC, 'fotos')

def troca(s, velho, novo):
    assert velho in s, 'mudou, ajuste: ' + velho[:70]
    return s.replace(velho, novo, 1)

SAIR = '<a href="/sair" style="font:600 12px var(--f-corpo);color:var(--apagado);text-decoration:none;border:1px solid var(--linha);border-radius:99px;padding:6px 12px">Sair</a>'
def com_sair(s):
    return troca(s, '<span class="exemplo">Dados de exemplo</span>', '<span class="exemplo">Dados de exemplo</span>' + SAIR)

# 1 · tela de acesso: o login aprovado (prototipo/login.html), agora com e-mail + código conferido no servidor
s = open(os.path.join(SC, 'prototipo', 'login.html')).read()
for k in ['rafael', 'sf', 'passaporte', 'raposa']:
    p = os.path.join(FOTOS, 'casos', k + '.webp')
    if os.path.exists(p): s = s.replace(f'__{k.upper()}__', webp(p))
    for i in range(1, 5):
        p = os.path.join(FOTOS, 'casos', f'{k}-{i}.webp')
        if os.path.exists(p): s = s.replace(f'__{k.upper()}{i}__', webp(p))
for k, f in [('CINE', 'principal-cine.webp'), ('PROF', 'principal-prof.webp')]:
    p = os.path.join(FOTOS, f)
    s = s.replace(f'__{k}__', webp(p)) if os.path.exists(p) else re.sub(rf'<img id="foto\w+" src="__{k}__"[^>]*>', '', s)
s = troca(s, '<p class="sub">Primeira vez aqui? Crie sua conta com o código de acesso que você recebeu da nossa equipe.</p>',
          '<p class="sub">Primeira vez aqui? Crie sua conta com o código de acesso que você recebeu da nossa equipe. Depois é só entrar com e-mail e senha.</p>')
s = re.sub(r"const PAINEIS=\{.*?\};\n", '', s, count=1, flags=re.S)
s = re.sub(r"async function resumo\(t\)\{.*?\}\n", '', s, count=1)
novo = """f.addEventListener('submit',async e=>{e.preventDefault();av.className='aviso';const email=document.getElementById('usuario').value.trim();
 let rota='/api/entrar',corpo={email,senha:se.value};
 if(modo==='entrar'){if(!email||!se.value){av.textContent='Preencha o e-mail e a senha para entrar.';return}}
 else{const nome=document.getElementById('nome').value.trim();
  if(!nome||!email||!se.value||!cod.value){av.textContent='Preencha nome, e-mail, senha e código de acesso.';return}
  if(se.value.length<8){av.textContent='Use uma senha com pelo menos 8 caracteres.';return}
  rota='/api/criar';corpo={nome,email,senha:se.value,codigo:cod.value}}
 btn.disabled=true;av.textContent=modo==='entrar'?'Conferindo…':'Criando a sua conta…';
 try{const r=await fetch(rota,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(corpo)});const j=await r.json().catch(()=>({}));
  if(r.ok&&j.destino){av.className='aviso ok';av.textContent='Tudo certo. Abrindo o seu painel…';location.href=j.destino;return}
  av.textContent=j.erro||'Não consegui entrar agora. Tente de novo.'}catch(err){av.textContent='Sem conexão com a Central. Tente de novo.'}
 btn.disabled=false});
document.getElementById('esqueci').addEventListener('click',e=>{e.preventDefault();av.textContent='Esqueceu a senha? Fale com a nossa equipe pelo WhatsApp: a gente libera para você criar a conta de novo.'});"""
s = re.sub(r"f\.addEventListener\('submit',async e=>\{.*?\n(?=\}\)\(\);)", novo + '\n', s, count=1, flags=re.S)
s = troca(s, 'const ok=i=>i.complete&&', 'if(!im||!dp)return;const ok=i=>i.complete&&')  # sem a foto do Lindson, o efeito 3D não roda
assert '/api/entrar' in s and '/api/criar' in s and 'PAINEIS' not in s and 'resumo(' not in s
open(os.path.join(OUT, 'index.html'), 'w').write(s)

# 2 · painéis dos clientes (gerados pelos scripts de cada cliente) com o botão Sair
for cli, arq in [('jaci', os.path.join(SC, 'jaci-cunha', 'painel-jaci.html')), ('leo', os.path.join(SC, 'leo-pinto', 'painel-leo.html'))]:
    open(os.path.join(OUT, 'painel', cli + '.html'), 'w').write(com_sair(open(arq).read()))

# 3 · painel do administrador (Lindson): resumo com os números reais de cada cliente (dados do repositório privado)
import json
DADOS = os.environ.get('CENTRAL_DADOS', os.path.join(D, '..', '..', '..', '..', 'centrallindsonalmeida', 'dados'))
clientes = [json.load(open(os.path.join(DADOS, c + '.json'))) for c in ['jaci', 'leo'] if os.path.exists(os.path.join(DADOS, c + '.json'))]
resumo = [{k: c.get(k) for k in ['cliente', 'nome', 'seg', 'atualizado', 'instagram']} for c in clientes]
for r in resumo:
    if r.get('instagram'): r['instagram'] = {k: r['instagram'].get(k) for k in ['perfil', 'data', 'periodo', 'seguidores', 'visualizacoes', 'var_seguidores', 'var_visualizacoes']}
a = open(os.path.join(D, 'admin.html')).read().replace('__CLIENTES__', json.dumps(resumo, ensure_ascii=False).replace('</', '<\\/'))
open(os.path.join(OUT, 'painel', 'admin.html'), 'w').write(a)
shutil.copy(os.path.join(D, 'contas.html'), os.path.join(OUT, 'painel', 'contas.html'))
open(os.path.join(OUT, '_headers'), 'w').write("/*\n  X-Frame-Options: DENY\n  Referrer-Policy: same-origin\n  X-Content-Type-Options: nosniff\n/painel/*\n  Cache-Control: private, no-store\n  X-Robots-Tag: noindex\n")
open(os.path.join(OUT, 'robots.txt'), 'w').write("User-agent: *\nDisallow: /\n")
for r, _, fs in os.walk(OUT):
    for f in fs: print(os.path.relpath(os.path.join(r, f), OUT), os.path.getsize(os.path.join(r, f)) // 1024, 'KB')
