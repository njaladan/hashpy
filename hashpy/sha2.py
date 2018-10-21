"""
Contains implementation for SHA-2 type hashes
Based off of the IETF RFC 4634: https://tools.ietf.org/html/rfc4634

Author: Nagaganesh Jaladanki
License: MIT
"""

import utils
from hash import Hash
from sha2constants import K_SHA_32, K_SHA_64


class SHA2(Hash):
    """General computation for hashes from the SHA-2 family.

    Used as a base class for the rest of the SHA-2 family; do not
    instantiate this object.

    Args:
        data (str/bytes, optional): wrapper for the `update` function

    Attributes:
        name: name of derivative hash function being called
        block_size: size in number of bytes of block per round of computation
        word_size: size in bytes of the smallest element of data manipulated
        digest_size: size in bytes of the output of the hash function
        rounds: number of rounds to scramble input from each block
        K: static constants for scrambling stage
        bitmask: Python-necessary mask to "simulate" integer overflow

    """

    def update(self, bytestring, debug=False):
        """ Updates current hash object with data.

        Args:
            bytestring (str/bytes): data to append to existing hash data
        """

        # Step 0: Convert input to bytearray if necessary
        if not isinstance(bytestring, bytes):
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)
        self.data += bytestring
        if debug:
            print("Parsed input data is: {0}".format(self.data))

        # Step 1: Add padding bits to ensure final message is
        # divisible by block_size
        field_length_size = 2 * self.word_size
        proper_pad_length = self.block_size - field_length_size
        numtopad = proper_pad_length - (len(self.data) % self.block_size)
        if numtopad <= 0:
            numtopad += self.block_size

        # Minor protection against length-extension attacks before zero-padding
        padded = self.data + bytearray([128])
        padded += bytearray(numtopad - 1)

        # Step 2: Append length of the original message to the
        # padded bytestring
        padded += (len(self.data) * 8).to_bytes(field_length_size, 'big')
        if debug:
            print("Padded data is: {0}".format(padded))

        # Step 3: Iterate computation for each block in data
        self.H = self.H_IV[:]
        for j in range(len(padded) // self.block_size):
            chunk_start_index = self.block_size * j
            chunk_end_index = self.block_size * (j + 1)
            chunk = padded[chunk_start_index: chunk_end_index]

            # Prepare the message schedule `W`
            W = [0] * self.rounds
            for i in range(16):
                byte_slice_start = self.word_size * i
                byte_slice_end = self.word_size * (i + 1)
                num = chunk[byte_slice_start: byte_slice_end]
                W[i] = int.from_bytes(num, byteorder='big')

            for i in range(16, self.rounds):
                W[i] = (self.ssig1(W[i - 2]) + W[i - 7] +
                        self.ssig0(W[i - 15]) + W[i - 16]) & self.bitmask
            if debug:
                print("Round {0} message schedule W is: {1}".format(j, W))

            # Initialize the working variables
            a, b, c, d, e, f, g, h = self.H

            # Primary hash computation
            for i in range(self.rounds):
                t1 = h + self.bsig1(e) + utils.ch(e, f, g) + self.K[i] + W[i]
                t2 = self.bsig0(a) + utils.maj(a, b, c)
                h = g
                g = f
                f = e
                e = (d + t1) & self.bitmask
                d = c
                c = b
                b = a
                a = (t1 + t2) & self.bitmask

            # Compute the intermediate hash value
            li = [a, b, c, d, e, f, g, h]
            for i in range(8):
                self.H[i] = (self.H[i] + li[i]) & self.bitmask
            if debug:
                print("Intermediate hash value is: {0}".format(self.hexdigest()))

        if debug:
            print("Final hash value is: {0}".format(self.hexdigest()))
        # Return object for method chaining
        return self

    def hexdigest(self):
        """ Generate human-readable string of the hex representation
        of the current hash value

        :return: str
        """

        hexdigest = 0
        iteration_count = self.digest_size // self.word_size
        for i in range(iteration_count):
            hexdigest = (hexdigest << self.word_size * 8) + self.H[i]
        hexdigest = hex(hexdigest)[2:]
        zero_pad = 2 * self.digest_size - len(hexdigest)
        return '0' * zero_pad + hexdigest

    def digest(self):
        """ Generate a bytes object of the current hash digest.

        :return: bytes
        """

        digest = bytes()
        iteration_count = self.digest_size // self.word_size
        for i in range(iteration_count):
            digest += self.H[i].to_bytes(self.word_size, 'big', signed=False)
        return digest


class SHA32bit(SHA2):
    """ Base class for the 32-bit word SHA-2 family """

    block_size = 64
    word_size = 4
    rounds = 64
    K = K_SHA_32
    bitmask = 0xffffffff
    bsig0 = staticmethod(utils.bsig0_32)
    bsig1 = staticmethod(utils.bsig1_32)
    ssig0 = staticmethod(utils.ssig0_32)
    ssig1 = staticmethod(utils.ssig1_32)


class SHA64bit(SHA2):
    """ Base class for the 64-bit word SHA-2 family """

    block_size = 128
    word_size = 8
    rounds = 80
    K = K_SHA_64
    bitmask = 0xffffffffffffffff
    bsig0 = staticmethod(utils.bsig0_64)
    bsig1 = staticmethod(utils.bsig1_64)
    ssig0 = staticmethod(utils.ssig0_64)
    ssig1 = staticmethod(utils.ssig1_64)


class SHA224(SHA32bit):
    """ SHA-224 hash object """

    name = "SHA-224"
    digest_size = 28
    H_IV = [0xc1059ed8, 0x367cd507,
            0x3070dd17, 0xf70e5939,
            0xffc00b31, 0x68581511,
            0x64f98fa7, 0xbefa4fa4]


class SHA256(SHA32bit):
    """ SHA-256 hash object """

    name = "SHA-256"
    digest_size = 32
    H_IV = [0x6a09e667, 0xbb67ae85,
            0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c,
            0x1f83d9ab, 0x5be0cd19]


class SHA384(SHA64bit):
    """ SHA-384 hash object """

    name = "SHA-384"
    digest_size = 48
    H_IV = [0xcbbb9d5dc1059ed8, 0x629a292a367cd507,
            0x9159015a3070dd17, 0x152fecd8f70e5939,
            0x67332667ffc00b31, 0x8eb44a8768581511,
            0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4]


class SHA512(SHA64bit):
    """ SHA-512 hash object """

    name = "SHA-512"
    digest_size = 64
    H_IV = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b,
            0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
            0x510e527fade682d1, 0x9b05688c2b3e6c1f,
            0x1f83d9abfb41bd6b, 0x5be0cd19137e2179]
