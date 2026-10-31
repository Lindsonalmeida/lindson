"""Plano C do acervo: baixa da Web Gallery of Art (wga.hu) a mesma obra quando o Commons bloqueia (429). python3 acervo_wga.py"""
import urllib.request,io,json,os,time,subprocess
from PIL import Image
OUT='/home/user/lindson/conteudo/youtube/raposa-e-leao/img/acervo'
L={'bernardo_bellotto_the_piazza_della_signoria_in_f.jpg':('/art/b/bellotto/1/bello103.jpg','Bernardo Bellotto, The Piazza della Signoria in Florence, 1740'),
'botticelli_giuliano_de_medici_accademia_carrara.jpg':('/art/b/botticel/7portrai/05medici.jpg',"Sandro Botticelli, Giuliano de' Medici, c. 1478"),
'sandro_botticelli_giuliano_de_medici_gem_ldegale.jpg':('/art/b/botticel/7portrai/07medici.jpg',"Sandro Botticelli, Giuliano de' Medici, c. 1478"),
'albrecht_altdorfer_schlacht_bei_issus_alte_pinak.jpg':('/art/a/altdorfe/1/5battle.jpg','Albrecht Altdorfer, The Battle of Alexander, 1529'),
'the_battle_of_alexander_at_issus_by_albrecht_alt.jpg':('/art/a/altdorfe/1/5battle1.jpg','Albrecht Altdorfer, The Battle of Alexander (detalhe), 1529'),
'castiglione_raffaello.jpg':('/art/r/raphael/5roma/3/01castig.jpg','Rafael, Retrato de Baldassare Castiglione, 1514-15'),
'leao_x_raffaello.jpg':('/art/r/raphael/5roma/5/09leo_x.jpg',"Rafael, Papa Leão X com os cardeais Giulio de' Medici e Luigi de' Rossi, 1518"),
'julio_ii_raffaello.jpg':('/art/r/raphael/5roma/1/09julius.jpg','Rafael, Retrato de Júlio II, 1511-12'),
'prisao_cristo_caravaggio.jpg':('/art/c/caravagg/03/191captu.jpg','Caravaggio, A Prisão de Cristo, c. 1602'),
'beijo_judas_giotto.jpg':('/art/g/giotto/padova/3christ/chris15.jpg','Giotto, Cenas da vida de Cristo: 15. A Prisão de Cristo (Beijo de Judas), Pádua'),
'embaixadores_holbein.jpg':('/art/h/holbein/hans_y/1535a/0ambassa.jpg','Hans Holbein, o Jovem, Os Embaixadores, 1533'),
'multidao_bruegel.jpg':('/art/b/bruegel/pieter_e/08/11calvar.jpg','Pieter Bruegel, o Velho, Cristo carregando a cruz, 1564'),
'batalha_ostia_raffaello.jpg':('/art/r/raphael/4stanze/3borgo/2battle.jpg','Rafael e oficina, A Batalha de Óstia, 1514-15, Vaticano'),
'batalha_ponte_milvio_raffaello.jpg':('/art/r/raphael/4stanze/4constan/2battle.jpg','Oficina de Rafael, A Batalha da Ponte Mílvia, 1520-24, Vaticano'),
}
cred=json.load(open(OUT+'/creditos.json')); por={c['arquivo']:c for c in cred}
for arq,(p,t) in L.items():
    for k in range(6):
        if os.path.exists(f'{OUT}/{arq}'): break
        tmp=f'/tmp/{arq}'
        r=subprocess.run(['curl','-sSfL','--retry','3','-m','300','-A','Mozilla/5.0','-o',tmp,'https://www.wga.hu'+p])
        try: Image.open(tmp).convert('RGB').save(f'{OUT}/{arq}',quality=93)
        except Exception as e: print('erro',arq,e,flush=True); time.sleep(10)
    if not os.path.exists(f'{OUT}/{arq}'): print('FALHOU',arq,flush=True); continue
    r=por.get(arq)
    if r is None: r={'arquivo':arq}; cred.append(r); por[arq]=r
    r.update(fonte_baixada='https://www.wga.hu'+p, obra=t, licenca_obra='domínio público (obra anterior a 1900; reprodução fiel de obra 2D)')
    r.setdefault('titulo',t)
    json.dump(cred,open(OUT+'/creditos.json','w'),ensure_ascii=False,indent=1)
    print('ok',arq,Image.open(f'{OUT}/{arq}').size,flush=True)
print('FIM')
