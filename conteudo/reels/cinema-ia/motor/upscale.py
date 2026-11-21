import onnxruntime as ort,numpy as np,sys
from PIL import Image
s=ort.InferenceSession('/root/.modelos/real_esrgan_x2.onnx');n=s.get_inputs()[0].name
for src,dst in zip(sys.argv[1::2],sys.argv[2::2]):
    im=np.asarray(Image.open(src).convert('RGB')).astype(np.float32)/255;H,W,_=im.shape;T,P=192,16
    out=np.zeros((2*H,2*W,3),np.float32)
    for y in range(0,H,T):
        for x in range(0,W,T):
            y0,x0=max(0,y-P),max(0,x-P);y1,x1=min(H,y+T+P),min(W,x+T+P)
            r=s.run(None,{n:im[y0:y1,x0:x1].transpose(2,0,1)[None]})[0][0].transpose(1,2,0)
            ye,xe=min(H,y+T),min(W,x+T)
            out[2*y:2*ye,2*x:2*xe]=r[2*(y-y0):2*(ye-y0),2*(x-x0):2*(xe-x0)]
    Image.fromarray((np.clip(out,0,1)*255).astype(np.uint8)).save(dst,quality=94)
