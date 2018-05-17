def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def rotr(x, n):
    return (x >> n) | (x << (32 - n)) & 0xffffffff

def rotl(x, n):
    return (x << n) | (x >> (32 - n)) & 0xffffffff

def rotr_64(x, n):
    return (x >> n) | (x << (64 - n)) & 0xffffffffffffffff

def rotl_64(x, n):
    return (x << n) | (x >> (64 - n)) & 0xffffffffffffffff

def ch(x, y, z):
    return (x & y) ^ ((~ x) & z)