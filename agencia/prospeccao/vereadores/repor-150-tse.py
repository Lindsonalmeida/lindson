# Repõe a fila do SDR com N vereadores novos (padrão 150/dia, regra do Lindson 28/11/2026) a partir dos DADOS ABERTOS do TSE 2024:
# WhatsApp e Instagram declarados no registro de candidatura. Só eleitos e suplentes, celular válido, sem repetir wa/ig/id da base.
# Prioridade: MA → Nordeste → resto do Brasil; mandato antes de suplente. Uso: python3 repor-150-tse.py [/caminho/central] [N]
import csv,re,json,glob,os,sys,subprocess,collections
C=sys.argv[1] if len(sys.argv)>1 else '/home/user/centrallindsonalmeida'; N=int(sys.argv[2]) if len(sys.argv)>2 else 150
T='/tmp/tse2024'; os.makedirs(T,exist_ok=True)
for z,u in [('cc.zip','consulta_cand/consulta_cand_2024.zip'),('rs.zip','consulta_cand/rede_social_candidato_2024.zip')]:
  if not os.path.exists(f'{T}/{z}'): subprocess.run(['curl','-s','-m','600','-o',f'{T}/{z}','https://cdn.tse.jus.br/estatistica/sead/odsele/'+u],check=True)
subprocess.run(f'cd {T} && unzip -o -q rs.zip && unzip -o -q cc.zip consulta_cand_2024_BRASIL.csv',shell=True,check=True)
rd=lambda f:csv.DictReader(open(f,encoding='latin1'),delimiter=';')
red=collections.defaultdict(list)
for f in glob.glob(f'{T}/rede_social_candidato_2024_*.csv'):
  for r in rd(f): red[r['SQ_CANDIDATO']].append(r['DS_URL'].strip())
p=f'{C}/functions/_sdr.js'; s=open(p).read()
base=[json.loads(m) for m in re.findall(r'^(\{"id".*\}),?$',s,re.M)]
waB={re.sub(r'\D','',c.get('wa',''))[-8:] for c in base}; igB={c.get('ig','').lower() for c in base}|{c['id'].lower() for c in base}
REG={**{u:'NORDESTE' for u in 'MA PI CE RN PB PE AL SE BA'.split()},**{u:'NORTE' for u in 'AC AM AP PA RO RR TO'.split()},**{u:'CENTROOESTE' for u in 'GO MT MS DF'.split()},**{u:'SUDESTE' for u in 'SP RJ MG ES'.split()},**{u:'SUL' for u in 'PR SC RS'.split()}}
out=[];seen=set()
for c in rd(f'{T}/consulta_cand_2024_BRASIL.csv'):
  if c['DS_CARGO']!='VEREADOR' or c['SG_UF'] not in REG: continue
  sit=c['DS_SIT_TOT_TURNO']
  if not (sit.startswith('ELEITO') or sit=='SUPLENTE'): continue
  wa=ig=None
  for u in red.get(c['SQ_CANDIDATO'],[]):
    if 'wa.me/' in u: 
      d=re.sub(r'\D','',u.split('wa.me/')[-1].split('?')[0]); d=d[2:] if d.startswith('55') else d
      if re.fullmatch(r'[1-9]\d9\d{8}',d): wa='55'+d
    mi=re.search(r'instagram\.com/([A-Za-z0-9_.]+)',u)
    if mi and mi.group(1).lower() not in ('p','reel','accounts','stories','explore'): ig=mi.group(1).rstrip('.')
  if not(wa and ig) or wa[-8:] in waB or ig.lower() in igB or wa in seen: continue
  seen.add(wa); out.append(c|{'wa':wa,'ig':ig,'tag':'mandato' if sit.startswith('ELEITO') else 'suplente'})
out.sort(key=lambda o:(o['SG_UF']!='MA',REG[o['SG_UF']]!='NORDESTE',o['tag']!='mandato'))
tit=lambda x:' '.join(w if w in('da','de','do','das','dos','e') else w.capitalize() for w in x.lower().split())
ids=set(re.findall(r'"id":"([^"]+)"',s)); L=[]
for o in out[:N]:
  f=o.get('DS_GENERO')=='FEMININO'; nome=tit(o['NM_URNA_CANDIDATO'])
  nm=(('Vereadora ' if f else 'Vereador ') if o['tag']=='mandato' else ('Suplente de vereadora ' if f else 'Suplente de vereador '))+nome
  i=re.sub(r'[^a-z0-9_.]','',o['ig'].lower()) or o['SQ_CANDIDATO']
  if i in ids: i+='_'+o['SQ_CANDIDATO'][-4:]
  ids.add(i)
  L.append(json.dumps({"id":i,"nome":nm,"ig":o['ig'],"wa":o['wa'],"nicho":"vereador","cidade":f"{tit(o['NM_UE'])}/{o['SG_UF']}","nota":100 if o['tag']=='mandato' else 85,"tag":o['tag'],
   "motivo":f"{'Eleito' if o['tag']=='mandato' else 'Suplente'} 2024 ({o['SG_PARTIDO']}), TSE; WhatsApp e Instagram declarados no registro de candidatura (TSE dados abertos)","msg":"",
   "fonte":f"https://divulgacandcontas.tse.jus.br/divulga/#/candidato/{REG[o['SG_UF']]}/{o['SG_UF']}/2045202024/{o['SQ_CANDIDATO']}/2024/{o['SG_UE']}"},ensure_ascii=False,separators=(',',':'))+',')
if L: open(p,'w').write(s.replace('\n];','\n'+'\n'.join(L)+'\n];',1))
print(f'{len(L)} novos; restam {max(0,len(out)-N)} na reserva do TSE;', collections.Counter(o['SG_UF'] for o in out[:N]).most_common(8))
