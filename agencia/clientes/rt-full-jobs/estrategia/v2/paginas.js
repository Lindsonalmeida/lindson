// Estratégia completa Real Time v2 (conta Leandro, 03/11/2026): 19 páginas 4:5 no modelo aprovado
// (agencia/processos/modelo-estrategia/README.md), com a marca nova v1 e a composição do template VideoLab
// já escolhido para este projeto (identidade/v1/TEMPLATE.md). Sem preços, sem números inventados.
const M='../../identidade/v1/marca/',F='../../identidade/v1/fotos/';let pg=0;const P=[];
const tc=()=>`00:00:${String(pg).padStart(2,'0')}:00`;
const hd=(sec)=>`<div class="hd"><img src="${M}assinatura-horizontal-mono-branco.svg"><span>${sec}<i></i></span></div><div class="fio" style="top:118px"></div>`;
const ft=()=>`<div class="ft"><span>REALTIME · PLANO DE VENDAS · 2026</span><span class="r">REC ${tc()}</span></div>`;
const visor=(foto,{h=420,tc2='00:01:28',pos='center'}={})=>`<div class="visor" style="height:${h}px"><span class="k1"></span><span class="k2"></span><div class="f" style="background-image:url(${F}${foto}.jpg);background-position:${pos}"><div class="g"></div></div><span class="rec">REC</span><span class="hd2"><i>HD</i><i>4K</i></span><span class="tc">${tc2}</span></div>`;
function page(sec,html){pg++;P.push(`<section class="pg">${sec?hd(sec):''}${html}${ft()}</section>`)}
const n2=i=>String(i).padStart(2,'0');
const linhas=(arr,fs=24)=>arr.map((r,i)=>`<div class="ln"><span class="n">${n2(i+1)}</span><div><div class="t" style="font-size:${fs+6}px">${r[0]}</div><p style="font-size:${fs-4}px">${r[1]}</p></div></div>`).join('');
const celular=(foto,txt,bt,{w=300,rot=0}={})=>`<div style="width:${w}px;height:${w*1.9}px;border-radius:${w*.14}px;background:#050505;padding:${w*.035}px;border:1.5px solid var(--fio);transform:rotate(${rot}deg)"><div style="position:relative;width:100%;height:100%;border-radius:${w*.11}px;overflow:hidden;background:url(${F}${foto}.jpg) center/cover"><div style="position:absolute;top:${w*.04}px;left:50%;transform:translateX(-50%);width:34%;height:${w*.075}px;border-radius:99px;background:#050505"></div><div style="position:absolute;inset:auto 0 0;height:60%;background:linear-gradient(180deg,transparent,rgba(5,7,11,.95))"></div><div style="position:absolute;left:8%;right:8%;bottom:7%"><div style="font:600 ${w*.085}px/1.05 Geist;text-transform:uppercase;color:#fff">${txt}</div><div style="margin-top:12px;background:var(--az);color:#fff;text-align:center;border-radius:10px;padding:10px;font:600 ${w*.055}px Geist">${bt}</div></div><span style="position:absolute;left:8%;top:11%;font:600 ${w*.045}px Geist;color:#fff">realtime_fulljobs · <span style="opacity:.7">Patrocinado</span></span></div></div>`;

// 01 capa
page('',`<div class="hd"><img src="${M}assinatura-horizontal.svg"><span>PLANO DE VENDAS<i></i></span></div><div class="fio" style="top:118px"></div>
<div style="position:absolute;left:64px;right:64px;top:190px"><div class="rot">Estratégia completa · 90 dias</div><h1 style="margin-top:24px;font-size:122px">Equipamento<br><span class="cz">reservado.<br>Estúdio cheio.</span></h1></div>
<div style="position:absolute;left:64px;width:400px;top:800px"><div class="dest"><b>Um plano para a Real Time vender locação, estúdio e produção todo mês.</b><p class="txt">Conteúdo, anúncios, WhatsApp e relatório: o passo a passo dos próximos 90 dias.</p></div></div>
<div style="position:absolute;right:64px;width:520px;top:720px">${visor('kit',{h:400,tc2:'00:00:01:00'})}</div>
<div style="position:absolute;left:64px;right:64px;bottom:110px" class="abas">${['01 Locação','02 Estúdio','03 Conteúdo','04 Produções'].map(a=>`<span>${a}</span>`).join('')}</div>`);

