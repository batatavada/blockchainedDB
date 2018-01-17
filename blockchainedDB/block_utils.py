
def hexbits_to_target(bits):
    """ 
    Converts LittleEndian bits in compact format to BigEndian target.

    ARGS:
        - bits: compact format of 4 bytes (STRING) eg. "0x1d00ffff"
    RETURNS:
        - target: 256-bit/32 byte hex number with prefix '0x' (STRING) 
        eg. "0x00ffff0000000000000000000000000000000000000000000000000000000000"
    
    REFERENCE: https://bitcoin.stackexchange.com/questions/44579/how-is-a-block-header-hash-compared-to-the-target-bits

    """
    exponent, coefficient = bits[:4], "0x" + bits[4:]
    target = '0x'+hex(int(coefficient,16) * 2**(8*(int(exponent,16) - 3))).rstrip("L").lstrip("0x").zfill(64)
    return target






def decimalbits_to_target(bits):
    """
    Converts bits decimal to BigEndian target.

    ARGS: 
        - bits: decimal number in Big Endian format (INT)
    RETURNS: 
        - target: equivalent hex number in 256-bit/32 byte representation (STRING)
    
    REFERENCE: https://bitcoin.stackexchange.com/questions/44579/how-is-a-block-header-hash-compared-to-the-target-bits

    """
    return hexbits_to_target(hexLittleEndian(bits))






def target_to_bits(target):
    """ 
    Converts BigEndian target to corresponding LittleEndian bits(compact form of target)

    ARGS: 
        - target: 256-bit/32 byte hex number with prefix '0x'(STRING)
    RETURNS:
        - bits: compact format of 4 bytes (STRING) eg. "0x1d00ffff" in BigEndian format

    REFERENCE: https://bitcoin.stackexchange.com/questions/2924/how-to-calculate-new-bits-value

    """
    # NUMBER OF DIGITS IN BASE 256 REPRESENTATION
    length = len(hex(int(target,16))[2:]) >> 1 

    if(int(hex(int(target,16))[2:4],16) > 127):
        length+=1
        compact =hex(int(length)) + "00"+ hex(int(target,16))[2:6]
    else:
        compact = hex(int(length)) + hex(int(target,16))[2:6] + "00"
    return compact






def bits_to_difficulty(max_target, bits):
    """ 
    Converts BigENdian bits to difficulty

    ARGS: 
        - bits: compact format of 4 bytes (STRING) eg. "0x1d00ffff"
        - max_target : 256-bit/32 byte hex number with prefix '0x' (corresponds to lowest difficulty ie. 1) (STRING)

    RETURNS:
        - difficulty (FLOAT)

    REFERENCE: https://bitcoin.stackexchange.com/questions/2924/how-to-calculate-new-bits-value

    """  
    target = bu.hexbits_to_target(bits)
    return int(max_target,16)/int(target,16)






def difficulty_to_target(difficulty, max_target):
    """
    Get BigEndian target as hex STRING from difficulty.

    ARGS:
        - difficulty (float)
        - max_target: 256-bit/32 byte  hex number with prefix '0x' (STRING)
    RETURNS:
        - target: 256-bit/32 byte  hex number with prefix '0x' (STRING)

    NOTES: MAX TARGET IS TARGET WITH LOWEST DIFFICULTY

    """
    target = hex(int(max_target,16)/difficulty)
    return target






def hexLittleEndian(decimal):
    """ 
    Converts BigEndian decimal data to LittleEndian hex data.

    ARGS:
        - decimal: decimal number (INT)
    RETURNS: 
        - h: hex number with prefix "0x" (STRING)

    """
    h  = little_endian(hex(decimal))
    return h






def little_endian(hex):
    """ 
    Converts BigEndian hex data to LittleEndian hex data.

    ARGS:
        - hex: hex number (STRING) with no prefix '0x'
    RETURNS: 
        - littleEndian: hex number in LittleEndian (STRING) with prefix '0x'

    """
    littleEndian = "";
    if len(hex) % 2 != 0:
        return littleEndian 
    for x in reversed(hex):
        littleEndian += hex[-2:]
        hex = hex[:-2]
    return '0x'+littleEndian






