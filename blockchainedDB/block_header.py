import      hash_sha256     as h
import      hashcash        as hc
import      random          as r
import      time
import      datetime
import      hashlib
import      codecs


'''
Block headers are serialized in the 80-byte format described below and then hashed as part of Bitcoin’s proof-of-work algorithm, making the serialized header format part of the consensus rules.

        +-----------------------------------+
        |           |           |           |
        |   BYTES   |   NAME    | DATA TYPE | 
        |           |           |           |    
        |-----------|-----------|-----------|
        |     4     |  version  |  int32_t  | 
        |-----------|-----------|-----------| 
        |    32     | previous  |  char[32] |
        |           |block hash |           | 
        |-----------|-----------|-----------| 
        |     4     |  time     |  uint32_t | 
        |-----------|-----------|-----------| 
        |     4     |  nBits    |  uint32_t | 
        |-----------|-----------|-----------|  
        |     4     |  nonce    |  uint32_t | 
        +-----------------------------------+

        '''


class BlockHeader:

    def __int__(self, version, height):
        self.height = height
        self.version = version
        self.previousBlockHash = None
        self.merkleRoot = None
        self.timestamp = None 
        self.bits = None
        self.nonce = None
        self.difficulty = None

        '''
        self.n_tx = 22,
        self.size = 9195, 
        self.block_index = 818044,
        self.main_chain = true,
        self.height = 154595,
        self.received_time = 1322131301,
        self.relayed_by = "108.60.208.156",
        #self.tx = [--Array of Transactions--]
        '''





    def createBlock(self, version):
        self.height += 1
        self.version = version
        self.merkleRoot = getMerkleRoot()
        self.timestamp = int(time.time())
        self.nonce = r.randint(1,2**32)
        self.difficulty, self.bits = retarget()



'''

    def proof_of_work(self):
        print("\n\nBlock Height (I): {}".format(self.height))
        timestamp = int(time.time()) 
        current_difficulty, target = test_hashcash.retarget(index, blocks, update_limit, num_blocks, expected_time)

        test_header_vars = test_header.prep_block_vars(version, prev_block_hash, merkle_root, str(timestamp), bits)
        
        nonce, mining_time, final_hash = test_hashcash.proofOfWork_random(test_header_vars, target)
        






    def add_to_chain(self, version, prev_block_hash, merkle_root, timestamp, bits):
        
        self.version = version
        #print("\nVersion: " + self.version)

        self.prev_block_hash = self.little_endian(prev_block_hash)
        #print("\nPrev block hash: " + self.prev_block_hash)

        self.merkle_root = self.little_endian(merkle_root)
        #print("\nMerkle root: " + self.merkle_root)

        self.timestamp = self.hexLittleEndian(timestamp)
        #print("\nTimestamp: " + self.timestamp)

        self.bits = self.hexLittleEndian(bits)
        #print("\nBits: " + self.bits)

        block = str(self.version + self.prev_block_hash + self.merkle_root + self.timestamp + self.bits)

        return block






    def get_block_hash(self, vars, nonce):

        self.nonce = self.hexLittleEndian(nonce)
        #print("\nNonce: " + self.nonce)

        block = (vars + self.nonce)

        #print("\nBlock Header: {}".format(block))
        block_hash = self.hash_calculation(block)

        #print("\nBlock Header Hash: {}".format(block_hash))
        return str(block_hash)






    def hash_calculation(self, block):
        x = h.hashing()
        return x.get_block_hash(block)
'''


'''
    # HASH FUNCTION OF REQUIRED NUMBER OF ARGUMENTS
    #def get_block_hash(self):


    def search(self):
        search = 
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

   

'''