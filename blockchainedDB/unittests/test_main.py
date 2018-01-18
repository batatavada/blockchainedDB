import chain as c
import unittest
import block_utils as bu
import block_header as bh
import hash_sha256 as hs
import block_header_hash as bhh
import hashcash as hc
import time
import csv


class test_main(unittest.TestCase):

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

        max_target = "0x0000FFFF00000000000000000000000000000000000000000000000000000000"
        difficulty = 1
        version = "01000000" #HEX BYTES     
    
        f = open('Blockchain.csv', 'w')
        writer = csv.writer(f) 

        #INITIAL DECLARATION OF VALUES      

        chain = self.create_chain()  

        genesis_block = self.create_genesis_block(version, max_target)
        chain.addBlock(genesis_block) 
        writer.writerow((genesis_block.version, genesis_block.prev_block_hash, genesis_block.merkle_root, genesis_block.timestamp, genesis_block.bits, genesis_block.nonce))

        

        now = time.time()
        end = now + 10*60   

        while(now < end):
            print("here")
            newBlock = chain.extendChain(version)
            chain.addBlock(newBlock)
            writer.writerow((newblock.version, newblock.prev_block_hash, newblock.merkle_root, newblock.timestamp, newblock.bits, newblock.nonce))  



    




    def create_chain(self):
        print("create_chain")
        ch = c.Blockchain()
        chain = ch.createChain()

        print(type(chain))
        return chain
    





    def create_genesis_block(self, version, max_target): 
        print("create_genesis_block")

        """ GENESIS BLOCK: CREATION """
        block = bh.BlockHeader()                

        """ GENESIS BLOCK: HEADER VALUES
         ----------------------------------------------------------------------------------------"""
        block.version = version
        block.prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        block.merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
        block.timestamp = int(time.time())
        block.bits = bu.target_to_bits(max_target)
        block.nonce = None
        """ ----------------------------------------------------------------------------------------"""
        difficulty = 1              

        """ GENESIS BLOCK: FINDING NONCE
         --------------------------------------------------------------------------------------------"""                

        # 1. GET HASH OF ALL HEADER VALUES (EXCEPT NONCE)
        genvars = bhh.get_genvars(block)        

        # 2. PROOF OF WORK
        block.nonce, mining_time, genesis_hash = hc.proofOfWork_random(genvars, max_target)
        print("genesis_hash:"+str(genesis_hash))
        return block





if __name__ == '__main__':
        unittest.main(verbosity = 2)



