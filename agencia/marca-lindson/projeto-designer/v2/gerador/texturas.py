# Projeto Designer v2 (conta Leandro, 16/11/2026): texturas das marcas para os mockups 3D.
# Usa o logo e a paleta oficiais do brand book (agencia/processos/brand-book-premium/gerar.py).
# Uso: BB_TMP=<tmp> python3 texturas.py <saida>
import sys, os, importlib.util, html
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bb', os.path.join(HERE, '../../../../processos/brand-book-premium/gerar.py'))
_src = open(spec.origin).read().replace("L = '/home/user/lindson/agencia'", "L = %r" % os.path.abspath(os.path.join(HERE, '../../../..'))).replace("DB = '/home/user/lindson/apps", "DB = %r + '" % os.path.abspath(os.path.join(HERE, '../../../../../apps')) + "")
import types; bb = types.ModuleType('bb'); bb.__file__ = spec.origin; exec(compile(_src, spec.origin, 'exec'), bb.__dict__)
OUT = os.path.abspath(sys.argv[1])
MARCAS = {'leo': 'Leo Pinto', 'realtime': 'Real Time', 'curso': 'Processo Legislativo', 'wf': 'WF Celulares', 'oregano': 'Orégano Turbo', 'duble': 'Dublê'}
# frase curta de cada marca (do brand book). Leo: sem conteúdo de campanha.
FRASE = {'leo': 'Identidade visual 2026.', 'realtime': 'No ar, agora.', 'curso': 'Chega de improviso na câmara.',
         'wf': 'Procedência que dá para ver.', 'oregano': 'Uma folha que sobe.', 'duble': 'Só grava quem disse sim.'}
HANDLE = {'leo': 'leopinto', 'realtime': 'realtimefulljobs', 'curso': 'processolegislativo', 'wf': 'wfcelulares', 'oregano': 'oreganoturbo', 'duble': 'duble.app'}

