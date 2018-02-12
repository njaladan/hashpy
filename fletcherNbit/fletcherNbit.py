# algorithm comes in 16, 32, and 64 bit variants
# simple input will let user choose which one they want
# (to be implemented later)

# 32 NEEDS TO TAKE IN 2 BYTES AT A TIME

class Fletcher16:
    
    #takes no arguments, since you add string by updating
    def __init__(self):
        self.c0 = 0
        self.c1 = 0
        self.cb0 = 0
        self.cb1 = 0

    def update(self, bytestring):

        # prevents unicode or weirdly encoded strings
        # from being passed in
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)
        for s in bytestring:
            self.c0 = (self.c0 + s) % 255
            self.c1 = (self.c1 + self.c0) % 255

        # compute check bytes
        self.cb0 = 255 - ((self.c0 + self.c1) % 255)
        self.cb1 = 255 - ((self.c0 + self.cb0) % 255)
        
    # needs work, broken
    def hexdigest(self):
        translated_number = hex((self.c1 << 8) + (self.c0))
        if len(translated_number) % 2 == 0:
            return '0x' + translated_number[2:]
        return '0x0' + translated_number[2:]

    def cb_hexdigest(self):
        translated_number = hex((self.cb0 << 8) + (self.cb1))
        if len(translated_number) % 2 == 0:
            return translated_number[2:]
        return '0' + translated_number[2:]

class Fletcher32:

    #takes no arguments, since you add string by updating
    def __init__(self):
        self.c0 = 0
        self.c1 = 0
        self.cb0 = 0
        self.cb1 = 0

    def update(self, bytestring):
        # prevents unicode or weirdly encoded strings
        # from being passed in
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)
        for i in range(0, len(bytestring)//2):
            bytepart = (bytestring[2*i+1] << 8) + bytestring[2*i]
            self.c0 = (self.c0 + bytepart) % 65535
            self.c1 = (self.c1 + self.c0) % 65535
        if len(bytestring) % 2 == 1:
            bytepart = bytestring[len(bytestring)-1]
            self.c0 = (self.c0 + bytepart) % 65535
            self.c1 = (self.c1 + self.c0) % 65535

        # compute check bytes
        self.cb0 = 65535 - ((self.c0 + self.c1) % 65535)
        self.cb1 = 65535 - ((self.c0 + self.cb0) % 65535)

    # needs work, broken
    def hexdigest(self):
        translated_number = hex((self.c1 << 16) + (self.c0))
        if len(translated_number) % 2 == 0:
            return '0x' + translated_number[2:]
        return '0x0' + translated_number[2:]

    def cb_hexdigest(self):
        translated_number = hex((self.cb0 << 16) + (self.cb1))
        if len(translated_number) % 2 == 0:
            return translated_number[2:]
        return '0' + translated_number[2:]


class Fletcher64:

    #takes no arguments, since you add string by updating
    def __init__(self):
        self.c0 = 0
        self.c1 = 0
        self.cb0 = 0
        self.cb1 = 0

    def update(self, bytestring):
        # prevents unicode or weirdly encoded strings
        # from being passed in
        if type(bytestring) != bytes:
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)

        iterations = ((len(bytestring) - 1) // 4) + 1
        for i in range(0, iterations):
            bytepart = int.from_bytes(bytestring[4*i:(4*(i+1))], byteorder="little")
            self.c0 = (self.c0 + bytepart) % 4294967295
            self.c1 = (self.c1 + self.c0) % 4294967295

        # compute check bytes
        self.cb0 = 4294967295 - ((self.c0 + self.c1) % 4294967295)
        self.cb1 = 4294967295 - ((self.c0 + self.cb0) % 4294967295)

    # needs work, broken
    def hexdigest(self):
        translated_number = hex((self.c1 << 32) + (self.c0))
        if len(translated_number) % 2 == 0:
            return '0x' + translated_number[2:]
        return '0x0' + translated_number[2:]

    def cb_hexdigest(self):
        translated_number = hex((self.cb0 << 32) + (self.cb1))
        if len(translated_number) % 2 == 0:
            return translated_number[2:]
        return '0' + translated_number[2:]




# I'm not sure how to write a user-friendly CLI
# maybe i can do the options thing in the cli,
# try that for part 2

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

        print(hexdigest)

##if __name__ == '__main__':
##    main()

