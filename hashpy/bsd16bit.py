print('BSD 16-bit checksum calculator')
print('Enter a file name.')
doc = input()
f = open(doc, "rb")
r = f.read()
f.close()

arr = bytearray(r)

checksum = 0 #initialize
bitmask = 0xffff
num_of_bytes = 0

for b in arr:
    # circular shift byte-array one position to the right
    # 16 bit, max valid amount is 0xffff
    num_of_bytes += 1
    checksum = (checksum >> 1) + ((checksum & 1) << 15)
    checksum = (checksum + b) & bitmask

print("Checksum: " + str(checksum))
print("Number of bytes processed: " + str(num_of_bytes))


