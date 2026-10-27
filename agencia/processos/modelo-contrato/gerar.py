# Gera contrato de marketing digital (padrão Jaci Cunha / Apple Black): python3 gerar.py agencia/contratos/<cliente>/dados.json
# Dados da contratada (Lindson/Alkantara): agencia/contratos/meus-dados.json (fora do GitHub)
import json, sys, os, subprocess, html
E_ = html.escape
d = json.load(open(sys.argv[1], encoding='utf-8'))
me = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'contratos', 'meus-dados.json'), encoding='utf-8'))
C = d['contratante']  # nome, qualificacao, email, whats, assinatura[]
n = [0]
def cl(titulo, itens):
    n[0] += 1; k = n[0]
    corpo, j = '', 0
    for t in itens:
        if isinstance(t, list): corpo += '<ul>' + ''.join(f'<li>{x}</li>' for x in t) + '</ul>'
        else: j += 1; corpo += f'<p>{k}.{j}. {t}</p>'
    return f'<h2>CLÁUSULA {k}ª — {titulo}</h2>{corpo}'
def letras(lst): return ['<b>' + chr(97+i) + ')</b> ' + x for i, x in enumerate(lst)]
v = d['valor']; venc = d['vencimento_dia']; ini, fim = d['inicio'], d['fim']; meses = d.get('meses', 3)
partes = []
partes.append(cl('DO OBJETO', [f"O presente contrato tem por objeto a prestação, pela CONTRATADA, de serviços de {E_(d['objeto'])} para a CONTRATANTE, na modalidade {E_(d['plano'])}, conforme descrito na Cláusula 2ª."]))
inc = [f"O {E_(d['plano'])} compreende, mensalmente:", letras(d['incluido'])]
if d.get('sem_numero_fixo', True): inc.append('A quantidade e o formato dos conteúdos (posts, stories, reels, vídeos e carrosséis) serão definidos mensalmente pela CONTRATADA conforme a estratégia, não havendo número fixo de publicações. O calendário editorial de cada mês será apresentado à CONTRATANTE antes do início da execução.')
inc += ['Não estão incluídos no valor deste contrato, podendo ser contratados à parte mediante orçamento:', letras(d['nao_incluido'])]
partes.append(cl('DO QUE ESTÁ INCLUÍDO', inc))
if d.get('gravacoes'): partes.append(cl('DAS GRAVAÇÕES', d['gravacoes']))
apr = [f"Todo conteúdo será enviado previamente à CONTRATANTE para aprovação pelo WhatsApp oficial indicado neste contrato, que também será o canal oficial para avisos e comunicações operacionais.",
       "A CONTRATANTE terá prazo de até 48 (quarenta e oito) horas para aprovar ou solicitar ajustes. Cada conteúdo contempla até 2 (duas) rodadas de ajustes.",
       "A ausência de retorno no prazo acima poderá acarretar o adiamento ou o cancelamento da publicação, sem que isso configure descumprimento contratual por parte da CONTRATADA. Conteúdos não aprovados dentro do mês não são acumulados para os meses seguintes e não geram desconto no valor mensal."]
if d.get('responsabilidade_tecnica'): apr.append(d['responsabilidade_tecnica'])
partes.append(cl('DA APROVAÇÃO DOS CONTEÚDOS', apr))
vt = f"Pela prestação dos serviços, a CONTRATANTE pagará à CONTRATADA o valor mensal de <b>{v}</b> em todos os meses de vigência deste contrato"
if d.get('tabela'): vt += f", já aplicado desconto especial sobre o valor de tabela do {E_(d['plano'])}, conforme abaixo:<table><tr><td>Valor de tabela do {E_(d['plano'])} (mensal)</td><td>{d['tabela']}</td></tr><tr><td>Desconto especial concedido</td><td>− {d['desconto']}</td></tr><tr><td><b>Valor mensal a ser pago</b></td><td><b>{v.split(' (')[0]}</b></td></tr></table>"
else: vt += '.'
partes.append(cl('DO VALOR E DA FORMA DE PAGAMENTO', [vt,
  f"O pagamento é antecipado (pré-pago): cada mensalidade deve ser paga antes do início do mês de serviço a que se refere. A primeira mensalidade vence em {ini} e as demais no dia {venc} dos meses seguintes, via PIX ou boleto bancário, conforme os dados enviados pela CONTRATADA, sendo a cobrança encaminhada ao e-mail {E_(C['email'])}.",
  "A execução dos serviços de cada mês somente terá início após a confirmação do pagamento da respectiva mensalidade.",
  "O atraso no pagamento acarretará multa de 2% (dois por cento) sobre o valor devido, acrescida de juros de 1% (um por cento) ao mês, pro rata die. Atraso superior a 15 (quinze) dias autoriza a CONTRATADA a suspender os serviços até a regularização, sem prejuízo da cobrança dos valores devidos."]))
