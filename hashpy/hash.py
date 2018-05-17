from abc import ABC, abstractmethod


class Hash(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def hexdigest(self):
        pass

    @abstractmethod
    def digest(self):
        pass

    @abstractmethod
    def copy(self):
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

