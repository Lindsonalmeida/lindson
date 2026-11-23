# Calendário v2: 60 Reels (2/dia), gancho A/B, reaproveitamento em Shorts e TikTok (conta Leandro, 23/11/2026)
import json, datetime, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
v1=json.load(open('../calendario.json'))
B={'Topo':['Quanto sobra da sua pizza?','O cliente é seu. A taxa, não.','Ninguém acha seu link','A massa que vira prejuízo','Fim de semana não salva o mês','Story sem preço, cliente sem pedido','Seu queijo não estica na foto','Atrasou 20 min. Perdeu o cliente.','Por que seu post não aparece?','O desconto que te empobrece','Responder ou apagar a 1 estrela?','Se você parar, a pizzaria para?','O sabor que todo mundo pede','Abrir no feriado vale a pena?','Seguidor não paga boleto','Ele só pede no sábado?','O Natal vai passar sem você?','A caixa que ninguém lê','Sabor campeão, lucro zero?','Sexta 21h e o WhatsApp explodiu','Promoção que ensina a esperar','O que a melhor do mundo posta'],
'Meio':['Luz do teto mata a pizza','Não baixe o preço. Responda assim.','Abrimos um perfil ao vivo','Legenda de 3 linhas que vende','A lista que salva a terça','Seu Google está vazio','Uma hora, dez vídeos','A ordem do cardápio vende','A pergunta da borda','De cima ou de lado?','Esse pedido veio do Reels?','5 cenas do seu forno','5 minutos para responder','Destaques na ordem certa','A conta que ninguém faz','A primeira mensagem do WhatsApp','Antes e depois (exemplo)','Anúncio só pro seu bairro','A segunda-feira do dono','Grave isso no balcão hoje'],
'Fundo':['Nota do seu Instagram em 2 minutos','Pedido direto, sem taxa do app','Só pizzaria. Por quê?','O número na mesa toda segunda','Seu perfil tira nota quanto?','Já se decepcionou com agência?','Você não precisa gravar sozinho','O Raio-X em vídeo, por dentro','3 pizzarias fundadoras','Impulsionar sem Raio-X é chute','Planos a partir de… sem enrolar','Raio-X de um perfil de exemplo','Seu primeiro mês com a gente','O Raio-X que vira desconto','A taxa que você já paga','Quem a gente não atende','Uma mensagem e seu Raio-X','O que a fundadora dá em troca']}
sel={'Topo':[x for x in v1 if x['etapa']=='Topo'][:22],'Meio':[x for x in v1 if x['etapa']=='Meio'][:20],'Fundo':[x for x in v1 if x['etapa']=='Fundo'][:18]}
for e in sel:
    for x,b in zip(sel[e],B[e]): x['gancho_b']=b
for x in sel['Fundo']:
    if x['cta']=='Comenta FUNDADORA' and 'Só 5' in x['gancho']: x['gancho']='Só 3 pizzarias fundadoras'
    if 'Raio-X grátis' in x['tema']: x['tema']=x['tema'].replace('Raio-X grátis','Raio-X automático (nota + 3 ajustes)')
it={k:iter(v) for k,v in sel.items()}
ini=datetime.date(2026,11,26);out=[];n=31
for d in range(30):
    a=next(it['Topo'] if d%2==0 else it['Meio'],None) or next(it['Meio'],None) or next(it['Topo'])
    b=next(it['Fundo']) if d%5 in (0,2,4) else (next(it['Meio'],None) or next(it['Topo']))
    for x,h in ((a,'12:10'),(b,'20:10')):
        x=dict(x);x.update(id=f'OT-{n}',data=(ini+datetime.timedelta(d)).strftime('%d/%m'),hora=h);n+=1;out.append(x)
c={e:sum(1 for x in out if x['etapa']==e) for e in sel}
json.dump(out,open('calendario-v2.json','w'),ensure_ascii=False,indent=1)
L=['# Calendário v2 · 30 dias · 60 Reels · Orégano Turbo (26/11 a 25/12/2026)','','> **v2 (23/11/2026, conta Leandro), melhorias pedidas pelo Lindson.** Substitui `../CALENDARIO-30-DIAS.md` (v1, 90 Reels, agora ANTERIOR).','',
f"**Conta:** Topo {c['Topo']} · Meio {c['Meio']} · Fundo {c['Fundo']} → conteúdo {c['Topo']+c['Meio']} (70%) e venda {c['Fundo']} (30%). 2 Reels/dia de alta qualidade, 12:10 e 20:10 (dentro da janela 8h-21h).",'',
'**Reaproveitamento:** cada Reel sai também como **YouTube Shorts** (título com palavra-chave, mesmo dia +2 h) e **TikTok** (mesmo dia +4 h, legenda curta, sem marca d\'água do Instagram). Mesma identidade nos 3 canais.','',
'**Gancho A/B:** o A sai no Instagram; o B sai no TikTok/Shorts no mesmo dia (teste natural, sem gastar post). Segunda-feira compara retenção aos 3 s e compartilhamentos; o vencedor vira o padrão do tema (ver `FUNIL-v2.md`, seção 5).','',
'Visual: Seu Turbo (mascote) · Pizza real = vídeo real (nunca foto parada com zoom) · Tela real = gravação de celular (nunca card de UI falso).','',
'| Nº | Data | Hora | Etapa | Tema | Gancho A (Instagram) | Gancho B (TikTok/Shorts) | Visual | CTA |','|---|---|---|---|---|---|---|---|---|']
for o in out: L.append(f"| {o['id']} | {o['data']} | {o['hora']} | {o['etapa']} | {o['tema']} | {o['gancho']} | {o['gancho_b']} | {o['visual']} | {o['cta']} |")
L+=['','Stories diários e 3 fixados: iguais à v1 (`../CALENDARIO-30-DIAS.md`), com a figurinha de link apontando para o Raio-X automático.']
open('CALENDARIO-30-DIAS-v2.md','w').write('\n'.join(L)+'\n');print(c,len(out))
