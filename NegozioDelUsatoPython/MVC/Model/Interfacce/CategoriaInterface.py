from abc import abstractmethod


# Una serie di metodi astratti da essere definiti nella classe che implementa l'interfaccia
class CategoriaInterface:

    @abstractmethod
    # utilizzabile per aggiungere le variabili interne ad un'istanza di classe appena creata
    def aggiungiCategoria(self):
        pass

    @abstractmethod
    # utilizzabile per per leggere la lista delle categorie
    def recuperaListaOggetti(self):
        pass

    @abstractmethod
    # utilizzabile per recuperare una categoria tramite id
    def trovaCategoriaTramiteId(self):
        pass

    @abstractmethod
    # utilizzabile per recuperare una categoria tramite nome
    def trovaCategoriaTramiteNome(self):
        pass
