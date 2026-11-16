// Pedra-chave 3D (conta Pedro, 16/11/2026): as 4 pedras do K se montam com o scroll. Three.js r160.
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
const cv = document.getElementById('k3d');
if (cv && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  try {
    const r = new THREE.WebGLRenderer({ canvas: cv, antialias: true, alpha: true, powerPreference: 'low-power' });
    r.setPixelRatio(Math.min(devicePixelRatio, innerWidth < 700 ? 1.5 : 2));
    const sc = new THREE.Scene(), cam = new THREE.PerspectiveCamera(32, 1, 1, 5000);
    cam.position.set(0, 0, 1500);
    const P = [[[0,0],[100,480],[164,480],[164,0]], [[196,0],[196,199.19],[380.54,0]], [[480,0],[424.16,0],[201.32,240.53],[384.39,458.93]], [[360.3,480],[196,283.99],[196,480]]];
    const pedra = new THREE.MeshStandardMaterial({ color: 0x2a2c32, roughness: .85, metalness: .1 });
    const latao = new THREE.MeshStandardMaterial({ color: 0xB8955A, roughness: .32, metalness: .9 });
    const g = new THREE.Group(); sc.add(g); const ps = [];
    P.forEach((pts, i) => {
      const sh = new THREE.Shape(pts.map(([x, y]) => new THREE.Vector2(x - 240, 240 - y)));
      const geo = new THREE.ExtrudeGeometry(sh, { depth: 70, bevelEnabled: true, bevelThickness: 4, bevelSize: 3, bevelSegments: 2 });
      geo.center(); const c = new THREE.Vector3(); sh.getPoints().forEach(p => c.add(new THREE.Vector3(p.x, p.y, 0))); c.divideScalar(sh.getPoints().length);
      const m = new THREE.Mesh(geo, i === 2 ? latao : pedra); m.userData = { alvo: c, de: new THREE.Vector3((i % 2 ? 1 : -1) * 520, (i < 2 ? 1 : -1) * 420, -600 + i * 150), rot: (i - 1.5) * .9 };
      g.add(m); ps.push(m);
    });
    sc.add(new THREE.AmbientLight(0xffffff, .45));
    const l1 = new THREE.DirectionalLight(0xffe2b0, 3.4); l1.position.set(600, 500, 700); sc.add(l1);
    const l2 = new THREE.PointLight(0xB8955A, 3, 2000); l2.position.set(-400, -200, 500); sc.add(l2);
    let prog = 0, alvo = 0, mx = 0, my = 0;
    const tam = () => { const w = cv.clientWidth, h = cv.clientHeight; r.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix(); g.position.x = w > 900 ? 260 : 0; g.position.y = w > 900 ? 40 : 160; g.scale.setScalar(w > 900 ? 1.1 : .9); };
    addEventListener('resize', tam); tam();
    const sv = document.querySelector('.hero .hero-simb'); if (sv) sv.style.display = 'none';
    addEventListener('scroll', () => { alvo = Math.min(1, scrollY / (innerHeight * .6)); }, { passive: true });
    addEventListener('pointermove', e => { mx = e.clientX / innerWidth - .5; my = e.clientY / innerHeight - .5; }, { passive: true });
    let t0 = performance.now(), vis = true;
    new IntersectionObserver(es => vis = es[0].isIntersecting).observe(cv);
    const ease = x => 1 - Math.pow(1 - x, 3);
    (function loop(t) {
      requestAnimationFrame(loop); if (!vis) return;
      const intro = Math.min(1, (t - t0) / 1800); prog += (Math.max(intro * .75, alvo * .25 + .75 * intro) - prog) * .08;
      const e = ease(Math.min(1, prog));
      ps.forEach(m => { const u = m.userData; m.position.lerpVectors(u.de, u.alvo, e); m.rotation.z = u.rot * (1 - e); m.rotation.y = (1 - e) * 1.2; });
      g.rotation.y += ((mx * .5 - .25 + alvo * .35) - g.rotation.y) * .05; g.rotation.x += ((my * .3) - g.rotation.x) * .05;
      l2.position.x = -400 + Math.sin(t / 1400) * 300;
      r.render(sc, cam);
    })(t0);
  } catch (e) { console.warn('k3d', e); }
}
