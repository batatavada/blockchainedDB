import hash_sha256 as h
import block_utils as bu



def get_genvars(block):
	""" Extract the available block instance variables and get their concatenated hash
	ARGS:
		- block instance variables like version, previous_block_hash etc in Big ENDIAN FORMAT
			+ block.version (STRING BE)
			+ block.prev_block_hash (STRING BE) "000.."
			+ block.merkle_root (STRING BE)  
			+ block.timestamp (DECIMAL INT BE)
			+ block.bits (HEX STRING BE)
			+ block.nonce (DECIMAL INT BE)
	RETURNS:
		- concatenated hash in STRING (BE)
	"""
	version = block.version
	print("\nVersion: " + version)

	prev_block_hash = block.prev_block_hash
	print("\nPrev block hash: " + prev_block_hash)

	merkle_root = bu.little_endian(block.merkle_root).lstrip('0x')
	print("\nMerkle root: " + merkle_root)

	timestamp = bu.hexLittleEndian(block.timestamp).strip('0x')
	timestamp = timestamp if(len(timestamp)%2==0) else timestamp.zfill(len(timestamp)+1)
	
	print("\nTimestamp: " + timestamp)

	bits = bu.little_endian(block.bits.lstrip('0x')).lstrip('0x')
	print("\nBits: " + bits)

	genvars = h.concat(version, prev_block_hash, merkle_root, timestamp, bits)

	return genvars





def get_blockvars(block):
	""" Extract the available block instance variables and get their concatenated hash
	ARGS:
		- block instance variables like version, previous_block_hash etc in Big ENDIAN FORMAT
			+ block.version (STRING BE)
			+ block.prev_block_hash (STRING BE)
			+ block.merkle_root (STRING BE)  
			+ block.timestamp (DECIMAL INT BE)
			+ block.bits (HEX STRING BE)
			+ block.nonce (DECIMAL INT BE)
	RETURNS:
		- concatenated hash in STRING (BE)
	"""
	version = block.version
	#print("\nVersion: " + version)

	prev_block_hash = bu.little_endian(block.prev_block_hash).lstrip('0x')
	#print("\nPrev block hash: " + prev_block_hash)

	merkle_root = bu.little_endian(block.merkle_root).lstrip('0x')
	#print("\nMerkle root: " + merkle_root)

	timestamp = bu.hexLittleEndian(block.timestamp).strip('0x')
	timestamp = timestamp if(len(timestamp)%2==0) else timestamp.zfill(len(timestamp)+1)
	#print("\nTimestamp: " + timestamp)

	bits = bu.little_endian(block.bits).strip('0x')
	#print("\nBits: " + bits)

	blockvars = h.concat(version, prev_block_hash, merkle_root, timestamp, bits)

	return blockvars






# USED DURING POW
def get_block_hash(blockvars, nonce):
	""" Concats blockvars with interim_nonce and returns hash during proof of work
	ARGS:
		- all block instance variables except nonce etc in Big ENDIAN FORMAT
			+ concatenated blockvars (HEX STRING)
		- block.nonce (DECIMAL INT BE)
	RETURNS:
		- concatenated hash in STRING (BE)n
	"""
	#print(nonce)
	n = bu.hexLittleEndian(nonce).strip('0x')

	# APPEND ZERO IF LENGTH OF NONCE IS ODD. BECAUSE BINASCII.UNHEXLIFYY(USED IN hash_sha256) REQUIRED EVEN LENGTH
	n = n if(len(n)%2==0) else n.zfill(len(n)+1)
	#print("\nNonce: " + n)
	block_hash = h.hash_args(blockvars, n)
	return block_hash









def get_hash(block):
	""" Extract the available block instance variables and get their concatenated hash
	ARGS:
		- block instance variables like version, previous_block_hash etc in Big ENDIAN FORMAT
			+ block.version (STRING BE)
			+ block.prev_block_hash (STRING BE)
			+ block.merkle_root (STRING BE)  
			+ block.timestamp (DECIMAL INT BE)
			+ block.bits (HEX STRING BE)
			+ block.nonce (DECIMAL INT BE)
	RETURNS:
		- concatenated hash in STRING (BE)
	"""
	version = block.version
	print("\nVersion: " + version)

	prev_block_hash = bu.little_endian(block.prev_block_hash).lstrip('0x')
	print("\nPrev block hash: " + block.prev_block_hash)

	merkle_root = bu.little_endian(block.merkle_root).lstrip('0x')
	print("\nMerkle root: " + merkle_root)

	timestamp = bu.hexLittleEndian(block.timestamp).strip('0x')
	print("\nTimestamp: " + timestamp)

	bits = bu.little_endian(block.bits).strip('0x')
	print("\nBits: " + bits)

	n = bu.hexLittleEndian(block.nonce).strip('0x')
	n = n if(len(n)%2==0) else n.zfill(len(n)+1)
	print("\nNonce: " + n)

	blockvars = h.concat(version, prev_block_hash, merkle_root, timestamp, bits, n)
	print(h.hash256(blockvars))

	return h.hash256(blockvars)
