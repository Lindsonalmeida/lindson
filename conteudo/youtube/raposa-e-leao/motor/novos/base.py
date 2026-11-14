"""Base dos roteiros dos longos 17-21 (conta Leandro, 14/11/2026). Cada lN.py define SEG e chama salvar()."""
import json,os
D=os.path.dirname(os.path.abspath(__file__));L=os.path.join(D,'..','..','longos')
def ab(h,s,img,txt):return {'tela':{'t':'abertura','h':h,'s':s,'img':img},'txt':txt}
def fr(h,txt):return {'tela':{'t':'frase','h':h},'txt':txt}
def cap(n,h,s,txt):return {'tela':{'t':'capitulo','n':str(n),'h':h,'s':s},'txt':txt}
def cit(h,s,txt):return {'tela':{'t':'citacao','h':h,'s':s},'txt':txt}
def im(img,h,s,txt):return {'tela':{'t':'imagem','img':img,'h':h,'s':s},'txt':txt}
def duo(a,as_,b,bs,txt):return {'tela':{'t':'duo','a':a,'as':as_,'b':b,'bs':bs},'txt':txt}
def pr(itens,txt,h='Na prática'):return {'tela':{'t':'pratica','h':h,'itens':itens},'txt':txt}
def li(h,itens,txt):return {'tela':{'t':'lista','h':h,'itens':itens},'txt':txt}
def cv(tipo,h,x,img,txt):return {'tela':{'t':'conversa','tipo':tipo,'h':h,'x':x,'img':'../img/'+img},'txt':txt}
def ins(tag,s,txt):return {'tela':{'t':'inscreva','tag':tag,'s':s},'txt':txt}
def comp(h,d,txt):return {'tela':{'t':'compromisso','h':h,'digita':d},'txt':txt}
def res(itens,txt):return {'tela':{'t':'resumo','itens':itens},'txt':txt}
def fim(txt):return {'tela':{'t':'fim'},'txt':txt}
def salvar(n,titulo,seg):
    p=os.path.join(L,n);os.makedirs(p,exist_ok=True)
    json.dump({'titulo':titulo,'seg':seg},open(p+'/roteiro.json','w'),ensure_ascii=False,indent=1)
    w=sum(len(s['txt'].split()) for s in seg);print(n,titulo,len(seg),'segmentos',w,'palavras',round(w/150,1),'min')
