import hash
from base64 import b64encode, b64decode 

class main:
	print('im maining')
	data = b64encode(b"srijita:paul:kjsce:computers")
	h = hash.hash_sha256(data)