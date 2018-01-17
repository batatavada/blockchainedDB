import random
import time
import hashlib

data = "we are at barc"

nonce = 0

hash_int = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

target = 0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

start_time = time.time()

while(hash_int > target):
	print(nonce)
	nonce += 1
	string = data + str(nonce)
	hash = hashlib.sha256(string.encode('utf-8')).hexdigest()
	hash_int = int(hash,16)

end_time = time.time()

print("Nonce: {} found in Time: {} seconds.".format(nonce, end_time - start_time))
print("Hash: {}".format(hash))