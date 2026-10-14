/* Assistência técnica: marcas, problemas e ilustração de cada problema (SVG 240×240).
   Usado pelo card de prévia (os/card.html). */
(function (root) {
  var G = "#F5C518", R = "#FF5A4E";
  // Celular visto de frente
  function cel(tela) {
    return '<defs><linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1f2b4d"/><stop offset="1" stop-color="#0a0f1e"/></linearGradient></defs>' +
      '<rect x="66" y="16" width="108" height="208" rx="20" fill="#1b1c21" stroke="' + G + '" stroke-width="4"/>' +
      '<rect x="74" y="26" width="92" height="188" rx="13" fill="' + (tela || "url(#scr)") + '"/>' +
      '<circle cx="120" cy="35" r="3.5" fill="#000"/>';
  }
  var ILU = {
    tela: cel() +
      '<g stroke="#e9eef9" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".95">' +
      '<path d="M128 92 L104 60 L92 30"/><path d="M128 92 L152 70 L166 52"/><path d="M128 92 L110 128 L80 150"/>' +
      '<path d="M128 92 L150 130 L158 176 L166 205"/><path d="M128 92 L96 98 L74 92"/><path d="M110 128 L122 160 L114 212"/>' +
      '<path d="M104 60 L88 70"/><path d="M150 130 L166 122"/></g>' +
      '<circle cx="128" cy="92" r="6" fill="#e9eef9"/>',
    bateria: cel() +
      '<rect x="96" y="80" width="48" height="90" rx="8" fill="none" stroke="#e9eef9" stroke-width="5"/>' +
      '<rect x="110" y="70" width="20" height="10" rx="3" fill="#e9eef9"/>' +
      '<rect x="103" y="148" width="34" height="15" rx="3" fill="' + R + '"/>' +
      '<path d="M120 98 v24" stroke="' + R + '" stroke-width="6" stroke-linecap="round"/><circle cx="120" cy="134" r="3.5" fill="' + R + '"/>',
    carrega: cel() +
      '<path d="M108 90 l-12 30 h22 l-10 32" fill="none" stroke="#e9eef9" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity=".5"/>' +
      '<rect x="108" y="228" width="24" height="10" rx="2" fill="#9aa0ad"/><path d="M120 238 v2" stroke="#9aa0ad" stroke-width="6"/>' +
      '<circle cx="166" cy="170" r="26" fill="' + R + '"/><path d="M155 159 l22 22 M177 159 l-22 22" stroke="#fff" stroke-width="6" stroke-linecap="round"/>',
    camera:
      '<rect x="40" y="56" width="160" height="128" rx="30" fill="#1b1c21" stroke="' + G + '" stroke-width="4"/>' +
      '<circle cx="120" cy="120" r="46" fill="#d7d9de"/><circle cx="120" cy="120" r="38" fill="#07080b"/><circle cx="120" cy="120" r="22" fill="#1d2b55"/>' +
      '<g stroke="#e9eef9" stroke-width="2.4" fill="none" stroke-linecap="round"><path d="M120 120 L98 92"/><path d="M120 120 L148 106"/><path d="M120 120 L112 156"/><path d="M120 120 L146 146"/></g>' +
      '<circle cx="176" cy="78" r="7" fill="#f3ead2"/>' +
      '<circle cx="186" cy="176" r="22" fill="' + R + '"/><path d="M186 164 v14" stroke="#fff" stroke-width="5" stroke-linecap="round"/><circle cx="186" cy="186" r="3" fill="#fff"/>',
    som: cel() +
      '<path d="M98 108 h14 l18 -16 v56 l-18 -16 h-14 z" fill="#e9eef9"/>' +
      '<path d="M140 104 l18 18 M158 104 l-18 18" stroke="' + R + '" stroke-width="5" stroke-linecap="round"/>' +
      '<rect x="112" y="166" width="16" height="26" rx="8" fill="none" stroke="#e9eef9" stroke-width="4"/><path d="M104 182 a16 16 0 0 0 32 0 M120 198 v8" fill="none" stroke="#e9eef9" stroke-width="4" stroke-linecap="round"/>' +
      '<path d="M100 166 l40 40" stroke="' + R + '" stroke-width="5" stroke-linecap="round"/>',
    molhou: cel("#0d1a33") +
      '<path d="M74 150 q12 -10 23 0 t23 0 t23 0 t23 0 V214 a13 13 0 0 1 -13 13 H87 a13 13 0 0 1 -13 -13 z" fill="#2f7fe0" opacity=".85"/>' +
      '<path d="M120 62 c14 20 22 32 22 44 a22 22 0 0 1 -44 0 c0 -12 8 -24 22 -44z" fill="#4da3ff"/>' +
      '<path d="M190 96 c7 10 11 16 11 22 a11 11 0 0 1 -22 0 c0 -6 4 -12 11 -22z" fill="#4da3ff"/>' +
      '<path d="M48 70 c6 9 10 14 10 19 a10 10 0 0 1 -20 0 c0 -5 4 -10 10 -19z" fill="#4da3ff"/>',
    software: cel() +
      '<g transform="translate(120 112)"><circle r="30" fill="none" stroke="#e9eef9" stroke-width="10" stroke-dasharray="14 9"/><circle r="14" fill="#1f2b4d" stroke="#e9eef9" stroke-width="5"/></g>' +
      '<rect x="88" y="168" width="64" height="10" rx="5" fill="#2a3557"/><rect x="88" y="168" width="22" height="10" rx="5" fill="' + G + '"/>' +
      '<circle cx="168" cy="54" r="20" fill="' + R + '"/><path d="M168 44 v12" stroke="#fff" stroke-width="5" stroke-linecap="round"/><circle cx="168" cy="63" r="3" fill="#fff"/>',
    outro: cel() +
      '<g transform="translate(120 120) rotate(-40)"><rect x="-6" y="-58" width="12" height="80" rx="4" fill="#cfd3dc"/><path d="M-18 -58 a18 18 0 1 1 36 0 h-10 v10 h-16 v-10z" fill="#cfd3dc"/></g>' +
      '<g transform="translate(120 120) rotate(40)"><rect x="-4" y="-60" width="8" height="66" rx="3" fill="' + G + '"/><rect x="-9" y="6" width="18" height="50" rx="6" fill="#e9eef9"/></g>'
  };
  root.RI_OS = {
    marcas: { xiaomi: "Xiaomi", iphone: "iPhone", realme: "Realme", samsung: "Samsung", motorola: "Motorola", outra: "Celular" },
    problemas: {
      tela: { nome: "Tela quebrada", chip: "Tela quebrada" },
      bateria: { nome: "Bateria", chip: "Bateria" },
      carrega: { nome: "Não carrega", chip: "Não carrega" },
      camera: { nome: "Câmera", chip: "Câmera" },
      som: { nome: "Som e microfone", chip: "Som / microfone" },
      molhou: { nome: "Molhou", chip: "Molhou" },
      software: { nome: "Software", chip: "Software" },
      outro: { nome: "Avaliação técnica", chip: "Outro" }
    },
    svg: function (p) { return '<svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">' + (ILU[p] || ILU.outro) + '</svg>'; }
  };
})(window);
