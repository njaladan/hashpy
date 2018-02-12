a = str.encode('abcdef')

c0 = (a[1] << 8) + a[0]
c1 = c0
c0 = (c0 + (a[3] << 8) + a[2]) % 65535
c1 = (c1 + c0) % 65535
c0 = (c0 + (a[5] << 8) + a[4]) % 65535
c1 = (c1 + c0) % 65535


print(hex(c0), hex(c1))

total = (c1 << 16) + c0
print(hex(total))


a = str.encode('abcde')

c0 = (a[1] << 8) + a[0]
c1 = c0
c0 = (c0 + (a[3] << 8) + a[2]) % 65535
c1 = (c1 + c0) % 65535
c0 = (c0 + a[4]) % 65535
c1 = (c1 + c0) % 65535


print(hex(c0), hex(c1))

total = (c1 << 16) + c0
print(hex(total))


