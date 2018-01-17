import unittest
import hashcash as hc
import block_header_hash as b
import hash_sha256 as h256
import datetime, time
import csv
import random
import traceback
import numpy as np 


class test_comparehc(unittest.TestCase):

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
        print("TESTING BEGINS")
        MAX_TARGET = "0x0000FFFF00000000000000000000000000000000000000000000000000000000"
        NUM_ITERS = 100

        print("Target: {}".format(MAX_TARGET))

        # CHAIN OF BLOCKS
        Rblocks = []

        # EACH BLOCK IN CHAIN OF BLOCKS
        Rblock = []

        # BLOCK: CREATION (ALL FIELDS EXCEPT TIMESTAMP AND NONCE REMAIN SAME FOR ALL BLOCKS)
        # ----------------------------------------------------------------------------------------
        version = "01000000"
        prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
        merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"    
        timestamp_org = int(time.time())
        bits = "ffff0020"
        nonce = random.randint(1,2**32)
        # ----------------------------------------------------------------------------------------
        difficulty = 1
        test_header = b.block_hash()
        test_hashcash = hc.hashcash()



        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 0



        #---------------------------------TESTING COMPARSION---------------------------------------


        # # RANDOM NONCE GENERATION

        timestamp = timestamp_org
        while(index <= NUM_ITERS): # time.time() - start_time < 600):

            print("\n\nBlock Height (R): {}".format(index))
            
            test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
            
            nonce, mining_time, final_hash = test_hashcash.proof_of_work_random(test_header_vars, MAX_TARGET)
            
            #            0         1        2        3       4
            Rblock = [timestamp, bits, 1, nonce, final_hash, mining_time]

            print(Rblock)
            Rblocks.append(Rblock)
            index += 1
            timestamp += random.randint(1,10)

        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        print("Mining Rate (R): {} blocks per minute".format(mining_rate))


        with open('comparehc_random1_diff4_iter100.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(Rblocks)



    def test2(self):
        print("TESTING BEGINS")
        MAX_TARGET = "0x0000FFFF00000000000000000000000000000000000000000000000000000000"
        NUM_ITERS = 100

        print("Target: {}".format(MAX_TARGET))

        # CHAIN OF BLOCKS
        Iblocks = []

        # EACH BLOCK IN CHAIN OF BLOCKS
        Iblock = []

        # BLOCK: CREATION (ALL FIELDS EXCEPT TIMESTAMP AND NONCE REMAIN SAME FOR ALL BLOCKS)
        # ----------------------------------------------------------------------------------------
        version = "01000000"
        prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
        merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"    
        timestamp_org = int(time.time())
        bits = "ffff0020"
        nonce = 0
        # ----------------------------------------------------------------------------------------
        difficulty = 1
        test_header = b.block_hash()
        test_hashcash = hc.hashcash()


        # TESTING PROOF OF WORK WITH RETARGETS #
        # ----------------------------------------------------------------------------------------
        
        start_time = time.time()
        index = 0


        #---------------------------------TESTING COMPARSION---------------------------------------

        # # ITERATIVE NONCE GENERATION

        timestamp = timestamp_org
        while(index <= NUM_ITERS): # time.time() - start_time < 600):

            print("\n\nBlock Height (I): {}".format(index))
            
            test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
            
            nonce, mining_time, final_hash = test_hashcash.proof_of_work(test_header_vars, MAX_TARGET)
            
            #            0         1        2        3       4
            Iblock = [timestamp, bits, 1, nonce, final_hash, mining_time]

            print(Iblock)
            Iblocks.append(Iblock)
            index += 1
            timestamp += random.randint(1,10)

        end_time = time.time()
        mining_rate = index/(end_time - start_time)*60

        print("Mining Rate (I): {} blocks per minute".format(mining_rate))
        # WRITE BLOCKS TO FILE
        with open('comparehc_iter1_diff4_iter100.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
            writer.writerows(Iblocks)

        


'''
    def test_compare_plot(self):

        NUM_ITERS = 100
        from numpy import genfromtxt
        import matplotlib.pyplot as plt
        from matplotlib.font_manager import FontProperties

        data_iterative = genfromtxt('comparehc_iter1_diff4.csv', delimiter=',', skiprows=1)
        data_random = genfromtxt('comparehc_random1_diff4.csv', delimiter=',', skiprows=1)
        
        time_iterative = np.array(data_iterative[:,0] - data_iterative[0][0])
        time_random = np.array(data_random[:,0] - data_random[0][0])

        fig = plt.figure(figsize=(10,10))
        plt.xlabel("TIME")
        plt.ylabel("BLOCK INDEX")
        plt.title("PROOF OF WORK COMPARISON")     

        #print(len([i for i in range(len(time_iterative))]))
        #print(len(time_iterative))

        plt.plot(time_iterative, np.array([i for i in range(len(time_iterative))]), label = "iteractive method")
        plt.plot(time_random, np.array([i for i in range(NUM_ITERS)]), label = "random method")
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        fontP = FontProperties()
        fontP.set_size('large')
        plt.legend(["random method","iteractive method"], prop=fontP)
        plt.show() 
        fig.savefig('PROOF OF WORK COMPARISON.png')


'''


if __name__ == '__main__':

    MAX_TARGET = "0x00FFFF0000000000000000000000000000000000000000000000000000000000"
    NUM_ITERS = 100
    unittest.main(verbosity = 2)







