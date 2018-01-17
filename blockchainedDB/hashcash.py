from base64 import b64encode, b64decode 
import 		block_header_hash 	as bhh
import 		hash_sha256 		as h
import 		block_utils 		as bu
import 		binascii
import 		time
import 		random
import 		unittest



def proofOfWork_random(vars, tar):
	#print("----------------PROOF OF WORK----------------")
	target = tar[2:]
	#print("TARGET: {}".format(target))
	nonce = random.randint(1,2**32)
	interim_hash = bhh.get_block_hash(vars, nonce)
	#print("interim_hash: {}".format(interim_hash))
	start_time = time.time()	
	while(int(interim_hash, 16) > int(target, 16)):
		print("n:{}".format(nonce))
		interim_hash = bhh.get_block_hash(vars, nonce)					
		nonce = random.randint(1,2**32)
	end_time = time.time()
	mining_time = end_time - start_time
	#print("Nonce: {} found in Time: {} seconds.".format(nonce,mining_time))
	#print("Final hash: {}".format(interim_hash))
	return nonce, mining_time, interim_hash





def proofOfWork_iran( vars, tar):
	#print("----------------PROOF OF WORK----------------")
	target = tar[2:]
	#print("TARGET: {}".format(target))
	nonce = random.randint(1,2**32)
	interim_hash = bhash.get_block_hash(vars, str(nonce))
	start_time = time.time()	
	while(int(interim_hash, 16) > int(target, 16)):
		#print(nonce)
		interim_hash = bhash.get_block_hash(vars, str(nonce))					
		nonce = nonce + 1
	end_time = time.time()
	mining_time = end_time - start_time
	return nonce, mining_time, interim_hash




	
def proofOfWork_iterative( vars, tar):
	#print("----------------PROOF OF WORK----------------")
	target = tar[2:]
	#print("TARGET: {}".format(target))
	nonce = 0
	interim_hash = bhash.get_block_hash(vars, str(nonce))
	#print("interim_hash: {}".format(interim_hash))
	start_time = time.time()	
	while(int(interim_hash, 16) > int(target, 16)):
		#print(nonce)
		interim_hash = bhash.get_block_hash(vars, str(nonce))		
		nonce = nonce + 1
	end_time = time.time()
	mining_time = end_time - start_time
	return nonce, mining_time, interim_hash




	
def retarget( index, blocks, update_limit, num_blocks, target_timespan):
	""" Conducts re-targeting every interval of num_blocks
   	Args: 
   		1. index
   		2. blocks
   		3.update_limit : max/min limit, above/below the factor of which difficulty cannot change
   		4. num_blocks : number of blocks after which difficulty is updated
					(correct) 1440 blocks per day ie. 1 block per minute
					(test) 10 blocks every 5 minutes ie. 2 blocks per minute
   		5. target_timespan : number of blocks after which difficulty is updated
						(correct) 1440 blocks per day ie. 1 block per minute
						(test) 10 blocks every 5 minutes ie. 2 blocks per minute
   	Returns: 
   		1. updated difficulty
   		2. retarget
   	"""
	#            0         1        2        3       4
	#block = [timestamp, bits, difficulty, nonce, final_hash]
	current_difficulty = blocks[index-1][2]
	#            0         1        2        3       4
	#block = [timestamp, bits, difficulty, nonce, final_hash]
	current_bits = blocks[index-1][1]
	current_target = hexbits_to_target(current_bits)
	#print("current_difficulty: {}".format(current_difficulty))
	# timestamp of last block ie (current block - 1)
	time_prev_1 = blocks[index-1][0]
	#print("time_prev_1: {}".format(time_prev_1))
	# timestamp of block which was num_blocks away ie (index = current block index - num_blocks)
	time_prev_10 = blocks[index-num_blocks][0] if(index >= num_blocks) else 0
	#print("time_prev_10: {}".format(time_prev_10))
	# check if current block is multiple of num_block
	if( (index % num_blocks) != 0): #or current_difficulty <= update_limit):
		#print("Difficulty = {} ".format(current_difficulty))
		return current_difficulty
	
	else:
		# LIMIT ADJUSTMENT STEP
		actual_timespan = abs(time_prev_1 - time_prev_10)
		#print("actual_timespan: {}".format(actual_timespan))
		
		if actual_timespan < target_timespan/update_limit:
			actual_timespan = target_timespan/update_limit
		if actual_timespan > target_timespan*update_limit:
			actual_timespan = target_timespan*update_limit
		#print("actual_timespan: {}".format(actual_timespan))
		
		# RE-TARGETING
		retarget = float(current_target) * (actual_timespan/ target_timespan)
		updated_difficulty = float(current_difficulty) * (actual_timespan/ target_timespan)
		if(updated_difficulty< 1):
			updated_difficulty = 1
		#print("Difficulty = {} (RETARGET)".format(updated_difficulty))
		return updated_difficulty, retarget




'''
The Bitcoin difficulty started at 1 (and can never go below that). Then for every 2016 blocks that are found, the timestamps of the blocks are compared to find out how much time it took to find 2016 blocks, call it T. We want 2016 blocks to take 2 weeks, so if T is different, we multiply the difficulty by (2 weeks / T) - this way, if the hashrate continues the way it was, it will now take 2 weeks to find 2016 blocks.

For example, if it took only 10 days it means difficulty is too low and thus will be increased by 40%.

The difficulty can increase or decrease depending on whether it took less or more than 2 weeks to find 2016 blocks. Generally, the difficulty will decrease after the network hashrate drops.

If the correction factor is greater than 4 (or less than 1/4), then 4 or 1/4 are used instead, to prevent the change to be too abrupt.
'''



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
