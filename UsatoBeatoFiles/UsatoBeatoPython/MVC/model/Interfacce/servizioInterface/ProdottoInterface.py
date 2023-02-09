from abc import abstractmethod


class ProdottoInterface:

    @abstractmethod
    # utilizzabile per
    def aggiornaProdotto(self, nomeCategoria, dataEsposizione,
                         nomeProdotto, prezzoCorrente, nomeScaffaleLe, idProdotto):
        pass

    @abstractmethod
    # utilizzabile per
    def scontaProdotti(self):
        pass

    @abstractmethod
    # utilizzabile per
    def spostaProdotto(self, id, start, end):
        pass
