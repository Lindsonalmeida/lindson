#!/usr/bin/env python3
# Põe a aba "SDR · Prospecção" (time de SDR, conta Pedro 22/11/2026) no painel/admin.html montado: link no menu (grupo Minha agência)
# e o script ../admin-sdr.js entre marcadores. Idempotente: rodar de novo só troca o bloco. Chamado pelo montar-site.py.
# Uso avulso: python3 injetar_sdr.py /home/user/centrallindsonalmeida/painel/admin.html
import os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
LINK = '<a href="#sdr" data-v="sdr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 4h18l-7 8v6l-4 2v-8z"/></svg>SDR · Prospecção</a>'
def injetar_sdr(caminho):
    h = open(caminho, encoding='utf-8').read()
    js = open(os.path.join(D, '..', 'admin-sdr.js'), encoding='utf-8').read().replace('</', '<\\/')
    if 'data-v="sdr"' not in h:
        h, n = re.subn(r'(<h4>Minha agência</h4>)', r'\1' + LINK.replace('\\', '\\\\'), h, count=1)
        if not n: raise SystemExit('Grupo "Minha agência" não achado no menu do admin.')
    bloco = '<!--sdr-time-->\n<script>\n' + js + '</script>\n<!--/sdr-time-->'
    if '<!--sdr-time-->' in h: h = re.sub(r'<!--sdr-time-->.*?<!--/sdr-time-->', lambda m: bloco, h, flags=re.S)
    elif '</body>' in h: h = h.replace('</body>', bloco + '\n</body>', 1)
    else: h = h.rstrip('\n') + '\n' + bloco + '\n'
    open(caminho, 'w', encoding='utf-8').write(h)
    return 'ok'
if __name__ == '__main__': print('aba SDR:', injetar_sdr(sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida/painel/admin.html'))
