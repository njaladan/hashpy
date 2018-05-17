def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def rotr(x, n):
    return (x >> n) | (x << (32 - n))

def rotl(x, n):
    return (x << n) | (x >> (32 - n))

def rotr_64(x, n):
    return (x >> n) | (x << (64 - n))

def rotl_64(x, n):
    return (x << n) | (x >> (64 - n))

def ch(x, y, z):
    return (x & y) ^ ((~ x) & z)