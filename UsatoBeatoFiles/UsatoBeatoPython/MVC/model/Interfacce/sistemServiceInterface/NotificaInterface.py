from abc import abstractmethod


class NotificaInterface:

    @abstractmethod
    # utilizzabile per
    def gestioneEmailDIRegistrazione(self, email, password):
        pass

    @abstractmethod
    # utilizzabile per
    def gestioneEmailDiVendita(self, listProdottiVenduti):
        pass

    @abstractmethod
    # utilizzabile per
    def gestioneEmailDiEliminazione(self, idProdotto):
        pass

