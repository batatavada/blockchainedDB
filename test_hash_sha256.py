import unittest
from base64 import b64encode, b64decode 
import hash_sha256 as h

'''
Using Python's built-in unittest framework, any member function whose name begins with test in a class deriving from unittest.TestCase will be run, and its assertions checked, when unittest.main() is called.
'''

class test_hash_256(unittest.TestCase):

	
	print("Testing manually with five different inputs")
	print("1. Strings: (srijita, paul, kjsce, computers)")
	print("2. Strings:(null, 12345678, 987654321, null)")
	print("3. Strings:(null)")
	print("4. Strings:(null, srijita4567, paul!?$%^&*(, #%&$(!$%,\")")
	print("5. Strings:(null, 00000, 11111, null)")
	

	'''Tests for `hash_256`.'''
	'''
	Procedure to calculate:
	1. Take base64-encoded Strings that you want to test: eg: x,y,z
	2. Pass x,y,z to the concat function eg: test.concat(x,y,z)
	3. Resultant final hash calculated by the hash_sha256 class is stored in test

	#CROSS CHECKING the output
	4. Decode the strings and concat them. eg: data = "decode(x):decoded(y):decoded(z)" (Suggestion: https://www.base64encode.org/)
	5. Find the hash of the data online. (Suggestion: http://www.xorbin.com/tools/sha256-hash-calculator)
	5. Make online_calculated_hash variable equal to hash obtained
	6. Check if the assertEqual function is True.


	'''
	

	'''
	THE SETUP CLASS: setUpClass()
	A class method called before tests in an individual class run.
	It is called once before any tests in class.
	TestCase class has a setUpClass() method which can be overridden to execute before the execution of individual tests inside a TestCase class.
	'''
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
		data = test.concat(b64encode(b"srijita"), b64encode(b"paul"), b64encode(b"kjsce"), b64encode(b"computers"))
		output = test.get_hash(data)

		#hash solution found online
		online_calculated_hash = b"3bf7530c961a121c0d166207b99a3b3caf63fd15d98a7a1aa7ec596e3562b24b"
		encoded_online_calculated_hash = b64encode(online_calculated_hash)

		self.assertEqual(output, encoded_online_calculated_hash)



	def test_2(self):
		print('im here')
		#Get hash from hash_256 

		#data = b64encode(b"12345678:987654321")
		test = h.hashing()
		data = test.concat(b64encode(b""), b64encode(b"12345678"), b64encode(b"987654321"), b64encode(b""))
		output = test.get_hash(data)

		#hash solution found online
		#hash calculated for "12345678:987654321"
		online_calculated_hash = b"9649fddabfab5fd12172e7d57de070b2a8048a9ce0654c76e2590ea8b5709403"
		encoded_online_calculated_hash = b64encode(online_calculated_hash)
		#print(encoded_online_calculated_hash)

		self.assertEqual(output, encoded_online_calculated_hash)


	def test_3(self):
		#Get hash from hash_256 

		#data = null 
		test = h.hashing()
		data = test.concat(b64encode(b""))
		output = test.get_hash(data)

		#hash solution found online
		online_calculated_hash = b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
		encoded_online_calculated_hash = b64encode(online_calculated_hash)

		self.assertEqual(output, encoded_online_calculated_hash)


	def test_4(self):
		#print('im here')
		#Get hash from hash_256 

		#data = b64encode(b"srijita:paul:kjsce:computers") #= c3Jpaml0YTpwYXVsOmtqc2NlOmNvbXB1dGVycw==
		test = h.hashing()
		data = test.concat(b64encode(b""), b64encode(b"srijita4567"), b64encode(b"paul!?$%^&*("), b64encode(b"#%&$(!$%,\""))
		output = test.get_hash(data)

		#hash solution found online
		online_calculated_hash = b"53b95f9564354fb1285ad8da74164ccbb932f4aa1a9efb4345339b1c30dc7df7"
		encoded_online_calculated_hash = b64encode(online_calculated_hash)

		self.assertEqual(output, encoded_online_calculated_hash)


	def test_5(self):
		print('im here')
		#Get hash from hash_256 

		#data = b64encode(b"srijita:paul:kjsce:computers") #= c3Jpaml0YTpwYXVsOmtqc2NlOmNvbXB1dGVycw==
		test = h.hashing()
		data = test.concat(b64encode(b""), b64encode(b"00000000"), b64encode(b"11111111"), b64encode(b""))
		output = test.get_hash(data)

		#hash solution found online
		online_calculated_hash = b"31b4e08db12a1ebc2d1fa5ed4113224952f6e4a52e824cf7d9a1fe9c91b8ff11"
		encoded_online_calculated_hash = b64encode(online_calculated_hash)

		self.assertEqual(output, encoded_online_calculated_hash)


if __name__ == '__main__':
		unittest.main(verbosity = 2)



'''
Every module has a name and statements in a module can find out the name of its module. This is especially handy in one particular situation - When a module is imported for the first time, the main block in that module is run. What if we want to run the block only if the program was used by itself and not when it was imported from another module? This can be achieved using the __name__ attribute of the module. 
'''