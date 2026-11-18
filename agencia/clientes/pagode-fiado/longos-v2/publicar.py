# Título, descrição (com a letra) e tags de cada longo v2, no padrão do roteiro do clipe:
# "Pagode Fiado - <Faixa> (Ao Vivo no Bar do Seu Tião)". Gera publicar.json.
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(AQUI + '/letras.json'))
ORDEM = sorted(L); out = {}
FAIXAS = ' · '.join(f"{k} {L[k]['titulo']}" for k in ORDEM)
for i, k in enumerate(ORDEM):
    f = L[k]; prox = L[ORDEM[i + 1]]['titulo'] if i + 1 < len(ORDEM) else None
    letra, ult = [], None
    for parte, quem, txt in f['linhas']:
        if parte != ult: letra.append(''); ult = parte
        letra.append(f'{quem}: "{txt}"' if parte == 'Fala' else txt)
    d = (f"{f['titulo']}, {'o prólogo' if k == '00' else 'faixa ' + k} do Álbum 01 \"Copo Americano\" do Pagode Fiado, ao vivo no Bar do Seu Tião.\n\n"
         f"{f['cap']}: {f['historia']}\n\n"
         + (f"Próximo capítulo: {prox}\n\n" if prox else "Fim do Álbum 01. Pendura na conta!\n\n")
         + "Letra:\n" + '\n'.join(letra).strip() + "\n\n"
         f"Álbum 01 · Copo Americano: {FAIXAS}\n\n"
         "🍺 Pendura na conta: inscreva-se e ative o sininho. Toda sexta tem roda no Bar do Seu Tião.\n\n#pagode #pagoderomantico #pagodefiado")
    out[k] = dict(titulo=f"Pagode Fiado - {f['titulo']} (Ao Vivo no Bar do Seu Tião)", descricao=d,
                  tags=['pagode', 'pagode romântico', 'pagode 2026', 'pagode ao vivo', 'roda de pagode', 'sofrência', 'pagode fiado', f['titulo'].lower(), 'bar do seu tião', 'copo americano'],
                  lembrete='No upload: marcar "conteúdo alterado ou sintético" (regra do projeto).')
json.dump(out, open(AQUI + '/publicar.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
