"""
Contains implementation for MD5
Based off of the IETF RFC 1321: https://tools.ietf.org/html/rfc1321

Author: Nagaganesh Jaladanki
License: MIT
"""

import struct
from hash import Hash
from md5constants import T

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


class MD5(Hash):

    def update(self, bytestring, debug=False):

        # Step 0: Convert to proper type if necessary
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)
        self.data += bytestring

        # Step 1: Pad null bits to ensure MD construction
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
