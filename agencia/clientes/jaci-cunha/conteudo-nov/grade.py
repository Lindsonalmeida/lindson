# Prévia da grade do perfil (3 colunas, mais novo em cima) com os carrosséis de ../instagram-nov (conta Leandro)
import json, sys
from PIL import Image
T = json.load(open('textos.json')); O = ['r01','c1','r02','r03','r04','r05','c2','r06','r07','r08','r09','c3','r10','r11','d02','r12','d01','r13','c4','r14','r15','d03','r16']
arq = lambda i: f'../instagram-nov/{i}-1.jpg' if i.startswith('c') else f'feed/{i}.jpg'
O = O[::-1]; w, h, g = 360, 450, 6; o = Image.new('RGB', (3 * w + 2 * g, ((len(O) + 2) // 3) * (h + g)), 'white')
for n, i in enumerate(O): o.paste(Image.open(arq(i)).convert('RGB').resize((w, h)), ((n % 3) * (w + g), (n // 3) * (h + g)))
o.save(sys.argv[1] if len(sys.argv) > 1 else 'previa-grade.jpg', quality=88)
