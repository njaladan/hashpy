"""
Base class Hash implementation
Author: Nagaganesh Jaladanki
License: MIT
"""

from abc import ABCMeta, abstractmethod


class Hash(metaclass=ABCMeta):

    def __init__(self, data=None):
        """Initialize the hash object"""

        self.data = data
        if data is not None:
            self.data = bytearray(0)
        self.update(data)

    @abstractmethod
    def update(self, bytestring):
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

    @abstractmethod
    def copy(self):
        """Returns a deepcopy of the object"""
        pass
