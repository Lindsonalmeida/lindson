// Fixados Barzakh (conta Leandro, 21/11/2026): UMA cena 3D contínua (painel 3240x1440 = 3 posts).
// Parede de concreto + banco de concreto atravessando os 3 posts, luz rasante de janela vinda da esquerda.
// Post 1: papelaria (caderno, timbrado, envelope, cartões). Post 2: placa em arco aprovada. Post 3: caixa, selo, ecobag.
// Composição copia: Mova Street v5 (painel contínuo aprovado 19/11) + ref-03 (kit preto e ouro) + Pentagram/Koto (objeto herói centralizado).
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
const Q = new URLSearchParams(location.search), T = Q.get('tex'), W = +Q.get('w'), H = +Q.get('h');
const r = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
r.setSize(W, H); r.setPixelRatio(1); r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.05; r.outputColorSpace = THREE.SRGBColorSpace;
document.body.appendChild(r.domElement);
const scene = new THREE.Scene(); scene.background = new THREE.Color(0x0d0d0f);
scene.environment = new THREE.PMREMGenerator(r).fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.32;
const LD = new THREE.TextureLoader();
const tx = (n, srgb = true) => new Promise(ok => LD.load(`${T}/${n}.png`, t => { if (srgb) t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 16; ok(t); }));
async function mat(n) { const [m, mr] = await Promise.all([tx(n), tx(n + '_mr', false)]);
  return new THREE.MeshStandardMaterial({ map: m, roughnessMap: mr, metalnessMap: mr, roughness: 1, metalness: 1, envMapIntensity: 2.2 }); }
function concrete(hex, rep, seed) {
  const c = document.createElement('canvas'); c.width = c.height = 1024; const g = c.getContext('2d');
  g.fillStyle = hex; g.fillRect(0, 0, 1024, 1024); const id = g.getImageData(0, 0, 1024, 1024), d = id.data;
  let s = seed; const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647; const low = new Float32Array(4096).map(rnd);
  for (let y = 0; y < 1024; y++) for (let x = 0; x < 1024; x++) { const i = (y * 1024 + x) * 4;
    const fx = x / 16, fy = y / 16, x0 = fx | 0, y0 = fy | 0, ax = fx - x0, ay = fy - y0, L = (a, b) => low[(b & 63) * 64 + (a & 63)];
    const lv = (L(x0, y0) * (1 - ax) + L(x0 + 1, y0) * ax) * (1 - ay) + (L(x0, y0 + 1) * (1 - ax) + L(x0 + 1, y0 + 1) * ax) * ay;
    const v = (lv - .5) * 22 + (rnd() - .5) * 26 + (rnd() < .002 ? -40 : 0);
    d[i] += v; d[i + 1] += v; d[i + 2] += v; }
  g.putImageData(id, 0, 0); g.strokeStyle = 'rgba(0,0,0,.18)'; g.lineWidth = 2;
  for (let k = 0; k < 3; k++) { g.beginPath(); g.moveTo(0, 340 * k + 10); g.lineTo(1024, 340 * k + 10); g.stroke(); }
  for (let k = 0; k < 9; k++) { g.fillStyle = 'rgba(0,0,0,.25)'; g.beginPath(); g.arc(170 + (k % 3) * 340, 170 + Math.floor(k / 3) * 340, 7, 0, 7); g.fill(); }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(...rep);
  return new THREE.MeshStandardMaterial({ map: t, roughness: .92, bumpMap: t, bumpScale: 1.2 }); }
const add = (o, x, y, z) => { o.position.set(x, y, z); o.castShadow = o.receiveShadow = true; scene.add(o); return o; };
const edge = new THREE.MeshStandardMaterial({ color: 0x1a1a1c, roughness: .8 });
const edgeP = new THREE.MeshStandardMaterial({ color: 0xd8d2c6, roughness: .9 });

