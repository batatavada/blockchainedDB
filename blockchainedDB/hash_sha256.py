from Crypto.Hash import SHA256
from base64 import b64encode, b64decode 
import hashlib
import codecs

# BITCOIN USES base-58 FOR ENCODING ADDRESSES
# WE HAVE USED base-64
'''
Why base-58 instead of standard base-64 encoding? (IN BITCOIN)
  -  Don't want 0OIl characters that look the same in some fonts and could be used to create visually identical looking account numbers.
  -  A string with non-alphanumeric characters is not as easily accepted as an account number.
  -  E-mail usually won't line-break if there's no punctuation to break at.
  -  Doubleclicking selects the whole number as one word if it's all alphanumeric.
'''

#Concatenating incoming arguments and hashing with sha256
class hashing:

	# Concatenating incoming arguments using ":"
	def concat(self, args):
		data = ""
		for arg in args:
			data+= "" if (arg == "") else (str(arg))
		return data

		#assuming incoming arguments(strings) are of base-64 encoded format
		#convert to utf-8 as SHA only accepts byte-streams

	def get_hash(self, data):
		import binascii
		data=binascii.hexlify(bytearray(data, 'utf-8'))
		h = SHA256.new()
		h.update(data)
		final_hash = b64encode(h.digest())
		return final_hash

	def get_block_hash(self, data):
		import binascii
		string = data.strip()
		header_bin = binascii.unhexlify(string)
		ha = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
		h = str(binascii.hexlify(bytearray(data, 'utf-8')))
		#hash.encode('hex_codec')
		#h = ha.encode('hex_codec')
		h = codecs.encode(ha[::-1],'hex')
		#print(h)
		return h
		#except Exception,e: print "EXCEPTION: " + str(e)

'''
				header_bin = codecs.decode(data, 'hex')
		ha = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
		codecs.encode(ha,'hex')
		h = codecs.encode(ha[::-1],'hex')
		print(h)
		print(type(h))
		return str(h,'ascii')'''