#
# SHA-2 384-bit hash implementation
# _author: nagaganesh jaladanki
#
import struct

def rotr(x, n):
    return (x >> n) | (x << (64 - n))

def rotl(x, n):
    return (x << n) | (x >> (64 - n))

def ch(x, y, z):
    return (x & y)  ^ ((~ x) & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def bsig0(x):
    return rotr(x, 28) ^ rotr(x, 34) ^ rotr(x, 39)

def bsig1(x):
    return rotr(x, 14) ^ rotr(x, 18) ^ rotr(x, 41)

def ssig0(x):
    return rotr(x, 1) ^ rotr(x, 8) ^ (x >> 7)

def ssig1(x):
    return rotr(x, 19) ^ rotr(x, 61) ^ (x >> 6)


K = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
     0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
     0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
     0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
     0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
     0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
     0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
     0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
     0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
     0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
     0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
     0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
     0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
     0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
     0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
     0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
     0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
     0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
     0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
     0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]



class sha512():

    def __init__(self, data=None):
        
        self.data = data
        if data != None:
            self.data = bytearray(0)
        self.update(data)

    def update(self, bytestring):
        self.H = [0xcbbb9d5dc1059ed8, 0x629a292a367cd507,
                  0x9159015a3070dd17, 0x152fecd8f70e5939,
                  0x67332667ffc00b31, 0x8eb44a8768581511,
                  0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4]
        
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)

        self.data += bytestring
        
        # step 1: padding bits
        numtopad = 112 - (len(bytestring) % 128)
        if numtopad <= 0:
            numtopad += 112

        padded = self.data + bytearray([128])
        padded += bytearray(numtopad - 1)

        # step 2: append length
        padded += (len(self.data) * 8).to_bytes(16, 'big', signed=False)

        # step 3: run computation on each block
        for j in range(len(padded) // 128):
            chunk = padded[128 * j : 128 * (j + 1) ]
            W = [0] * 80
            for i in range(16):  
                num = chunk[8 * i : 8 * (i + 1)]
                W[i] = int.from_bytes(num, byteorder='big', signed=False)

            for i in range(16, 80):
                W[i] = (ssig1(W[i - 2]) + W[i - 7] + ssig0(W[i - 15]) + W[i - 16]) & 0xffffffffffffffff
            a, b, c, d, e, f, g, h = self.H

            for i in range(80):
                t1 = h + bsig1(e) + ch(e, f, g) + K[i] + W[i]
                t2 = bsig0(a) + maj(a, b, c)
                h = g
                g = f
                f = e
                e = (d + t1) & 0xffffffffffffffff
                d = c
                c = b
                b = a
                a = (t1 + t2) & 0xffffffffffffffff

                
            self._h_update(a, b, c, d, e, f, g, h)


        return self

    def _h_update(self, a, b, c, d, e, f, g, h):
        # refactor to make cleaner
        li = [a, b, c, d, e, f, g, h]
        for i in range(8):
            self.H[i] = (self.H[i] + li[i]) & 0xffffffffffffffff
            
    @property
    def hexdigest(self):
        dgt = self.H[0]
        for i in range(1, 6):
            dgt = (dgt << 64) + self.H[i]
        return hex(dgt)