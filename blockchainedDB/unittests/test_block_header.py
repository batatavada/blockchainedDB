
import  hashcash             as hc
import  block_header_hash    as b
import  block_header         as bh
import  hash_sha256          as h256
import  unittest             as ut

class test_hashcash(ut.TestCase):
    
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






    def test_create_merkle(self):
        #
        merkle_data = "Welcome. You are now viewing the genesis block. This is where it all begins. So tighten your seat belts and get ready for an adventure or a lifetime."
        test_block_header = bh.block_header()
        output = test_block_header.create_merkle(merkle_data)

        online_calculated_hash = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
        
        self.assertEqual(output, online_calculated_hash)






if __name__ == '__main__':
        ut.main(verbosity = 2)
