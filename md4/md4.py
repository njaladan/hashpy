#
# MD4 hash implementation
# _author: nagaganesh jaladanki
#


def convert_to_64bit(data):
    bytearr = bytearray(64)
    count = 63
    while data:
        bytearr[count] = data % 256
        data = int((data - (data % 256)) / 256)
        count -= 1
    return bytearr

def f(x,y,z):
    (x & y) | (~x & z)

def g(x,y,z):
    (x & y) | (x & z) | (y & z)

def h(x,y,z):
    return x ^ y ^ z

def leftrotate(i, n):
    return ((i << n) & 0xffffffff) | (i >> (32 - n))


class md4():

    def __init__(self, data=None):
        self.hash = 0
        self.data = bytearray(0)
        self.vals = [
                0x67452301,
                0xefcdab89,
                0x98badcfe,
                0x10325476
                ]
        
        if data != None:
            self.update(data)


    def update(self, bytestring):
        
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)

        self.data += bytestring

        # step 1: padding bits
        numtopad = 48 - (len(bytestring) % 64)
        if numtopad <= 0:
            numtopad += 64

        padded = self.data + bytearray([128])
        padded += bytearray(numtopad - 1)

        
        # step 2: append length
        padded += convert_to_64bit(len(self.data) * 8)

        # step 3: process message
        vals = self.vals
        X = bytearray(16)
        blocks = int(len(padded) / 16) - 1
        for i in range(0, blocks):
            X = padded[4*i + 4*(i+1)]

        s = (3,7,11,19)
        for i in range(16):
            r = (16-i)%4
            k = i
            a = vals[r]
            b = vals[(r + 1) % 4]
            c = vals[(r + 2) % 4]
            d = vals[(r + 3) % 4]
            vals[r] = leftrotate(a + f(b,c,d) + X[k], s)

            

        
    @property
    def digest(self):
        return bytes(self.hash)

    @property
    def hexdigest(self):
        return self.hash.hex()


md4(b'hello')

        
