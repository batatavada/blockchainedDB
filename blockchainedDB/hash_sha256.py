
from base64 import b64encode, b64decode 
from Crypto.Hash import SHA256
import hashlib
import codecs






def hash_args(*args):
		# Concatenating incoming arguments using ":"
	data = ""
	for arg in args:
		data+= "" if (arg == "") else (str(arg))
	return hash256(data)






def concat(*args):
	# Concatenating incoming arguments using ":"
	data = ""
	for arg in args:
		data+= "" if (arg == "") else (str(arg))
	return data






def hash256(data):
	print("od:"+data)
	import binascii
	# get the binary data (byte string) represented by the hexadecimal string
	header_bin = binascii.unhexlify(data)
	# get double hash with sha-256 of above binary data
	ha = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
	# get the hexadecimal representation of the hashed binary data
	h = binascii.hexlify(bytearray(data, 'utf-8'))
	# convert bytes string to utf-8 encoded string
	h = str(codecs.encode(ha[::-1],'hex'),'utf-8')
	return h