partes.append(cl('DA VIGÊNCIA', [f"O presente contrato vigorará pelo prazo de {meses} ({ {3:'três',6:'seis',12:'doze'}.get(meses,str(meses)) }) meses, com início em {ini} e término em {fim}, sendo renovado automaticamente por iguais períodos caso nenhuma das partes manifeste o contrário, por escrito, com antecedência mínima de 30 (trinta) dias do seu término."]))
partes.append(cl('DO REAJUSTE', [f"O valor mensal previsto na cláusula de pagamento permanecerá fixo durante o primeiro período de {meses} meses.",
  f"A cada renovação, o valor mensal poderá ser reajustado pela CONTRATADA, observado o valor de tabela do {E_(d['plano'])} vigente à época, mediante comunicação por escrito à CONTRATANTE com antecedência mínima de 30 (trinta) dias do fim do período em curso.",
  "Na ausência de comunicação de reajuste, o valor será corrigido a cada 12 (doze) meses de contrato pela variação acumulada do IPCA/IBGE no período, ou por outro índice oficial que venha a substituí-lo.",
  "Caso a CONTRATANTE não concorde com o novo valor comunicado, poderá optar pela não renovação, sem aplicação de multa, desde que o informe antes do fim do período em curso."]))
partes.append(cl('DAS OBRIGAÇÕES DA CONTRATADA', [letras(["Executar os serviços com zelo, qualidade e dentro dos prazos acordados;", "Submeter todo conteúdo à aprovação prévia da CONTRATANTE;", "Seguir as regras das plataformas, o CONAR e o Código de Defesa do Consumidor;", "Manter sigilo sobre informações, estratégias e dados da CONTRATANTE e de seus clientes, mesmo após o término do contrato, nos termos da Lei nº 13.709/2018 (LGPD);", "Responder pelos encargos trabalhistas e tributários de sua equipe."] + d.get('obrig_contratada_extra', []))]))
partes.append(cl('DAS OBRIGAÇÕES DA CONTRATANTE', [letras(["Efetuar os pagamentos nas datas acordadas;", "Fornecer, em até 48 (quarenta e oito) horas úteis após a assinatura, os acessos, informações, logotipos, fotos e materiais necessários à execução dos serviços;", "Responder às solicitações de aprovação nos prazos previstos;", "Obter e fornecer as autorizações de uso de imagem de terceiros, quando houver;", "Pagar a verba dos anúncios diretamente às plataformas, quando houver;", "Não alterar campanhas ou publicações em andamento sem alinhamento prévio com a CONTRATADA."] + d.get('obrig_contratante_extra', []))]))
partes.append(cl('DOS RESULTADOS E DAS PLATAFORMAS', ["A presente contratação é obrigação de meio, e não de resultado. A CONTRATADA se compromete a empregar as melhores técnicas para alcançar as metas definidas em conjunto, mas não garante número específico de seguidores, clientes, contatos ou vendas, que dependem de fatores externos como o funcionamento das plataformas, a concorrência e o atendimento da própria CONTRATANTE.",
  "A CONTRATADA não se responsabiliza por instabilidades, mudanças de regras ou de algoritmo, nem por bloqueios ou restrições aplicados pelas plataformas (Meta, TikTok, Google/YouTube), salvo quando causados diretamente por sua conduta."]))
partes.append(cl('DA RESCISÃO', [f"Em caso de rescisão imotivada por iniciativa da CONTRATANTE antes do término do período de {meses} meses, esta pagará os valores dos serviços já prestados e multa de 20% (vinte por cento) sobre o valor das parcelas restantes do período em curso.",
  "Após o período inicial, qualquer das partes poderá rescindir o contrato mediante aviso prévio por escrito de 30 (trinta) dias, sem multa, sendo devido o valor dos serviços prestados até o fim do aviso.",
  "O descumprimento de qualquer cláusula autoriza a parte prejudicada a rescindir o contrato de imediato, mediante notificação, sem aplicação da multa acima quando o descumprimento for da CONTRATADA.",
  "Não haverá devolução de valores referentes a meses já iniciados."]))
