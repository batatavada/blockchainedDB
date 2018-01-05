
difficulty = 1			#lowest difficulty

ideal_timespan = 60		#60 seconds

message = "This is a random message." 	#Block header and Transactions
time_beg = time.time()				#time of block that was 2016 blocks ago
time_prev  = time_beg
						# set variable to null again at 2017th element ie. index=2016
index = 1
block_hash = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"

def get_difficulty(self, current_time)
		
		if(index == 2016):	#in Bitcoin, index is multiple of 2016
			# Limit adjustment step
			actual_timespan = abs(time_prev - time_beg)
			
			if actual_timespan < ideal_timespan/4:
				actual_timespan = ideal_timespan/4
			if actual_timespan > ideal_timespan*4:
				actual_timespan = ideal_timespan*4
			
			# Retarget
			difficulty = difficulty * (actual_timespan / ideal_timespan)
			time_prev = current_time #set time_prev for the next 2016 blocks

		index = index+1;

#proof_of_work
def proof_of_work(self):
	block_hash = 
	target = 
	while hash > target:
		current_time = time.time()
		difficulty = get_difficulty(current_time)

import string
import random
def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size)