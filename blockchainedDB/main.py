import hash
from base64 import b64encode, b64decode
import chain
import block_utils as bu
import block_header as bh
import hash_sha256 as hs
import block_header_hash as bhh


class main:



    max_target = "0x0000FFFF00000000000000000000000000000000000000000000000000000000"
    difficulty = 1
    version = "01000000" #HEX BYTES   



    def __init__(self):
            #INITIAL DECLARATION OF VALUES  

        chain = create_chain()
        genesis_block = create_genesis_block()
        chain.add_block(genesis_block)
    




	def create_chain(self):
		c = chain.BlockChain(version, max_target, difficulty)
        return c






	def create_genesis_block(self):

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
        return block



