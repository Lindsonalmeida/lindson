import sys,shutil,json
from gradio_client import Client
P={
"IA1":"Vertical photo, Brazilian pizzeria kitchen at night, wood-fired brick oven glowing orange with real flames, a pizzaiolo's hands sliding a wooden peel out of the oven carrying two bubbling mozzarella pizzas, steam rising, warm practical light, shallow depth of field, cinematic realistic food photography, no text, no logos, no letters",
"IA2":"Vertical photo, close-up of a pizzeria worker's hands folding a plain brown cardboard pizza box on a steel counter, a fresh pizza inside, motorcycle helmet blurred in the background, mixed fluorescent and warm light, realistic photography, plain unprinted box, no text, no logos, no letters",
"IA3":"Vertical top-down photo, a pizza on a dark wooden board, left half calabresa sausage with onion rings, right half shrimp, a large chef knife resting exactly on the middle line, melted cheese, moody side light, realistic food photography, no text, no logos, no letters",
"IA4":"Vertical photo, blank folded paper menu card lying on a flour-dusted wooden counter, one finger touching it, blurred wood-fired oven fire in the background, warm light, the paper has no printing at all, completely blank, realistic photography, no text, no letters, no logos",
"IA5":"Vertical macro photo, a slice of pizza topped with shredded carne de sol beef and grilled coalho cheese cubes being lifted from the pie, long melted cheese pull, glossy and steaming, dark background with warm ember bokeh, realistic food photography, no text, no logos",
}
k=sys.argv[1]; v=sys.argv[2] if len(sys.argv)>2 else "a"
c=Client('black-forest-labs/FLUX.1-Krea-dev',verbose=False)
r,seed=c.predict(P[k],0,True,720,1280,4.5,28,api_name="/infer")
p=r if isinstance(r,str) else r.get('path')
shutil.copy(p,f"{k}-{v}.webp" if p.endswith('webp') else f"{k}-{v}"+p[p.rfind('.'):])
print(k,v,seed,p)