def plot_timevsblocks_fromlists(lst, xindex, yindex, heading, x_label, y_label):
    """Plots graph wherein the x and y attributes exist in the same list.

    ARGS:
        - lst: list of lists
        - index1: index of attribute in list to be plotted on x-axis
        - index2: index of attribute in list to be plotted on y-axis
        - heading: Title of graph
        - x_label
        - y_label
    RETURNS:
        - plotted graph

    """
    x=[]
    y=[]        
    for i in range(len(lst)):
            x.append(lst[i][xindex])
            y.append(lst[i][yindex])       
    
    import matplotlib.pyplot as plt
    plt.subplots(figsize=(10,10))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(heading)
    plt.plot(x,y)
    plt.legend()
    plt.show()






def plot_timevsblocks_fromcsv(name_csvfile, xindex, yindex, heading, x_label, y_label):
    """Plots graph wherein the x and y attributes exist in the same csv file.
    
    ARGS:
        - name_csvfile: name of csv file
        - index1: index of attribute in file to be plotted on x-axis
        - index2: index of attribute in file to be plotted on y-axis
        - heading: Title of graph
        - x_label
        - y_label
    RETURNS:
        - plotted graph

    """
    import numpy as np
    import matplotlib.pyplot as plt     

    data=np.genfromtxt(name_csvfile, delimiter=',', skip_header=1)
    x = data[:,xindex] - data[0,xindex]
    y = np.arange(1,len(x))
    fig, ax = plt.subplots(figsize=(10,10))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(heading)        
    ax.plot(x,y)
    plt.legend()
    plt.show()      




