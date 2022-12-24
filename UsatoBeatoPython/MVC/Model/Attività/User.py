from Database.PathDatabase import PathDatabase
from MVC.Model.Interfacce.UserInterface import UserInterface
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Filtri import Filtri
from MVC.Model.SistemService.Logging import Logging


class User(UserInterface, object):

    # Costruttore della classe User, create() in EA
    def __init__(self):
        pass

    # Metodo per la ricerca di un prodotto con id
    def ricercaProdotto(self, idProdotto):
        prodotto = Prodotto().trovaOggettoTramiteId(idProdotto)
        return prodotto

    # Metodo di filtraggio dei prodotti in base alla data
    def filtraProdottiConDataEsposizione(self, dataInizio, dataFine):
        fileName = PathDatabase().inVenditaTxt
        filtered = Filtri().filtraDataEsposizione(dataInizio, dataFine, fileName)
        return filtered

    # Metodo di filtraggio dei prodotti in base all prezzo
    def filtraProdottiConPrezzo(self, prezzoMin, prezzoMax):
        fileName = PathDatabase().inVenditaTxt
        filtered = Filtri().filtraPrezzo(prezzoMin, prezzoMax, fileName)
        return filtered

    # Metodo di filtraggio dei prodotti in base alla categoria
    def filtraProdottiConCategoria(self, idCategoria):
        fileName = PathDatabase().inVenditaTxt
        filtered = Filtri().filtraCategoria(idCategoria, fileName)
        return filtered

    # Metodo che utilizzabile per effetturare un login di un utente
    def login(self, email, password):
        return Logging().login(email, password)

    # Metodo che recupera la lista dei prodotti in vendita
    def visualizzaProdotti(self):
        listProdotti = Prodotto().recuperaListaProdottiInVendita()
        return listProdotti
