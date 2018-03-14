#
# MD4 hash implementation
# _author: nagaganesh jaladanki
#


class md4():

    def __init__(self, data=None):
        self.hash = 0
        self.data = bytearray(0)
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476
        
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

        print(len(padded))
        
        # step 2: append length
        padded += convert_to_64bit(len(self.data) * 8)

        # step 3: process message        



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


    @property
    def digest(self):
        # this is not elegant
        return bytes(self.hash)

    @property
    def hexdigest(self):
        return self.hash.hex()


def main():
    print('MD2 checksum calculator')
    

if __name__ == '__main__':
    main()

        
