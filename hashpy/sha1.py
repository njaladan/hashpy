"""
Contains implementation for SHA-1 160 bit hash
Based off of the IETF RFC 3174: https://tools.ietf.org/html/rfc3174

Author: Nagaganesh Jaladanki
License: MIT
"""

import utils
from hash import Hash


def f0(b, c, d):
    return d ^ (b & (c ^ d))


def f1(b, c, d):
    return b ^ c ^ d


def f2(b, c, d):
    return (b & c) | (b & d) | (c & d)


def f3(b, c, d):
    return b ^ c ^ d


def f(t, b, c, d):
    """ Helper function to choose which scrambling function to
    invoke given current round value"""

    if t < 20:
        return f0(b, c, d)
    elif t < 40:
        return f1(b, c, d)
    elif t < 60:
        return f2(b, c, d)
    return f3(b, c, d)


K = [0x5A827999,
     0x6ED9EBA1,
     0x8F1BBCDC,
     0xCA62C1D6]


class SHA1(Hash):
    """Computes the SHA-1 160-bit hash"""

    name = "SHA-1"
    block_size = 64
    word_size = 4
    digest_size = 20
    rounds = 80
    H_IV = [0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0]

    def update(self, bytestring, debug=False):
        """ Updates current hash object with data.

        Args:
            bytestring (str/bytes): data to append to existing hash data
            debug (bool): prints debug data to stdout if set
        """

        # Step 0: Convert to appropriate type if necessary
        if not isinstance(bytestring, bytes):
            bytestring = str.encode(bytestring)
        bytestring = bytearray(bytestring)
        self.data += bytestring
        if debug:
            print("Input data is: {0}".format(self.data))

        # Step 1: Pad null bytes until suitable for MD construction
        numtopad = 56 - (len(bytestring) % 64)
        if numtopad <= 0:
            numtopad += 64

        # Minor protection against length extension attacks
        padded = self.data + bytearray([128])
        padded += bytearray(numtopad - 1)

        # Step 2: Append length to padded message
        padded += (len(self.data) * 8).to_bytes(8, 'big', signed=False)
        if debug:
            print("Padded data is: {0}".format(padded))

        # Step 3: Cycle computation on each block
        self.H = self.H_IV[:]
        for j in range(len(padded) // 64):
            chunk_start_index = self.block_size * j
            chunk_end_index = self.block_size * (j + 1)
            chunk = padded[chunk_start_index: chunk_end_index]

            W = [0] * 80
            for i in range(16):
                byte_slice_start = self.word_size * i
                byte_slice_end = self.word_size * (i + 1)
                num = chunk[byte_slice_start: byte_slice_end]
                W[i] = int.from_bytes(num, byteorder='big', signed=False)

            for i in range(16, 80):
                xor = W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16]
                W[i] = utils.rotl32(xor, 1)

            if debug:
                print("Round {0} message schedule is: {1}".format(j, W))

            a, b, c, d, e = self.H
            for i in range(80):
                temp = (utils.rotl32(a, 5) + f(i, b, c, d) +
                        e + W[i] + K[i // 20]) & 0xffffffff
                e, d = d, c
                c = utils.rotl32(b, 30)
                b, a = a, temp

            # Update intermediate hash values
            li = [a, b, c, d, e]
            for i in range(5):
                self.H[i] = (self.H[i] + li[i]) & 0xffffffff

            if debug:
                print(
                    "Round {0} hash value is: {1}".format(
                        j, self.hexdigest()))

        if debug:
            print("Final hash value: {0}".format(self.hexdigest()))

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
