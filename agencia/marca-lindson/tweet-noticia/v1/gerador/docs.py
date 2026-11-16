import json
from PIL import Image
exec(open('conteudo.py').read()); meta=json.load(open('meta.json'))
V='/home/user/lindson/agencia/marca-lindson/tweet-noticia/v1'
NOMES={'marketing-ia':'Marketing e IA','negocios':'Negócios','sao-luis':'São Luís','assessor-politico':'Assessor político','grupo-tecnologia':'Dono de grupo de tecnologia (Al Kántara)','agencia-design':'Dono de agência de design'}
TAGS={'marketing-ia':[['#marketingdigital','#inteligenciaartificial','#metaads','#instagramparanegocios','#saoluisma'],['#whatsappbusiness','#atendimentoaocliente','#iaparanegocios','#pequenonegocio','#maranhao'],['#chatgpt','#lojavirtual','#modafeminina','#vendasonline','#saoluis'],['#googleads','#gemini','#trafegopago','#negociolocal','#slz']],
'negocios':[['#blackfriday','#margemdelucro','#pequenasempresas','#empreendedorismo','#saoluisma'],['#varejodigital','#ecommerce','#iaparavendas','#donodenegocio','#maranhao'],['#chatgpt','#presencadigital','#instagramquevende','#comercio','#saoluis'],['#mei','#sebrae','#vendaspelowhatsapp','#gestaofinanceira','#nordeste']],
'sao-luis':[['#saoluis','#comerciodesaoluis','#fimdeano','#empregos','#maranhao'],['#turismomaranhao','#saoluisma','#restaurantesemsaoluis','#hotelaria','#tap'],['#afroturismo','#quilombourbano','#culturamaranhense','#saoluis','#economiacriativa'],['#feiradoempreendedor','#sebraema','#empreendedorismo','#saoluisma','#negocioslocais']],
'assessor-politico':[['#comunicacaopolitica','#marketingpolitico','#deepfake','#assessoria','#maranhao'],['#tse','#eleicoes2026','#propagandaeleitoral','#iaresponsavel','#mandato'],['#bastidoresdacampanha','#comunicacaopublica','#ia','#marketingpolitico','#saoluis'],['#tse','#gestaodemandato','#comunicacaodigital','#assessorpolitico','#nordeste']],
'grupo-tecnologia':[['#inteligenciaartificial','#fusoeseaquisicoes','#holding','#startups','#tecnologia'],['#datacenter','#holdingdetecnologia','#crescimento','#negocios','#maranhao'],['#acquihire','#startupsbrasil','#talentos','#tecnologia','#lideranca'],['#ma','#ia','#holding','#venturecapital','#empreendedorismodigital']],
'agencia-design':[['#rebranding','#branding','#creatoreconomy','#agencia','#designer'],['#identidadevisual','#designnordestino','#posicionamento','#agenciadedesign','#saoluis'],['#redesign','#marca','#designgrafico','#agenciadecomunicacao','#maranhao'],['#branding','#agenciaintegrada','#posicionamentodemarca','#design','#saoluisma']]}
cnt={};leg=['# Legendas · Tweet + notícia v1 (conta Leandro, 16/11/2026)\n']
fon=[];capas=[]
for c in C:
  l,k,veic,data,tit,tw,lic=c; cnt[l]=cnt.get(l,0)+1; n=cnt[l]
  intro=tw[0].replace('🚨 ','').replace('BOMBA: ','')
  L=f"""## {NOMES[l]} {n:02d} · {tit}

{tit.upper()}!

{intro} {tw[1]}

**O que aconteceu**
{tw[2]} Fonte: {veic}, {data}.

**O que isso muda para o seu negócio**
{tw[3]} {lic}

**Exemplo prático**
Antes de qualquer ferramenta nova, abra seu perfil como se fosse um cliente: a bio diz o que você faz? Tem foto real? Tem um jeito fácil de chamar?

**Conclusão**
A notícia passa. O que fica é quem estava preparado quando o cliente procurou.

Quer um Instagram que trabalhe por você? Me chama no direct com a palavra PROPOSTA.

{' '.join(TAGS[l][n-1])}
"""
  assert len(L)<2200,(l,n,len(L)); leg.append(L)
  fon.append(f'| {NOMES[l]} {n:02d} | {tit} | {veic} · {data} · {meta[k]["url"]} |')
  capas.append(f'{V}/{l}/{n:02d}/01.png')
open(V+'/LEGENDAS.md','w').write('\n'.join(leg))
cols=6;W=270;H=338
g=Image.new('RGB',(cols*W+(cols+1)*10,4*H+5*10),'#222')
for i,p in enumerate(capas):
  im=Image.open(p).convert('RGB').resize((W,H)); g.paste(im,(10+(i%cols)*(W+10),10+(i//cols)*(H+10)))
g.save(V+'/previa-grade.jpg',quality=88)
open('fontes.md','w').write('\n'.join(fon))
