from abc import abstractmethod


class UserInterface:

    # utilizzabile per per la ricerca di un prodotto con id
    @abstractmethod
    def ricercaProdotto(self):
        pass

    @abstractmethod
    def filtraProdottiConDataEsposizione(self):
        # utilizzabile per il filtraggio dei prodotti in base alla data
        pass

    # utilizzabile per il filtraggio dei prodotti in base all prezzo
    @abstractmethod
    def filtraProdottiConPrezzo(self):
        pass

    # utilizzabile per il filtraggio dei prodotti in base alla categoria
    @abstractmethod
    def filtraProdottiConCategoria(self):
        pass

    # utilizzabile per effetturare un login di un utente
    @abstractmethod
    def login(self):
        pass

    # utilizzabile per recuperare la lista dei prodotti in vendita
    @abstractmethod
    def visualizzaProdotti(self):
        pass
