import unittest
import hashcash as hc
import block_header_hash as bhh
import hash_sha256 as h256
import datetime, time
import csv
import random
import block_header as bh
import block_utils as bu

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


    def test_r(self):
        max_target = "0x00000FFFF0000000000000000000000000000000000000000000000000000000"
        """ GENESIS BLOCK: CREATION """
        bl = bh.BlockHeader() 
        update_limit = 2
        expected_time = 10*60
        num_blocks = 10        

        """ GENESIS BLOCK: HEADER VALUES
         ----------------------------------------------------------------------------------------"""
        bl.version = "01000000"
        bl.prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        bl.merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
        bl.timestamp = int(time.time())
        bl.bits = bu.target_to_bits(max_target)
        bl.nonce = None

        merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
        bits = bu.target_to_bits(max_target)
        version = "01000000"
        """ ----------------------------------------------------------------------------------------"""
        difficulty = 1              

        """ GENESIS BLOCK: FINDING NONCE
         --------------------------------------------------------------------------------------------"""                

        # 1. GET HASH OF ALL HEADER VALUES (EXCEPT NONCE)
        genvars = bhh.get_genvars(bl)        

        # 2. PROOF OF WORK
        nonce, mining_time, genesis_hash = hc.proofOfWork_random(genvars, max_target)
        print("genhash:"+genesis_hash)
        # genhash:0000c5faa68c1fc743c26cc047ed2f7756cad9f9fc64c7bae2ebc5607b579bf2
        print("mining_time: {}".format(mining_time))
        # ----------------------------------------------------------------------------------------
        difficulty = 1

        # 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
        blocks = []
        block = []
        block = [bl.timestamp, bl.bits, difficulty, nonce, genesis_hash, mining_time]
        #print(block)
        blocks.append(block)    
        print(blocks)
        prev_block_hash = genesis_hash   

        print("genesis_block: {}".format(block))
        # ----------------------------------------------------------------------------------------


        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 1

        # TESTING FOR A PERIOD OF TEN MINUTES
        while(index< 100): # time.time() - start_time < 600):

            print("\n\nBlock Height (R): {}".format(index))

            bl.timestamp = int(time.time()) 

            # GET DIFFICULTY AND CHECK RETARGET CONDITION
            difficulty = hc.retarget_old(index, blocks, update_limit, num_blocks, expected_time)
            
            target = bu.difficulty_to_target(difficulty, max_target)
            #print("target: {}".format(target))

            bl.bits = bu.target_to_bits(max_target)

            test_header_vars = bhh.get_blockvars(bl)
            
            nonce, mining_time, final_hash = hc.proofOfWork_random(test_header_vars, target)
            
            #            0         1        2        3       4
            block = [bl.timestamp, bits, difficulty, nonce, final_hash, mining_time]
            blocks.append(block)
            prev_block_hash = final_hash
            index += 1

            print("Difficulty: {}".format(difficulty))
            print("Final Hash: {} ".format(final_hash.zfill(64)))
            print("Mining Time: {} seconds".format(mining_time))



        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        print("Mining Rate (R): {} blocks per minute".format(mining_rate))

        # WRITE BLOCKS TO FILE

        with open('i_pow_iter10000_diff2_ul2_et25mins_RE.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(blocks)



'''

    def test_i(self):
        max_target = "0x000000FFFF00000000000000000000000000000000000000000000000000000000"
        """ GENESIS BLOCK: CREATION """
        bl = bh.BlockHeader() 
        update_limit = 2
        expected_time = 5*60
        num_blocks = 10        

        """ GENESIS BLOCK: HEADER VALUES
         ----------------------------------------------------------------------------------------"""
        bl.version = "01000000"
        bl.prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        bl.merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
        bl.timestamp = int(time.time())
        bl.bits = bu.target_to_bits(max_target)
        bl.nonce = None

        merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
        bits = bu.target_to_bits(max_target)
        version = "01000000"
        """ ----------------------------------------------------------------------------------------"""
        difficulty = 1              

        """ GENESIS BLOCK: FINDING NONCE
         --------------------------------------------------------------------------------------------"""                

        # 1. GET HASH OF ALL HEADER VALUES (EXCEPT NONCE)
        genvars = bhh.get_genvars(bl)        

        # 2. PROOF OF WORK
        nonce, mining_time, genesis_hash = hc.proofOfWork_iterative(genvars, target)
        print("genhash:"+genesis_hash)
        # genhash:0000c5faa68c1fc743c26cc047ed2f7756cad9f9fc64c7bae2ebc5607b579bf2
        print("mining_time: {}".format(mining_time))
        # ----------------------------------------------------------------------------------------
        difficulty = 1

        # 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
        blocks = []
        block = []
        block = [bl.timestamp, bl.bits, difficulty, nonce, genesis_hash, mining_time]
        #print(block)
        blocks.append(block)    
        print(blocks)
        prev_block_hash = genesis_hash   

        print("genesis_block: {}".format(block))
        # ----------------------------------------------------------------------------------------


        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 1

        # TESTING FOR A PERIOD OF TEN MINUTES
        while(index< 100): # time.time() - start_time < 600):

            print("\n\nBlock Height (I): {}".format(index))

            bl.timestamp = int(time.time()) 

            # GET DIFFICULTY AND CHECK RETARGET CONDITION
            difficulty = hc.retarget_old(index, blocks, update_limit, num_blocks, expected_time)
            
            target = bu.difficulty_to_target(difficulty, max_target)

            bl.bits = bu.target_to_bits(max_target)

            test_header_vars = bhh.get_blockvars(bl)
            
            nonce, mining_time, final_hash = hc.proofOfWork_iterative(test_header_vars, max_target)
            
            #            0         1        2        3       4
            block = [bl.timestamp, bits, difficulty, nonce, genesis_hash, mining_time]
            blocks.append(block)
            prev_block_hash = final_hash
            index += 1

            print("Difficulty: {}".format(difficulty))
            print("Mining Time: {} seconds".format(mining_time))


        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60  

        print("Mining Rate (I): {} blocks per minute".format(mining_rate))

        # WRITE BLOCKS TO FILE

        with open('i_pow_iter10000_diff2_ul2_et25mins_RE.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(blocks)




'''
    

if __name__ == '__main__':
        unittest.main(verbosity = 2)




