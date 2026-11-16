from PIL import Image
import glob
fs=sorted(glob.glob('artes/*.jpg'));W=360;H=450
s=Image.new('RGB',(3*W+20,10*H+90),'white')
for k,f in enumerate(reversed(fs)): s.paste(Image.open(f).resize((W,H)),((k%3)*(W+10),(k//3)*(H+10)))
s.save('previa-grid.jpg',quality=85)
