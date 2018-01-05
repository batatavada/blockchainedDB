import unittest
from base64 import b64encode, b64decode 
import hash_sha256 as h

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
		#Get hash from hash_256 

		#data = b64encode(b"srijita:paul:kjsce:computers") #= c3Jpaml0YTpwYXVsOmtqc2NlOmNvbXB1dGVycw==
		test = h.hashing()
		block = ["01000000","81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000", "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b", "c7f5d74d", "f2b9441a", "42a14695"]
		data = test.concat("block")
		output = test.get_block_hash("0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a146950x")
		#print(output)
		#hash solution found online
		online_calculated_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

		self.assertEqual(output, online_calculated_hash)



if __name__ == '__main__':
		unittest.main(verbosity = 2)
