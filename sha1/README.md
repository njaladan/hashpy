# SHA-1

## Description
SHA-1 stands for Secure Hash Algorithm (1) and was developed by the NSA in the mid-1990s. Although developed to be relatively secure, the algorithm hasn't been considered the most secure. Attacks have been found, and it's possible to produce a collision with relatively little effort with a modern computer. SHA-1 is rather outdated today, and most systems have moved away from this hash function. SHA-1 produces a 160 bit hash, has a word size of 32 bits, and a block size of 512 bits.

## Personal thoughts
Writing this hash function was much easier, partially because I think the [RFC](https://tools.ietf.org/html/rfc3174) was very well written. In addition, I think that this function is semantically much easier than MD4, for instance, as this one doesn't have such a huge number of rounds using various functions. I'm beginning to understand how a better description or spec can ease the pain of a programmer.
