from abc import abstractmethod


class ClienteProprietarioInterface:

    @abstractmethod
    # utilizzabile per visualizzare i dati personali
    def controllaStatoProdotti(self):
        pass

    @abstractmethod
    # utilizzabile per visualizzare i dati personali
    def visualizzaDatiPersonali(self):
        pass
