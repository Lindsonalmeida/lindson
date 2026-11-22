#!/usr/bin/env python3
# Põe a aba "Robôs" (todos os robôs e automações num lugar só; conta Leandro, 22/11/2026) no painel/admin.html montado:
# link no menu (grupo Minha agência, logo depois do SDR) e window.__ROBOS (../../robos/robos.json) + ../admin-robos.js entre marcadores.
# Idempotente. Chamado pelo montar-site.py depois do injetar_sdr. Não mexe na aba SDR (conta Pedro): só lê /api/sdr.
# Uso avulso: python3 injetar_robos.py /home/user/centrallindsonalmeida/painel/admin.html
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
LINK = '<a href="#robos" data-v="robos"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01M9.5 16.5h5M3 12v3M21 12v3"/></svg>Robôs</a>'
def injetar_robos(caminho):
    h = open(caminho, encoding='utf-8').read()
    dados = json.load(open(os.path.join(D, '..', '..', 'robos', 'robos.json'), encoding='utf-8'))
    js = ('window.__ROBOS=' + json.dumps(dados, ensure_ascii=False) + ';\n' + open(os.path.join(D, '..', 'admin-robos.js'), encoding='utf-8').read()).replace('</', '<\\/')
    if 'data-v="robos"' not in h:
        alvo = re.search(r'<a href="#sdr" data-v="sdr">.*?</a>', h, re.S)
        if alvo: h = h[:alvo.end()] + LINK + h[alvo.end():]
        else:
            h, n = re.subn(r'(<h4>Minha agência</h4>)', lambda m: m.group(1) + LINK, h, count=1)
            if not n: raise SystemExit('Grupo "Minha agência" não achado no menu do admin.')
    bloco = '<!--robos-->\n<script>\n' + js + '</script>\n<!--/robos-->'
    if '<!--robos-->' in h: h = re.sub(r'<!--robos-->.*?<!--/robos-->', lambda m: bloco, h, flags=re.S)
    elif '</body>' in h: h = h.replace('</body>', bloco + '\n</body>', 1)
    else: h = h.rstrip('\n') + '\n' + bloco + '\n'
    open(caminho, 'w', encoding='utf-8').write(h)
    return 'ok'
if __name__ == '__main__': print('aba Robôs:', injetar_robos(sys.argv[1] if len(sys.argv) > 1 else '/home/user/centrallindsonalmeida/painel/admin.html'))
