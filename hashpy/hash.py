from abc import ABC, abstractmethod


class Hash(ABC):
    @abstractmethod
    def update(self):
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

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def digest_size(self):
        pass

    @property
    @abstractmethod
    def block_size(self):
        pass

