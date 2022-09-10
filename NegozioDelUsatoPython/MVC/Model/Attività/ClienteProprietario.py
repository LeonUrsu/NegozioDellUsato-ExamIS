from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Attività.User import User
from MVC.Model.SistemService.File import File
from MVC.Model.SistemService.Logging import Logging


class ClienteProprietario(User):


    # Metodo che restituisce 3 liste di Prodotti: inVendita, venduti, scaduti.
    # L'assegnazione deve essere: inVendita, venduti, scaduti = controllaStatoProdotti(account)
    def controllaStatoProdotti(self):
        if not self.checkAccontLoggatoConLogging():
            return None
        fileNameInVendita = PathDatabase().inVenditaTxt
        fileNameVenduti = PathDatabase().vendutiTxt
        filenameScaduti = PathDatabase().scadutiTxt
        account = Account().trovaOggettoTramiteId(Logging().accountLoggato.idAccount)
        inVendita = self.recuperaProdottiClienteProprietario(account.idAccount, fileNameInVendita)
        venduti = self.recuperaProdottiClienteProprietario(account.idAccount, fileNameVenduti)
        scaduti = self.recuperaProdottiClienteProprietario(account.idAccount, filenameScaduti)
        return inVendita, venduti, scaduti


    # Metodo che recupera l'account dell'utente loggato e lo restituisce se è effettivamente loggato
    # altrimenti restituisce None
    def visualizzaDatiPersonali(self):
        if not self.checkAccontLoggatoConLogging():
            return None
        return Logging.accountLoggato



    # Metodo che recupera la lista di prodotti appartenenti all'account di un
    # Cliente Proprietario tramite la ricerca degli oggetti tramite l'idAccount nella listProdotti del file.
    def recuperaProdottiClienteProprietario(self, idAccount, fileName):
        if not self.checkAccontLoggatoConLogging():
            return None
        listProdotti = File().deserializza(fileName)
        filteredListProdotti = list()
        for prodotto in listProdotti:
            if prodotto.idAccount == idAccount:
                filteredListProdotti.append(prodotto)
        return filteredListProdotti


    #Metodo che verifica se l'utente è loggato
    def checkAccontLoggatoConLogging(self):
        risultato = Logging().checkAccontLoggato()
        return risultato