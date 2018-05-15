#
# SHA-1 hash implementation
# _author: nagaganesh jaladanki
#
import struct

def f(t,b,c,d):
    if t < 20:
        return f0(b,c,d)
    elif t < 40:
        return f1(b,c,d)
    elif t < 60:
        return f2(b,c,d)
    return f3(b,c,d)

def f0(b,c,d):
    return d ^ (b & (c ^ d))

def f1(b,c,d):
    return b ^ c ^ d

def f2(b,c,d):
    return (b & c) | (b & d) | (c & d)

def f3(b,c,d):
    return b ^ c ^ d

def leftshift(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff

K = [0x5A827999,
     0x6ED9EBA1,
     0x8F1BBCDC,
     0xCA62C1D6]

class sha1():

    def __init__(self, data=None):
        self.H = [0x67452301,
                  0xEFCDAB89,
                  0x98BADCFE,
                  0x10325476,
                  0xC3D2E1F0]
        
        self.data = data
        if data != None:
            self.data = bytearray(0)
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
        padded += (len(self.data) * 8).to_bytes(8, 'big', signed=False)

        # step 3: run computation on each block
        for j in range(len(padded) // 64):
            chunk = padded[64 * j : 64 * (j + 1) ]
            W = [0]*80
            for i in range(16):  
                num = chunk[4 * i : 4 * (i + 1)]
                W[i] = int.from_bytes(num, byteorder='big', signed=False)

            for i in range(16, 80):
                xor = W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16]
                W[i] = leftshift(xor, 1)
            a, b, c, d, e = self.H

            for i in range(80):
                temp = (leftshift(a, 5) + f(i, b, c, d) + e + W[i] + K[i // 20]) & 0xffffffff
                e, d = d, c
                c = leftshift(b, 30)
                b, a = a, temp
            self._h_update(a,b,c,d,e)


        return self

    def _h_update(self, a, b, c, d, e):
        # refactor to make cleaner
        li = [a,b,c,d,e]
        for i in range(5):
            self.H[i] = (self.H[i] + li[i]) & 0xffffffff
            
    @property
    def hexdigest(self):
        dgt = self.H[0]
        for i in self.H:
            dgt = (dgt << 32) + i
        return hex(dgt)

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
        print('SHA-1 ("{0}") = {1}'.format(vector.decode(), sha1(data=vector).hexdigest))
    pass

if __name__ == '__main__':
    main()

