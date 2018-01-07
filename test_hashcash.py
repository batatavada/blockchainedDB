import unittest
from base64 import b64encode, b64decode 
import hashcash as hc
import block_header_hash as b
import hash_sha256 as h256


class test_hashcash(unittest.TestCase):
    
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

    '''
    def test_get_target(self):
        #
        version = "01000000"
        prev_block_hash = "00000000000007d0f98d9edca880a6c124e25095712df8952e0439ac7409738a"
        merkle_root = "935aa0ed2e29a4b81e0c995c39e06995ecce7ddbebb26ed32d550a72e8200bf5"
        timestamp = "1322131230" #Unix time of May 21, 2011 10:56:31 PM
        bits = "437129626"
        nonce = 0 #random
        #
        bits = "76270618"
        test = hc.hashcash()
        target = test.get_target(bits)

        #hash solution found online
        online_target = '0000000000000000062776000000000000000000000000000000000000000000'

        self.assertEqual(target, online_target)

'''
    def test_proof_of_work(self):
        print("TESTING BEGINS")
        version = "01000000"
        prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
        merkle_root = "2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3"
        timestamp = "1305998791" #Unix time of May 21, 2011 10:56:31 PM
        bits = "440711666"

        test_header = b.block_hash()
        test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, timestamp, bits)
        test_hashcash = hc.hashcash()
        nonce = test_hashcash.proof_of_work(test_header_vars)
        final_hash = test_header.get_block_hash(test_header_vars, str(nonce))

        #hash solution found online
        online_calculated_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

        self.assertEqual(final_hash  , online_calculated_hash)

if __name__ == '__main__':
        unittest.main(verbosity = 2)
