import unittest
import hashcash as hc
import block_header_hash as b
import hash_sha256 as h256
import datetime, time
import csv
import random
import traceback
import numpy as np 

'''
TEST RETARGET


'''

class test_retarget(unittest.TestCase):

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



    def test1(self):
        #print("TESTING BEGINS")

        # CHAIN OF BLOCKS
        blocks = []
        # EACH BLOCK IN CHAIN OF BLOCKS
        block = []
        

        # GENESIS BLOCK: CREATION 

        # GENESIS BLOCK: HEADER VALUES
        # ----------------------------------------------------------------------------------------
        version = "01000000"
        prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"    
        timestamp = int(time.time())
        bits = "ffff0020"
        nonce = random.randint(1,2**32)
        # ----------------------------------------------------------------------------------------
        difficulty = 1


        # GENESIS BLOCK: FINDING NONCE
        # ----------------------------------------------------------------------------------------
        
        # 1. GET HASH OF ALL HEADER VALUES (EXCEPT NONCE)
        test_header = b.block_hash()
        test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)

        # 2. PROOF OF WORK
        test_hashcash = hc.hashcash()
        max_target = "00FFFF0000000000000000000000000000000000000000000000000000000000"
        nonce, mining_time, genesis_hash = test_hashcash.proof_of_work_random(test_header_vars, max_target)
        # genesis hash = 0008b5b41a6365207a9a5f7e891da2e3441ff6653bdd79d347aff114c2c97fa4

        # 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
        blocks = []
        block = []
        block = [timestamp, bits, difficulty, nonce, genesis_hash, mining_time]
        blocks.append(block)     

        print("genesis_block: {}".format(blocks))

        # ----------------------------------------------------------------------------------------

        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        start_time = time.time()
        index = 0
        NUM_ITERS = 100

        # TESTING FOR A PERIOD OF TEN MINUTES
        # # FIND  PROOF OF WORK WITH RANDOM NONCE GENERATION
		while(index <= NUM_ITERS):

			print("\n\nBlock Height (POW RANDOM): {}".format(index))

            timestamp = int(time.time()) 

            # GET DIFFICULTY AND CHECK RETARGET CONDITION
            current_difficulty = test_hashcash.retarget(index, blocks)

            # GET TARGET FROM DIFFICULTY
            target = test_hashcash.difficulty_to_target(current_difficulty)

            test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
            
            nonce, mining_time = test_hashcash.proof_of_work_random(test_header_vars, target)
            
            final_hash = test_header.get_block_hash(test_header_vars, str(nonce))
            
            #            0         1        2        3       4
            block = [timestamp, bits, current_difficulty, nonce, final_hash, mining_time]


        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        print("Mining Rate: {} blocks per minute".format(mining_rate))

        # WRITE BLOCKS TO FILE

        with open('POW_RANDOM.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(blocks)



if __name__ == '__main__':

    NUM_ITERS = 100
    unittest.main(verbosity = 2)