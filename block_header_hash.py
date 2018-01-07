#BLOCK HASH
# Block hash calculated as per this block:
# https://blockexplorer.com/block/00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d 

import hash_sha256 as h

class block_hash:

	def prep_block_vars(self, version, prev_block_hash, merkle_root, timestamp, bits):
		#print("test_proof_of_work")
		self.version = version
		#print("\nVersion: " + self.version)

		self.prev_block_hash = self.little_endian(prev_block_hash)
		#print("\nPrev block hash: " + self.prev_block_hash)

		self.merkle_root = self.little_endian(merkle_root)
		#print("\nMerkle root: " + self.merkle_root)

		self.timestamp = self.hexLittleEndian(timestamp)
		#print("\nTimestamp: " + self.timestamp)

		self.bits = self.hexLittleEndian(bits)
		#print("\nBits: " + self.bits)

		block = str(self.version + self.prev_block_hash + self.merkle_root + self.timestamp + self.bits)

		return block


	def get_block_hash(self, vars, nonce):

		self.nonce = self.hexLittleEndian(nonce)
		#print("\nNonce: " + self.nonce)

		block = (vars + self.nonce)

		#print("\nBlock Header: {}".format(block))
		block_hash = self.hash_calculation(block)

		#print("\nBlock Header Hash: {}".format(block_hash))
		return str(block_hash,'utf-8')



	def hexLittleEndian(self, data):
		x = hex(int(data))
		data  = self.little_endian(x)
		return data[:-2]



	def little_endian(self, hex):
		littleEndian = "";
		if len(hex) % 2 != 0:
		    return littleEndian	

		for x in reversed(hex):
			littleEndian = littleEndian + hex[-2:]
			hex = hex[:-2]
		return littleEndian


	def hash_calculation(self, block):
		# creating object of hash_sha256 class
		x = h.hashing()
		return x.get_block_hash(block)