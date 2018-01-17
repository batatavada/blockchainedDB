
import unittest
import hash_sha256 as h






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

		# REFERENCE: https://en.bitcoin.it/wiki/Block_hashing_algorithm
		v = "01000000"
		p = "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000"
		m = "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b"
		t = "c7f5d74d"
		ta = "f2b9441a"
		n = "42a14695"
		h256 = h.hash_args(v,p,m,t,ta,n)

		tested_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

		self.assertEqual(h256, tested_hash)






if __name__ == '__main__':
		unittest.main(verbosity = 2)
