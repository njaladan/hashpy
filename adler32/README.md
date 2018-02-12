# Fletcher N-bit Checksum

## Description
The Adler-32 checksum is really similar to the Fletcher-32 bit checksum. Both of them output a digest of 32 bits, and use a similar rolling two-checksum calculator. However, something interesting is that Adler-32 uses a prime modulus (65521, the largest prime that fits in a 16 bit digest), and only one-byte words. This causes a decrease in efficiency due to the greater number of iterations needing to run be as a result of the smaller word size, as well as due to the prime modulus (a costly computation).

The prime modulus is pretty clever, in theory. There's an excellent write-up [here](https://stackoverflow.com/questions/927277/why-modulo-65521-in-adler-32-checksum-algorithm), and I encourage you to check it out if you're interested.

## Personal thoughts
I ended up using the same class from my Fletcher N-bit, since the bulk of the algorithm is the same. However, I think that's pretty inefficient. Perhaps I could have imported the N-bit into this folder and just created a subclass. When I start trying to make this a real library, I'll work on doing that. Also, I think I'm beginning to appreciate Java interfaces more and understand why Python's class structures aren't the best. A lot of programming seems to be internalization of what you plan to do, and things like Java interfaces can help with that.
