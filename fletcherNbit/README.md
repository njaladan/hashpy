# Fletcher N-bit Checksum

## Description
The actual algorithm isn't called the "N-bit checksum", though I decided to call it that since I wanted to make a program that would work well for the 16-, 32-, and 64-bit implementations of it. The algorithm is a checksum in the very traditional sense such that it literally involves checking sums (aha!). There's two sums that are tallied up, for error-correction / propagation purposes, and some checkbytes that essentially act as a checksum for the checksum.

## Personal thoughts
I went through a long process on this one, particularly because the 32- and 64- bit algorithms turned out to be more complicated than I expected. In particular, reading the bytes in portions (of 2 bytes each, for example), was pretty difficult. I ended up writing a very slow and inefficient method to do the splitting up by taking the various bytes from the bytearray and manually shifting apart the bits with bitshift operators. It was inefficient and later completely scrapped when I found out about the very useful `int.from_bytes` method.

I think I kind of understand the distinction between the necessity for checksums and hashes now - a lot of these checksums are very easy to compute and can detect a likely error in a majority of the cases, which is good where security isn't necessary but speed is (such as for TCP packets).  

Something interesting: this particular checksum gives different results based off of whether the bytes are read in big or little endian. I ended up having a lot of trouble during the beginning of the project when I tried doing all of this manually and didn't know that it would have an effect. However, I kind of understand it more now, and it makes me wonder how more complicated hashes standardize this between operating systems that use different endian systems.

## A few things I learned
 * `if __name__ == '__main__':` this pattern is used for launching a method at the beginning of the file being run, but won't run anything if that particular file isn't run (such as if it's in a library)
 * More about bitshift operators - I think I'm getting more intuitive with them but it does get kind of annoying to keep checking my answers with `bin()` because it's hard to understand the decimal output of a bitshift
 * Object-orientation. I wrote the entire program as separate classes for each type of checksum until I realized that they all had something in common and could be collapsed into a single class. I used to think the inheritance thing was just a part of object-orientation, but now I feel like that's the most important thing.
 *
