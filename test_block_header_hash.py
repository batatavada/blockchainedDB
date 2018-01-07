import unittest
import block_header_hash as b

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

	
	def test_1(self):

		print("TEST 1")
		# example from https://blockexplorer.com/block/00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d
		version = "01000000"
		prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
		merkle_root = "2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3"
		timestamp = "1305998791" #Unix time of May 21, 2011 10:56:31 PM
		bits = "440711666"
		nonce = "2504433986"

		test = b.block_hash()
		block_header_vars = test.prep_block_vars(version, prev_block_hash, merkle_root, timestamp, bits)
		print("block_header_vars: {}".format(block_header_vars))

		output = test.get_block_hash(block_header_vars, nonce)

		#hash solution found online
		online_calculated_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

		self.assertEqual(output, online_calculated_hash)


	def test_2(self):

		print("\n\nTEST 2")
		# example from https://blockchain.info/api/blockchain_api
		version = "01000000"
		prev_block_hash = "00000000000007d0f98d9edca880a6c124e25095712df8952e0439ac7409738a"
		merkle_root = "935aa0ed2e29a4b81e0c995c39e06995ecce7ddbebb26ed32d550a72e8200bf5"
		timestamp = "1322131230" #Unix time of May 21, 2011 10:56:31 PM
		bits = "437129626"
		nonce = "2964215930"

		#block = [version, prev_block_hash, merkle_root, timestamp, bits, nonce]
		test = b.block_hash()
		block_header_vars = test.prep_block_vars(version, prev_block_hash, merkle_root, timestamp, bits)

		output = test.get_block_hash(block_header_vars, nonce)

		#hash solution found online
		online_calculated_hash = '0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103'

		self.assertEqual(output, online_calculated_hash)


if __name__ == '__main__':
		unittest.main(verbosity = 2)