// 02 ponto de partida
page('PONTO DE PARTIDA',`<div class="c"><div class="rot">O que a Real Time já tem</div><h2>O mais difícil<br><span class="cz">já está pronto</span></h2>
<div class="nums" style="margin-top:54px"><div><b>7k</b><span>seguidores<br>no Instagram</span></div><div><b>6</b><span>refletores<br>Aputure STORM</span></div><div><b>6</b><span>intercomu-<br>nicadores</span></div><div><b>1</b><span>estúdio com<br>fundo verde</span></div></div>
<div class="cartao" style="margin-top:40px;min-height:470px"><div style="padding:14px">${visor('opticas',{h:440,tc2:'00:00:02:00'})}</div><div class="p"><span class="n">O KIT</span><div><div class="t">Estrutura<br><span class="cz">de cinema</span></div><p>Sony FX3 com cage e matte box Tilta, lentes DZOFilm VESPID Prime 2, Sony GM e Zeiss, adaptador Metabones PL–E, transmissão Hollyland Pyro 7 e teleprompter.</p></div></div></div>
<p class="txt" style="margin-top:34px;color:var(--b)">E um feed que já mostra set real, bastidor real e equipamento real. O começo está feito.</p></div>`);

// 03 desafio
page('O DESAFIO',`<div class="c"><div class="rot">Onde está a venda</div><h2>Muita gente vê.<br><span class="cz">Pouca gente reserva.</span></h2>
<div class="lnwrap" style="margin-top:56px">${linhas([
['O post mostra, mas não pede','Quem precisa de um kit para sexta não sabe que pode reservar agora pelo WhatsApp.'],
['Cada cliente compra de um jeito','O videomaker aluga por diária. A empresa quer vídeo todo mês. A agência pede orçamento por projeto.'],
['Equipamento parado não paga nada','Cada dia sem diária é um dia que o kit custou e não rendeu.']],26)}</div>
<p class="txt" style="margin-top:40px">A estrutura já é de produtora grande. O plano é fazer o Maranhão saber disso e reservar.</p></div>`);

// 04 pilares e fases
page('O PLANO',`<div class="c"><div class="rot">4 pilares · 3 fases</div><h2>A máquina<br><span class="cz">de reservas</span></h2>
<div class="cols" style="margin-top:50px">${[['01','Conteúdo','Kit em ação, estúdio pronto e bastidor, com chamada em todo post.'],['02','Tráfego','Anúncio por produto, para o público certo de cada frente.'],['03','Atendimento','WhatsApp com roteiro: da pergunta à reserva confirmada.'],['04','Medição','Toda semana: quantos chamaram, de onde e quantos fecharam.']].map(c=>`<div><div class="n">${c[0]}</div><div class="t">${c[1]}</div><p>${c[2]}</p></div>`).join('')}</div>
<div class="lnwrap" style="margin-top:46px">${linhas([['Fase 1 · Base (semanas 1 e 2)','Ferramentas, rastreio e perfil que vende.'],['Fase 2 · Ativação (semanas 3 a 8)','Conteúdo diário, anúncios por produto e roteiro de WhatsApp.'],['Fase 3 · Escala (semanas 9 a 13)','Mais verba no que vendeu, contratos mensais e agências.']],24)}</div></div>`);

// 05 fase 1 base técnica
page('FASE 1 · BASE',`<div class="c"><div class="rot">Semanas 1 e 2</div><h2>A base<br><span class="cz">técnica</span></h2>
<div class="lnwrap" style="margin-top:46px">${linhas([
['Gerenciador de Negócios da Meta','Instagram, página e conta de anúncio no nome da Real Time, com acesso da agência.'],
['Pixel e eventos','Instalado no site e no link da bio: conta quem clicou para reservar.'],
['WhatsApp Business','Catálogo com os kits e o estúdio, etiquetas por etapa e mensagem de ausência.'],
['Links rastreados com código','Cada anúncio leva um código na mensagem (RT-CINEMA, RT-LUZ, RT-ESTUDIO, RT-PROD) para saber o que vendeu.'],
['Públicos salvos','Videomakers, empresas e agências já prontos para anunciar.'],
['Google Meu Negócio','Ficha do estúdio com fotos reais, horário e botão de WhatsApp.']],22)}</div></div>`);

