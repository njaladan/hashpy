# algorithm comes in 16, 32, and 64 bit variants
# simple input will let user choose which one they want

class Fletcher:
    
    modulus = 255
    bitshift = 8
    bytes_read = 1

    def __init__(self):
        self.c0 = 0
        self.c1 = 0
        self.cb0 = 0
        self.cb1 = 0

    def update(self, bytestring):
        # prevents unicode or weirdly encoded strings
        # from being passed in naked
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)

        iterations = ((len(bytestring) - 1) // self.bytes_read) + 1
        for i in range(0, iterations):
            start = self.bytes_read*i
            end = self.bytes_read*(i+1)
            
            bytepart = int.from_bytes(bytestring[start:end], byteorder="little")
            self.c0 = (self.c0 + bytepart) % self.modulus
            self.c1 = (self.c1 + self.c0) % self.modulus

        # compute check bytes
        self.cb0 = self.modulus - ((self.c0 + self.c1) % self.modulus)
        self.cb1 = self.modulus - ((self.c0 + self.cb0) % self.modulus)


    def hexdigest(self):
        translated_number = hex((self.c1 << self.bitshift) + (self.c0))
        if len(translated_number) % 2 == 0:
            return '0x' + translated_number[2:]
        return '0x0' + translated_number[2:]

    def cb_hexdigest(self):
        translated_number = hex((self.cb0 << self.bitshift) + (self.cb1))
        if len(translated_number) % 2 == 0:
            return translated_number[2:]
        return '0' + translated_number[2:]
       

class Fletcher16(Fletcher):

    modulus = 255
    bitshift = 8
    bytes_read = 1

class Fletcher32(Fletcher):

    modulus = 65535
    bitshift = 16
    bytes_read = 2

class Fletcher64(Fletcher):

    modulus = 4294967295
    bitshift = 32
    bytes_read = 4

# I'm not sure how to write a user-friendly CLI
# maybe I can do the options thing in the cli,

def main():
    print('Fletcher N-bit checksum calculator')
    
    while(True):
        print('Enter a file name.')
        inp = input()
        f = open(inp, 'rb')
        print('Enter 16, 32, or 64 bit checksum')
        inp = int(input())
        if inp==16:
            hashobj = Fletcher16()
            hashobj.update(f.read())
            hexdigest = hashobj.hexdigest()
        elif inp==32:
            hashobj = Fletcher32()
            hashobj.update(f.read())
            hexdigest = hashobj.hexdigest()
        elif inp==64:
            hashobj = Fletcher64()
            hashobj.update(f.read())
            hexdigest = hashobj.hexdigest()


        print(hexdigest)

##if __name__ == '__main__':
##    main()

