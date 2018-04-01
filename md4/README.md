# MD4

## Description
MD4, which stands for Message Digest 4, is a hashing function that was invented by Ronald Rivest in 1992. This was around the era where hashing functions began to get more complicated and rose in popularity, especially when compared with the simple checksums from the earlier decade. We can directly see this by the increasing length of the code, as well as the complexity of the computations. MD4 was designed to work quickly on 32-bit machine. The code reflects this due to working in chunks (known as words) of 32 bits each.

## Personal thoughts
Wow! This was definitely one of the more technical things I've ever coded, mostly due to the complexity of the algorithm. It was really difficult to understand how necessary working and converting to little-endian was, especially since MD4 worked in words on 32 bits each. This was a big cause of several of the problems that I had.

Something else that's getting me thinking is the fact that I don't really understand *why* these hash functions work. What gives running XOR in these special formations the collision resistance that a hash function requires? Why is this a hash function? To be fair, implementing the function from the RFC itself was pretty difficult, though I'm not even sure what resources to pursue to understand the code that I'm writing.

I think it goes back to Bloom's taxonomy - I *understand* and *remember* what I've written, but I don't think I can evaluate or apply it by any means. I'll have to work on that.

For this particular module, I decided to forego the "input your file" main function in lieu of just running the test vectors. I think I might go with this for now, and maybe have another module / function that lets the user input any file and choose the particular function they want to run on it. I think this is better coding, since it takes advantage of abstraction.

## A few things I learned
* Code documentation can sometimes made a concept seem less efficient as a tradeoff to explaining it simply. [RFC 1320](https://tools.ietf.org/html/rfc1320) does exactly this when explaining the three rounds of processing that each block goes through. However, I think that I was able to take the main idea and code it more concisely - a bit proud of that.

* The `struct` function has a lot of byte manipulation features that I think I'll use in the future. Although I originally wanted to create a library without using any external modules, I think using low-level operations like these will help.

* Similarly, something I have to start avoiding is writing functions for things that have already been implemented - I ended up writing a long function to convert a number to its bytewise representation, though it later turned out that I could simply have used the `int.from_bytes` function for that.

* Having the update function return the object at the end can lead to cool "function stringing" like so `md4('hello').hexdigest`. I thought this was really cool.

## Thanks
Thanks to @rwg for his MD4 test vector breakdown [here](https://gist.github.com/rwg/ff60663d8dbf37f8c53b) - I couldn't have done it without this.