// 06 perfil que vende
page('FASE 1 · PERFIL',`<div class="c"><div class="rot">O perfil que vende</div><h2>Em 5 segundos,<br><span class="cz">a pessoa entende</span></h2>
<div class="cartao" style="margin-top:44px;min-height:300px"><div class="p" style="background:var(--pn2)"><span class="n">BIO PROPOSTA</span><p class="mono" style="font-size:20px;color:var(--b);line-height:1.7">Locação de equipamento de cinema<br>Estúdio com fundo verde · Maranhão<br>Produção de vídeo para marcas<br>👇 Reserve seu kit no WhatsApp</p></div><div class="p"><span class="n">POR QUÊ</span><p>O que aluga, onde fica e o próximo passo. Sem frase de efeito: as palavras que o cliente digita na busca.</p></div></div>
<div class="cols" style="margin-top:34px;grid-template-columns:1fr 1fr 1fr">${[['Destaques','Kits · Estúdio · Produções · Bastidor · Como reservar · Clientes'],['Fixados','1 Kit completo · 2 Estúdio fundo verde · 3 Produções'],['Resposta automática','Palavra KIT no direct: manda a lista de kits e o link do WhatsApp.']].map((c,i)=>`<div><div class="n">${n2(i+1)}</div><div class="t">${c[0]}</div><p>${c[1]}</p></div>`).join('')}</div></div>`);

// 07 linhas editoriais
page('LINHAS EDITORIAIS',`<div class="c"><div class="rot">Com quem cada post fala</div><h2>6 linhas<br><span class="cz">de conteúdo</span></h2>
<table class="tb" style="margin-top:40px"><tr><th>Linha</th><th>O que mostra</th><th>Formato</th></tr>
${[['Kit em ação','o equipamento gravando de verdade','Reels'],['Estúdio pronto','o fundo verde montado e o que dá para gravar','Reels e carrossel'],['Bastidor','do take ao corte final','Reels e stories'],['Como usar','dica técnica simples de luz, lente e câmera','carrossel'],['Projetos','campanha, clipe ou filme feito, contado como caso','carrossel e Reels'],['Quem grava aqui','cliente real falando do set','Reels e stories']].map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join('')}</table>
<p class="txt" style="margin-top:30px">Toda arte leva a tag da linha na prévia e no card de aprovação, para saber com quem ela fala.</p></div>`);

// 08 roteiro de reels
page('ROTEIRO DE REELS',`<div class="c"><div class="rot">4 tempos em 30 segundos</div><h2>Gancho, mostra,<br><span class="cz">prova, chama</span></h2>
<div class="cols" style="margin-top:46px">${[['0–3 s','Gancho','A frase que para o dedo.'],['3–15 s','Mostra','O kit ou o estúdio em uso.'],['15–25 s','Prova','O resultado na tela.'],['25–30 s','Chama','Reserve no WhatsApp.']].map(c=>`<div><div class="n mono">${c[0]}</div><div class="t">${c[1]}</div><p>${c[2]}</p></div>`).join('')}</div>
<div class="pn" style="margin-top:40px"><div class="rot" style="color:var(--az)">Ganchos prontos</div><div class="lista" style="margin-top:10px">${['"Essa câmera grava filme de cinema. E você pode alugar."','"Gravou em casa e ficou escuro? Olha a diferença."','"Fundo verde: grava aqui, aparece em qualquer lugar."','"O que tem numa diária de cinema?"','"Antes e depois da luz certa."'].map((g,i)=>`<div class="${i==0?'on':''}" style="font-size:28px;text-transform:none;margin:12px 0"><sup>${n2(i+1)}</sup>${g}</div>`).join('')}</div></div></div>`);

// 09 semana
page('A SEMANA',`<div class="c"><div class="rot">Feed + stories</div><h2>Cada dia vende<br><span class="cz">uma frente</span></h2>
<div class="lnwrap" style="margin-top:44px">${linhas([['Segunda · Kit Cinema','Reels do kit em ação. Stories: agenda da semana com enquete.'],['Terça · Como usar','Carrossel de dica técnica. Stories: caixa de perguntas.'],['Quarta · Estúdio','Reels do fundo verde. Stories: bastidor ao vivo.'],['Quinta · Projetos','Caso real contado em carrossel.'],['Sexta · Kit Luz','Reels antes e depois da luz. Stories: "ainda tem data no fim de semana".'],['Fim de semana · Bastidor','Stories do set e repost de quem gravou.']],22)}</div>
<p class="txt" style="margin-top:26px">O post que mais trouxer conversa vira anúncio. Quem decide é o resultado.</p></div>`);

// 10 funil
page('FUNIL DE TRÁFEGO',`<div class="c"><div class="rot">3 etapas</div><h2>Do primeiro play<br><span class="cz">à reserva</span></h2>
<div class="lnwrap" style="margin-top:56px">${linhas([['Descobrir','Reels do kit e do estúdio para quem ainda não conhece a Real Time. Objetivo: visualização de vídeo.'],['Considerar','Quem assistiu mais da metade vê o kit completo, o depoimento e o como reservar. Objetivo: conversa no WhatsApp.'],['Reservar','Quem chamou e não fechou vê "ainda tem data esta semana". Objetivo: reserva confirmada.']],28)}</div>
<div class="abas" style="margin-top:60px">${['Visualização','Conversa','Reserva'].map(a=>`<span>${a}</span>`).join('')}</div></div>`);

