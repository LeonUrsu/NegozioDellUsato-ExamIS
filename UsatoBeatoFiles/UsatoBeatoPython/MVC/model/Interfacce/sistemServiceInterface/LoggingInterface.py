from abc import abstractmethod


class LoggingInterface:

    @abstractmethod
    # utilizzabile per
    def timeout(self, log):
        pass

    @abstractmethod
    # utilizzabile per
    def verificaDettagliLogin(self, log, account, password):
        pass

