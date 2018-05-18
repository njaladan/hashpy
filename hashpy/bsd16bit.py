from hash import Hash


class bsd16bit(Hash):

    def __init__(self, *args):
        assert len(args) == 1, "Too many arguments"
        self.data = args[0]
        self.checksum = 0
        if self.data:
            self.update(self.data)

    def update(self, data):
        self.data = bytearray(data)
        for b in self.data:
            self.checksum = (self.checksum >> 1) + ((self.checksum & 1) << 15)
            self.checksum = (self.checksum + b) & 0xffff
        self.data = None

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
