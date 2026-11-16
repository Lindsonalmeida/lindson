# Al Kántara Group v2 · símbolo "Pedra-chave" (conta Pedro, 16/11/2026)
# Aduela-chave (trapézio do topo de um arco: al-qantara = a ponte/o arco). As juntas entre 4 pedras desenham um K.
# 4 pedras = 4 divisões (Labs, Studio, Media, Ventures); a chave inteira = o Group.
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
U = 24  # grid de construção 24 x 24
KEY = Polygon([(0,0),(24,0),(19,24),(5,24)])
G = 1.6  # largura da junta (1,6 módulo)
XV = 9.0; JY = 12.0
juntas = [LineString([(XV,-1),(XV,25)]), LineString([(XV,JY),(21.6,-1.6)]), LineString([(XV,JY),(20.4,25.6)])]
def pecas():
    cut = unary_union([l.buffer(G/2, cap_style=2, join_style=2) for l in juntas])
    d = KEY.difference(cut)
    ps = sorted(d.geoms, key=lambda p: (round(p.centroid.x>XV), p.centroid.y))
    # ordem: haste (Labs), topo (Studio), meio (Media), base (Ventures)
    return ps
def path(p, s=1, ox=0, oy=0):
    c = list(p.exterior.coords)
    return 'M' + ' L'.join(f'{ox+x*s:.2f},{oy+y*s:.2f}' for x,y in c[:-1]) + ' Z'
if __name__ == '__main__':
    for i,p in enumerate(pecas()): print(i, [tuple(round(v,2) for v in c) for c in p.exterior.coords])
