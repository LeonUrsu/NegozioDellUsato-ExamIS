from abc import abstractmethod


class FileInterface:

    @abstractmethod
    # utilizzabile per
    def deserializza(self, fileName):
        pass

    @abstractmethod
    # utilizzabile per
    def serializza(self, fileName, contenuto):
        pass
