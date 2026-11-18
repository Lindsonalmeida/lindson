"""MotionForge · remoção de fundo local com rembg.
Ref: https://github.com/danielgatis/rembg
Instalar: pip install "rembg[gpu]" pillow   (ou "rembg[cpu]" sem placa NVIDIA)

Uso:
  python remove_bg.py entrada.png saida.png [modelo]           # uma imagem (compatível com o MVP)
  python remove_bg.py --batch pasta_in pasta_out [--model m]   # sequência (vídeo), mantém os nomes
  python remove_bg.py --check                                  # diagnóstico para a aba Config
  python remove_bg.py --prep entrada saida.jpg [--max 2048]    # reduz imagem para envio à nuvem

Modelos: birefnet-general, birefnet-general-lite, birefnet-portrait, isnet-general-use, u2net, u2netp, u2net_human_seg
Saída: uma linha JSON por evento em stdout ({"event": "progress", "done": 3, "total": 120} ...).
"""
import argparse
import json
import os
import sys
import time

IMG_EXT = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")


def emit(**kw):
    sys.stdout.write(json.dumps(kw, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def open_rgb(path):
    from PIL import Image, ImageOps
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
    return im


def make_session(model):
    from rembg import new_session
    return new_session(model)


def cut(session, src, dst):
    from rembg import remove
    out = remove(open_rgb(src), session=session)
    tmp = dst + ".tmp.png"
    out.save(tmp, "PNG")
    os.replace(tmp, dst)


def cmd_single(src, dst, model):
    t = time.time()
    emit(event="status", msg="carregando modelo " + model)
    s = make_session(model)
    emit(event="status", msg="processando")
    cut(s, src, dst)
    emit(event="done", out=dst, seconds=round(time.time() - t, 2))


def cmd_batch(src_dir, dst_dir, model):
    files = sorted(f for f in os.listdir(src_dir) if f.lower().endswith(IMG_EXT))
    if not files:
        raise SystemExit("nenhum frame em " + src_dir)
    os.makedirs(dst_dir, exist_ok=True)
    emit(event="status", msg="carregando modelo " + model)
    s = make_session(model)
    t = time.time()
    for i, f in enumerate(files, 1):
        dst = os.path.join(dst_dir, os.path.splitext(f)[0] + ".png")
        if not (os.path.exists(dst) and os.path.getsize(dst) > 0):  # retomável
            cut(s, os.path.join(src_dir, f), dst)
        emit(event="progress", done=i, total=len(files))
    emit(event="done", out=dst_dir, frames=len(files), seconds=round(time.time() - t, 2))


def cmd_check():
    info = {"python": sys.version.split()[0]}
    try:
        import rembg  # noqa: F401
        from importlib.metadata import version
        info["rembg"] = version("rembg")
    except Exception as e:  # noqa: BLE001
        info["rembg"] = None
        info["erro"] = str(e)
    try:
        import onnxruntime as ort
        info["providers"] = ort.get_available_providers()
        info["gpu"] = "CUDAExecutionProvider" in info["providers"] or "DmlExecutionProvider" in info["providers"]
    except Exception:  # noqa: BLE001
        info["providers"] = []
        info["gpu"] = False
    emit(event="check", **info)


def cmd_prep(src, dst, max_side):
    from PIL import Image
    im = open_rgb(src)
    w, h = im.size
    s = min(1.0, float(max_side) / max(w, h))
    if s < 1.0:
        im = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
    if im.mode == "RGBA":  # nuvem de vídeo não usa alpha: compõe sobre preto
        bg = Image.new("RGB", im.size, (0, 0, 0))
        bg.paste(im, mask=im.split()[3])
        im = bg
    im.save(dst, "JPEG", quality=92)
    emit(event="done", out=dst, width=im.size[0], height=im.size[1])


def main():
    if len(sys.argv) >= 3 and not sys.argv[1].startswith("--"):
        return cmd_single(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "birefnet-general")
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", nargs=2)
    ap.add_argument("--prep", nargs=2)
    ap.add_argument("--max", type=int, default=2048)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--model", default="birefnet-general")
    a = ap.parse_args()
    if a.check:
        return cmd_check()
    if a.batch:
        return cmd_batch(a.batch[0], a.batch[1], a.model)
    if a.prep:
        return cmd_prep(a.prep[0], a.prep[1], a.max)
    ap.print_help()
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main() or 0)
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        emit(event="error", msg=str(e))
        sys.exit(1)
