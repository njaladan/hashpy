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
    return (b & c) | ((~b) & d)

def f1(b,c,d):
    return b ^ c ^ d

def f2(b,c,d):
    return (b & c) | (b & d) | (c & d)

def f3(b,c,d):
    b ^ c ^ d

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

    def update(self, bytestring):
        return self

    @property
    def digest(self):
        pass
    
    @property
    def hexdigest(self):
        pass

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
        print('SHA-1 ("{0}") = {1}'.format(vector.decode(), md4(data=vector).hexdigest))

if __name__ == '__main__':
    main()