window.render = async () => {
  // parede e chão
  const wall = add(new THREE.Mesh(new THREE.PlaneGeometry(260, 140), concrete('#5d5b58', [4, 2.2], 11)), 0, 50, 0);
  const floor = add(new THREE.Mesh(new THREE.PlaneGeometry(260, 160), concrete('#3a3937', [4, 2.5], 29)), 0, 0, 60); floor.rotation.x = -Math.PI / 2;
  // banco de concreto contínuo (o elemento que atravessa as 3 divisas)
  add(new THREE.Mesh(new RoundedBoxGeometry(150, 9, 20, 4, .5), concrete('#6a6763', [3, .4], 5)), 0, 4.5, 12);
  // POST 2: placa em arco (frente texturizada + corpo extrudado)
  const pw = 31, ph = 38, sh = new THREE.Shape();
  sh.moveTo(-pw / 2, 0); sh.lineTo(pw / 2, 0); sh.lineTo(pw / 2, ph - pw / 2); sh.absarc(0, ph - pw / 2, pw / 2, 0, Math.PI, false); sh.lineTo(-pw / 2, 0);
  const body = add(new THREE.Mesh(new THREE.ExtrudeGeometry(sh, { depth: 1.4, bevelEnabled: true, bevelSize: .15, bevelThickness: .15, curveSegments: 96 }), edge), 0, 12, 1);
  const fg = new THREE.ShapeGeometry(sh, 96), p = fg.attributes.position, uv = fg.attributes.uv;
  for (let i = 0; i < p.count; i++) uv.setXY(i, (p.getX(i) + pw / 2) / pw, p.getY(i) / ph);
  add(new THREE.Mesh(fg, await mat('placa')), 0, 12, 2.58);
  // POST 1: papelaria apoiada na parede e sobre o banco
  const cad = add(new THREE.Mesh(new THREE.BoxGeometry(14, 19.6, .9), [edgeP, edgeP, edgeP, edgeP, await mat('caderno'), edge]), -36, 9 + 10.5, 6); cad.rotation.set(-.1, .12, 0);
  const tim = add(new THREE.Mesh(new THREE.BoxGeometry(14.8, 21, .08), [edgeP, edgeP, edgeP, edgeP, await mat('timbrado'), edgeP]), -46.5, 9 + 10.9, 3.6); tim.rotation.set(-.08, .05, .02);
  const env = add(new THREE.Mesh(new THREE.BoxGeometry(16, 8, .25), [edge, edge, edge, edge, await mat('envelope'), edge]), -26.5, 9 + 4.1, 9.5); env.rotation.set(-.16, -.18, 0);
  const cm = await mat('cartao');
  for (let i = 0; i < 7; i++) { const c = add(new THREE.Mesh(new THREE.BoxGeometry(8.5, .06, 5.5), [edge, edge, cm, edge, edge, edge]), -40 + i * .02, 9.03 + i * .07, 16.5); c.rotation.y = .25 + i * .01; }
  const c2 = add(new THREE.Mesh(new THREE.BoxGeometry(8.5, .06, 5.5), [edge, edge, cm, edge, edge, edge]), -30, 9.03, 18); c2.rotation.y = -.3;
  // POST 3: caixa, selo de cera, ecobag
  const cx = await mat('caixa');
  const box = add(new THREE.Mesh(new RoundedBoxGeometry(15, 15, 15, 3, .25), edge), 27.5, 9 + 7.5, 10); box.rotation.y = -.42;
  const bf = add(new THREE.Mesh(new THREE.PlaneGeometry(14.4, 14.4), cx), 0, 0, 7.52); box.remove(bf); box.add(bf); bf.position.set(0, 0, 7.52);
  const tampa = add(new THREE.Mesh(new RoundedBoxGeometry(11, 2.6, 11, 3, .2), edge), 28.1, 9 + 15 + 1.3, 10.4); tampa.rotation.y = -.15;
  const seal = add(new THREE.Mesh(new THREE.CylinderGeometry(1.9, 2.05, .55, 64), new THREE.MeshStandardMaterial({ color: 0x2b3a8f, roughness: .35, metalness: .1 })), 28.1, 9 + 15 + 2.9, 10.4);
  const bag = add(new THREE.Mesh(new RoundedBoxGeometry(17, 20, 1.6, 3, .6), [edge, edge, edge, edge, await mat('ecobag'), edge]), 41.5, 9 + 10, 5); bag.rotation.set(-.08, -.22, .015);
  const bfm = add(new THREE.Mesh(new THREE.PlaneGeometry(16.2, 19.2), await mat('ecobag')), 0, 0, .81); bag.remove(bfm); bag.add(bfm); bfm.position.set(0, 0, .81);
  for (const dx of [-4, 4]) { const h = new THREE.Mesh(new THREE.TorusGeometry(3.2, .35, 12, 48, Math.PI), new THREE.MeshStandardMaterial({ color: 0x1c1c1e, roughness: .9 })); h.position.set(dx, 10, 0); h.castShadow = true; bag.add(h); }
  // luz: janela rasante da esquerda (spot com máscara de caixilho) + preenchimento fraco + brilho Lápis atrás da placa
  const ck = document.createElement('canvas'); ck.width = ck.height = 512; const g = ck.getContext('2d');
  g.fillStyle = '#000'; g.fillRect(0, 0, 512, 512); g.fillStyle = '#fff';
  for (let i = 0; i < 3; i++) for (let j = 0; j < 2; j++) g.fillRect(80 + i * 122, 110 + j * 150, 110, 138);
  g.filter = 'blur(6px)'; g.drawImage(ck, 0, 0);
  const spot = new THREE.SpotLight(0xffd9a8, 22000, 0, .5, .35, 1.6); spot.position.set(-150, 60, 80); spot.target.position.set(10, 20, 0);
  const cookie = new THREE.CanvasTexture(ck); cookie.colorSpace = THREE.SRGBColorSpace; spot.map = cookie;
  spot.castShadow = true; spot.shadow.mapSize.set(4096, 4096); spot.shadow.bias = -.0004; spot.shadow.radius = 4; scene.add(spot, spot.target);
  const key = new THREE.DirectionalLight(0xfff0dc, .4); key.position.set(-60, 60, 90); key.castShadow = true; key.shadow.mapSize.set(4096, 4096);
  Object.assign(key.shadow.camera, { left: -90, right: 90, top: 60, bottom: -20, far: 300 }); key.shadow.radius = 8; scene.add(key);
  scene.add(new THREE.HemisphereLight(0x8a93b8, 0x2a2622, .2));
  const lapis = new THREE.PointLight(0x3c52c8, 70, 45, 1.6); lapis.position.set(0, 30, 9); scene.add(lapis);
  const cam = new THREE.PerspectiveCamera(25.5, W / H, 1, 1000); cam.position.set(0, 26, 132); cam.lookAt(0, 27, 0);
  scene.updateMatrixWorld(); r.render(scene, cam); r.render(scene, cam);
  return r.domElement.toDataURL('image/png');
};
window.ready = true;
