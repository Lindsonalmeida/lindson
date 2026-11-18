#!/usr/bin/env bash
# MotionForge - gera o .zxp no macOS (ZXPSignCmd da Adobe) ou, em qualquer sistema, a pasta limpa + zip.
# Uso: tools/empacotar-zxp.sh [senha]
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$RAIZ/com.motionforge.panel"; DIST="$RAIZ/dist"; STAGE="$DIST/stage/com.motionforge.panel"
SENHA="${1:-motionforge}"
VERSAO=$(sed -n 's/.*ExtensionBundleVersion="\([^"]*\)".*/\1/p' "$SRC/CSXS/manifest.xml" | head -1)
rm -rf "$DIST/stage"; mkdir -p "$STAGE" "$DIST/bin"
(cd "$SRC" && tar cf - --exclude=tests --exclude=node_modules --exclude=.debug .) | (cd "$STAGE" && tar xf -)
(cd "$DIST/stage" && rm -f "../MotionForge-$VERSAO-pasta.zip" && zip -qr "../MotionForge-$VERSAO-pasta.zip" com.motionforge.panel)
echo "Pasta limpa: $STAGE"
echo "Zip para instalação manual: $DIST/MotionForge-$VERSAO-pasta.zip"
ZXP="$DIST/bin/ZXPSignCmd"
if [[ "$(uname)" == "Darwin" ]]; then
  if [[ ! -x "$ZXP" ]]; then
    curl -fsSL -o "$ZXP" https://raw.githubusercontent.com/Adobe-CEP/CEP-Resources/master/ZXPSignCMD/4.1.3/macOS/ZXPSignCmd
    chmod +x "$ZXP"; xattr -d com.apple.quarantine "$ZXP" 2>/dev/null || true
  fi
  CERT="$DIST/motionforge-cert.p12"
  [[ -f "$CERT" ]] || "$ZXP" -selfSignedCert BR MA "Lindson Almeida" MotionForge "$SENHA" "$CERT"
  rm -f "$DIST/MotionForge-$VERSAO.zxp"
  "$ZXP" -sign "$STAGE" "$DIST/MotionForge-$VERSAO.zxp" "$CERT" "$SENHA" -tsa http://timestamp.digicert.com || "$ZXP" -sign "$STAGE" "$DIST/MotionForge-$VERSAO.zxp" "$CERT" "$SENHA"
  echo "Pronto: $DIST/MotionForge-$VERSAO.zxp"
else
  echo "Assinatura .zxp: rode tools/empacotar-zxp.ps1 no Windows (ou este script no macOS)."
fi
