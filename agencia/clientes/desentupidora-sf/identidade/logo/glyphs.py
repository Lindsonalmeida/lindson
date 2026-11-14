# Converte texto em caminho SVG (Montserrat), para a logo não depender de fonte instalada.
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
F='/home/user/lindson/agencia/clientes/desentupidora-sf/identidade/manual/'
_c={}
def font(n):
    if n not in _c: _c[n]=TTFont(F+n)
    return _c[n]
def text_path(txt,fontfile,size,x,y,track=0):
    f=font(fontfile);gs=f.getGlyphSet();cmap=f.getBestCmap();upm=f['head'].unitsPerEm
    s=size/upm;pen=SVGPathPen(gs);cx=0
    for ch in txt:
        g=cmap[ord(ch)];tp=TransformPen(pen,(s,0,0,-s,x+cx,y));gs[g].draw(tp)
        cx+=gs[g].width*s+track
    return pen.getCommands(),cx-track
def width(txt,fontfile,size,track=0):
    return text_path(txt,fontfile,size,0,0,track)[1]
