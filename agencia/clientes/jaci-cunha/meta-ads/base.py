import re
VINHO, OURO, CAFE, CREME = '#6E1A2A', '#B9A27A', '#5A4033', '#F3EADD'
def md(s):  # **bold** e _itálico serif_
    s = str(s).replace('\n', '<br>')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s); return re.sub(r'_(.+?)_', r'<i class="S">\1</i>', s)
F='FOTOS'
def foto(arq, pos='50% 30%', extra=''): return f'<img class="a bg" src="{F}/{arq}" style="object-position:{pos};{extra}">'
def topo(cor='#fff'):
    return (f'<div class="a topo" style="color:{cor}"><span><b>CLINICA.</b>DRA<b>JACI</b>CUNHA<i class="ok">✓</i></span><span>CIRURGIÃ-DENTISTA</span><span>@clinica.dra<b>jaci</b>cunha</span></div>')
def rodape(cor='#fff', centro=False):
    if centro: return f'<div class="a rod c" style="color:{cor}">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA DO VIVA - ZÉ DOCA/MA.</small></div>'
    return (f'<div class="a rod" style="color:{cor}"><div>DRA JACI CUNHA<br><small>HARMONIZAÇÃO FACIAL<br>@clinica.drajacicunha</small></div>'
            f'<div style="text-align:right">CLÍNICA DRA. JACI CUNHA<br><small>AV. MILITAR, EM FRENTE À PRAÇA<br>DO VIVA - ZÉ DOCA/MA.</small></div></div>')
def pontos(i, n, cor='#fff'): return f'<div class="a dots">{"".join(f"<i style=\'background:{cor};opacity:{1 if k == i else .4}\'></i>" for k in range(n))}</div>'
ARR = '<div class="a arr" style="color:{c}"><b>ARRASTE</b> PARA O LADO</div>'

CSS = """<style>*{margin:0;padding:0;box-sizing:border-box} body{background:#222} .f{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px;background:#ddd} .a{position:absolute}
.bg{inset:0;width:1080px;height:1350px;object-fit:cover} .S{font-family:'Playfair Display';font-style:italic} .sans{font-family:Poppins;font-size:30px;letter-spacing:.01em} .sans b{font-weight:700}
.topo{left:88px;right:88px;top:96px;display:flex;justify-content:space-between;font-family:Poppins;font-size:20px;letter-spacing:.02em;font-weight:400} .topo b{font-weight:700} .ok{font-style:normal;display:inline-grid;place-items:center;width:15px;height:15px;border-radius:50%;background:#3897F0;color:#fff;font-size:9px;margin-left:6px;vertical-align:4px}
.rod{left:88px;right:88px;top:1210px;display:flex;justify-content:space-between;font-family:Poppins;font-size:17px;letter-spacing:.08em;line-height:1.25} .rod small{font-size:12.5px;opacity:.75;letter-spacing:.06em} .rod.c{display:block;text-align:center;top:1240px}
.big{font-size:190px;line-height:.9;font-weight:400} .balao{display:inline-block;background:#fff;color:#222;font-family:Poppins;font-size:24px;line-height:1.15;padding:12px 22px;border-radius:18px;position:relative;margin-left:340px;margin-bottom:-14px} .balao b{font-weight:700}
.balao:after{content:"";position:absolute;left:30px;bottom:-12px;border:8px solid transparent;border-top-color:#fff;border-left-color:#fff}
.arr{left:88px;top:1210px;font-family:Poppins;font-size:22px} .arr b,.arr2 b{font-weight:700} .arr2{font-family:Poppins;font-size:20px;color:#fff;margin-top:12px} .u{text-decoration:underline;text-underline-offset:6px}
.fio{display:flex;align-items:center;justify-content:center;gap:0;margin:12px auto} .fio span{background:linear-gradient(90deg,rgba(185,162,122,.9),rgba(185,162,122,.75));color:#fff;padding:2px 26px 8px} .fio i{width:60px;height:2px;background:{OURO};position:relative} .fio i:first-child:before,.fio i:last-child:after{content:"";position:absolute;top:-4px;width:10px;height:10px;border-radius:50%;background:{OURO}} .fio i:first-child:before{left:-4px} .fio i:last-child:after{right:-4px}
.faixa{display:inline;background:rgba(170,150,120,.72);color:#fff;padding:0 18px 4px;box-decoration-break:clone;-webkit-box-decoration-break:clone;line-height:1.25}
.fv{display:inline-block;background:{VINHO};color:#fff;font-family:Poppins;font-size:44px;font-weight:400;padding:2px 16px;margin-top:6px;letter-spacing:.01em;text-transform:uppercase} .fv b{font-weight:700}
.tit{font-family:Poppins;font-weight:700;font-size:56px;line-height:1.1;text-transform:uppercase;text-align:center;margin-bottom:40px} .tit b{font-weight:800}
.li{display:flex;gap:24px;align-items:flex-start;font-family:Poppins;font-size:37px;line-height:1.25;margin-bottom:34px} .li i{flex:none;display:grid;place-items:center;width:46px;height:46px;border:2.5px solid #2F5B3A;border-radius:50%;color:#2F5B3A;font-style:normal;font-size:24px;margin-top:-2px} .li b{font-weight:700}
.tx{font-family:Poppins;font-size:42px;line-height:1.35;text-align:center} .tx b{font-weight:700} .nota{font-size:30px;text-align:center;margin-top:40px;line-height:1.2}
.mv{margin-bottom:38px;text-align:center} .mv .fv{font-size:40px} .mv p{font-family:Poppins;font-size:36px;line-height:1.3;margin-top:14px} .mv b{font-weight:700}
.pill{display:inline-block;margin-top:34px;border:2px solid #fff;border-radius:999px;padding:12px 30px;font-family:Poppins;font-size:24px;color:#fff;letter-spacing:.02em}
.esq .tx,.esq .mv,.esq .mv p{text-align:left} .esq .li{font-size:31px} .esq .tx{font-size:34px} .inv .tx{text-align:left} .inv .mv{text-align:left} .inv .tit{text-align:left} .dots{right:88px;top:1170px;display:flex;gap:8px} .dots i{width:12px;height:12px;border-radius:50%;display:block}
</style>"""

for _k,_v in [('VINHO',VINHO),('OURO',OURO),('CAFE',CAFE),('CREME',CREME)]: CSS = CSS.replace('{'+_k+'}', _v)
