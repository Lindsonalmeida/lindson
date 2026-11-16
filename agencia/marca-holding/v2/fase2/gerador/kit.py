"""Kit comercial Al Kántara (A4): proposta, contrato, orçamento, case e onboarding. Campos [ ] = preencher.
Contrato adaptado de agencia/processos/modelo-contrato (cláusulas do padrão aprovado), sem dado pessoal.
Fase 2, 16/11/2026."""
import os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'); O = os.path.join(B, 'kit'); os.makedirs(O, exist_ok=True)
F = '../site/f/'
CSS = f'''@font-face{{font-family:F;src:url({F}fraunces.ttf)}}@font-face{{font-family:F;font-style:italic;src:url({F}fraunces-it.ttf)}}
@font-face{{font-family:I;src:url({F}inter.ttf);font-weight:500}}@font-face{{font-family:I;src:url({F}inter-sb.ttf);font-weight:600}}
@page{{size:A4;margin:22mm 20mm 20mm}}@page:first{{margin:0}}body{{font:500 10.5pt/1.6 I;color:#0B0C0E;margin:0}}
.capa{{height:296mm;box-sizing:border-box;background:#0B0C0E;color:#EFEAE1;margin:0;padding:30mm 20mm;position:relative;page-break-after:always;overflow:hidden}}
.capa img{{height:9mm}}.capa h1{{font:400 54pt/.95 F;letter-spacing:-.03em;margin:70mm 0 8mm}}.capa h1 em{{color:#B8955A}}.capa .k{{position:absolute;right:-40mm;top:40mm;width:150mm;opacity:.9}}
.capa p{{color:#8E8A82;font:600 8pt I;letter-spacing:.24em;text-transform:uppercase}}
h2{{font:400 22pt/1.1 F;margin:9mm 0 3mm;letter-spacing:-.01em}}h2 em{{color:#8a6a35}}h3{{font:600 10.5pt I;margin:5mm 0 1mm}}
.mono{{font:600 7.5pt I;letter-spacing:.22em;text-transform:uppercase;color:#8E8A82}}
.c{{border:1px dashed #B8955A;color:#8a6a35;padding:0 5px;border-radius:4px;background:#faf6ee}}
table{{width:100%;border-collapse:collapse;margin:3mm 0}}td,th{{border-bottom:1px solid #ddd6ca;padding:7px 4px;text-align:left;vertical-align:top}}th{{font:600 7.5pt I;letter-spacing:.18em;text-transform:uppercase;color:#8E8A82}}
td.r,th.r{{text-align:right}}.tot td{{font:400 15pt F;border-top:2px solid #0B0C0E}}
.ass{{display:flex;gap:14mm;margin-top:22mm;page-break-inside:avoid}}.ass div{{flex:1;border-top:1px solid #000;padding-top:2mm;text-align:center;font-size:9pt}}
.faixa{{display:flex;height:3px;margin:6mm 0}}.faixa i{{flex:1}}p{{margin:0 0 2.5mm;text-align:justify}}ul,ol{{margin:0 0 3mm 5mm;padding-left:4mm}}li{{margin-bottom:1.5mm}}'''
K = '<svg class="k" viewBox="0 0 480 480"><path fill="#1A1C20" d="M0,0 L100,480 L164,480 L164,0 Z"/><path fill="#1A1C20" d="M196,0 L196,199.19 L380.54,0 Z"/><path fill="#B8955A" d="M480,0 L424.16,0 L201.32,240.53 L384.39,458.93 Z"/><path fill="#1A1C20" d="M360.3,480 L196,283.99 L196,480 Z"/></svg>'
FX = '<div class="faixa"><i style="background:#2E4BFF"></i><i style="background:#E8461E"></i><i style="background:#F0A202"></i><i style="background:#0E8C66"></i></div>'
c = lambda t: f'<span class="c">[ {t} ]</span>'
def doc(nome, tit, sub, corpo):
    open(os.path.join(O, nome + '.html'), 'w').write(f'''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><style>{CSS}</style>
<section class="capa">{K}<img src="../site/i/horizontal-negativo.svg"><h1>{tit}</h1><p>{sub}</p></section>{corpo}''')

