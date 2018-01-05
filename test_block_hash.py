import unittest
import block_hash as b

class test_hash_256(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		pass

	'''
	THE TEARDOWN CLASS: setUpClass()
	tearDownClass() method will be executed after all test in the class.
	'''
	@classmethod
	def tearDownClass(cls):
		print 'Testing Completed'

	
	def test_1(self):
		version = "01000000"
		prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
		merkle_root = "2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3"
		timestamp = "1305998791" #Unix time of May 21, 2011 10:56:31 PM
		bits = "1a44b9f2"
		nonce = "2504433986"

		#block = [version, prev_block_hash, merkle_root, timestamp, bits, nonce]
		test = b.block_hash()
		output = test.get_block_hash(version, prev_block_hash, merkle_root, timestamp, bits, nonce)

		#hash solution found online
		online_calculated_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

		self.assertEqual(output, online_calculated_hash)


if __name__ == '__main__':
		unittest.main(verbosity = 2)
