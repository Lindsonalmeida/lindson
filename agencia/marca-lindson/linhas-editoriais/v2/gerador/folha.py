import sys,glob
from PIL import Image
fs=sys.argv[2:];W=360;H=450;c=min(6,len(fs))
o=Image.new('RGB',(c*W,((len(fs)+c-1)//c)*H))
for i,f in enumerate(fs): o.paste(Image.open(f).resize((W,H)),((i%c)*W,(i//c)*H))
o.save(sys.argv[1],quality=80)
