#
# SHA-2 256-bit hash implementation
# _author: nagaganesh jaladanki
#
import struct

def rotr(x, n):
    return (x >> n) | (x << (32 - n))

def rotl(x, n):
    return (x << n) | (x >> (32 - n))

def ch(x, y, z):
    return (x & y)  ^ ((~ x) & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def bsig0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def bsig1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def ssig0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def ssig1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)


K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
     0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
     0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
     0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
     0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
     0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
     0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
     0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
     0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
     0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
     0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
     0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
     0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
     0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]



class sha256():

    def __init__(self, data=None):
        
        self.data = data
        if data != None:
            self.data = bytearray(0)
        self.update(data)

    def update(self, bytestring):
        self.H = [0x6a09e667, 0xbb67ae85,
                  0x3c6ef372, 0xa54ff53a,
                  0x510e527f, 0x9b05688c,
                  0x1f83d9ab, 0x5be0cd19]
        
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
            W = [0]*64
            for i in range(16):  
                num = chunk[4 * i : 4 * (i + 1)]
                W[i] = int.from_bytes(num, byteorder='big', signed=False)

            for i in range(16, 64):
                W[i] = (ssig1(W[i - 2]) + W[i - 7] + ssig0(W[i - 15]) + W[i - 16]) & 0xffffffff
            a, b, c, d, e, f, g, h = self.H

            for i in range(64):
                t1 = h + bsig1(e) + ch(e, f, g) + K[i] + W[i]
                t2 = bsig0(a) + maj(a, b, c)
                h = g
                g = f
                f = e
                e = (d + t1) & 0xffffffff
                d = c
                c = b
                b = a
                a = (t1 + t2) & 0xffffffff

                
            self._h_update(a, b, c, d, e, f, g, h)


        return self

    def _h_update(self, a, b, c, d, e, f, g, h):
        # refactor to make cleaner
        li = [a, b, c, d, e, f, g, h]
        for i in range(8):
            self.H[i] = (self.H[i] + li[i]) & 0xffffffff
            
    @property
    def hexdigest(self):
        dgt = self.H[0]
        for i in range(8):
            dgt = (dgt << 32) + self.H[i]
        return hex(dgt)