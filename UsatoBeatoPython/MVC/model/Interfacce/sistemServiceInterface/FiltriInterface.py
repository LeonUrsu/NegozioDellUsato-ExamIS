from abc import abstractmethod


class FiltriInterface:

    @abstractmethod
    # utilizzabile per
    def filtraClienti(self, nome, cognome):
        pass

    @abstractmethod
    # utilizzabile per
    def filtraCategoria(self, idCategoria, fileName):
        pass

    @abstractmethod
    # utilizzabile per
    def filtraDataEsposizione(self, dataInizio, dataFine, fileName):
        pass

    @abstractmethod
    # utilizzabile per
    def filtraPrezzo(self, prezzoMin, prezzoMax, fileName):
        pass
