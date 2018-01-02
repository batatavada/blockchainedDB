import hashcash
import hash_256
import time
import datetime, time
from random import randrange

'''
This is a 4-byte timestamp, encoded as a Unix ‘Epoch’ timestamp which is a system for describing a point in time, defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, minus the number of leap seconds that have taken place since then. 
        
A timestamp is accepted as valid if it is greater than the median timestamp of previous 11 blocks, and less than the network-adjusted time + 2 hours. “Network-adjusted time” is the median of the timestamps returned by all nodes connected to you. As a result, block timestamps are not exactly accurate, and they do not even need to be in order. Block times are accurate only to within an hour or two. An added feature of this field is to make it more difficult to hash the block and hence more difficult to hack it.

'''
        
class block_header:
    def __int__(self, difficulty_target):
        self.version = None
        self.index = index
        self.previous_block_hash = None
        self.timestamp = get_unix_time() #This is used in bitcoin
        self.timestamp_readable = get_readable_time()
        self.difficulty_target = difficulty_target
        self.nonce = set_nonce()
 

    # HASH FUNCTION OF REQUIRED NUMBER OF ARGUMENTS
    def get_block_hash(self):
        block_hash = hash_256(self.version, self.previous_block_hash, self.timestamp, get_difficulty_target, randomly_incremented_nonce)

    def search(self):
        self.increment_nonce()


    # SETTING TIME
    def get_unix_time():
        return time.time()
    def get_readable_time():
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    # GETTING AND SETTING VERSION
    def set_version(self):
        self.version = version
    def get_version(self):
        return self.version
    
    # GETTING AND SETTING NONCE
    def set_nonce(self, nonce):
        self.nonce = randrange(2**32)
    def get_nonce(self):
        return self.nonce
    

    # PROOF OF WORK
    def randomly_incremented_nonce(self):
        self.nonce = randrange(2**32)
        return self.nonce
    #https://en.bitcoin.it/wiki/Hashcash READ THIS
    def proof_of_work(self, starting_value):
        #write code
        pass
    

    # GETTING AND SETTING PREVIOUS BLOCK HASH
    def set_previous_block_hash(self):
        previous_block = get_previous_block()
        previous_block_hash = get_hash(previous_block)
    def get_previous_block(self):
        ##write code
        return previous_block
    

    # GETTING AND SETTING DIFFICULTY TARGET
    def set_difficulty_target(self):
        self.difficulty_target = 1 # temporarily
    def get_difficulty_target(self):
        return self.difficulty_target

   

