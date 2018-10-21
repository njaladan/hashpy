"""
Common utilities and constants for hash functions
Author: Nagaganesh Jaladanki
License: MIT
"""


bitmask_32bit = 0xffffffff
bitmask_64bit = 0xffffffffffffffff

def rotr32(x, n):
    return ((x >> n) | (x << (32 - n))) & bitmask_32bit

def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & bitmask_32bit

def rotr64(x, n):
    return ((x >> n) | (x << (64 - n))) & bitmask_64bit

def rotl64(x, n):
    return ((x << n) | (x >> (64 - n))) & bitmask_64bit


""" SHA-1 family """



""" SHA-2 family """

def ch(x, y, z):
    return (x & y) ^ ((~ x) & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def bsig0_32(x):
    return rotr32(x, 2) ^ rotr32(x, 13) ^ rotr32(x, 22)

def bsig1_32(x):
    return rotr32(x, 6) ^ rotr32(x, 11) ^ rotr32(x, 25)

def ssig0_32(x):
    return rotr32(x, 7) ^ rotr32(x, 18) ^ (x >> 3)

def ssig1_32(x):
    return rotr32(x, 17) ^ rotr32(x, 19) ^ (x >> 10)

def bsig0_64(x):
    return rotr64(x, 28) ^ rotr64(x, 34) ^ rotr64(x, 39)

def bsig1_64(x):
    return rotr64(x, 14) ^ rotr64(x, 18) ^ rotr64(x, 41)

def ssig0_64(x):
    return rotr64(x, 1) ^ rotr64(x, 8) ^ (x >> 7)

def ssig1_64(x):
    return rotr64(x, 19) ^ rotr64(x, 61) ^ (x >> 6)
