from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.File import File
from MVC.Model.SistemService.Filtri import Filtri
from MVC.Model.SistemService.Logging import Logging


class User(object):


    # Costruttore della classe User, create() in EA
    def __init__(self):
        self.accessiAccount = None


    # Metodo per la ricerca di un prodotto
    def ricercaProdotto(self, idProdotto, listProdotti):
        for prodotto in listProdotti:
            if prodotto.idProdotto == idProdotto:
                return prodotto

    # Metodo di filtraggio dei prodotti in base alla data
    def filtraProdottiConData(self, dataInizio, dataFine):
        fileName = 'Database\Prodotti\InVendita.txt'
        filtered = Filtri().filtraData(dataInizio, dataFine, fileName)
        return filtered


    # Metodo di filtraggio dei prodotti in base all prezzo
    def filtraProdottiConPrezzo(self, prezzoMin, prezzoMax):
        fileName = 'Database\Prodotti\InVendita.txt'
        filtered = Filtri().filtraPrezzo(prezzoMin, prezzoMax, fileName)
        return filtered


    # Metodo di filtraggio dei prodotti in base alla categoria
    def filtraProdottiConCategoria(self, codiceCategoria):
        fileName = 'Database\Prodotti\InVendita.txt'
        filtered = Filtri().filtraCategoria(codiceCategoria)
        return filtered


    def login(self, email, password):
        Logging().login(email, password)
        return True


    # MEtodo che recupera la lista dei prodotti in vendita
    def visualizzaProdotti(self):
        fileName = 'Database\Prodotti\InVendita.txt'
        return File().deserializza(fileName)
