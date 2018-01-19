# algorithm comes in 16, 32, and 64 bit variants
# simple input will let user choose which one they want
# (to be implemented later)

# to-do: give checksum at the end
# TODO: make all of these a class

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

    def digest(self):
        return chr(self.c1) + chr(self.c0)

    # needs work, broken
    def hexdigest(self):
        translated_number = hex((self.c1 << 8) + (self.c0))
        if len(translated_number) % 2 == 0:
            return translated_number[2:]
        return '0' + translated_number[2:]

    def cb_digest(self):
        return chr(self.cb0) + chr(self.cb1)

    def cb_hexdigest(self):
        translated_number = hex((self.cb0 << 8) + (self.cb1))
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
        print('Enter 16-, 32-, or 64-bit checksum')
        inp = input()
        
    
        print(type(f.read()))

if __name__ == '__main__':
    main()

