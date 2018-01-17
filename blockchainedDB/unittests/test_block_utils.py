import      hashcash            as hc
import      block_header_hash   as b
import      block_utils         as bu
import      datetime, time
import      csv
import      random
import      unittest


# ----------------------------------------------------------------------------------------------------#

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






    def test_hexbits_to_target(self):
        bits = "0x1d00ffff"
        target = bu.hexbits_to_target(bits)
        tested_target = '0x00000000ffff0000000000000000000000000000000000000000000000000000'
        self.assertEqual(target, tested_target) 






    def test_decimalbits_to_target(self):
        bits = 4294901789
        target = bu.decimalbits_to_target(bits)
        tested_target = '0x00000000ffff0000000000000000000000000000000000000000000000000000'
        self.assertEqual(target, tested_target)






    def test_target_to_bits(self):
        target = "0x00000000ffff0000000000000000000000000000000000000000000000000000"
        bits = bu.target_to_bits(target)
        tested_bits = "0x1d00ffff"
        self.assertEqual(bits, tested_bits)






    def test_bits_to_difficulty(self):
        bits = "0x1d00ffff"
        max_target = "0x00000000FFFF0000000000000000000000000000000000000000000000000000"
        difficulty = bu.bits_to_difficulty(max_target,bits)

        tested_difficulty = 1
        print(d)






    def test_plot_timevsblocks_fromlists(self):
        #    0 1 2 3   #indices
        m = [
            [0,1,2,3],
            [2,3,4,5],
            [3,4,5,6],
            [5,10,8,9]
            ]
        bu.plot_timevsblocks_fromlists(m,1,3, "TEST GRAPH (from list)", "TEST - X Attribute", "TEST - Y Attribute")
        # should plot x=[1,3,4,10] vs y=[3,5,6,9]





    def test_plot_timevsblocks_fromcsv(self):
        bu.plot_timevsblocks_fromcsv('output.csv',6,0, "TEST GRAPH (from csv)", "TEST - X Attribute (time)", "TEST - Y Attribute (block index)")






if __name__ == '__main__':
        unittest.main(verbosity = 2)