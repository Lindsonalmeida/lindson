# Vídeo longo do álbum completo (00 a 10 em sequência, ~38 min) e capítulos do YouTube.
# Junta os longos v2 sem recodificar (mesmo formato) e escreve album-capitulos.txt.
# Uso: python3 montar-album.py <pasta_trabalho>
import json, sys, os, subprocess
W = sys.argv[1]; AQUI = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(AQUI + '/letras.json'))
ks = sorted(L); lista = f'{W}/album.txt'; t = 0.0; caps = []
with open(lista, 'w') as f:
    for k in ks:
        v = f'{W}/pagode-fiado-{k}-v2.mp4'; f.write(f"file '{v}'\n")
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', v], capture_output=True, text=True).stdout)
        m, s = divmod(int(t), 60); caps.append(f'{m}:{s:02d} {k} · {L[k]["titulo"]}'); t += d
saida = f'{W}/pagode-fiado-album-01-copo-americano-ao-vivo.mp4'
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lista, '-c', 'copy', '-movflags', '+faststart', saida], check=True)
txt = ('Pagode Fiado - Álbum Copo Americano Completo (Ao Vivo no Bar do Seu Tião)\n\n'
       'A história de Davi e Lívia, contada no Bar do Seu Tião, do prólogo até a última roda. 11 faixas, uma história só.\n\nCapítulos:\n' + '\n'.join(caps) +
       '\n\n🍺 Pendura na conta: inscreva-se e ative o sininho.\n\n#pagode #pagoderomantico #pagodefiado')
open(AQUI + '/album-capitulos.txt', 'w').write(txt); print(saida, round(t / 60, 1), 'min'); print(txt)
