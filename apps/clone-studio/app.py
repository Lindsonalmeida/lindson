"""Dublê: o app interno de clone de voz e imagem do Lindson (conta Pedro, 03/11/2026).
Tela nova (v2) copiada da composição do template Sermo (Framer Marketplace, sermo-ai.framer.website),
na identidade do Dublê (identidade/IDENTIDADE.md). A página fica em web/; este arquivo é o servidor local.
Abre em http://127.0.0.1:7860, só no computador do Lindson. Motor e trava: motor_voz.py e biblioteca.py.
A tela antiga em Gradio ficou em app_gradio_antigo.py (reprovada pelo Lindson em 03/11)."""
import datetime as dt, os, shutil, subprocess, tempfile, threading, webbrowser
import soundfile as sf
import uvicorn
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import biblioteca as bib, motor_voz as mv

AQUI = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(AQUI, 'web')
SAIDA = os.path.join(bib.RAIZ, 'saidas')
PORTA = int(os.environ.get('DUBLE_PORTA', '7860'))
FRASE = ('Eu, [nome completo], autorizo o Lindson Almeida a usar a minha imagem e a minha voz para '
         'criar conteúdo com inteligência artificial para [finalidade], até [data]. Hoje é [data de hoje].')

app = FastAPI(title='Dublê', docs_url=None, redoc_url=None)
_trava = threading.Lock()                     # uma geração por vez (a placa tem 4 GB)
_prog = {'ativo': False, 'feito': 0, 'total': 0, 'texto': ''}


def _saidas():
    if not os.path.isdir(SAIDA): return []
    arqs = sorted((f for f in os.listdir(SAIDA) if f.endswith('.wav')), reverse=True)
    out = []
    for f in arqs[:30]:
        try: d = sf.info(os.path.join(SAIDA, f)).duration
        except Exception: d = 0
        out.append({'arquivo': f, 'duracao': round(d, 1), 'dublê': f.rsplit('-', 2)[0]})
    return out


@app.get('/api/estado')
def estado():
    dubles = []
    for pid, p in bib.lista().items():
        ok, motivo = bib.liberado(p)
        dubles.append({'id': pid, 'nome': p['nome'], 'tipo': p['tipo'], 'liberado': ok, 'motivo': motivo,
                       'validade': p.get('validade', ''), 'atualizado': p.get('atualizado', '')})
    s = _saidas()
    return {'dubles': dubles, 'saidas': s, 'tipos': bib.TIPOS, 'frase': FRASE,
            'segundos': round(sum(x['duracao'] for x in s), 1)}


def _tmp(up):
    if not up or not up.filename: return None
    d = tempfile.mkdtemp(); c = os.path.join(d, os.path.basename(up.filename))
    with open(c, 'wb') as f: shutil.copyfileobj(up.file, f)
    return c


def _wav(c):
    """Amostra gravada no microfone do navegador vem em webm/ogg: vira wav para o motor de voz."""
    if not c or os.path.splitext(c)[1].lower() in ('.wav', '.mp3', '.flac'): return c
    o = os.path.splitext(c)[0] + '.wav'
    subprocess.run([mv.ffmpeg(), '-y', '-loglevel', 'error', '-i', c, '-ac', '1', '-ar', '44100', o], check=True)
    return o


@app.post('/api/dubles')
def salvar(nome: str = Form(...), tipo: str = Form(...), validade: str = Form(''), fonte: str = Form(''),
           amostra: UploadFile = File(None), termo: UploadFile = File(None),
           video: UploadFile = File(None), base: UploadFile = File(None)):
    try:
        pid, ok, motivo = bib.cadastra(nome, tipo, _wav(_tmp(amostra)), _tmp(termo), _tmp(video), validade, fonte, _tmp(base))
    except ValueError as e:
        raise HTTPException(400, str(e))
    return {'id': pid, 'liberado': ok,
            'aviso': 'Dublê salvo e liberado.' if ok else 'Dublê salvo, mas bloqueado: ' + motivo}


@app.delete('/api/dubles/{pid}')
def apagar(pid: str):
    bib.apaga(pid); return {'ok': True}


class Pedido(BaseModel):
    id: str
    texto: str
    emocao: float = 0.5
    humano: bool = True


@app.get('/api/progresso')
def progresso(): return _prog


@app.post('/api/voz')
def voz(p: Pedido):
    d = bib.lista().get(p.id)
    if not d: raise HTTPException(400, 'Escolha um dublê na Biblioteca.')
    ok, motivo = bib.liberado(d)
    if not ok: raise HTTPException(403, 'Esse dublê está bloqueado: ' + motivo + ' Resolva na Biblioteca.')
    if not p.texto.strip(): raise HTTPException(400, 'Escreva o texto.')
    if not _trava.acquire(blocking=False): raise HTTPException(409, 'Já tem uma voz sendo gerada. Espere terminar.')
    try:
        _prog.update(ativo=True, feito=0, total=len(mv.frases(p.texto)) or 1, texto='Carregando o modelo de voz…')
        def cb(par, desc=''): _prog.update(feito=par[0], total=par[1], texto=desc)
        a = mv.narrar(p.texto, d['amostra_voz'], p.emocao, humanizar=p.humano, progresso=cb)
        os.makedirs(SAIDA, exist_ok=True)
        nome = f"{p.id}-{dt.datetime.now():%Y%m%d-%H%M%S}.wav"
        sf.write(os.path.join(SAIDA, nome), a, mv.S)
        seg = round(len(a) / mv.S, 1)
        return {'arquivo': nome, 'duracao': seg,
                'aviso': f'Pronto: {seg:.1f} s de áudio. Feito com IA: avise o público quando parecer real.'}
    finally:
        _prog.update(ativo=False); _trava.release()


@app.get('/api/saidas/{arquivo}')
def baixar(arquivo: str):
    c = os.path.join(SAIDA, os.path.basename(arquivo))
    if not os.path.isfile(c): raise HTTPException(404, 'Áudio não encontrado.')
    return FileResponse(c, media_type='audio/wav', filename=os.path.basename(c))


@app.get('/')
def inicio(): return FileResponse(os.path.join(WEB, 'index.html'))


app.mount('/identidade', StaticFiles(directory=os.path.join(AQUI, 'identidade')), name='identidade')
app.mount('/web', StaticFiles(directory=WEB), name='web')

if __name__ == '__main__':
    if os.environ.get('DUBLE_SEM_NAVEGADOR') != '1':
        threading.Timer(1.5, lambda: webbrowser.open(f'http://127.0.0.1:{PORTA}')).start()
    print(f'Dublê aberto em http://127.0.0.1:{PORTA} (feche esta janela para desligar)')
    uvicorn.run(app, host='127.0.0.1', port=PORTA, log_level='warning')