def page(k):
    c = bb.C[k]; e = html.escape
    up = 'uppercase' if c['up'] else 'none'
    L = c['logo']; LOGO = f'file://{OUT}/{k}/logo.png'
    disp = f"font-family:{c.get('serif') or c['disp']};font-style:{'italic' if c.get('serif') else 'normal'};font-weight:{400 if c.get('serif') else c['dw']}"
    grain = ""
    def tile(i):
        t = [f'<div style="width:100%;height:100%;background:{c["bg"]};display:grid;place-items:center"><div style="width:260px;height:124px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>',
             f'<div style="width:100%;height:100%;background:{c["ac"]};color:{c["on_ac"]};display:flex;align-items:flex-end;padding:9%;font:{c["dw"]} 48px/0.95 {c["disp"]};text-transform:{up}">{e(FRASE[k])}</div>',
             f'<div style="width:100%;height:100%;display:grid;grid-template-rows:5fr 3fr 2fr"><i style="background:{c["bg"]}"></i><i style="background:{c["bg2"]}"></i><i style="background:{c["ac"]}"></i></div>',
             f'<div style="width:100%;height:100%;background:{c["bg2"]};color:{c["fg"]};display:grid;place-items:center;font:{c["dw"]} 230px/1 {c["disp"]}">Aa</div>',
             f'<div style="width:100%;height:100%;background:{c["fg"]};display:grid;place-items:center;padding:22%"><div style="filter:invert(1) hue-rotate(180deg);width:220px;height:105px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>',
             f'<div style="width:100%;height:100%;background:{c["bg"]};color:{c["fg"]};padding:10%;display:flex;flex-direction:column;justify-content:space-between"><div style="font:600 22px {c["mono"]};letter-spacing:.2em;color:{c["ac"]}">{e(MARCAS[k].upper())}</div><div style="{disp};font-size:46px;line-height:1">{e(c["essencia"][0])}</div></div>',
             f'<div style="width:100%;height:100%;background:{c["ac2"]};display:grid;place-items:center"><div style="width:220px;height:105px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>',
             f'<div style="width:100%;height:100%;background:{c["bg2"]};color:{c["fg"]};padding:10%;display:flex;align-items:center;{disp};font-size:48px;line-height:1">{e(c["essencia"][1])}</div>',
             f'<div style="width:100%;height:100%;background:{c["bg"]};display:grid;place-items:center"><div style="width:62%;aspect-ratio:1;border-radius:50%;border:3px solid {c["ac"]};display:grid;place-items:center"><div style="width:170px;height:81px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div></div>']
        return t[i % 9]
    grid = ''.join(f'<div style="aspect-ratio:1;overflow:hidden">{tile(i)}</div>' for i in range(9))
    ig = f'''<div id="ig" style="width:1170px;height:2532px;background:#000;color:#fff;font-family:Inter,sans-serif;position:relative;overflow:hidden">
<div style="height:150px"></div><div style="display:flex;justify-content:space-between;padding:0 40px;font:700 44px Inter">{HANDLE[k]}<span>≡</span></div>
<div style="display:flex;align-items:center;gap:60px;padding:40px">
<div style="width:250px;height:250px;border-radius:50%;background:{c["bg"]};display:grid;place-items:center;box-shadow:0 0 0 6px #000,0 0 0 10px {c["ac"]}"><div style="width:170px;height:81px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>
<div style="display:flex;gap:70px;font:700 44px Inter;text-align:center"><div>9<br><span style="font:400 32px Inter">posts</span></div><div>&nbsp;<br><span style="font:400 32px Inter">seguidores</span></div><div>&nbsp;<br><span style="font:400 32px Inter">seguindo</span></div></div></div>
<div style="padding:0 40px;font:700 38px Inter">{e(MARCAS[k])}</div><div style="padding:6px 40px;font:400 36px/1.35 Inter;color:#ddd">{e(c["sub"])}<br>{e(FRASE[k])}</div>
<div style="display:flex;gap:16px;padding:30px 40px"><div style="flex:1;background:#262626;border-radius:16px;padding:22px;text-align:center;font:600 34px Inter">Seguir</div><div style="flex:1;background:#262626;border-radius:16px;padding:22px;text-align:center;font:600 34px Inter">Mensagem</div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-top:20px">{grid}</div></div>'''
    els = f'''
<div id="logo" style="width:1120px;padding:60px;display:inline-block"><div style="width:1000px">{L}</div></div>
<div id="card_front" style="width:1050px;height:600px;background:{c["bg"]};display:grid;place-items:center;{grain}"><div style="width:560px;height:268px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>
<div id="card_back" style="width:1050px;height:600px;background:{c["ac"]};color:{c["on_ac"]};padding:70px;display:flex;flex-direction:column;justify-content:space-between;{grain}">
 <div style="font:600 22px {c["mono"]};letter-spacing:.3em">{e(MARCAS[k].upper())}</div><div style="font:{c["dw"]} 74px/0.95 {c["disp"]};text-transform:{up};max-width:820px">{e(FRASE[k])}</div></div>
<div id="letter" style="width:1240px;height:1754px;background:#F4F1EA;position:relative"><div style="padding:70px 0;background:{c["bg"]};display:grid;place-items:center"><div style="width:400px;height:192px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>
 <div style="padding:110px 120px;display:grid;gap:26px">{''.join(f'<i style="display:block;height:14px;background:#00000014;width:{w}%"></i>' for w in [40,100,96,100,88,100,72,0,100,93,100,60])}</div>
 <div style="position:absolute;bottom:0;left:0;right:0;height:22px;background:{c["ac"]}"></div></div>
<div id="env" style="width:1600px;height:800px;background:{c["bg2"]};position:relative;{grain}"><div style="position:absolute;left:90px;top:80px;width:380px;height:182px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div><div style="position:absolute;right:0;bottom:0;width:100%;height:16px;background:{c["ac"]}"></div></div>
<div id="poster" style="width:1200px;height:1700px;background:{c["bg"]};color:{c["fg"]};padding:110px;display:flex;flex-direction:column;justify-content:space-between;{grain}">
 <div style="width:520px;height:249px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div><div style="{disp};font-size:150px;line-height:.95;text-transform:{up if not c.get('serif') else 'none'};color:{c["fg"]}">{e(FRASE[k])}</div>
 <div style="display:flex;justify-content:space-between;font:600 26px {c["mono"]};letter-spacing:.2em;color:{c["ac"]}"><span>{e(MARCAS[k].upper())}</span><span>@{HANDLE[k]}</span></div></div>
<div id="bill" style="width:2400px;height:800px;background:{c["bg"]};color:{c["fg"]};display:grid;grid-template-columns:1fr 1.1fr;align-items:center;padding:0 140px;gap:120px;{grain}">
 <div style="height:430px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div><div style="{disp};font-size:130px;line-height:.95;text-transform:{up if not c.get('serif') else 'none'}">{e(FRASE[k])}</div></div>
<div id="wrap" style="width:2048px;height:800px;background:{c["bg"]};display:grid;place-items:center;{grain}"><div style="width:420px;height:201px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>
<div id="box" style="width:1600px;height:1600px;background:{c["bg"]};display:grid;place-items:center;{grain}"><div style="width:780px;height:374px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>
<div id="side" style="width:1600px;height:400px;background:{c["ac"]};color:{c["on_ac"]};display:flex;align-items:center;padding:0 80px;font:{c["dw"]} 90px {c["disp"]};text-transform:{up}">{e(FRASE[k])}</div>
<div id="sign" style="width:2000px;height:640px;background:{c["bg"]};display:grid;place-items:center"><div style="width:1100px;height:528px"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain"></div></div>
{ig}'''
    return f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family={c["fonts"]}&family=Inter:wght@400;600;700&display=swap" rel="stylesheet"><style>*{{box-sizing:border-box;margin:0}}body{{background:transparent;color:{c["fg"]}}}body>div{{margin-bottom:20px}}i{{font-style:normal}}img{{max-width:100%}}</style></head><body>{els}</body></html>'

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
        p = b.new_page(viewport={'width': 2600, 'height': 1200})
        for k in (sys.argv[2:] or MARCAS):
            hp = os.path.join(OUT, k + '.html'); open(hp, 'w').write(page(k))
            p.goto('file://' + hp, wait_until='networkidle'); p.evaluate('document.fonts.ready'); p.wait_for_timeout(500)
            os.makedirs(f'{OUT}/{k}', exist_ok=True)
            p.query_selector('#logo').screenshot(path=f'{OUT}/{k}/logo.png', omit_background=True)
            from PIL import Image
            im = Image.open(f'{OUT}/{k}/logo.png'); im.crop(im.getbbox()).save(f'{OUT}/{k}/logo.png')  # logo recortado rente
            p.goto('file://' + hp, wait_until='networkidle'); p.evaluate('document.fonts.ready'); p.wait_for_timeout(500)
            for el in ['card_front', 'card_back', 'letter', 'env', 'poster', 'bill', 'wrap', 'box', 'side', 'sign', 'ig']:
                p.query_selector('#' + el).screenshot(path=f'{OUT}/{k}/{el}.png', omit_background=(el == 'logo'))
            print(k, 'ok')
        b.close()
