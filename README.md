# hashbrowns
Collection of various hash functions.

## Introduction
Hash functions are pretty interesting, but I never really understood them. This is just a small personal project where I'm trying to write various hash functions to try to understand them better.

I'm writing them in Python now, but I might move into other language in the future.

## File structure

Each directory consists of several Python files and a couple of test documents to test the hash functions out with.

Each directory also contains a `README.md` documenting my understanding and a (hopefully) easy-to-understand description of the function. I hope it helps out if you're trying to understand it in an easy manner.

## Hash functions
This is a pretty optimistic list.

- [x] BSD 16-bit checksum
- [x] Fletcher checksum
- [x] Adler-32
- [ ] CRC32
- [x] MD2
- [ ] MD4
- [ ] MD5
- [ ] Jenkins
- [ ] BLAKE
- [ ] SHA-0
- [ ] SHA-2

## Future
Efficiency is a big deal when parsing lots of data in Python (well, maybe Python's not the right thing anyway), so I'd like to work on that first. Also, I really want to try porting it to a library as well.

MIT License.
