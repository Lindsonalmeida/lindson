"""Passaporte: capas CLARAS dos Shorts (substituem as escuras da 1ª versão).
Imagem = gravura da 1ª cena do Short em pintura.json; texto de até 3 palavras abaixo.
python3 capas_shorts_claras.py [short-02 ...]  -> passaporte/capas/<id>.jpg (fora do Git, como os vídeos)"""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.join(D, '..')
sys.path.insert(0, os.path.join(RAIZ, '..', 'comum')); from capa_short import gerar

TEXTO = {'short-02': 'Comece por aqui', 'short-03': 'Travou em Levítico?', 'short-04': 'Não recomece', 'short-05': 'Sono lendo?',
         'short-06': 'Rute', 'short-07': 'Jonas e Jesus', 'short-08': '6 paradas', 'short-09': 'Tanto nome?', 'short-10': 'Apocalipse dá medo?',
         'short-11': 'Forte e fraco', 'short-12': 'O detalhe', 'short-13': '1 por dia', 'short-14': 'Meu próximo?', 'short-15': 'Escravo a governador',
         'short-16': 'Elias cansou', 'short-17': 'Ossos vivem?', 'short-18': 'Por que Isaque?', 'short-19': 'Por que afundou?', 'short-20': 'Salmos pra dor'}
IMG = {'short-07': '054'}  # evita repetir a gravura do short-04
spec = {v['id']: v for v in json.load(open(os.path.join(RAIZ, 'pintura.json')))}
ids = sys.argv[1:] or list(TEXTO)
gerar([dict(img=f"{RAIZ}/dore/{IMG.get(k) or spec[k]['cenas'][0]['gravura']}.jpg", texto=TEXTO[k], marca='PASSAPORTE DA BÍBLIA',
            saida=f'{RAIZ}/capas/{k}.jpg') for k in ids])