doc('proposta', 'Proposta<br><em>comercial.</em>', f'PARA {c("EMPRESA")} · {c("DATA")} · VÁLIDA POR 15 DIAS', f'''
<p class="mono">01 · O QUE ENTENDEMOS</p><h2>Seu momento, <em>nas suas palavras.</em></h2><p>{c("Resumo da conversa: situação atual, o que trava, o que a empresa quer alcançar. Usar as palavras do cliente.")}</p>
<p class="mono">02 · O QUE PROPOMOS</p><h2>Escopo <em>por escrito.</em></h2><p>Divisão responsável: {c("Labs / Studio / Media / Ventures")}</p>
<table><tr><th>Entrega</th><th>Descrição</th><th class="r">Prazo</th></tr>{''.join(f'<tr><td>{c("entrega")}</td><td>{c("o que é, em uma linha")}</td><td class="r">{c("dias")}</td></tr>' for _ in range(4))}</table>
<h3>Não está incluído</h3><ul><li>{c("item fora do escopo")}</li><li>Custos de terceiros (mídia paga, domínios, licenças), salvo quando listados acima.</li></ul>
<p class="mono">03 · COMO TRABALHAMOS</p><h2>Um preço, um prazo, <em>um responsável.</em></h2>
<ol><li>Reunião de início e onboarding (acessos, materiais, pessoas).</li><li>Entrega por etapas, com aprovação pelo WhatsApp oficial em até 48 h e 2 rodadas de ajuste.</li><li>Relatório {c("semanal / mensal")} com o que foi feito e o que vem.</li><li>Responsável: {c("nome e WhatsApp")}.</li></ol>
<p class="mono">04 · INVESTIMENTO</p><h2>Valores.</h2><p>Ver orçamento anexo ({c("número do orçamento")}). Pagamento pré-pago; o serviço começa após a confirmação.</p>
<p class="mono">05 · O QUE NÃO PROMETEMOS</p><p>Trabalhamos com obrigação de meio: entregamos o que está no escopo, com qualidade e prazo. Resultados de venda dependem de fatores fora do nosso controle e variam.</p>
{FX}<p>Para aprovar, responda “aprovado” no WhatsApp ou assine o contrato enviado em seguida.</p>''')

CL = [('OBJETO', [f'Prestação, pela CONTRATADA, dos serviços de {c("descrição")} pela divisão Al Kántara {c("divisão")}, conforme a proposta {c("número")}, que integra este contrato.']),
 ('O QUE ESTÁ INCLUÍDO E O QUE NÃO ESTÁ', [f'Incluído: {c("lista")}.', f'Não incluído: {c("lista")}; custos de terceiros (mídia, domínio, licenças) salvo previsão expressa.']),
 ('APROVAÇÕES', ['As entregas serão enviadas pelo WhatsApp oficial; a CONTRATANTE aprova ou pede ajuste em até 48 horas, com até 2 rodadas de ajuste por entrega.', 'Sem retorno no prazo, a etapa é adiada, sem acúmulo de entregas nem desconto.']),
 ('PAGAMENTO', [f'Valor: {c("R$ valor")} {c("mensal / único")}, com vencimento todo dia {c("dia")}.', 'O serviço é pré-pago e começa após a confirmação do pagamento.', 'Atraso: multa de 2% e juros de 1% ao mês pro rata; após 15 dias, os serviços podem ser suspensos.']),
 ('VIGÊNCIA E REAJUSTE', [f'Vigência de {c("3")} meses a partir de {c("data")}, com renovação automática salvo aviso por escrito com 30 dias de antecedência.', 'Os valores podem ser reajustados a cada renovação pela tabela vigente ou, no mínimo anual, pelo IPCA.']),
 ('OBRIGAÇÕES DAS PARTES', ['CONTRATADA: executar o escopo com qualidade e no prazo, indicar um responsável e manter sigilo sobre informações da CONTRATANTE.', 'CONTRATANTE: fornecer acessos, materiais e informações verdadeiras, aprovar no prazo e pagar em dia.']),
 ('NATUREZA DA OBRIGAÇÃO', ['A obrigação da CONTRATADA é de meio. Não há garantia de resultado de vendas, alcance ou faturamento, que dependem de fatores externos.']),
 ('PROPRIEDADE E DADOS', ['Após a quitação, código, artes e arquivos finais entregues pertencem à CONTRATANTE. A CONTRATADA pode citar o trabalho em portfólio, sem dados pessoais nem informação sigilosa.', 'Dados pessoais são tratados conforme a LGPD (Lei 13.709/2018), apenas para a execução deste contrato.']),
 ('RESCISÃO', ['Qualquer parte pode rescindir com aviso por escrito de 30 dias. Valores de etapas já iniciadas não são devolvidos.']),
 ('FORO', ['Fica eleito o foro da comarca de São Luís (MA).'])]
cont = f'''<p class="mono">CONTRATO DE PRESTAÇÃO DE SERVIÇOS</p><h2>Partes.</h2>
<p><b>CONTRATADA:</b> {c("razão social, CNPJ e endereço: agencia/contratos/meus-dados.json")}, nome comercial Al Kántara Group, neste ato representada por {c("representante")}.</p>
<p><b>CONTRATANTE:</b> {c("nome / razão social, CPF/CNPJ, endereço, e-mail e WhatsApp")}.</p>''' + ''.join(f'<h3>CLÁUSULA {i+1}ª · {t}</h3>' + ''.join(f'<p>{x}</p>' for x in its) for i, (t, its) in enumerate(CL)) + \
 f'<p style="margin-top:8mm">São Luís (MA), {c("data")}.</p><div class="ass"><div>CONTRATADA<br>Al Kántara Group</div><div>CONTRATANTE<br>{c("nome")}</div></div>'
