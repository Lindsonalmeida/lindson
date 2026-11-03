"""Biblioteca de rostos e vozes do Clone Studio, com a trava de consentimento.
Regra (pesquisa em conteudo/referencias/ia-video-voz/, copiada de HeyGen, ElevenLabs, Synthesia e Tavus):
- Lindson e clientes: só gera com TERMO assinado + VÍDEO DE CONSENTIMENTO + validade em dia.
- Personagem (domínio público ou voz sintética): só gera com a FONTE registrada (obra, autor, licença).
Tudo fica na pasta `dados/` do computador do Lindson, fora do GitHub (repositório público)."""
import datetime as dt, json, os, re, shutil, unicodedata

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados')
TIPOS = ['Lindson', 'Cliente com autorização', 'Personagem (domínio público)']


def _slug(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-') or 'sem-nome'


def _arq(): return os.path.join(RAIZ, 'biblioteca.json')


def lista():
    if not os.path.exists(_arq()): return {}
    return json.load(open(_arq(), encoding='utf-8'))


def _salva(b):
    os.makedirs(RAIZ, exist_ok=True)
    json.dump(b, open(_arq(), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def _copia(origem, pid, nome):
    if not origem: return ''
    d = os.path.join(RAIZ, pid); os.makedirs(d, exist_ok=True)
    destino = os.path.join(d, nome + os.path.splitext(origem)[1].lower())
    shutil.copyfile(origem, destino); return destino


def cadastra(nome, tipo, amostra_voz, termo=None, video_consentimento=None, validade='', fonte='', video_base=None):
    if not nome.strip(): raise ValueError('Dê um nome.')
    if tipo not in TIPOS: raise ValueError('Escolha o tipo.')
    if not amostra_voz: raise ValueError('Envie a amostra de voz (10 s a 2 min, voz limpa, sem música).')
    b = lista(); pid = _slug(nome)
    p = b.get(pid, {})
    p.update(nome=nome.strip(), tipo=tipo, validade=validade.strip(), fonte=fonte.strip(),
             atualizado=dt.datetime.now().isoformat(timespec='minutes'))
    p['amostra_voz'] = _copia(amostra_voz, pid, 'amostra-voz')
    if termo: p['termo'] = _copia(termo, pid, 'termo-assinado')
    if video_consentimento: p['video_consentimento'] = _copia(video_consentimento, pid, 'video-consentimento')
    if video_base: p['video_base'] = _copia(video_base, pid, 'video-base')
    b[pid] = p; _salva(b)
    ok, motivo = liberado(p)
    return pid, ok, motivo


def liberado(p):
    """(pode gerar?, motivo). É a trava do app: nada sai sem consentimento."""
    if p['tipo'].startswith('Personagem'):
        return (True, 'Personagem com fonte registrada.') if p.get('fonte') else (False, 'Falta registrar a fonte (obra, autor e licença).')
    if not p.get('termo'): return False, 'Falta o termo de autorização assinado.'
    if not p.get('video_consentimento'): return False, 'Falta o vídeo de consentimento (a própria pessoa autorizando, com nome e data).'
    if p.get('validade'):
        try:
            if dt.date.fromisoformat(p['validade']) < dt.date.today(): return False, 'O termo venceu em ' + p['validade'] + '.'
        except ValueError:
            return False, 'Validade em formato errado (use AAAA-MM-DD).'
    return True, 'Termo e consentimento em dia.'


def apaga(pid):
    b = lista(); b.pop(pid, None); _salva(b)
    shutil.rmtree(os.path.join(RAIZ, pid), ignore_errors=True)
