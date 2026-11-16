// Projeto Designer v2 (conta Leandro, 16/11/2026): mockups 3D fotorrealistas em Three.js.
// Cada cena recebe as texturas oficiais da marca (texturas.py) e devolve um render com luz natural e sombra suave.
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';

const Q = new URLSearchParams(location.search);
const T = Q.get('tex'), SC = Q.get('cena'), W = +Q.get('w') || 2400, H = +Q.get('h') || 1800;
const P = JSON.parse(decodeURIComponent(Q.get('pal')));   // {bg, bg2, ac, chao}
const r = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
r.setSize(W, H); r.setPixelRatio(1);
r.shadowMap.enabled = true; r.shadowMap.type = THREE.VSMShadowMap;
r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.0; r.outputColorSpace = THREE.SRGBColorSpace;
document.body.appendChild(r.domElement);
const scene = new THREE.Scene();
const pm = new THREE.PMREMGenerator(r);
scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = 0.55;
const loader = new THREE.TextureLoader();
const tex = n => new Promise(ok => loader.load(`${T}/${n}.png`, t => { t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 16; ok(t); }));

// superfície com textura procedural (pedra, gesso, madeira clara)
function surf(hex, kind = 'pedra', rep = 1) {
  const c = document.createElement('canvas'); c.width = c.height = 1024; const g = c.getContext('2d');
  g.fillStyle = hex; g.fillRect(0, 0, 1024, 1024);
  const id = g.getImageData(0, 0, 1024, 1024), d = id.data;
  let s = 7; const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647;
  // ruído de baixa e alta frequência
  const low = new Float32Array(64 * 64).map(() => rnd());
  for (let y = 0; y < 1024; y++) for (let x = 0; x < 1024; x++) {
    const lx = x / 16, ly = y / 16, x0 = lx | 0, y0 = ly | 0, fx = lx - x0, fy = ly - y0;
    const L = (i, j) => low[((j & 63) * 64) + (i & 63)];
    const v = L(x0, y0) * (1 - fx) * (1 - fy) + L(x0 + 1, y0) * fx * (1 - fy) + L(x0, y0 + 1) * (1 - fx) * fy + L(x0 + 1, y0 + 1) * fx * fy;
    let n = (v - 0.5) * (kind === 'gesso' ? 10 : 18) + (rnd() - 0.5) * (kind === 'madeira' ? 6 : 14);
    if (kind === 'madeira') n += Math.sin(y * 0.05 + Math.sin(x * 0.004) * 6) * 9;
    const i = (y * 1024 + x) * 4; d[i] += n; d[i + 1] += n; d[i + 2] += n;
  }
  g.putImageData(id, 0, 0);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(rep, rep);
  const b = new THREE.CanvasTexture(c); b.wrapS = b.wrapT = THREE.RepeatWrapping; b.repeat.set(rep, rep);
  return new THREE.MeshStandardMaterial({ map: t, roughness: 0.92, bumpMap: b, bumpScale: kind === 'gesso' ? 0.6 : 1.2 });
}
const paper = (map, rough = 0.75) => new THREE.MeshStandardMaterial({ map, roughness: rough, metalness: 0 });
const edge = new THREE.MeshStandardMaterial({ color: 0xf2efe8, roughness: 0.9 });
function cardMesh(front, back, w = 8.5, h = 5.5, t = 0.06) {
  const g = new THREE.BoxGeometry(w, t, h);
  const m = [edge, edge, paper(front), paper(back || front), edge, edge];
  const o = new THREE.Mesh(g, m); o.castShadow = o.receiveShadow = true; return o;
}
function sheet(map, w, h, t = 0.03) { const o = new THREE.Mesh(new THREE.BoxGeometry(w, t, h), [edge, edge, paper(map, 0.85), edge, edge, edge]); o.castShadow = o.receiveShadow = true; return o; }
function floor(mat, size = 400) { const o = new THREE.Mesh(new THREE.PlaneGeometry(size, size), mat); o.rotation.x = -Math.PI / 2; o.receiveShadow = true; scene.add(o); return o; }
function sun(x, y, z, I = 2.6, col = 0xfff1de, area = 60, rad = 6) {
  const l = new THREE.DirectionalLight(col, I); l.position.set(x, y, z); l.castShadow = true;
  l.shadow.mapSize.set(4096, 4096); l.shadow.radius = rad; l.shadow.blurSamples = 25; l.shadow.bias = -0.0004;
  Object.assign(l.shadow.camera, { left: -area, right: area, top: area, bottom: -area, near: 1, far: 400 }); scene.add(l); return l;
}
function cam(fov, pos, look) {
  // retrato (pin 2:3): afasta a câmera para nada ficar cortado na borda
  const k = H > W ? 1.75 : 1, p = pos.map((v, i) => look[i] + (v - look[i]) * k);
  const c = new THREE.PerspectiveCamera(fov, W / H, 0.1, 3000); c.position.set(...p); c.lookAt(...look); return c;
}

