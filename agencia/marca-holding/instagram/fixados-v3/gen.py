import json,base64,sys,urllib.request,os
P=sys.argv[1];out=sys.argv[2];model=sys.argv[3] if len(sys.argv)>3 else 'gemini-3-pro-image'
body={"contents":[{"parts":[{"text":P}]}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"21:9"}}}
r=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"content-type":"application/json"})
d=json.load(urllib.request.urlopen(r,timeout=300))
for p in d["candidates"][0]["content"]["parts"]:
    if "inlineData" in p: open(out,"wb").write(base64.b64decode(p["inlineData"]["data"]));print("ok",out);break
else: print(json.dumps(d)[:500])
