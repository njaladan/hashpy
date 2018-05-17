#
# MD2 hash implementation
# _author: nagaganesh jaladanki
#

from md2_stable import md2_stable


class md2():

    def __init__(self, data=None):
        self.hash = 0
        self.data = bytearray(0)
        self.table = md2_stable()
        if data != None:
            self.update(data)


    def update(self, bytestring):
        
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)

        self.data += bytestring

        number_to_pad = 16-(len(self.data) % 16)
        to_pad = [number_to_pad for i in range(number_to_pad)]
        padded = self.data + bytearray(to_pad)

        checksum = bytearray(16)

        L = 0
        
        for i in range(len(padded)//16):
            for j in range(16):
                c = padded[16*i + j]
                checksum[j] = checksum[j] ^ self.table.lookup(c ^ L)
                L = checksum[j]

        padded_checksum = padded + checksum
        buffer = bytearray(48)

        for i in range(0, len(padded_checksum)//16):
            for j in range(0, 16):
                buffer[j+16] = padded_checksum[16*i+j]
                buffer[j+32] = buffer[j+16] ^ buffer[j]

            t = 0
            for j in range(0, 18):
                for k in range(0, 48):
                    t = buffer[k] ^ self.table.lookup(t)
                    buffer[k] = t
                t = (t+j) % 256

        self.hash = buffer[0:16]
        return self

    @property
    def digest(self):
        # this is not elegant
        return bytes(self.hash)

    @property
    def hexdigest(self):
        return self.hash.hex()