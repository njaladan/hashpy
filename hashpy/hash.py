"""
Base class Hash implementation
Author: Nagaganesh Jaladanki
License: MIT
"""

from abc import ABCMeta, abstractmethod


class Hash(metaclass=ABCMeta):
    """Base level class for hash computation

    Suggested use of debug is to manually check if hash computation is
    proceeding as expected

    Args:
        data (string / bytes): data for the hash to proceed on
        debug (bool): prints debugging/test information to stdout

    Suggested attributes:
        name: name of derivative hash function being called
        block_size: size in number of bytes of block per round of computation
        word_size: size in bytes of the smallest element of data manipulated
        digest_size: size in bytes of the output of the hash function
        rounds (optional): number of rounds to scramble input from each block
    """

    def __init__(self, data=None, debug=False):
        """Initialize the hash object"""

        self.data = data
        if data is not None:
            self.data = bytearray(0)
        self.update(data, debug=debug)

    @abstractmethod
    def update(self, bytestring, debug=False):
        """Updates the hash with the data passed in."""
        pass

    @abstractmethod
    def hexdigest(self):
        """Returns the hash in the form of a hex string"""
        pass

    @abstractmethod
    def digest(self):
        """Returns the hash in the form of a binary string"""
        pass
