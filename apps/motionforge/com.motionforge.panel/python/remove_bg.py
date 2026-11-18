"""Remoção de fundo local.
Ref: https://github.com/danielgatis/rembg
Instalar: pip install "rembg[gpu]" pillow   (ou "rembg[cpu]")
Uso: python remove_bg.py entrada.png saida.png [modelo]
Modelos: u2net, isnet-general-use, birefnet-general, birefnet-portrait ...
"""
import sys
from PIL import Image
from rembg import new_session, remove

def main():
    src, dst = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "birefnet-general"
    session = new_session(model)
    remove(Image.open(src), session=session).save(dst)
    print("ok")

if __name__ == "__main__":
    main()
