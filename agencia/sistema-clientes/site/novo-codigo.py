"""Gera um código de acesso novo para um cliente da Central, sem mexer nos segredos da Cloudflare (conta Zuleide, 03/11/2026).
  python3 novo-codigo.py sf SFD
Mostra o código (mande só para o cliente; não salve em repositório nenhum) e a linha {sal, hash, cli} para colar em
CentralLindsonALmeida/functions/_codigos.js (repositório PRIVADO). O site confere em functions/_lib.js (clienteDoCodigo)."""
import hashlib, secrets, sys
cli = sys.argv[1]; pre = (sys.argv[2] if len(sys.argv) > 2 else cli[:3]).upper()[:3]
AB = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'  # sem 0/O, 1/I/L
corpo = ''.join(secrets.choice(AB) for _ in range(8))
codigo = f'{pre}-{corpo[:4]}-{corpo[4:]}'; norm = (pre + corpo).upper()
assert len(norm) == 11
sal = secrets.token_bytes(16)
h = hashlib.pbkdf2_hmac('sha256', norm.encode(), sal, 100000, 32)
print('CÓDIGO:', codigo)
print("LINHA:  { sal: '%s', hash: '%s', cli: '%s' }," % (sal.hex(), h.hex(), cli))
