"""Clone Studio: o app interno de clone de voz e imagem do Lindson (conta Pedro, 03/11/2026).
Abre no navegador (http://127.0.0.1:7860), só no computador dele. Etapa 1: Biblioteca + Voz.
Etapa 2 (próxima): Vídeo com a boca sincronizada (MuseTalk 1.5) e Gravuras vivas (LivePortrait)."""
import datetime as dt, os
import gradio as gr, soundfile as sf
import biblioteca as bib, motor_voz as mv

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
        aviso = ('✅ ' if ok else '⛔ ') + motivo
    except Exception as e:
        aviso = '⚠️ ' + str(e)
    return aviso, _tabela(), gr.update(choices=_nomes())


def gerar_voz(nome, texto, expressao, humanizar, progresso=gr.Progress()):
    pid, p = _pid(nome)
    if not p: raise gr.Error('Escolha uma pessoa ou personagem da Biblioteca.')
    ok, motivo = bib.liberado(p)
    if not ok: raise gr.Error('Bloqueado: ' + motivo)
    if not texto.strip(): raise gr.Error('Escreva o texto.')
    a = mv.narrar(texto, p['amostra_voz'], expressao, humanizar=humanizar, progresso=progresso)
    os.makedirs(SAIDA, exist_ok=True)
    arq = os.path.join(SAIDA, f"{pid}-{dt.datetime.now():%Y%m%d-%H%M%S}.wav")
    sf.write(arq, a, mv.S)
    return arq, f'Pronto: {len(a) / mv.S:.1f} s de áudio, salvo em {arq}. Feito com IA: avise o público quando for realista.'


with gr.Blocks(title='Clone Studio') as app:
    gr.Markdown('# Clone Studio\nVoz e imagem clonadas, só com autorização. Uso interno do Lindson.')
    with gr.Tab('Biblioteca'):
        gr.Markdown('Cadastre cada rosto e voz. **Lindson e clientes:** termo assinado + vídeo de consentimento. '
                    '**Personagens:** registre a fonte (obra, autor, licença).\n\n'
                    f'Frase do vídeo de consentimento (gravar ao vivo, a própria pessoa, sozinha, rosto visível):\n> {FRASE_CONSENTIMENTO}')
        with gr.Row():
            nome = gr.Textbox(label='Nome'); tipo = gr.Dropdown(bib.TIPOS, label='Tipo', value=bib.TIPOS[0])
            validade = gr.Textbox(label='Termo válido até (AAAA-MM-DD)')
        with gr.Row():
            amostra = gr.Audio(label='Amostra de voz (10 s a 2 min, voz limpa)', type='filepath')
            base = gr.Video(label='Vídeo base, para a etapa de vídeo (2 min olhando para a câmera)')
        with gr.Row():
            termo = gr.File(label='Termo de autorização assinado (PDF ou foto)', type='filepath')
            video = gr.Video(label='Vídeo de consentimento')
            fonte = gr.Textbox(label='Fonte do personagem (obra, autor, licença)')
        aviso = gr.Markdown(); bt = gr.Button('Salvar na biblioteca', variant='primary')
        tabela = gr.Dataframe(headers=['Nome', 'Tipo', 'Situação', 'Motivo', 'Validade'], value=_tabela(), interactive=False)
    with gr.Tab('Voz'):
        with gr.Row():
            quem = gr.Dropdown(_nomes(), label='Voz de quem')
            expressao = gr.Slider(.25, 1, .5, step=.05, label='Expressão (mais alto = mais emoção)')
            humanizar = gr.Checkbox(True, label='Humanizar (pausas, respiração, som de estúdio)')
        texto = gr.Textbox(lines=8, label='Texto', placeholder='Escreva como se fala: frases curtas, números por extenso.')
        gerar = gr.Button('Gerar voz', variant='primary')
        audio = gr.Audio(label='Resultado', type='filepath'); info = gr.Markdown()
    with gr.Tab('Vídeo (em breve)'):
        gr.Markdown('Próxima etapa: boca sincronizada no vídeo base (MuseTalk 1.5, roda na RTX 3050) e gravuras vivas '
                    '(LivePortrait). Corpo e gestos vão para a nuvem (Modal), só quando precisar.')
    bt.click(cadastrar, [nome, tipo, amostra, termo, video, validade, fonte, base], [aviso, tabela, quem])
    gerar.click(gerar_voz, [quem, texto, expressao, humanizar], [audio, info])

if __name__ == '__main__':
    app.queue().launch(server_name='127.0.0.1', inbrowser=True)
