import sys,glob
from PIL import Image
n=sys.argv[1];fs=sorted(glob.glob(f'tmp/v{n}/q*.jpg'),key=lambda f:float(f.split('/q')[1][:-4]));W=Image.new('RGB',(5*270,2*480))
for i,f in enumerate(fs[:10]): W.paste(Image.open(f).resize((270,480)),((i%5)*270,(i//5)*480))
W.save(f'tmp/f{n}.jpg')