'''
def rand_bytes(n, secure=True):
    """ Returns n random bytes.
    ARGS:
        n (INT): number of bytes to return.
        secure (bool): If True, uses os.urandom to generate
            cryptographically secure random bytes. Otherwise, uses
            random.randint() which generates pseudo-random numbers.
    RETURNS:
        b (bytes): n random bytes.
    """
    if secure:
        return os.urandom(n)
    else:
        return bytes([random.randint(0, 255) for i in range(n)])


def bytes_to_str(b):
    """ Converts bytes into a hex-encoded STRING.
    ARGS:
        b (bytes): bytes to encode
    RETURNS:
        h (str): hex-encoded STRING corresponding to b.
    """
    return codecs.encode(b, 'hex_codec').decode('ascii')


def hex_str_to_bytes(h):
    """ Converts a hex-encoded STRING to bytes.
    ARGS:
        h (str): hex-encoded STRING to convert.
    RETURNS:
        b (bytes): bytes corresponding to h.
    """
    return bytes.fromhex(h)


# Is there a better way of doing this?
def render_int(n):
    """ Renders an int in the shortest possible form.
    When packing the height into the coinbase script, the integer
    representing the height must be encoded in the shortest possible
    manner. See: https://bitcoin.org/en/developer-REFERENCE#coinbase.
    ARGS:
        n (INT): number to be encoded.
    RETURNS:
        b (bytes): bytes representing n in the shortest possible form.
    """
    # little-endian byte stream
    if n < 0:
        neg = True
        n = -n
    else:
        neg = False
    r = []
    while n:
        r.append(n & 0xff)
        n >>= 8
    if neg:
        if r[-1] & 0x80:
            r.append(0x80)
        else:
            r[-1] |= 0x80
    elif r and (r[-1] & 0x80):
        r.append(0)
    return bytes(r)


def pack_compact_int(i):
    """ See
    https://bitcoin.org/en/developer-REFERENCE#compactsize-unsigned-integers
    ARGS:
        i (INT): Integer to be serialized.
    RETURNS:
        b (bytes): Serialized bytes corresponding to i.
    """
    if i < 0xfd:
        return struct.pack('<B', i)
    elif i <= 0xffff:
        return struct.pack('<BH', 0xfd, i)
    elif i <= 0xffffffff:
        return struct.pack('<BI', 0xfe, i)
    else:
        return struct.pack('<BQ', 0xff, i)


def unpack_compact_int(bytestr):
    """ See
    https://bitcoin.org/en/developer-REFERENCE#compactsize-unsigned-integers
    ARGS:
        bytestr (bytes): bytes containing an unsigned integer to be
            deserialized.
    RETURNS:
        n (INT): deserialized integer.
    """

    b0 = bytestr[0]
    if b0 < 0xfd:
        return (b0, bytestr[1:])
    elif b0 == 0xfd:
        return (struct.unpack('<H', bytestr[1:3])[0], bytestr[3:])
    elif b0 == 0xfe:
        return (struct.unpack('<I', bytestr[1:5])[0], bytestr[5:])
    elif b0 == 0xff:
        return (struct.unpack('<Q', bytestr[1:9])[0], bytestr[9:])
    else:
        return None


def pack_u32(i):
    """ Serializes a 32-bit integer into little-endian form.
    ARGS:
        i (INT): integer to be serialized.
    RETURNS:
        b (bytes): 4 bytes containing the little-endian serialization of i.
    """
    return struct.pack('<I', i)


def unpack_u32(b):
    """ Deserializes a 32-bit integer from bytes.
    ARGS:
        b (bytes): At least 4 bytes containing the serialized integer.
    RETURNS:
        (i, b) (tuple): A tuple containing the deserialized integer and the
        remainder of the byte stream.
    """
    u32 = struct.unpack('<I', b[0:4])
    return (u32[0], b[4:])


def pack_u64(i):
    """ Serializes a 64-bit integer into little-endian form.
    ARGS:
        i (INT): integer to be serialized.
    RETURNS:
        b (bytes): 8 bytes containing the little-endian serialization of i.
    """
    return struct.pack('<Q', i)


def unpack_u64(b):
    """ Deserializes a 64-bit integer from bytes.
    ARGS:
        b (bytes): At least 8 bytes containing the serialized integer.
    RETURNS:
        (i, b) (tuple): A tuple containing the deserialized integer and the
        remainder of the byte stream.
    """
    u64 = struct.unpack('<Q', b[0:8])
    return (u64[0], b[8:])


def pack_var_str(s):
    """ Serializes a variable length byte stream.
    ARGS:
        s (bytes): byte stream to serialize
    Return:
        b (bytes): Serialized bytes, prepended with the length of the
        byte stream.
    """
    return pack_compact_int(len(s)) + s


def unpack_var_str(b):
    """ Deserializes a variable length byte stream.
    ARGS:
        b (bytes): variable length byte stream to deserialize
    RETURNS:
        (s, b) (tuple): A tuple containing the variable length byte stream
        and the remainder of the input byte stream.
    """
    strlen, b0 = unpack_compact_int(b)
    return (b0[:strlen], b0[strlen:])


def bits_to_target(bits):
    """ Decodes the full target from a compact representation.
    See: https://bitcoin.org/en/developer-REFERENCE#target-nbits
    ARGS:
        bits (INT): Compact target (32 bits)
    RETURNS:
        target (Bignum): Full 256-bit target
    """
    shift = bits >> 24
    target = (bits & 0xffffff) * (1 << (8 * (shift - 3)))
    return target


def bits_to_difficulty(bits):
    """ Determines the difficulty corresponding to bits.
    See: https://en.bitcoin.it/wiki/Difficulty
    ARGS:
        bits (INT): Compact target (32 bits)
    RETURNS:
        diff (float): Measure of how hard it is to find a solution
        below the target represented by bits.
    """
    target = bits_to_target(bits)
    return MAX_TARGET / target


def difficulty_to_target(difficulty):
    """ Converts a difficulty to a long-form target.
    ARGS:
        difficulty (float): The difficulty to return the appropriate target for
    RETURNS:
        target (INT): The corresponding target
    """
    return int(MAX_TARGET / difficulty)


def target_to_bits(target):
    """ Creates a compact target representation for a given target.
    ARGS:
        target (Bignum): The long-form target to make compact.
    RETURNS:
        ct (INT): Compact target
    """
    # Get bit length
    nbits = target.bit_length()
    # Round up to next 8-bits
    nbits = ((nbits + 7) & ~0x7)
    exponent = (int(nbits/8) & 0xff)
    coefficient = (target >> (nbits - 24)) & 0xffffff
    if coefficient & 0x800000:
        coefficient >>= 8
        exponent += 1
    return (exponent << 24) | coefficient


def difficulty_to_bits(difficulty):
    """ Converts a difficulty to a compact target.
    ARGS:
        difficulty (float): The difficulty to create a target for
    RETURNS:
        ct (INT): Compact target
    """
    return target_to_bits(difficulty_to_target(difficulty))
'''