doc('contrato', 'Contrato de<br><em>prestação de serviços.</em>', 'MODELO · ADAPTADO DO PADRÃO APROVADO (MODELO-CONTRATO)', cont)

doc('orcamento', 'Orça<br><em>mento.</em>', f'Nº {c("000")} · {c("DATA")} · VÁLIDO POR 15 DIAS', f'''
<p class="mono">CLIENTE</p><p>{c("nome / empresa")} · {c("contato")}</p><p class="mono" style="margin-top:6mm">DIVISÃO</p><p>Al Kántara {c("divisão")} · responsável {c("nome")}</p>
<table><tr><th>Item</th><th class="r">Qtd.</th><th class="r">Valor unit.</th><th class="r">Total</th></tr>{''.join(f'<tr><td>{c("item")}</td><td class="r">{c("1")}</td><td class="r">{c("R$")}</td><td class="r">{c("R$")}</td></tr>' for _ in range(5))}
<tr class="tot"><td colspan="3">Total</td><td class="r">{c("R$")}</td></tr></table>
<p class="mono">CONDIÇÕES</p><ul><li>Pagamento: {c("Pix / boleto / cartão")}, pré-pago.</li><li>Prazo de entrega: {c("dias")} após pagamento e envio dos materiais.</li><li>Não inclui custos de terceiros, salvo os listados.</li></ul>{FX}
<p>Valores definidos pelo Lindson para cada proposta. Nenhum preço fixo neste modelo.</p>''')

doc('case', 'Case<br><em>{c("nome do projeto")}.</em>'.replace('{c("nome do projeto")}', c('projeto')), 'MODELO DE ESTUDO DE CASO · 1 PROJETO POR DOCUMENTO', f'''
<p class="mono">CLIENTE · DIVISÃO</p><h2>{c("Cliente")} · <em>Al Kántara {c("divisão")}</em></h2>
<p class="mono">O DESAFIO</p><p>{c("A situação antes, em 3 linhas, com as palavras do cliente.")}</p>
<p class="mono">O QUE FIZEMOS</p><ol><li>{c("passo")}</li><li>{c("passo")}</li><li>{c("passo")}</li></ol>
<p class="mono">O QUE MUDOU</p><p>{c("Só dado real, medido e autorizado pelo cliente, com a fonte (ex.: painel do Instagram, de/até). Sem dado: descrever a entrega, sem número.")}</p>
<p class="mono">NO AR</p><p>{c("link")} · {c("imagens: 2 a 4 telas reais")}</p>
<p class="mono">AUTORIZAÇÃO</p><p>Publicado com autorização de {c("nome")} em {c("data")}. Regras do setor respeitadas (ex.: conselho profissional).</p>''')

doc('onboarding', 'Boas-vindas<br><em>ao grupo.</em>', f'ONBOARDING · {c("CLIENTE")} · AL KÁNTARA {c("DIVISÃO")}', f'''
<p class="mono">QUEM CUIDA DE VOCÊ</p><h2>Seu responsável: <em>{c("nome")}</em></h2><p>WhatsApp oficial: {c("número")}. Atendimento {c("dias e horários")}. Tudo que for combinado fica registrado por escrito.</p>
<p class="mono">PRIMEIROS 7 DIAS</p><table><tr><th>Dia</th><th>O que acontece</th><th>Quem</th></tr>
<tr><td>1</td><td>Reunião de início (30 min): objetivos, prazos e aprovações</td><td>Nós + você</td></tr>
<tr><td>1–2</td><td>Envio de acessos e materiais (lista abaixo)</td><td>Você</td></tr>
<tr><td>3–5</td><td>Diagnóstico e plano da primeira etapa</td><td>Nós</td></tr>
<tr><td>7</td><td>Primeira entrega ou prévia para aprovação</td><td>Nós</td></tr></table>
<p class="mono">CHECKLIST DE ACESSOS E MATERIAIS</p><ul><li>☐ Logo e manual da marca (se houver)</li><li>☐ Fotos reais do negócio, equipe e produtos (uma por mensagem)</li><li>☐ Acesso às redes e ao gerenciador de anúncios (como parceiro)</li><li>☐ Domínio, hospedagem e e-mail (se o projeto for site ou sistema)</li><li>☐ Lista de dúvidas frequentes dos seus clientes</li><li>☐ {c("item específico do projeto")}</li></ul>
<p class="mono">COMO APROVAR</p><p>Responda “aprovado” ou mande os ajustes em uma mensagem só, em até 48 h. São 2 rodadas de ajuste por entrega.</p>
<p class="mono">SEU PAINEL</p><p>Você acompanha entregas, aprovações e arquivos no seu painel na Central: {c("link /painel/cliente")}.</p>{FX}''')
print('kit ok')
