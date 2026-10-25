"""Raposa e Leão — python3 short.py <pasta>  (pasta com voz.wav, palavras.json e cenas.json)"""
import json,sys,os,re,unicodedata,subprocess
P=os.path.abspath(sys.argv[1]);D=os.path.dirname(os.path.abspath(__file__))
W=json.load(open(P+'/palavras.json'));C=json.load(open(P+'/cenas.json'))
norm=lambda s:re.sub(r'[^\w]','',unicodedata.normalize('NFC',s.lower()))
def idx(ref):
    w,n=(ref.split('#')+['1'])[:2];n=int(n);k=0
    for i,(x,_) in enumerate(W):
        if norm(x)==norm(w):
            k+=1
            if k==n:return i
    raise SystemExit(f'palavra não encontrada: {ref}')
tm=lambda ref:W[idx(ref)][1]
cs=C['cenas']
for c in cs:
    c['ini']=0 if c is cs[0] else (tm(c['apos'])+.8 if 'apos' in c else tm(c['w'])-.15)
    for it in c.get('items',[]):
        it['at']=tm(it['w']) if 'w' in it else c['ini']+.1+it.get('d',0)
        if 'riscar' in it:it['riscar']=tm(it['riscar'])+.45
        if c['t']=='stack' and not c.get('bg','').startswith('foto'):it['y']+=110
    for k in 'ab':
        if k in c:c[k]['at']=tm(c[k]['w']) if 'w' in c[k] else c['ini']+.1
    if 'meio' in c:c['meioAt']=tm(c['meioW'])
    if c['t']=='pagina':
        a,b=idx(c['de']),idx(c['ate']);c['ws']=W[a:b+1];c['hl']=[i-a for i in map(idx,c.get('hl',[]))]
    if c['t']=='orbita':c['bom']=tm(c['bom']);c['mau']=tm(c['mau'])
    if c['t']=='emb':c['fox']=tm(c['fox']);c['lion']=tm(c['lion'])
total=round(max(W[-1][1]+2.6,cs[-1]['ini']+3.2),2)
for i,c in enumerate(cs):c['fim']=cs[i+1]['ini'] if i+1<len(cs) else total+1
json.dump({'cenas':cs,'total':total,'tom':C.get('tom',73.42)},open(P+'/spec.json','w'),ensure_ascii=False)
subprocess.run([sys.executable,D+'/build.py','cenas.html',P],check=True)