const CENAS = {
  // 1. cartões de visita em close, luz rasante de janela
  async cartoes() {
    const [f, b] = await Promise.all([tex('card_front'), tex('card_back')]);
    floor(surf(P.chao, 'pedra', 3));
    for (let i = 0; i < 6; i++) { const c = cardMesh(f, b); c.position.set(-4.2 + i * 0.01, 0.03 + i * 0.062, 1.2 - i * 0.008); c.rotation.y = 0.32 + i * 0.006; scene.add(c); }
    const top = cardMesh(b, f); top.position.set(5.2, 0.03, -1.6); top.rotation.y = -0.22; scene.add(top);
    const t2 = cardMesh(f, b); t2.position.set(3.4, 0.09, 4.4); t2.rotation.y = -0.05; scene.add(t2);
    sun(-30, 34, 18, 2.8); scene.add(new THREE.AmbientLight(0xffffff, 0.15));
    return cam(32, [0.5, 19, 24], [0.4, 0, 0.6]);
  },
  // 2. papelaria vista de cima (flat lay)
  async papelaria() {
    const [f, b, l, e] = await Promise.all([tex('card_front'), tex('card_back'), tex('letter'), tex('env')]);
    floor(surf(P.chao, 'gesso', 4));
    const L = sheet(l, 21, 29.7); L.position.set(-8, 0.02, 0); L.rotation.y = 0.06; scene.add(L);
    const E = sheet(e, 22, 11, 0.12); E.position.set(10.5, 0.07, -8.5); E.rotation.y = -0.05; scene.add(E);
    const c1 = cardMesh(f, b); c1.position.set(9, 0.05, 4); c1.rotation.y = 0.12; scene.add(c1);
    const c2 = cardMesh(b, f); c2.position.set(12.5, 0.05, 11); c2.rotation.y = -0.2; scene.add(c2);
    const pen = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 14, 32), new THREE.MeshStandardMaterial({ color: P.bg2, roughness: 0.35, metalness: 0.2 }));
    pen.rotation.z = Math.PI / 2; pen.rotation.y = 0.5; pen.position.set(3, 0.42, 13); pen.castShadow = true; scene.add(pen);
    const cap = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.44, 3.4, 32), new THREE.MeshStandardMaterial({ color: P.ac, roughness: 0.3, metalness: 0.5 }));
    cap.rotation.copy(pen.rotation); cap.position.set(3 + Math.cos(0.5) * 7.2, 0.44, 13 - Math.sin(0.5) * 7.2); cap.castShadow = true; scene.add(cap);
    sun(-40, 60, -30, 2.6, 0xfff1de, 60, 4); scene.add(new THREE.AmbientLight(0xffffff, 0.2));
    return cam(24, [1.2, 92, 0.01], [1.2, 0, 0]);
  },
  // 3. celular com o Instagram da marca sobre a mesa
  async celular() {
    const [ig, f, b] = await Promise.all([tex('ig'), tex('card_front'), tex('card_back')]);
    floor(surf(P.chao, 'madeira', 2));
    const body = new THREE.Mesh(new RoundedBoxGeometry(7.4, 0.8, 15.6, 6, 1.1), new THREE.MeshStandardMaterial({ color: 0x1b1b1d, roughness: 0.25, metalness: 0.85 }));
    body.castShadow = body.receiveShadow = true;
    const scr = new THREE.Mesh(new THREE.PlaneGeometry(6.9, 15.0), new THREE.MeshStandardMaterial({ map: ig, emissive: 0xffffff, emissiveMap: ig, emissiveIntensity: 0.9, roughness: 0.08, metalness: 0 }));
    scr.rotation.x = -Math.PI / 2; scr.position.y = 0.41;
    const ph = new THREE.Group(); ph.add(body, scr); ph.position.set(-2.4, 0.4, 0); ph.rotation.y = 0.28; scene.add(ph);
    const c1 = cardMesh(f, b); c1.position.set(7.8, 0.03, 3.6); c1.rotation.y = -0.35; scene.add(c1);
    const c2 = cardMesh(b, f); c2.position.set(8.6, 0.09, 0.2); c2.rotation.y = -0.15; scene.add(c2);
    sun(-25, 40, 10, 2.4); scene.add(new THREE.AmbientLight(0xffffff, 0.15));
    return cam(28, [3, 30, 17], [1.6, 0, 0.5]);
  },
  // 4. pôster na parede com luz de janela
  async poster() {
    const [p] = await Promise.all([tex('poster')]);
    const wall = new THREE.Mesh(new THREE.PlaneGeometry(400, 300), surf(P.parede, 'gesso', 6)); wall.receiveShadow = true; wall.position.z = -0.01; scene.add(wall);
    const fl = floor(surf(P.chao, 'madeira', 3)); fl.position.y = -60;
    const fr = new THREE.Mesh(new THREE.BoxGeometry(52, 72, 2.2), new THREE.MeshStandardMaterial({ color: 0x151515, roughness: 0.5 })); fr.position.set(0, 10, 1.1); fr.castShadow = fr.receiveShadow = true; scene.add(fr);
    const pp = new THREE.Mesh(new THREE.PlaneGeometry(48, 68), paper(p, 0.6)); pp.position.set(0, 10, 2.25); pp.receiveShadow = true; scene.add(pp);
    const gl = new THREE.Mesh(new THREE.PlaneGeometry(48, 68), new THREE.MeshPhysicalMaterial({ transparent: true, opacity: 0.08, roughness: 0.02, metalness: 0, transmission: 0 })); gl.position.set(0, 10, 2.35); scene.add(gl);
    // aparador
    const tb = new THREE.Mesh(new THREE.BoxGeometry(110, 4, 30), surf('#b89a78', 'madeira', 1)); tb.position.set(0, -34, 15); tb.castShadow = tb.receiveShadow = true; scene.add(tb);
    const vase = new THREE.Mesh(new THREE.CylinderGeometry(5, 4, 16, 48), new THREE.MeshStandardMaterial({ color: 0xe9e3d8, roughness: 0.6 })); vase.position.set(38, -24, 12); vase.castShadow = true; scene.add(vase);
    const l = sun(-60, 50, 70, 2.4, 0xfff0dc, 120, 3);
    scene.add(new THREE.AmbientLight(0xffffff, 0.25));
    return cam(34, [-22, 2, 150], [0, 4, 0]);
  },
  // 5. embalagem: caixa e copo
  async embalagem() {
    const [bx, sd, wr] = await Promise.all([tex('box'), tex('side'), tex('wrap')]);
    floor(surf(P.chao, 'pedra', 3));
    const sideM = paper(sd, 0.7), topM = paper(bx, 0.7);
    const box = new THREE.Mesh(new THREE.BoxGeometry(16, 4, 16), [sideM, sideM, topM, sideM, sideM, sideM]); box.position.set(-5, 2, 0); box.rotation.y = 0.5; box.castShadow = box.receiveShadow = true; scene.add(box);
    const box2 = new THREE.Mesh(new THREE.BoxGeometry(13, 3.4, 13), [sideM, sideM, topM, sideM, sideM, sideM]); box2.position.set(-4.4, 5.7, -0.4); box2.rotation.y = 0.32; box2.castShadow = box2.receiveShadow = true; scene.add(box2);
    wr.wrapS = THREE.RepeatWrapping; wr.offset.x = 0.25;
    const cup = new THREE.Mesh(new THREE.CylinderGeometry(4.2, 3.3, 11, 96, 1, true), new THREE.MeshStandardMaterial({ map: wr, roughness: 0.55, side: THREE.DoubleSide })); cup.position.set(8.5, 5.5, 3); cup.rotation.y = -1.3; cup.castShadow = true; scene.add(cup);
    const lid = new THREE.Mesh(new THREE.CylinderGeometry(4.35, 4.35, 0.9, 96), new THREE.MeshStandardMaterial({ color: 0xf3f0ea, roughness: 0.5 })); lid.position.set(8.5, 11.4, 3); lid.castShadow = true; scene.add(lid);
    const bot = new THREE.Mesh(new THREE.CircleGeometry(3.3, 64), edge); bot.rotation.x = -Math.PI / 2; bot.position.set(8.5, 0.01, 3); scene.add(bot);
    sun(-30, 40, 25, 2.6); scene.add(new THREE.AmbientLight(0xffffff, 0.18));
    return cam(30, [3, 22, 38], [1.5, 4, 0]);
  },
  // 6. outdoor ao entardecer
  async outdoor() {
    const [bl] = await Promise.all([tex('bill')]);
    const sky = document.createElement('canvas'); sky.width = 4; sky.height = 512; const g = sky.getContext('2d');
    const gr = g.createLinearGradient(0, 0, 0, 512); gr.addColorStop(0, '#2b4a7a'); gr.addColorStop(0.55, '#e7a06a'); gr.addColorStop(0.8, '#f6cf94'); gr.addColorStop(1, '#f9e1b8');
    g.fillStyle = gr; g.fillRect(0, 0, 4, 512); const st = new THREE.CanvasTexture(sky); st.colorSpace = THREE.SRGBColorSpace; scene.background = st;
    scene.fog = new THREE.Fog(0xe9b98a, 120, 520);
    floor(new THREE.MeshStandardMaterial({ color: 0x6b6152, roughness: 1 }), 3000);
    const grey = new THREE.MeshStandardMaterial({ color: 0x3a3a3c, roughness: 0.6, metalness: 0.6 });
    const pole = new THREE.Mesh(new THREE.CylinderGeometry(1.4, 1.6, 52, 24), grey); pole.position.set(0, 26, -2); pole.castShadow = true; scene.add(pole);
    const frame = new THREE.Mesh(new THREE.BoxGeometry(92, 32, 2), grey); frame.position.set(0, 64, 0); frame.castShadow = true; scene.add(frame);
    const face = new THREE.Mesh(new THREE.PlaneGeometry(88, 29.3), new THREE.MeshStandardMaterial({ map: bl, roughness: 0.55, emissive: 0xffffff, emissiveMap: bl, emissiveIntensity: 0.15 })); face.position.set(0, 64, 1.02); scene.add(face);
    const walk = new THREE.Mesh(new THREE.BoxGeometry(92, 0.6, 4), grey); walk.position.set(0, 47.6, 2); walk.castShadow = true; scene.add(walk);
    for (let i = -3; i <= 3; i++) { const lp = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 4), grey); lp.position.set(i * 13, 81, 2.5); scene.add(lp); }
    // prédios ao fundo
    for (let i = 0; i < 26; i++) { const h = 20 + Math.random() * 70; const bd = new THREE.Mesh(new THREE.BoxGeometry(18 + Math.random() * 20, h, 20), new THREE.MeshStandardMaterial({ color: 0x4a4a55, roughness: 0.9 })); bd.position.set(-260 + i * 21, h / 2, -230 - Math.random() * 80); scene.add(bd); }
    sun(-120, 50, 80, 2.2, 0xffc890, 120, 3); scene.add(new THREE.HemisphereLight(0xa8c0e8, 0x6b5a48, 0.6));
    return cam(36, [-34, 14, 120], [0, 58, 0]);
  },
  // 7. placa luminosa na fachada, à noite
  async fachada() {
    const [sg] = await Promise.all([tex('sign')]);
    const wall = new THREE.Mesh(new THREE.PlaneGeometry(400, 300), surf(P.fachada, 'pedra', 5)); wall.receiveShadow = true; scene.add(wall);
    const sign = new THREE.Mesh(new THREE.BoxGeometry(100, 32, 5), [edge, edge, edge, edge, new THREE.MeshStandardMaterial({ map: sg, emissive: 0xffffff, emissiveMap: sg, emissiveIntensity: 1.1, roughness: 0.3 }), edge]);
    sign.material[0] = sign.material[1] = sign.material[2] = sign.material[3] = new THREE.MeshStandardMaterial({ color: 0x1a1a1a, roughness: 0.4, metalness: 0.7 });
    sign.position.set(0, 30, 2.5); sign.castShadow = true; scene.add(sign);
    const glow = new THREE.PointLight(new THREE.Color(P.ac), 2400, 140, 2); glow.position.set(0, 30, 18); scene.add(glow);
    const glass = new THREE.Mesh(new THREE.PlaneGeometry(150, 70), new THREE.MeshStandardMaterial({ color: 0x0c0d10, roughness: 0.05, metalness: 0.9 })); glass.position.set(0, -32, 0.5); scene.add(glass);
    const warm = new THREE.Mesh(new THREE.PlaneGeometry(146, 66), new THREE.MeshBasicMaterial({ color: 0x3b2a18 })); warm.position.set(0, -32, 0.3); scene.add(warm);
    scene.environmentIntensity = 0.12; scene.add(new THREE.AmbientLight(0x8090b0, 0.08));
    const s = sun(-80, 120, 90, 0.35, 0x9fb4ff, 160, 4);
    return cam(38, [-46, -6, 150], [0, 6, 0]);
  },
};

window.render = async () => {
  const c = await CENAS[SC](); scene.updateMatrixWorld();
  r.render(scene, c); r.render(scene, c);
  return r.domElement.toDataURL('image/png');
};
window.ready = true;
