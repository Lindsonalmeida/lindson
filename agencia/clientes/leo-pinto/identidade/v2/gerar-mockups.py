# Gera os mockups fotográficos da v2 pelos Spaces do Hugging Face (ZeroGPU).
# Precisa do token do Hugging Face funcionando nesta sessão; sem ele a cota anônima acaba na hora.
# Uso: python3 gerar-mockups.py   (salva em mockups/)
import os, shutil
from gradio_client import Client
NEG = "text, letters, words, logo, watermark, blurry, distorted, cartoon, illustration"
CENAS = {
 "bandeira": "photorealistic large orange flag waving on a pole over flooded green fields and a lake in Maranhao Brazil, golden hour, plain fabric, no print",
 "bone": "photorealistic product photo of a plain royal blue baseball cap with a flat front panel, on a light wooden table, soft studio light",
 "camiseta": "photorealistic flat lay of a plain bright yellow polo shirt, blank chest, on light concrete, soft shadow",
 "cracha": "photorealistic blank white ID badge on a royal blue lanyard, lying on an office desk, shallow depth of field",
 "placa": "photorealistic blank royal blue acrylic sign plate on a white wall next to an office door, municipal building, daylight",
 "faixa": "photorealistic long blank white banner hanging between two poles at an outdoor community event in a small Brazilian town, festa junina bunting, evening",
 "redes": "photorealistic hand holding a smartphone with a blank white screen, street of a small Brazilian town in background, bokeh",
}
os.makedirs("mockups", exist_ok=True)
c = Client("mcp-tools/Qwen-Image", token=os.environ.get("HF_TOKEN"))
for nome, prompt in CENAS.items():
    r = c.predict(prompt, 0, True, "4:3", NEG, 4, 16, api_name="/generate_image")
    img = r[0] if isinstance(r, (list, tuple)) else r
    shutil.copy(img, f"mockups/{nome}.webp")
    print("ok", nome)
