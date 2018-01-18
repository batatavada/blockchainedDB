import unittest
import block_header_hash as bhh
import block_header as bh
import time
import block_utils as bu
import random
import hashcash as hc
import csv

class test_block_header_hash(unittest.TestCase):
	
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








	def test1_block_header_hash(self):
		max_target = "0x0000FFFF00000000000000000000000000000000000000000000000000000000"
		""" GENESIS BLOCK: CREATION """
		block = bh.BlockHeader()	
		print(block.version)			

		""" GENESIS BLOCK: HEADER VALUES
		 ----------------------------------------------------------------------------------------"""
		block.version = "01000000"
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
		nonce, mining_time, genesis_hash = hc.proofOfWork_random(genvars, max_target)
		print("genhash:"+genesis_hash)
		# genhash:0000c5faa68c1fc743c26cc047ed2f7756cad9f9fc64c7bae2ebc5607b579bf2
		print("mining_time: {}".format(mining_time))
		'''
		# 3. ADD GENESIS BLOCK TO BLOCKCHAIN LIST
		block = [timestamp, bits, difficulty, nonce, genesis_hash, mining_time]
		blocks.append(block)     				

		print("genesis_block: {}".format(blocks))'''






	def test2_block_header_hash(self):
		#print("\n\nTEST 2")
		block = bh.BlockHeader()
		# example from https://blockchain.info/api/blockchain_api
		block.version = "01000000"
		block.prev_block_hash = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
		block.merkle_root = "2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3"
		block.timestamp = 1305998791 #Unix time of May 21, 2011 10:56:31 PM
		block.bits = "1a44b9f2" #0x1903a30c
		block.nonce = 2504433986

		#block = [version, prev_block_hash, merkle_root, timestamp, bits, nonce]
		blockvars = bhh.get_blockvars(block)
		output = bhh.get_block_hash(blockvars, block.nonce)

		#hash solution found online
		online_calculated_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

		self.assertEqual(output, online_calculated_hash)

		with open('test.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerow([["TIMESTAMP"],["BITS"],["DIFFICULTY"], ["NONCE"], ["HASH"], ["MINING_TIME"]])
			writer.writerow((block.version, block.prev_block_hash, block.merkle_root, block.timestamp))







if __name__ == '__main__':
		unittest.main(verbosity = 2)
