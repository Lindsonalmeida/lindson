# Mascote da Orégano Turbo: a folhinha de orégano de óculos de corrida e lenço ao vento (conta Leandro, 05/11/2026).
# Gera marca/mascote.svg (e variações de expressão). Uso: python3 mascote.py
VERDE, VERDE2, VERDE3, AMARELO, TOMATE, ASFALTO, CREME = '#2FA35A', '#1F8A4C', '#7BD08F', '#FFC81E', '#E8432E', '#141414', '#FFF3DC'
def mascote(boca='sorriso', olhar=(6, 0), velocidade=True):
    px, py = olhar
    bocas = {
      'sorriso': f'<path d="M158 252 Q200 300 244 250 Q238 286 200 290 Q164 288 158 252Z" fill="#6B1A12"/><path d="M168 256 Q200 270 234 255 L232 264 Q200 274 170 265Z" fill="#fff"/><path d="M180 282 Q200 292 222 281 Q210 272 196 274 Q186 276 180 282Z" fill="{TOMATE}"/>',
      'uau': f'<ellipse cx="202" cy="268" rx="22" ry="26" fill="#6B1A12"/><ellipse cx="202" cy="280" rx="13" ry="9" fill="{TOMATE}"/>',
      'piscada': f'<path d="M160 256 Q200 292 242 254" fill="none" stroke="#6B1A12" stroke-width="12" stroke-linecap="round"/>',
    }
    lentes = ''.join(f'''<circle cx="{x}" cy="176" r="40" fill="{AMARELO}"/><circle cx="{x}" cy="176" r="29" fill="#DFF4FF"/>
      <circle cx="{x + px}" cy="{178 + py}" r="13" fill="{ASFALTO}"/><circle cx="{x + px + 5}" cy="{173 + py}" r="4.5" fill="#fff"/>
      <path d="M{x - 18} {162} Q{x - 6} {150} {x + 8} {154}" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9"/>''' for x in (160, 244))
    if boca == 'piscada':
        lentes = lentes.replace(f'<circle cx="{244 + px}" cy="{178 + py}" r="13" fill="{ASFALTO}"/>', f'<path d="M230 180 Q244 170 258 180" fill="none" stroke="{ASFALTO}" stroke-width="8" stroke-linecap="round"/>')
    linhas = (f'<g stroke="{AMARELO}" stroke-width="14" stroke-linecap="round"><line x1="18" y1="150" x2="78" y2="150"/><line x1="4" y1="198" x2="70" y2="198"/><line x1="26" y1="246" x2="80" y2="246"/></g>' if velocidade else '')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 420">
{linhas}
<g transform="rotate(8 210 220)">
<path d="M120 300 C 70 312, 40 300, 20 318 C 46 330, 84 332, 128 320 Z" fill="{TOMATE}"/><path d="M118 316 C 70 344, 52 348, 34 368 C 70 370, 104 356, 132 330 Z" fill="#C7321F"/>
<path d="M210 384 C 214 400, 222 408, 236 414" fill="none" stroke="{VERDE2}" stroke-width="12" stroke-linecap="round"/>
<path d="M210 386 C 92 352, 70 176, 210 34 C 350 176, 328 352, 210 386 Z" fill="{VERDE}"/>
<path d="M210 386 C 328 352, 350 176, 210 34 C 268 150, 286 300, 210 386 Z" fill="{VERDE2}"/>
<path d="M210 140 C 208 110, 209 90, 210 72" fill="none" stroke="{VERDE3}" stroke-width="6" stroke-linecap="round" opacity=".55"/><path d="M210 372 C 207 356, 207 345, 208 334" fill="none" stroke="{VERDE3}" stroke-width="6" stroke-linecap="round" opacity=".55"/>
<path d="M100 296 Q210 344 318 290 L312 318 Q210 368 108 322 Z" fill="{TOMATE}"/>
<rect x="96" y="160" width="228" height="30" rx="15" fill="{ASFALTO}"/>
{lentes}
<rect x="196" y="166" width="12" height="20" rx="6" fill="{AMARELO}"/>
{bocas[boca]}
</g>
</svg>'''
if __name__ == '__main__':
    import os; os.makedirs('marca', exist_ok=True)
    open('marca/mascote.svg', 'w').write(mascote())
    open('marca/mascote-uau.svg', 'w').write(mascote('uau', (0, -4)))
    open('marca/mascote-piscada.svg', 'w').write(mascote('piscada', (6, 2)))
    open('marca/mascote-parado.svg', 'w').write(mascote(velocidade=False))
    print('ok')
