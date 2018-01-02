from Crypto.Hash import SHA256
from base64 import b64encode, b64decode 

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
class hash_256
	
	data = None

	def __init__(self, *args):

		# Concatenating incoming arguments using ":"
		for arg in *args:
			self.data.addTodata(arg)

		#assuming incoming arguments(strings) are of base-64 encoded format
		#convert to utf-8 as SHA only accepts byte-streams

		h = SHA256.new()
		#data = b64encode(b"srijita:paul:kjsce:computers")
		h.update(data)
		final_hash = b64encode(h.digest())
		print(final_hash)
		return final_hash 

	def addTodata(self, arg):
		self.data+=arg+":"
