#
# MD4 hash implementation
# _author: nagaganesh jaladanki
#
import struct

def f(x,y,z):
    return x & y | ~x & z

def g(x,y,z):
    return x & y | x & z | y & z

def h(x,y,z):
    return x ^ y ^ z

def leftrotate(n, b):
    #print(n,b)
    return ((n << b) | ((n & 0xffffffff) >> (32 - b))) & 0xffffffff

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
        numtopad = 56 - (len(bytestring) % 64)
        if numtopad <= 0:
            numtopad += 64

        padded = self.data + bytearray([128])
        padded += bytearray(numtopad - 1)

        # step 2: append length
        padded += (len(self.data) * 8).to_bytes(8, 'little', signed=False)

        # step 3: process message
        vals = [0x67452301,0xefcdab89,0x98badcfe,0x10325476]
        X = bytearray(16)
        blocks = int(len(padded) / 64)
        for i in range(0, blocks):
            valprev = vals[:]
            X = []
            for j in range(0, 64, 4):
                X.append(int.from_bytes(padded[64*i + j:64*i + j + 4], 'little', signed=False))

            # round 1
            s = (3,7,11,19)
            for i in range(16):
                r = (16-i)%4
                k = i
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]
                vals[r] = leftrotate(a + f(b,c,d) + X[k], s[k % 4])

            # round 2
            s = (3,5,9,13)
            for i in range(16):
                div, mod = divmod(i,4)
                r = (16-i)%4
                k = (mod*4 + div) % 16
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]
                vals[r] = leftrotate(a + g(b,c,d) + X[k] + 0x5A827999, s[i % 4])

            # round 3
            s = (3,9,11,15)
            k_ls = (0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15)
            for i in range(16):

                r = (16-i)%4
                k = k_ls[i]
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]

                vals[r] = leftrotate(a + h(b,c,d) + X[k] + 0x6ED9EBA1, s[i % 4])

            # register additions
            for i in range(4):
                vals[i] = (valprev[i] + vals[i]) % 2**32

        self.vals = vals
        return self

    @property
    def digest(self):
        return bytes(self.hash)

    @property
    def hexdigest(self):
        bh = bytearray(0)
        for i in range(4):
            bh = bh + bytearray(struct.pack('<I', self.vals[i]))
        return bh.hex()

# Binary strings contain bytewise data, similar to a bytearray
test_vectors = [b"",
                b"a",
                b"abc",
                b"message digest",
                b"abcdefghijklmnopqrstuvwxyz",
                b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
                b"12345678901234567890123456789012345678901234567890123456789012345678901234567890"]
def main():
    for vector in test_vectors:
        print('MD4 ("{0}") = {1}'.format(vector.decode(), md4(data=vector).hexdigest))

if __name__ == '__main__':
    main()
