import unittest
import hashcash as hc
import block_header_hash as b
import hash_sha256 as h256
import datetime, time
import csv
import random



class test_hashcash_compare(unittest.TestCase):

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



    def test1_proof_of_work_random(self):
        #print("TESTING BEGINS")

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
         
        #            0        2        3           4
        block = [timestamp, nonce, genesis_hash, mining_time]
        blocks.append(block)     

        print("genesis_block: {}".format(blocks))

        # ----------------------------------------------------------------------------------------


        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 1

        # TESTING FOR A PERIOD OF TEN MINUTES
        # # FIND  PROOF OF WORK WITH RANDOM NONCE GENERATION
        while(index <= NUM_ITERS): # time.time() - start_time < 600):

            print("\n\nBlock Height (RANDOM): {}".format(index))

            timestamp = int(time.time())

            test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
            
            nonce, mining_time, final_hash = test_hashcash.proof_of_work_random(test_header_vars, max_target)
            
            #            0        2        3           4
            block = [timestamp, nonce, final_hash, mining_time]
            
            print(block)
            blocks.append(block)
            prev_block_hash = final_hash
            index += 1


        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        print("Mining Rate: {} blocks per minute".format(mining_rate))

        # WRITE BLOCKS TO FILE

        with open('r_pow_iter1000_diff2_ul2.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(blocks)

 


    # FIND  PROOF OF WORK WITH ITERATIVE NONCE GENERATION
 
    def test_proof_of_work_iterative(self):
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
        nonce, mining_time, genesis_hash = test_hashcash.proof_of_work_iterative(test_header_vars, max_target)
        # genesis hash = 0008b5b41a6365207a9a5f7e891da2e3441ff6653bdd79d347aff114c2c97fa4

        # 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
        block = [timestamp, nonce, genesis_hash, mining_time]
        blocks.append(block)     

        print("genesis_block: {}".format(blocks))
        # ----------------------------------------------------------------------------------------



        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 1

        # TESTING FOR A PERIOD OF TEN MINUTES
        #RANDOM
        while(index <= NUM_ITERS): # time.time() - start_time < 600):

            print("\n\nBlock Height (ITERATIVE): {}".format(index))

            timestamp = int(time.time()) 

            test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
            
            nonce, mining_time, final_hash = test_hashcash.proof_of_work_iterative(test_header_vars, max_target)
            
            #            0        2        3           4
            block = [timestamp, nonce, final_hash, mining_time]
            print(block)
            blocks.append(block)
            prev_block_hash = final_hash
            index += 1


        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        #print("Mining Rate: {} blocks per minute".format(mining_rate))

        # WRITE BLOCKS TO FILE
        with open('i_pow_iter1000_diff2_ul2.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(blocks)


    def test_proof_of_work_iran(self):
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
        nonce, mining_time, genesis_hash = test_hashcash.proof_of_work_iran(test_header_vars, max_target)
        # genesis hash = 0008b5b41a6365207a9a5f7e891da2e3441ff6653bdd79d347aff114c2c97fa4

        # 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
        block = [timestamp, nonce, genesis_hash, mining_time]
        blocks.append(block)     

        print("genesis_block: {}".format(blocks))
        # ----------------------------------------------------------------------------------------



        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 1

        # TESTING FOR A PERIOD OF TEN MINUTES
        # RANDOM
        while(index <= NUM_ITERS): # time.time() - start_time < 600):

            print("\n\nBlock Height (IRAN): {}".format(index))

            timestamp = int(time.time()) 

            test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
            
            nonce, mining_time, final_hash = test_hashcash.proof_of_work_iran(test_header_vars, max_target)
            
            #            0        2        3           4
            block = [timestamp, nonce, final_hash, mining_time]
            print(block)
            blocks.append(block)
            prev_block_hash = final_hash
            index += 1


        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        #print("Mining Rate: {} blocks per minute".format(mining_rate))

        # WRITE BLOCKS TO FILE
        with open('ir_pow_iter1000_diff2_ul2.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(blocks)
'''

    def test_compare_performance_nonce(self):

        from numpy import genfromtxt
        import matplotlib.pyplot as plt
        from matplotlib.font_manager import FontProperties

        data_iterative = genfromtxt('i_pow_iter1000_diff2_ul2.csv', delimiter=',', skiprows=1)
        data_random = genfromtxt('r_pow_iter1000_diff2_ul2.csv', delimiter=',', skiprows=1)
        data_iran = genfromtxt('ir_pow_iter1000_diff2_ul2.csv', delimiter=',', skiprows=1)
        
        time_iterative = np.array(data_iterative[:,0] - data_iterative[0][0])
        time_random = np.array(data_random[:,0] - data_random[0][0])
        time_iran = np.array(data_iran[:,0] - data_iran[0][0])

        fig = plt.figure(figsize=(10,10))
        plt.xlabel("TIME")
        plt.ylabel("BLOCK INDEX")
        plt.title("pow_iter1000_diff2_ul2")     

        #print(len([i for i in range(len(time_iterative))]))
        #print(len(time_iterative))

        plt.plot(time_iterative, np.array([i for i in range(len(time_iterative))]), label = "iteractive method")
        plt.plot(time_random, np.array([i for i in range(len(time_random))]), label = "random method")
        plt.plot(time_iran, np.array([i for i in range(len(time_iran))]), label = "iran method")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        fontP = FontProperties()
        fontP.set_size('large')
        plt.legend(["iteractive method","random method","iran method"], prop=fontP)
        plt.show() 
        fig.savefig('pow_iter1000_diff2_ul2.png')


'''



if __name__ == '__main__':

    NUM_ITERS = 1000
    unittest.main(verbosity = 2)
