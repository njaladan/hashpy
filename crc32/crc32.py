#
# CRC32 hash implementation
# using polynomial 0x04c11db7
# _author: nagaganesh jaladanki
#

class crc32():

    def __init__(self, data=None):
        self.poly = 0x04c11db7
        if data != None:
            self.update(data)

    def update(self, bytestring):
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)
        padded = bytestring + bytearray(len(self.poly
        
        return self

    @property
    def digest(self):
        return bytes(self.hash)

    @property
    def hexdigest(self):
        return self.hash.hex()