// 11 campanhas por produto
page('CAMPANHAS',`<div class="c"><div class="rot">Uma campanha por frente</div><h2>Cada produto,<br><span class="cz">seu público</span></h2>
<table class="tb" style="margin-top:40px"><tr><th>Campanha</th><th>Público</th><th>Destino · código</th></tr>
${[['Kit Cinema e Ópticas','videomakers, diretores de fotografia, produtoras','WhatsApp · RT-CINEMA'],['Kit Luz','produtoras e quem grava publicidade','WhatsApp · RT-LUZ'],['Estúdio fundo verde','empresas, criadores, videocasts','WhatsApp · RT-ESTUDIO'],['Realtime Conteúdo','donos e marketing de empresas','WhatsApp · RT-MENSAL'],['Realtime Produções','agências, marcas, instituições','WhatsApp · RT-PROD']].map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td class="mono" style="font-size:17px">${r[2]}</td></tr>`).join('')}</table>
<p class="txt" style="margin-top:30px">Locação: anúncio de segunda a quinta, para reservas da semana. Empresas e agências: horário comercial.</p></div>`);

// 12 públicos
page('PÚBLICOS',`<div class="c"><div class="rot">Quem vê os anúncios</div><h2>5 públicos<br><span class="cz">e 1 exclusão</span></h2>
<div class="lnwrap" style="margin-top:46px">${linhas([['Quentes','Quem segue, engajou ou assistiu aos Reels nos últimos 30 dias.'],['Parecidos','Semelhantes a quem já chamou no WhatsApp.'],['Por interesse','Filmmaking, fotografia, produção audiovisual, Sony, Aputure.'],['Por cargo','Donos de empresa, marketing e agências de publicidade.'],['Por lugar','Maranhão, com raio maior em volta do estúdio.'],['Exclusão','Quem já reservou na semana não vê anúncio de reserva.']],22)}</div></div>`);

// 13 criativos + 90 dias
page('CRIATIVOS',`<div class="c"><div class="rot">Os primeiros anúncios</div><h2>3 criativos<br><span class="cz">para começar</span></h2>
<div style="display:flex;gap:26px;justify-content:space-between;margin-top:40px">${celular('kit','Kit de cinema<br>para a sua diária','Reservar meu kit')}${celular('mascote','Estúdio pronto.<br>É só gravar.','Ver datas livres')}${celular('set','Da ideia ao<br>filme pronto','Pedir orçamento')}</div>
<div class="cols" style="margin-top:34px;grid-template-columns:1fr 1fr 1fr">${[['Novembro','Campanhas e vídeos de fim de ano das empresas: locação e estúdio.'],['Dezembro','Retrospectivas, eventos e festas: kits por diária.'],['Janeiro','Planejamento do ano: contratos de conteúdo mensal.']].map((c,i)=>`<div><div class="n">${n2(i+1)}</div><div class="t">${c[0]}</div><p>${c[1]}</p></div>`).join('')}</div></div>`);

// 14 testes
page('TESTES',`<div class="c"><div class="rot">Como o dinheiro do anúncio é cuidado</div><h2>Testar, cortar,<br><span class="cz">escalar</span></h2>
<div class="lnwrap" style="margin-top:50px">${linhas([['3 criativos por campanha','Vídeo do kit, foto no visor e depoimento.'],['3 dias de teste','Sem mexer, para o anúncio aprender.'],['Corte','O que não trouxe conversa sai. Fica o melhor.'],['Escala de ~20%','Aumento aos poucos no que trouxe reserva, a cada 2 ou 3 dias.'],['Renovação','Criativo novo a cada 2 semanas, para não cansar o público.']],26)}</div></div>`);

// 15 whatsapp
page('WHATSAPP',`<div class="c"><div class="rot">Da pergunta à reserva</div><h2>6 passos<br><span class="cz">no WhatsApp</span></h2>
<div class="lnwrap" style="margin-top:44px">${linhas([['Responder rápido','Em poucos minutos no horário comercial. Fora dele, mensagem automática.'],['Perguntar a data e o job','"Qual dia é a gravação e o que vocês vão gravar?"'],['Indicar o kit certo','Sugerir o kit pelo tipo de gravação, com fotos do catálogo.'],['Mandar as condições','Valor, retirada, devolução e o que vem no kit.'],['Confirmar a reserva','Data bloqueada, etiqueta "reservado" e lembrete na véspera.'],['Depois do job','Pedir uma fala e uma foto do set para virar depoimento.']],22)}</div></div>`);

// 16 calendário 90 dias
page('90 DIAS',`<div class="c"><div class="rot">Semana a semana</div><h2>Calendário<br><span class="cz">de 90 dias</span></h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:40px">${[
['S1','Base técnica e Pixel'],['S2','Perfil, destaques, catálogo'],['S3','Conteúdo diário e 1ª campanha Kit Cinema'],['S4','Campanha Estúdio'],['S5','1º caso real em carrossel'],['S6','Campanha Kit Luz'],['S7','Depoimentos dos clientes'],['S8','Campanha Conteúdo mensal'],['S9','Escala do que vendeu'],['S10','Apresentação para agências'],['S11','Campanha Produções'],['S12','Ajustes e renovação'],['S13','Relatório dos 90 dias e próximo ciclo']].map((s,i)=>`<div class="pn" style="padding:20px 22px;${i%4==2?'border-top:2px solid var(--az)':''}"><div class="mono" style="font-size:15px;color:var(--cz)">${s[0]}</div><div style="font:500 21px/1.3 Geist;margin-top:8px">${s[1]}</div></div>`).join('')}</div>
<p class="txt" style="margin-top:26px">Fase 1: S1–S2 · Fase 2: S3–S8 · Fase 3: S9–S13</p></div>`);

// 17 relatório
page('RELATÓRIO',`<div class="c"><div class="rot">Toda segunda-feira</div><h2>Relatório<br><span class="cz">sem complicação</span></h2>
<div class="nums" style="margin-top:56px;grid-template-columns:repeat(2,1fr)">${[['Chamaram','quantas conversas no WhatsApp'],['De onde','qual código: cinema, luz, estúdio, mensal, produção'],['Orçamentos','quantos receberam as condições'],['Fecharam','quantas reservas e contratos']].map((x,i)=>`<div style="${i>1?'border-top:1.5px solid var(--fio);':''}flex-direction:column;align-items:flex-start;gap:10px;padding:30px 22px"><b style="font-size:40px">${x[0]}</b><span>${x[1]}</span></div>`).join('')}</div>
<p class="txt" style="margin-top:40px">Mais: o post e o anúncio que mais trouxeram conversa, e o que muda na semana seguinte. Números só da conta de anúncio e do WhatsApp, nunca estimados.</p></div>`);

// 18 quem faz o quê
page('QUEM FAZ O QUÊ',`<div class="c"><div class="rot">A divisão do trabalho</div><h2>Vocês gravam.<br><span class="az">Eu vendo.</span></h2>
<div class="cartao" style="margin-top:50px;min-height:520px"><div class="p" style="justify-content:flex-start;gap:20px"><span class="n">REAL TIME</span>${['Atender e fechar no WhatsApp','Mandar fotos e vídeos do set','Pedir a fala de quem gravou','Manter o catálogo de kits em dia'].map(t=>`<p style="font-size:22px;color:var(--b)">● ${t}</p>`).join('')}</div><div class="p" style="justify-content:flex-start;gap:20px;background:var(--pn2)"><span class="n">AGÊNCIA</span>${['Conteúdo e legendas da semana','Anúncios por produto','Roteiro e respostas do WhatsApp','Relatório toda segunda'].map(t=>`<p style="font-size:22px;color:var(--b)">● ${t}</p>`).join('')}</div></div></div>`);

// 19 próximo passo
page('',`<div class="hd"><img src="${M}assinatura-horizontal.svg"><span>PRÓXIMO PASSO<i></i></span></div><div class="fio" style="top:118px"></div>
<div style="position:absolute;left:64px;right:64px;top:180px">${visor('set',{h:420,tc2:'00:00:19:00',pos:'50% 30%'})}</div>
<div style="position:absolute;left:64px;right:64px;top:660px"><div class="rot">As empresas estão fechando os vídeos de fim de ano agora</div><p class="txt" style="font-size:26px;margin-top:20px;color:var(--b)">Quem aparece em novembro fica com as diárias de dezembro.</p>
<p class="txt" style="font-size:26px;margin-top:40px">Responda com</p><h1 style="font-size:116px;margin-top:10px" class="az">Quero começar</h1>
<p class="txt" style="font-size:24px;margin-top:24px">e eu marco 15 minutos para mostrar como isso funciona na Real Time.</p>
<div class="mono" style="margin-top:46px;color:var(--cz);font-size:17px;letter-spacing:.12em">LINDSON ALMEIDA · @LINDSONALMEIDA_</div></div>`);

document.getElementById('pp').innerHTML=P.join('');window.pronto=true;
