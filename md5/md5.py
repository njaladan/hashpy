#
# MD5 hash implementation
# _author: nagaganesh jaladanki
#
import struct

def F(x,y,z):
    return (x & y) | ((~x) & z)

def G(x,y,z):
    return (x & z) | (y & (~z))

def H(x,y,z):
    return x ^ y ^ z

def I(x,y,z):
    return y ^ (x | (~z))

def leftrotate(n, b):
    return ((n << b) | ((n & 0xffffffff) >> (32 - b))) & 0xffffffff

T = [3614090360, 3905402710, 606105819, 3250441966,
      4118548399, 1200080426, 2821735955, 4249261313,
      1770035416, 2336552879, 4294925233, 2304563134,
      1804603682, 4254626195, 2792965006, 1236535329,
      4129170786, 3225465664, 643717713, 3921069994,
      3593408605, 38016083, 3634488961, 3889429448,
      568446438, 3275163606, 4107603335, 1163531501,
      2850285829, 4243563512, 1735328473, 2368359562,
      4294588738, 2272392833, 1839030562, 4259657740,
      2763975236, 1272893353, 4139469664, 3200236656,
      681279174, 3936430074, 3572445317, 76029189,
      3654602809, 3873151461, 530742520, 3299628645,
      4096336452, 1126891415, 2878612391, 4237533241,
      1700485571, 2399980690, 4293915773, 2240044497,
      1873313359, 4264355552, 2734768916, 1309151649,
      4149444226, 3174756917, 718787259, 3951481745]

class md5():

    def __init__(self, data=None):
        self.hash = 0
        self.data = bytearray(0)


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
        self.vals = [0x67452301,
                     0xefcdab89,
                     0x98badcfe,
                     0x10325476]
        vals = self.vals
     
        X = bytearray(16)
        blocks = int(len(padded) / 64)
        for i in range(0, blocks):

            valprev = self.vals[:]
            X = []
            for j in range(0, 64, 4):
                X.append(int.from_bytes(padded[64*i + j:64*i + j + 4], 'little', signed=False))

            # round 1
            mods = (7,12,17,22)
            for i in range(16):
                k = i
                s = mods[i % 4]
                r = (16 - k) % 4
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]
                vals[r] = b + leftrotate(a + F(b, c, d) + X[k] + T[i], s) & 0xffffffff
            
            # round 2
            mods = (5,9,14,20)
            for i in range(16):
                k = (5 * i + 1) % 16
                s = mods[i % 4]
                r = (16 - i) % 4
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]
                vals[r] = b + leftrotate(a + G(b, c, d) + X[k] + T[i + 16], s) & 0xffffffff
            
            # round 3
            mods = (4,11,16,23)
            for i in range(16):
                k = (5 + 3 * i) % 16
                s = mods[i % 4]
                r = (16-i)%4
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]
                vals[r] = b + leftrotate(a + H(b, c, d) + X[k] + T[i + 32], s) & 0xffffffff
            
            # round 4
            mods = (6,10,15,21)
            for i in range(16):
                k = (7 * i) % 16
                s = mods[i % 4]
                r = (16-i)%4
                a = vals[r]
                b = vals[(r + 1) % 4]
                c = vals[(r + 2) % 4]
                d = vals[(r + 3) % 4]
                vals[r] = b + leftrotate(a + I(b, c, d) + X[k] + T[i + 48], s) & 0xffffffff

            # register additions
            for i in range(4):
                vals[i] = (valprev[i] + vals[i]) & 0xffffffff

        self.vals = vals
        return self

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
        print('MD5 ("{0}") = {1}'.format(vector.decode(), md5(data=vector).hexdigest))

if __name__ == '__main__':
    main()

