/* Lançamentos da Rafael Imports: ficha técnica (dados do fabricante) e foto real de cada aparelho (campo foto).
   Sem foto, o site mostra "Foto real em breve". A ilustração SVG fica só como referência interna, fora do site.
   Usado pelo mini site (index.html) e pelas artes de divulgação (artes/arte.html). */
(function (root) {
  var P = [
    {
      foto: null, /* foto real: "img/produtos/x8pro.jpg" */
      id: "x8pro", marca: "POCO", nome: "POCO X8 Pro", tag: "Desempenho topo",
      frase: "Chip de topo, tela 1,5K e bateria que aguenta o dia pesado.",
      cam: "duo",
      cores: [["Preto", "#2a2c30", "#141518"], ["Branco", "#f4f4f1", "#d6d7d3"], ["Verde menta", "#c8e8d6", "#8fc8ab"]],
      dest: [["Dimensity 8500", "chip 4 nm"], ["6.500 mAh", "bateria"], ["100 W", "carregamento"], ["50 MP OIS", "câmera Sony"]],
      ficha: [
        ["Tela", "6,59\" AMOLED 1,5K, 120 Hz, até 3.500 nits, HDR10+ e Dolby Vision"],
        ["Processador", "MediaTek Dimensity 8500-Ultra (4 nm)"],
        ["Memória", "8 GB ou 12 GB de RAM · 256 GB ou 512 GB"],
        ["Câmera traseira", "50 MP Sony IMX882 com OIS + 8 MP ultra-wide"],
        ["Câmera frontal", "20 MP"],
        ["Bateria", "6.500 mAh · carregamento 100 W"],
        ["Resistência", "IP68 contra água e poeira"],
        ["Sistema", "Xiaomi HyperOS 3 (Android 16)"],
        ["Desbloqueio", "Leitor de digital na tela"],
        ["Peso", "201 g · 157,5 × 75,2 × 8,4 mm"]
      ]
    },
    {
      foto: null, /* foto real: "img/produtos/note15pro.jpg" */
      id: "note15pro", marca: "Redmi", nome: "Redmi Note 15 Pro 5G", tag: "Câmera 200 MP",
      frase: "200 MP, tela gigante 1,5K e resistência IP68/IP69K.",
      cam: "pro",
      cores: [["Titânio", "#d3cdc2", "#9d968a"], ["Azul glacial", "#d3e6f4", "#93bde0"], ["Roxo névoa", "#ddd2ee", "#ad9ad0"], ["Preto", "#2a2c30", "#141518"]],
      dest: [["200 MP", "câmera principal"], ["6.580 mAh", "bateria"], ["6,83\" 1,5K", "AMOLED 120 Hz"], ["IP68/IP69K", "água e poeira"]],
      ficha: [
        ["Tela", "6,83\" AMOLED 1,5K, 120 Hz, até 3.200 nits, Gorilla Glass Victus 2"],
        ["Processador", "MediaTek Dimensity 7400-Ultra"],
        ["Memória", "8 GB ou 12 GB de RAM · 256 GB ou 512 GB"],
        ["Câmera traseira", "200 MP + 8 MP ultra-wide"],
        ["Câmera frontal", "20 MP"],
        ["Bateria", "6.580 mAh (silício-carbono) · 45 W · reverso 22,5 W"],
        ["Resistência", "IP68 e IP69K"],
        ["Rede", "5G"],
        ["Peso", "210 g"]
      ]
    },
    {
      foto: "img/produtos/note15.webp?v=1", /* foto oficial enviada pelo cliente */
      id: "note15", marca: "Redmi", nome: "Redmi Note 15 5G", tag: "Leve e completo",
      frase: "108 MP com estabilizador, tela curva AMOLED e só 178 g.",
      cam: "note",
      cores: [["Preto", "#2a2c30", "#141518"], ["Azul glacial", "#d3e6f4", "#93bde0"], ["Roxo névoa", "#ddd2ee", "#ad9ad0"]],
      dest: [["108 MP OIS", "câmera principal"], ["Snapdragon", "6 Gen 3"], ["6,77\" curva", "AMOLED 120 Hz"], ["178 g", "leve na mão"]],
      ficha: [
        ["Tela", "6,77\" AMOLED curva, Full HD+, 120 Hz, até 3.200 nits"],
        ["Processador", "Qualcomm Snapdragon 6 Gen 3"],
        ["Memória", "6, 8 ou 12 GB de RAM · 128, 256 ou 512 GB"],
        ["Câmera traseira", "108 MP Samsung HM9 com OIS + 8 MP ultra-wide"],
        ["Câmera frontal", "20 MP"],
        ["Bateria", "5.520 mAh (silício-carbono) · 45 W"],
        ["Resistência", "IP66"],
        ["Rede", "5G"],
        ["Peso", "178 g"]
      ]
    },
    {
      foto: null, /* foto real: "img/produtos/c85.jpg" */
      id: "c85", marca: "POCO", nome: "POCO C85", tag: "Custo-benefício",
      frase: "Telão de 6,9\", bateria de 6.000 mAh e carga rápida de 33 W.",
      cam: "ring",
      cores: [["Verde", "#b9e0c4", "#76b98f"], ["Roxo", "#d2c0ee", "#9a80d0"], ["Preto", "#2a2c30", "#141518"]],
      dest: [["6,9\" 120 Hz", "tela grande"], ["6.000 mAh", "bateria"], ["33 W", "carga rápida"], ["50 MP", "câmera"]],
      ficha: [
        ["Tela", "6,9\" LCD HD+, 120 Hz, até 810 nits, certificação TÜV de conforto visual"],
        ["Processador", "MediaTek Helio G81-Ultra"],
        ["Memória", "6 ou 8 GB de RAM · 128 ou 256 GB + microSD"],
        ["Câmera traseira", "50 MP f/1.8"],
        ["Câmera frontal", "8 MP"],
        ["Bateria", "6.000 mAh · 33 W · carregamento reverso"],
        ["Resistência", "IP64"],
        ["Extras", "Leitor de digital lateral · entrada P2 para fone"],
        ["Sistema", "Xiaomi HyperOS (Android 15)"],
        ["Peso", "205 g"]
      ]
    },
    {
      foto: "img/produtos/r15c.webp?v=1", /* foto oficial enviada pelo cliente */
      id: "r15c", marca: "Redmi", nome: "Redmi 15C", tag: "Bateria monstra",
      frase: "Bateria de 6.000 mAh, tela de 6,9\" e 50 MP pelo melhor preço.",
      cam: "ring",
      cores: [["Azul luar", "#cfdcee", "#8eaad2"], ["Verde menta", "#c8e8d6", "#8fc8ab"], ["Preto meia-noite", "#2a2c30", "#141518"], ["Laranja crepúsculo", "#f7cba6", "#e78a5c"]],
      dest: [["6.000 mAh", "bateria"], ["6,9\" 120 Hz", "tela grande"], ["33 W", "carga rápida"], ["50 MP", "câmera"]],
      ficha: [
        ["Tela", "6,9\" LCD HD+, 120 Hz, 660 nits"],
        ["Processador", "MediaTek Helio G81-Ultra (versão 4G)"],
        ["Memória", "Até 8 GB de RAM · 128 ou 256 GB + microSD"],
        ["Câmera traseira", "50 MP + sensor auxiliar"],
        ["Câmera frontal", "8 MP"],
        ["Bateria", "6.000 mAh · 33 W · reverso 10 W"],
        ["Resistência", "IP64"],
        ["Extras", "Leitor de digital lateral"],
        ["Sistema", "Xiaomi HyperOS (Android 15)"],
        ["Peso", "205 g · 171,6 × 79,5 × 8 mm"]
      ]
    },
    {
      foto: "img/produtos/a17-5g.webp?v=1", /* foto do cartaz da loja */
      id: "a17-5g", marca: "Samsung", nome: "Samsung Galaxy A17 5G", tag: "5G + NFC",
      frase: "Tela Super AMOLED, câmera tripla de 50 MP e 5G com NFC.",
      cam: "duo",
      cores: [["Preto", "#2a2c30", "#141518"], ["Azul", "#3b5fa8", "#22396b"], ["Cinza", "#c9cbcf", "#8f9298"]],
      dest: [["Super AMOLED", "6,7\" 90 Hz"], ["Exynos 1330", "5G"], ["50 MP", "câmera tripla"], ["5.000 mAh", "bateria"]],
      ficha: [
        ["Tela", "6,7\" Super AMOLED Full HD+, 90 Hz"],
        ["Processador", "Samsung Exynos 1330"],
        ["Memória", "4 GB de RAM · 128 GB"],
        ["Câmera traseira", "50 MP + 5 MP ultra-wide + 2 MP macro"],
        ["Câmera frontal", "13 MP"],
        ["Bateria", "5.000 mAh · 25 W"],
        ["Rede", "5G · NFC"],
        ["Resistência", "IP54"]
      ]
    },
    {
      foto: "img/produtos/a17-4g.webp?v=1", /* foto do cartaz da loja */
      id: "a17-4g", marca: "Samsung", nome: "Samsung Galaxy A17 4G", tag: "Samsung",
      frase: "Tela Super AMOLED, câmera tripla e bateria para o dia todo.",
      cam: "duo",
      cores: [["Preto", "#2a2c30", "#141518"], ["Azul claro", "#cfe0ee", "#9dbbd6"], ["Cinza", "#c9cbcf", "#8f9298"]],
      dest: [["Super AMOLED", "6,7\" 90 Hz"], ["Helio G99", "processador"], ["50 MP", "câmera tripla"], ["5.000 mAh", "bateria"]],
      ficha: [
        ["Tela", "6,7\" Super AMOLED Full HD+, 90 Hz, Gorilla Glass Victus+"],
        ["Processador", "MediaTek Helio G99"],
        ["Memória", "4 GB / 128 GB ou 8 GB / 256 GB"],
        ["Câmera traseira", "50 MP + 5 MP ultra-wide + 2 MP macro"],
        ["Câmera frontal", "13 MP"],
        ["Bateria", "5.000 mAh · 25 W"],
        ["Resistência", "IP54"],
        ["Sistema", "Android 15 · One UI 7"]
      ]
    },
    {
      foto: "img/produtos/p4power.webp?v=1", /* foto do cartaz da loja */
      id: "p4power", marca: "realme", nome: "Realme P4 Power", tag: "10.001 mAh",
      frase: "Bateria gigante de 10.001 mAh com carga de 80 W e tela AMOLED 144 Hz.",
      cam: "duo",
      cores: [["Azul", "#5b63d6", "#3a3fa3"], ["Laranja", "#e07a3c", "#b0541f"], ["Prata", "#e3e4e6", "#b5b7bb"]],
      dest: [["10.001 mAh", "bateria"], ["80 W", "carregamento"], ["AMOLED 144 Hz", "tela 6,8\""], ["Dimensity 7400", "processador"]],
      ficha: [
        ["Tela", "6,8\" AMOLED curva 1,5K, 144 Hz, HDR10+"],
        ["Processador", "MediaTek Dimensity 7400-Ultra (4 nm)"],
        ["Memória", "8 GB / 256 GB ou 12 GB / 512 GB"],
        ["Câmera traseira", "50 MP Sony + 8 MP"],
        ["Câmera frontal", "16 MP"],
        ["Bateria", "10.001 mAh · 80 W"],
        ["Resistência", "IP69"],
        ["Rede", "5G · NFC"],
        ["Peso", "219 g"]
      ]
    },
    {
      foto: "img/produtos/pad2.webp?v=1", /* foto do cartaz da loja */
      id: "pad2", marca: "Redmi", nome: "Redmi Pad 2 (com chip)", tag: "Tablet 4G",
      frase: "Tablet de 11\" que aceita chip, com bateria de 9.000 mAh.",
      cam: "duo",
      cores: [["Roxo", "#ddd2ee", "#ad9ad0"], ["Verde", "#cfe8df", "#9ccab8"], ["Cinza", "#4a4c52", "#2a2c30"]],
      dest: [["11\" 2,5K", "tela 90 Hz"], ["9.000 mAh", "bateria"], ["Aceita chip", "internet 4G"], ["Helio G100", "processador"]],
      ficha: [
        ["Tela", "11\" LCD IPS 2,5K, 90 Hz"],
        ["Processador", "MediaTek Helio G100-Ultra"],
        ["Memória", "4 GB / 128 GB"],
        ["Câmera traseira", "8 MP"],
        ["Câmera frontal", "5 MP"],
        ["Bateria", "9.000 mAh · 18 W"],
        ["Rede", "4G (aceita chip)"]
      ]
    },
    {
      foto: "img/produtos/a07.webp?v=1", /* foto do cartaz da loja */
      id: "a07", marca: "Samsung", nome: "Samsung Galaxy A07", tag: "Custo-benefício",
      frase: "Samsung de entrada com tela grande de 6,7\" e bateria de 5.000 mAh.",
      cam: "duo",
      cores: [["Prata", "#d9dade", "#a7a9ae"], ["Verde", "#2f6b5a", "#1b4338"], ["Preto", "#2a2c30", "#141518"]],
      dest: [["6,7\" 90 Hz", "tela grande"], ["Helio G99", "processador"], ["50 MP", "câmera"], ["5.000 mAh", "bateria"]],
      ficha: [
        ["Tela", "6,7\" LCD HD+, 90 Hz"],
        ["Processador", "MediaTek Helio G99"],
        ["Memória", "4 GB / 128 GB ou 4 GB / 256 GB"],
        ["Câmera traseira", "50 MP + 2 MP"],
        ["Câmera frontal", "8 MP"],
        ["Bateria", "5.000 mAh · 25 W"],
        ["Resistência", "IP54"]
      ]
    },
    {
      foto: "img/produtos/a36.webp?v=1", /* foto do cartaz da loja */
      id: "a36", marca: "Samsung", nome: "Samsung Galaxy A36 5G", tag: "Snapdragon",
      frase: "Super AMOLED de 6,7\" 120 Hz, Snapdragon e câmera tripla de 50 MP.",
      cam: "duo",
      cores: [["Preto", "#2a2c30", "#141518"], ["Branco", "#eef0f2", "#c9ccd1"], ["Verde-claro", "#d3e8d6", "#a3c9aa"], ["Lilás", "#d9d3ee", "#aaa0d0"]],
      dest: [["Super AMOLED", "6,7\" 120 Hz"], ["Snapdragon", "6 Gen 3"], ["50 MP", "câmera tripla"], ["IP67", "água e poeira"]],
      ficha: [
        ["Tela", "6,7\" Super AMOLED Full HD+, 120 Hz"],
        ["Processador", "Qualcomm Snapdragon 6 Gen 3"],
        ["Memória", "6 GB de RAM · 128 GB"],
        ["Câmera traseira", "50 MP + 8 MP ultra-wide + 5 MP macro"],
        ["Câmera frontal", "12 MP"],
        ["Bateria", "5.000 mAh · 45 W"],
        ["Rede", "5G · NFC"],
        ["Resistência", "IP67"]
      ]
    },
    {
      foto: "img/produtos/note17-4g.webp?v=1", /* foto do cartaz da loja */
      id: "note17-4g", marca: "Redmi", nome: "Redmi Note 17 4G", tag: "Lançamento",
      frase: "Telão AMOLED de 6,99\" e bateria de 7.700 mAh com carga de 45 W.",
      cam: "duo",
      cores: [["Preto", "#2a2c30", "#141518"], ["Lilás", "#ddd2ee", "#ad9ad0"], ["Azul-claro", "#d3e6ea", "#a2c4cc"]],
      dest: [["6,99\" AMOLED", "tela 120 Hz"], ["7.700 mAh", "bateria"], ["45 W", "carregamento"], ["50 MP", "câmera"]],
      ficha: [
        ["Tela", "6,99\" AMOLED Full HD+, 120 Hz"],
        ["Processador", "Qualcomm Snapdragon 6s Gen 2"],
        ["Memória", "4 GB / 128 GB ou 6 GB / 128 GB"],
        ["Câmera traseira", "50 MP"],
        ["Câmera frontal", "16 MP"],
        ["Bateria", "7.700 mAh · 45 W"],
        ["Resistência", "IP65"],
        ["Sistema", "Xiaomi HyperOS 3 (Android 16)"]
      ]
    },
    {
      foto: "img/produtos/r17.webp?v=1", /* foto do cartaz da loja */
      id: "r17", marca: "Redmi", nome: "Redmi 17", tag: "Bateria monstra",
      frase: "Bateria de 7.500 mAh que dura até 2 dias, com carga de 45 W.",
      cam: "duo",
      cores: [["Preto", "#2a2c30", "#141518"], ["Azul", "#3b5fa8", "#22396b"], ["Lilás", "#ddd2ee", "#ad9ad0"], ["Verde", "#3f4a3c", "#232a21"]],
      dest: [["7.500 mAh", "bateria"], ["45 W", "carregamento"], ["6,9\" 120 Hz", "tela grande"], ["50 MP", "câmera"]],
      ficha: [
        ["Tela", "6,9\" HD+, 120 Hz"],
        ["Processador", "MediaTek Helio G91 Ultra"],
        ["Memória", "4 GB de RAM · 128 GB ou 256 GB + microSD"],
        ["Câmera traseira", "50 MP + câmera auxiliar"],
        ["Câmera frontal", "8 MP"],
        ["Bateria", "7.500 mAh · 45 W · carrega outros aparelhos (22,5 W)"],
        ["Resistência", "IP64"],
        ["Sistema", "Xiaomi HyperOS (Android 16)"]
      ]
    },
    {
      foto: "img/produtos/a15.webp?v=1", /* foto do cartaz da loja */
      id: "a15", marca: "Samsung", nome: "Samsung Galaxy A15 5G", tag: "5G + NFC",
      frase: "Super AMOLED de 6,5\", câmera tripla de 50 MP e 5G.",
      cam: "duo",
      cores: [["Azul-escuro", "#232c45", "#141a2b"], ["Azul-claro", "#dfe8f4", "#b3c6de"], ["Amarelo", "#f3eebf", "#dcd38a"]],
      dest: [["Super AMOLED", "6,5\" 90 Hz"], ["5G", "com NFC"], ["50 MP", "câmera tripla"], ["5.000 mAh", "bateria"]],
      ficha: [
        ["Tela", "6,5\" Super AMOLED Full HD+, 90 Hz"],
        ["Processador", "MediaTek Dimensity 6100+"],
        ["Memória", "4 GB de RAM · 128 GB"],
        ["Câmera traseira", "50 MP + 5 MP ultra-wide + 2 MP macro"],
        ["Câmera frontal", "13 MP"],
        ["Bateria", "5.000 mAh · 25 W"],
        ["Rede", "5G · NFC"]
      ]
    },
    {
      foto: "img/produtos/g06.webp?v=1", /* foto do cartaz da loja */
      id: "g06", marca: "Motorola", nome: "Motorola Moto G06", tag: "Motorola",
      frase: "Tela grande de 6,88\" 120 Hz e bateria de 5.200 mAh.",
      cam: "duo",
      cores: [["Laranja", "#e0703c", "#b04f22"], ["Azul-petróleo", "#3c5a62", "#24393f"], ["Verde", "#7a9a3a", "#556d24"]],
      dest: [["6,88\" 120 Hz", "tela grande"], ["5.200 mAh", "bateria"], ["50 MP", "câmera"], ["IP64", "respingos e poeira"]],
      ficha: [
        ["Tela", "6,88\" LCD IPS HD+, 120 Hz, Gorilla Glass 3"],
        ["Processador", "MediaTek Helio G81"],
        ["Memória", "4 GB / 128 GB ou 4 GB / 256 GB"],
        ["Câmera traseira", "50 MP"],
        ["Câmera frontal", "8 MP"],
        ["Bateria", "5.200 mAh · 10 W"],
        ["Resistência", "IP64"],
        ["Sistema", "Android 15"]
      ]
    }
  ];

  // Lente: anéis metálicos + vidro escuro com reflexo
  function lente(x, y, r, uid, label) {
    return '<g>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + (r + 5) + '" fill="url(#ring' + uid + ')"/>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="#07080b"/>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + (r * .62) + '" fill="url(#glass' + uid + ')"/>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + (r * .22) + '" fill="#0b1630"/>' +
      '<ellipse cx="' + (x - r * .3) + '" cy="' + (y - r * .34) + '" rx="' + (r * .22) + '" ry="' + (r * .13) + '" fill="#fff" opacity=".55" transform="rotate(-30 ' + (x - r * .3) + ' ' + (y - r * .34) + ')"/>' +
      (label ? '<text x="' + x + '" y="' + (y + r + 20) + '" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" font-weight="700" fill="currentColor" opacity=".7">' + label + '</text>' : '') +
      '</g>';
  }
  function flash(x, y) {
    return '<circle cx="' + x + '" cy="' + y + '" r="8" fill="#f3ead2"/><circle cx="' + x + '" cy="' + y + '" r="5" fill="#fff7dc"/>';
  }

  // Ilustração do verso do aparelho (viewBox 300×620)
  function svg(p, ci) {
    var c = p.cores[ci || 0], uid = p.id + (ci || 0);
    var escuro = parseInt(c[1].slice(1, 3), 16) < 90;
    var tx = escuro ? "#e9e6dd" : "#2b2a27";
    var mod = "";
    if (p.cam === "duo") {
      mod = '<rect x="34" y="34" width="150" height="150" rx="38" fill="url(#isl' + uid + ')" stroke="rgba(255,255,255,.18)"/>' +
        lente(82, 84, 30, uid) + lente(140, 134, 22, uid) + flash(140, 74) +
        '<text x="62" y="160" font-family="JetBrains Mono,monospace" font-size="9" fill="' + tx + '" opacity=".6">50MP OIS</text>';
    } else if (p.cam === "pro") {
      mod = '<rect x="30" y="30" width="170" height="170" rx="46" fill="url(#isl' + uid + ')" stroke="rgba(255,255,255,.18)"/>' +
        '<circle cx="96" cy="96" r="50" fill="none" stroke="rgba(255,255,255,.25)"/>' +
        lente(96, 96, 36, uid) + lente(160, 70, 16, uid) + flash(160, 128) +
        '<text x="160" y="170" text-anchor="middle" font-family="Sora,sans-serif" font-size="13" font-weight="800" fill="' + tx + '">200MP</text>';
    } else if (p.cam === "note") {
      mod = '<rect x="34" y="34" width="156" height="156" rx="40" fill="url(#isl' + uid + ')" stroke="rgba(255,255,255,.18)"/>' +
        lente(90, 92, 32, uid) + lente(150, 72, 15, uid) + flash(150, 124) +
        '<text x="90" y="170" text-anchor="middle" font-family="Sora,sans-serif" font-size="12" font-weight="800" fill="' + tx + '">108MP</text>';
    } else {
      mod = '<rect x="36" y="36" width="96" height="184" rx="34" fill="url(#isl' + uid + ')" stroke="rgba(255,255,255,.18)"/>' +
        lente(84, 86, 28, uid) + lente(84, 160, 22, uid) + flash(84, 204) +
        '<text x="150" y="60" font-family="JetBrains Mono,monospace" font-size="10" fill="' + tx + '" opacity=".6">50MP AI</text>';
    }
    return '<svg viewBox="0 0 300 620" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ilustração do ' + p.nome + ' na cor ' + c[0] + '" style="color:' + tx + '">' +
      '<defs>' +
      '<linearGradient id="body' + uid + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="' + c[1] + '"/><stop offset="1" stop-color="' + c[2] + '"/></linearGradient>' +
      '<linearGradient id="isl' + uid + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="' + (escuro ? "#3a3c42" : "#ffffff") + '" stop-opacity=".55"/><stop offset="1" stop-color="' + c[2] + '" stop-opacity=".9"/></linearGradient>' +
      '<linearGradient id="ring' + uid + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f4f4"/><stop offset=".5" stop-color="#7d7f86"/><stop offset="1" stop-color="#d9dade"/></linearGradient>' +
      '<radialGradient id="glass' + uid + '" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#3b4f8c"/><stop offset=".55" stop-color="#121a34"/><stop offset="1" stop-color="#05060a"/></radialGradient>' +
      '<linearGradient id="sheen' + uid + '" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".0"/><stop offset=".5" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>' +
      '<clipPath id="clip' + uid + '"><rect x="8" y="8" width="284" height="604" rx="46"/></clipPath>' +
      '</defs>' +
      '<rect x="4" y="4" width="292" height="612" rx="50" fill="#0c0d10"/>' +
      '<rect x="8" y="8" width="284" height="604" rx="46" fill="url(#body' + uid + ')"/>' +
      '<g clip-path="url(#clip' + uid + ')">' +
      '<rect class="sheen" x="-200" y="-40" width="140" height="720" fill="url(#sheen' + uid + ')" transform="rotate(14)"/>' +
      '<rect x="8" y="8" width="14" height="604" fill="#fff" opacity=".12"/>' +
      '</g>' +
      '<rect x="296" y="150" width="4" height="70" rx="2" fill="#0c0d10"/><rect x="296" y="236" width="4" height="40" rx="2" fill="#0c0d10"/>' +
      mod +
      '<text x="150" y="560" text-anchor="middle" font-family="Sora,sans-serif" font-size="22" font-weight="800" letter-spacing="2" fill="' + tx + '" opacity=".8">' + p.marca.toUpperCase() + '</text>' +
      '</svg>';
  }

  root.RI_PRODUTOS = P;
  root.RI_SVG = svg;
})(window);
