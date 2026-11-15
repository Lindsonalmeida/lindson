from PIL import Image
for k,o in [('feed','folha-v2.jpg'),('story','folha-stories-v2.jpg')]:
  ims=[Image.open(f'pecas-v2/c{n:02d}-{k}.jpg') for n in range(1,11)]
  w=360; h=int(ims[0].height*w/1080)
  F=Image.new('RGB',(w*5+60,h*2+30),'#222')
  for i,im in enumerate(ims): F.paste(im.resize((w,h)),(10+(i%5)*(w+10),10+(i//5)*(h+10)))
  F.save(o,quality=85)
