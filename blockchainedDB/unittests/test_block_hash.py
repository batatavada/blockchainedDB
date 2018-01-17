import unittest
import block_header as bh

class test_block_header_hash(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		pass

	'''
	THE TEARDOWN CLASS: setUpClass()
	tearDownClass() method will be executed after all test in the class.
	'''
	@classmethod
	def tearDownClass(cls):
		print('Testing Completed')





	def test_block_header_hash(self):
		""" GENESIS BLOCK: CREATION """
		block = bh.BlockHeader()
		print(block)		

		""" GENESIS BLOCK: HEADER VALUES
		 ----------------------------------------------------------------------------------------"""
		block.version = "01000000"
		block.prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
		block.merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"    
		block.timestamp = int(time.time())
		block.bits = bu.target_to_bits(max_target)
		block.nonce = random.randint(1,2**32)
		""" ----------------------------------------------------------------------------------------"""
		difficulty = 1
		print(block)		
		

		""" GENESIS BLOCK: FINDING NONCE
		 --------------------------------------------------------------------------------------------"""		

		# 1. GET HASH OF ALL HEADER VALUES (EXCEPT NONCE)
		header_hash = bhh.get_block_hash(block)		

		# 2. PROOF OF WORK
		test_hashcash = hc.hashcash()
		nonce, mining_time, genesis_hash = test_hashcash.proof_of_work_iterative(test_header_vars, max_target)
		genesis_hash = test_header.get_block_hash(test_header_vars, str(nonce))		

		# 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
		block = [timestamp, bits, difficulty, nonce, genesis_hash, mining_time]
		blocks.append(block)     		

		print("genesis_block: {}".format(blocks))




'''

	def test_1(self):
		# example from https://blockexplorer.com/block/00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d
		version = "01000000"
		prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
		merkle_root = "2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3"
		timestamp = "1305998791" #Unix time of May 21, 2011 10:56:31 PM
		bits = "440711666"
		nonce = "2504433986"

		#block = [version, prev_block_hash, merkle_root, timestamp, bits, nonce]
		test = b.block_hash()
		output = test.get_block_hash(version, prev_block_hash, merkle_root, timestamp, bits, nonce)

		#hash solution found online
		online_calculated_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

		self.assertEqual(output, online_calculated_hash)






	def test_2(self):
		# example from https://blockchain.info/api/blockchain_api
		version = "01000000"
		prev_block_hash = "00000000000007d0f98d9edca880a6c124e25095712df8952e0439ac7409738a"
		merkle_root = "935aa0ed2e29a4b81e0c995c39e06995ecce7ddbebb26ed32d550a72e8200bf5"
		timestamp = "1322131230" #Unix time of May 21, 2011 10:56:31 PM
		bits = "437129626"
		nonce = "2964215930"

		#block = [version, prev_block_hash, merkle_root, timestamp, bits, nonce]
		test = b.block_hash()
		output = test.get_block_hash(version, prev_block_hash, merkle_root, timestamp, bits, nonce)

		#hash solution found online
		online_calculated_hash = '0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103'

		self.assertEqual(output, online_calculated_hash)
'''





if __name__ == '__main__':
		unittest.main(verbosity = 2)
