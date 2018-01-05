#BLOCK HASH
# Block hash calculated as per this block:
# https://blockexplorer.com/block/00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d 

import hash_sha256 as h

class block_hash:

	def get_block_hash(self, version, prev_block_hash, merkle_root, timestamp, bits, nonce):
		self.version = version
		print "Version: " + self.version

		self.prev_block_hash = self.little_endian(prev_block_hash)
		print "Prev block hash: " + self.prev_block_hash

		self.merkle_root = self.little_endian(merkle_root)
		print "Merkle root: " + self.merkle_root

		self.timestamp = self.get_timestamp(timestamp)
		print "Timestamp: " + self.timestamp

		self.bits = self.little_endian(bits)
		print "Bits: " + self.bits

		self.nonce = self.get_nonce(nonce)
		print "Nonce: " + self.nonce

		block = [self, self.version, self.prev_block_hash, self.merkle_root, self.timestamp, self.bits, self.nonce]
		#block = self.version + self.prev_block_hash + self.merkle_root + self.timestamp + self.bits + self.nonce

		block_hash = self.hash_calculation(block)

		print block_hash
		return block_hash


	def little_endian(self, hex):
		hexLittleEndian = "";
		if len(hex) % 2 != 0:
		    return hexLittleEndian	

		for x in reversed(hex):
			#print "in loop"
			hexLittleEndian = hexLittleEndian + hex[-2:]
			hex = hex[:-2]
		#print(hexLittleEndian)
		return hexLittleEndian


	def get_timestamp(self, time):
		# unix time for May 21, 2011 10:56:31 PM (not global, LOCAL TIME)
		# Suggested: https://www.epochconverter.com/
		x = hex(int(time))
		# Convert to little endian
		timestamp = self.little_endian(x)
		return timestamp[:-2]

	def get_nonce(self, nonce):
		x = hex(int(nonce))
		nonce  = self.little_endian(x)
		return nonce[:-2]


	def hash_calculation(self, block):
		# creating object of hash_sha256 class
		x = h.hashing()
		data = x. concat(block)
		return x.get_block_hash(str(data))