from abc import abstractmethod


class CategoriaInterface:

    @abstractmethod
    # utilizzabile per eliminare una categria in database
    def deleteInDatabase(self, idCategoria):
        pass

    @abstractmethod
    # utilizzabile per trovareuna categoria tramite id
    def trovaCategoria(self, idCategoria):
        pass
