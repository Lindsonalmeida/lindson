"""Dublê (antigo Clone Studio): o app interno de clone de voz e imagem do Lindson (conta Pedro, 03/11/2026).
Abre no navegador (http://127.0.0.1:7860), só no computador dele. Etapa 1: Biblioteca + Voz.
Etapa 2 (próxima): Vídeo com a boca sincronizada (MuseTalk 1.5) e Gravuras vivas (LivePortrait)."""
import datetime as dt, os
import gradio as gr, soundfile as sf
import biblioteca as bib, motor_voz as mv
from identidade.tema import TEMA, CSS, CABECALHO

AQUI = os.path.dirname(os.path.abspath(__file__))

SAIDA = os.path.join(bib.RAIZ, 'saidas')
FRASE_CONSENTIMENTO = ('Eu, [nome completo], autorizo o Lindson Almeida a usar a minha imagem e a minha voz para '
                       'criar conteúdo com inteligência artificial para [finalidade], até [data]. Hoje é [data de hoje].')


def _tabela():
    linhas = []
    for pid, p in bib.lista().items():
        ok, motivo = bib.liberado(p)
        linhas.append([p['nome'], p['tipo'], 'Liberado' if ok else 'Bloqueado', motivo, p.get('validade', '')])
    return linhas


def _nomes(): return [p['nome'] for p in bib.lista().values()]


def _pid(nome):
    for k, p in bib.lista().items():
        if p['nome'] == nome: return k, p
    return None, None


def cadastrar(nome, tipo, amostra, termo, video, validade, fonte, base):
    try:
        _, ok, motivo = bib.cadastra(nome, tipo, amostra, termo, video, validade, fonte, base)
        aviso = ('✅ Dublê salvo e liberado.' if ok else '⛔ Dublê salvo, mas bloqueado: ' + motivo)
    except Exception as e:
        aviso = '⚠️ ' + str(e)
    return aviso, _tabela(), gr.update(choices=_nomes())


def gerar_voz(nome, texto, expressao, humanizar, progresso=gr.Progress()):
    pid, p = _pid(nome)
    if not p: raise gr.Error('Escolha um dublê na Biblioteca.')
    ok, motivo = bib.liberado(p)
    if not ok: raise gr.Error('Esse dublê está bloqueado: ' + motivo + ' Resolva na Biblioteca.')
    if not texto.strip(): raise gr.Error('Escreva o texto.')
    a = mv.narrar(texto, p['amostra_voz'], expressao, humanizar=humanizar, progresso=progresso)
    os.makedirs(SAIDA, exist_ok=True)
    arq = os.path.join(SAIDA, f"{pid}-{dt.datetime.now():%Y%m%d-%H%M%S}.wav")
    sf.write(arq, a, mv.S)
    return arq, f'Pronto: {len(a) / mv.S:.1f} s de áudio, salvo em {arq}. Feito com IA: avise o público quando parecer real.'


with gr.Blocks(title='Dublê') as app:
    gr.HTML(CABECALHO)
    with gr.Tab('Biblioteca'):
        gr.HTML('<div class="dub-consentimento"><strong>Só com autorização.</strong> Rosto e voz de gente real só entram aqui com o termo '
                'assinado e um vídeo da própria pessoa dizendo que autoriza.</div>')
        gr.Markdown('Cadastre cada dublê. **Lindson e clientes:** termo assinado + vídeo de consentimento. '
                    '**Personagens:** registre a fonte (obra, autor, licença).\n\n'
                    f'Frase do vídeo de consentimento (gravar ao vivo, a própria pessoa, sozinha, rosto visível):\n> {FRASE_CONSENTIMENTO}')
        with gr.Row():
            nome = gr.Textbox(label='Nome do dublê'); tipo = gr.Dropdown(bib.TIPOS, label='Quem é', value=bib.TIPOS[0])
            validade = gr.Textbox(label='Termo vale até (AAAA-MM-DD)')
        with gr.Row():
            amostra = gr.Audio(label='Amostra de voz (10 s a 2 min, sem barulho)', type='filepath')
            base = gr.Video(label='Vídeo base, para a etapa de vídeo (2 min olhando para a câmera)')
        with gr.Row():
            termo = gr.File(label='Termo assinado (PDF ou foto)', type='filepath')
            video = gr.Video(label='Vídeo de consentimento')
            fonte = gr.Textbox(label='De onde vem o personagem (obra, autor, licença)')
        aviso = gr.Markdown(); bt = gr.Button('Salvar dublê', variant='primary')
        tabela = gr.Dataframe(headers=['Nome', 'Tipo', 'Situação', 'Motivo', 'Validade'], value=_tabela(), interactive=False)
    with gr.Tab('Voz'):
        with gr.Row():
            quem = gr.Dropdown(_nomes(), label='Voz de quem')
            expressao = gr.Slider(.25, 1, .5, step=.05, label='Emoção (mais alto = mais emoção)')
            humanizar = gr.Checkbox(True, label='Deixar humano (pausas, respiração, som de estúdio)')
        texto = gr.Textbox(lines=8, label='Texto', placeholder='Escreva como se fala: frases curtas e números por extenso.')
        gerar = gr.Button('Gerar voz', variant='primary')
        audio = gr.Audio(label='Resultado', type='filepath'); info = gr.Markdown()
    with gr.Tab('Vídeo (em breve)'):
        gr.Markdown('Próxima etapa: boca sincronizada no vídeo base (MuseTalk 1.5, roda na RTX 3050) e gravuras vivas '
                    '(LivePortrait). Corpo e gestos vão para a nuvem (Modal), só quando precisar.')
    gr.Markdown('Uso interno. Nada sai daqui sem a autorização da pessoa.', elem_classes='dub-rodape')
    bt.click(cadastrar, [nome, tipo, amostra, termo, video, validade, fonte, base], [aviso, tabela, quem])
    gerar.click(gerar_voz, [quem, texto, expressao, humanizar], [audio, info])

if __name__ == '__main__':
    app.queue().launch(server_name='127.0.0.1', inbrowser=True, theme=TEMA, css=CSS,
                       favicon_path=os.path.join(AQUI, 'identidade', 'favicon.svg'))
