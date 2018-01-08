''' 
hex = "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
hexLittleEndian = "";
if len(hex) % 2 != 0:
    print("0");

for x in reversed(hex):
    hexLittleEndian = hexLittleEndian + hex[-2:]
    hex = hex[:-2]
    print(hexLittleEndian)
    
print hexLittleEndian

block = ["01000000","81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000", "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b", "c7f5d74d", "f2b9441a", "42a14695"]
string = ""
for x in block:
    string = string + x
string = string

print string == "0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a14695"
print string
print "0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a146950x"


import hashlib
data = "0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a14695"
header_bin = data.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hash.encode('hex')
h = hash[::-1].encode('hex')
print h

'''
'''

def little_endian(hex):
    hexLittleEndian = "";
    if len(hex) % 2 != 0:
        return hexLittleEndian  

    for x in reversed(hex):
        #print "in loop"
        hexLittleEndian = hexLittleEndian + hex[-2:]
        hex = hex[:-2]
    #print(hexLittleEndian)
    return hexLittleEndian

def get_hex(data):
    x = hex(int(data))
    # Convert to little endian
    data = little_endian(x)
    return data[:-2]


nonce = get_hex("453248203")
print nonce
nonce = little_endian(nonce)
print "Nonce: " + nonce
print( len("440711666")>len("76270618"))
'''


#hash example
'''
import time

import hash_sha256 as h
m = b"Hello, world!"

start_time = time.time()

test = h.hashing()
nonce = 0
data = (m,nonce)
t = test.concat(data)
out = test.get_hash(t)

while(out.startswith(b'0000')==False):
    nonce = nonce + 1
    data = (m,nonce)
    t = test.concat(data)
    out = test.get_hash(t)

end_time = time.time()
print("Nonce: {} found in Time: {} seconds.".format(nonce,(end_time - start_time)))

'''

# OUTPUT: Nonce: 4848154 found in Time: -49.62666583061218
#Nonce: 4848154 found in Time: 49.02641320228577 seconds

#print 0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103 ==
'''
import hashlib
import time

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(header, difficulty_bits):

    target = 2 ** (256-difficulty_bits)
    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

        if long(hash_result, 16) < target:
            print "Success with nonce %d" % nonce
            print "Hash is %s" % hash_result
            return (hash_result, nonce)

    print "Failed after %d (max_nonce) tries" % nonce
    return nonce

if __name__ == '__main__':
    
    nonce = 0
    hash_result = ''

    for difficulty_bits in xrange(32):
        
        difficulty = 2 ** difficulty_bits
        print ""
        print "Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits)
        print "Starting search..."

        start_time = time.time()
        new_block = 'test block with transactions' + hash_result
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print "Elapsed time: %.4f seconds" % elapsed_time

        if elapsed_time > 0: 

            hash_power = float(long(nonce)/elapsed_time)
            print "Hashing power: %ld hashes per second" % hash_power
            '''

import sys
print(sys.version)