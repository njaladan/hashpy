from hash import Hash
from copy import deepcopy


class bsd16bit(Hash):

    def __init__(self, data=None):
        self.data = data
        self.checksum = 0
        self.bitmask = 0xffff
        if self.data:
            self.update(self.data)

    def update(self, data):
        if self.data is None:
            self.data = bytearray(data)
        else:
            self.data += bytearray(data)
        for b in self.data:
            self.checksum = (self.checksum >> 1) + ((self.checksum & 1) << 15)
            self.checksum = (self.checksum + b) & self.bitmask

    def hexdigest(self):
        return str(hex(self.checksum))

    def digest(self):
        return chr(self.checksum >> 8) + chr(self.checksum & 0xff)

    def copy(self):
        return deepcopy(self)

    @property
    def block_size(self):
        return 1

    @property
    def digest_size(self):
        return 2

    @property
    def name(self):
        return "bsd16bit"
