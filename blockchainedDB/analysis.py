# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 06:20:34 2018

@author: Srijita
"""

import hashcash as hc
import block_header_hash as bhh
import hash_sha256 as h256
import time
import csv
import block_header as bh
import block_utils as bu


max_target = "0xFFFF000000000000000000000000000000000000000000000000000000000000"
""" GENESIS BLOCK: CREATION """
bl = bh.BlockHeader() 
update_limit = 1
expected_time = 5*60
num_blocks = 10        
difficulty = 1500
f = open('diff 4.15-1000.csv', 'w')
writer = csv.writer(f)
writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])


""" GENESIS BLOCK: HEADER VALUES
 ----------------------------------------------------------------------------------------"""
bl.version = "01000000"
bl.prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
bl.merkle_root = "90eaf5f6d7a99dfe56ae97ff4e6791efe759d451d80dcc4c25b90749db9087d2"
bl.timestamp = int(time.time())
bl.bits = bu.target_to_bits(max_target)
bl.nonce = None

""" ----------------------------------------------------------------------------------------"""
             

""" GENESIS BLOCK: FINDING NONCE
 --------------------------------------------------------------------------------------------"""                

# 1. GET HASH OF ALL HEADER VALUES (EXCEPT NONCE)
genvars = bhh.get_genvars(bl)        

# 2. PROOF OF WORK
bl.nonce, mining_time, genesis_hash = hc.proofOfWork_random(genvars, max_target)
print("genhash:"+genesis_hash)
# genhash:0000c5faa68c1fc743c26cc047ed2f7756cad9f9fc64c7bae2ebc5607b579bf2
print("mining_time: {}".format(mining_time))
# ----------------------------------------------------------------------------------------

# 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
block = [bl.timestamp, bl.bits, difficulty, bl.nonce, genesis_hash, mining_time]
#print(block)  
writer.writerow(block)
bl.prev_block_hash = genesis_hash   

print("genesis_block: {}".format(block))
# ----------------------------------------------------------------------------------------

# TESTING PROOF OF WORK WITH RETARGETS #
# ----------------------------------------------------------------------------------------

start_time = time.time()
index = 1



while (difficulty < 10000):

    difficulty += 2.5
    index = 0

    while(index< 25):   

        print("\n\nDifficulty: (R): {}".format(difficulty)) 
        print("\n\nBlock Height (R): {}".format(index)) 

        bl.timestamp = int(time.time())
        
        target = bu.difficulty_to_target(difficulty, max_target)    

        bl.bits = bu.target_to_bits(max_target) 

        test_header_vars = bhh.get_blockvars(bl)
        
        bl.nonce, mining_time, final_hash = hc.proofOfWork_random(test_header_vars, target)
        
        #            0         1        2        3       4
        block = [bl.timestamp, bl.bits, difficulty, bl.nonce, final_hash, mining_time]
        writer.writerow(block)
        bl.prev_block_hash = final_hash
        index += 1  

        print("Difficulty: {}".format(difficulty))
        print("Mining Time: {} seconds".format(mining_time))
        print("Final Hash: {}".format(final_hash))


end_time = time.time()
mining_rate = index/(end_time - start_time)*60

print("Mining Rate (R): {} blocks per minute".format(mining_rate))
'''
# WRITE BLOCKS TO FILE

with open('diff 1-100.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["TIMESTAMP BITS DIFFICULTY NONCE HASH MINING_TIME"])
    writer.writerows(blocks)

'''