partes.append(cl('DOS DIREITOS AUTORAIS, ACESSOS E PORTFÓLIO', ["Após a quitação integral, os conteúdos publicados passam a ser de uso livre da CONTRATANTE. Os arquivos editáveis, modelos, estratégias e estruturas de campanha criados pela CONTRATADA permanecem de sua propriedade, nos termos da Lei nº 9.610/1998.",
  "Os materiais, fotos e artes enviados pela CONTRATANTE continuam sendo de sua propriedade.", "Ao término do contrato, a CONTRATADA devolverá todos os acessos às contas da CONTRATANTE.",
  "A CONTRATANTE autoriza a CONTRATADA a citar seu nome e logotipo e a exibir os trabalhos realizados em seu portfólio, com finalidade exclusivamente institucional."]))
partes.append(cl('DAS DISPOSIÇÕES GERAIS', ["Este contrato não cria vínculo trabalhista, societário ou de representação entre as partes, nem exclusividade: a CONTRATADA pode atender outros clientes, e a CONTRATANTE pode contratar outros prestadores.",
  "A impossibilidade de prestação do serviço causada por informação incorreta ou omitida pela CONTRATANTE não caracteriza descumprimento por parte da CONTRATADA.", "Os signatários declaram ser as partes ou seus representantes legais, com poderes para assumir as obrigações deste contrato."]))
partes.append(cl('DO FORO', ["As partes elegem o foro da Comarca de São Luís/MA para dirimir quaisquer dúvidas oriundas deste contrato, com renúncia a qualquer outro, por mais privilegiado que seja."]))
ass = lambda l: '<div>' + '<br>'.join(E_(x) for x in l) + '</div>'
doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>@page{{size:A4;margin:20mm 20mm 22mm}}body{{font:11pt/1.5 Arial,sans-serif;color:#111}}h1{{font-size:15pt;text-align:center;margin:0}}.sub{{text-align:center;font-size:10.5pt;margin:2mm 0 7mm}}h2{{font-size:11pt;margin:6mm 0 2mm}}p{{margin:0 0 2mm;text-align:justify}}ul{{list-style:none;margin:0 0 2mm 6mm;padding:0}}li{{margin:0 0 1.5mm;text-align:justify}}table{{border-collapse:collapse;margin:2mm 0 2mm 6mm;width:85%}}td{{border-bottom:1px solid #bbb;padding:4px 6px}}td+td{{text-align:right}}.ass{{display:flex;gap:14mm;margin-top:18mm;page-break-inside:avoid}}.ass div{{flex:1;text-align:center;border-top:1px solid #000;padding-top:2mm;font-size:9.5pt}}</style></head><body>
<h1>CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE MARKETING DIGITAL</h1><div class="sub">{E_(d['plano'])} — {E_(d['subtitulo'])}</div>
<p>Pelo presente instrumento particular, as partes abaixo qualificadas têm entre si justo e contratado o seguinte:</p>
<p><b>CONTRATANTE:</b> {E_(C['qualificacao'])}, e-mail para contrato e cobrança: {E_(C['email'])}, WhatsApp oficial: {E_(C['whats'])}.</p>
<p><b>CONTRATADA:</b> {E_(me['contratada_qualificacao'])}.</p>
{''.join(partes)}
<p style="margin-top:5mm">E, por estarem assim justas e contratadas, as partes assinam o presente instrumento em 2 (duas) vias de igual teor, juntamente com 2 (duas) testemunhas.</p>
<p style="text-align:center;margin-top:6mm">São Luís/MA, {E_(d.get('data_assinatura','____ de __________________ de 2026'))}.</p>
<div class="ass">{ass(C['assinatura'])}{ass(me['contratada_assinatura'])}</div>
<div class="ass"><div>Testemunha 1<br>Nome: ______________________<br>CPF: ______________________</div><div>Testemunha 2<br>Nome: ______________________<br>CPF: ______________________</div></div>
</body></html>'''
out = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), d['arquivo'] + '.pdf'); h = out[:-4] + '.html'
open(h, 'w', encoding='utf-8').write(doc)
foot = E_('Contrato de Prestação de Serviços — ' + C['nome'])
subprocess.run(['node', '-e', f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{h}');await p.pdf({{path:'{out}',format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style=\"font-size:8px;width:100%;text-align:center;color:#555\">{foot} — Página <span class=pageNumber></span></div>',margin:{{top:'20mm',bottom:'20mm',left:'20mm',right:'20mm'}}}});await b.close()}})()"], check=True)
print(out)
