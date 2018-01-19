# BSD 16-bit

## Description
Though the function itself is called the BSD checksum, it was popularized by the `sum` command in Unix. This particular one I implemented outputs a 16-bit checksum and takes in 8-bit inputs. The Wikipedia article [here](https://www.wikiwand.com/en/BSD_checksum) has a pretty great explanation of how it works, so I won't delve into that here.

## Personal thoughts
I learned a lot. Bitwise manipulation in Python isn't the easiest thing to visualize, so I ended up drawing out a lot of diagrams to understand bitshifts, AND, and other operators.

I kind of understand byte manipulation more now (especially in terms of bytewise I/O as well as byte arrays). This checksum isn't very safe (doesn't avalanche, not cryptographically secure), so it makes me wonder what the different use cases for hashing functions and checksums are. Checksums don't seem to be used as often nowadays, but I'll have to check.

Something slightly crazy is just how easily you can cause the checksum to be something you want; adding only one or two bytes in the entire file should be enough to ensure that. I think I'd like write a program that flips the checksum into a desired number by changing the fewest amount of bits.

Also, order of operations for bitwise operators is weird. There were situations where I thought the order would go one way, though it turned out to be completely different. A lesson in always using parantheses, I suppose.
