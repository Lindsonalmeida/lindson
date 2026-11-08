# Teste de lip-sync na CPU: Wav2Lip GAN 96 (ONNX do FaceFusion) sobre uma foto parada + áudio. Uso: foto.jpg audio.wav saida.mp4
import sys,time,subprocess,numpy as np,cv2,librosa,onnxruntime as ort,soundfile as sf
t0=time.time();foto,aud,out=sys.argv[1:4];FPS=25
img=cv2.imread(foto);g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fc=cv2.CascadeClassifier(__import__('os').path.expanduser('~/.modelos/haar.xml')).detectMultiScale(g,1.1,5,minSize=(120,120))
x,y,w,h=max(fc,key=lambda r:r[2]*r[3]);y1,y2,x1,x2=y,min(img.shape[0],y+h+int(h*.12)),x,x+w
wav,_=librosa.load(aud,sr=16000);wav=np.append(wav[0],wav[1:]-.97*wav[:-1])
S=np.abs(librosa.stft(wav,n_fft=800,hop_length=200,win_length=800));mel=np.dot(librosa.filters.mel(sr=16000,n_fft=800,n_mels=80,fmin=55,fmax=7600),S)
mel=20*np.log10(np.maximum(1e-5,mel))-20;mel=np.clip((2*4)*((mel+100)/100)-4,-4,4)
n=int(len(wav)/16000*FPS);chunks=[]
for i in range(n):
    s=int(80./FPS*i);c=mel[:,s:s+16]
    if c.shape[1]<16:c=mel[:,-16:]
    chunks.append(c)
face=cv2.resize(img[y1:y2,x1:x2],(96,96));m=face.copy();m[48:]=0
tgt=np.concatenate([m,face],2).transpose(2,0,1)[None].astype(np.float32)/255.
sess=ort.InferenceSession(__import__('os').path.expanduser('~/.modelos/wav2lip_gan_96.onnx'),providers=['CPUExecutionProvider'])
vw=cv2.VideoWriter('/tmp/ls/v.mp4',cv2.VideoWriter_fourcc(*'mp4v'),FPS,(img.shape[1]//2*2,img.shape[0]//2*2))
for i in range(0,n,16):
    src=np.stack([c[None] for c in chunks[i:i+16]]).astype(np.float32);b=len(src)
    o=sess.run(None,{'source':src,'target':np.repeat(tgt,b,0)})[0]
    for k in range(b):
        p=(o[k].transpose(1,2,0)*255).clip(0,255).astype(np.uint8);p=cv2.resize(p,(x2-x1,y2-y1))
        fr=img.copy();msk=np.zeros((y2-y1,x2-x1),np.float32);msk[int((y2-y1)*.5):]=1;msk=cv2.GaussianBlur(msk,(0,0),(x2-x1)*.04)[...,None]
        fr[y1:y2,x1:x2]=(p*msk+fr[y1:y2,x1:x2]*(1-msk)).astype(np.uint8);vw.write(fr[:img.shape[0]//2*2,:img.shape[1]//2*2])
vw.release()
subprocess.run(['ffmpeg','-v','error','-y','-i','/tmp/ls/v.mp4','-i',aud,'-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-shortest',out],check=True)
print('ok',round(time.time()-t0,1),'s para',round(len(wav)/16000,1),'s de fala; rosto',w,'px')
