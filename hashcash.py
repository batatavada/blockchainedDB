

import unittest
from base64 import b64encode, b64decode 
import block_header_hash as b
import hash_sha256 as h
import binascii
import time


class hashcash:

	bhash = b.block_hash()

	def get_target(self, bits):
		#REFERENCE: https://bitcoin.stackexchange.com/questions/44579/how-is-a-block-header-hash-compared-to-the-target-bits
		
		print("bits:"+bits)
		bits = self.bhash.little_endian(bits)
		exponent, coefficient = "0x" + bits[:2], "0x" + bits[2:]
		print("exponent, coefficient:"+ exponent, coefficient)
		target = hex(int(coefficient,16) * 2**(8*(int(exponent,16) - 3))).rstrip("L").lstrip("0x")
		print(target)
		target = target.zfill(64)
		#print("TARGET:" + target)
		return target


	def proof_of_work(self, vars):
		print("PROOF OF WORK")
		# example from https://blockexplorer.com/block/00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d

		#m = b"Hello, world!"
		print("vars:"+vars)
		target = self.get_target(vars[-8:])
		print("target: {}".format(target))

		nonce = 2504433940
		interim_hash = self.bhash.get_block_hash(vars, str(nonce))
		#print("interim_hash: {}".format(interim_hash))
		start_time = time.time()	

		while(interim_hash > target):
			print(nonce)
			nonce = nonce + 1
			interim_hash = self.bhash.get_block_hash(vars, str(nonce))		

		end_time = time.time()
		print("Nonce: {} found in Time: {} seconds.".format(nonce,(end_time - start_time)))
		print("Final hash: {}".format(interim_hash))
		return nonce
'''
#OUTPUT
...
...
...
2504433968
2504433969
2504433970
2504433971
2504433972
2504433973
2504433974
2504433975
2504433976
2504433977
2504433978
2504433979
2504433980
2504433981
2504433982
2504433983
2504433984
2504433985
Nonce: 2504433986 found in Time: 35692.147s  ie 9.9144444 hours
Final hash: 00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d
ok
Testing Completed


'''