# HashBrowns
Collection of self-written hash functions.


## Introduction
I think hash functions are one of those wonderful things that are a key part of technology and cryptography, but something that very few people really understand. As a result, I'm trying to understand how they work, and am writing a set of Python functions for each interesting hash/checksum function I run into.

I'm writing them in Python as that's what I'm familiar with now, but maybe I'll move onto other languages in the future. We'll see.

## File structure

Each directory consists of several Python files and a couple of test documents to test the hash functions out with.

Each directory also contains a `README.md` documenting my understanding and a (hopefully) easy-to-understand description of the function. I hope it helps out if you're trying to understand it in an easy manner.

## Hash functions
This is a pretty optimistic list.

- [x] BSD 16-bit checksum
- [x] Fletcher checksum
- [ ] Adler-32
- [ ] CRC32
- [ ] MD2
- [ ] MD4
- [ ] MD5
- [ ] Jenkins
- [ ] BLAKE
- [ ] SHA-0
- [ ] SHA-2

## Future
Efficiency is a big deal when parsing lots of data in Python (well, maybe Python's not the right thing anyway), so I'd like to work on that first. Maybe porting it into a library one day?

MIT License.
