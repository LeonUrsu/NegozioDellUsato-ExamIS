from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Ricevuta import Ricevuta
class Amministratore:


    def aggiornaAccount(self):
        pass

    def aggiornaProdotto(self):


    def effettuaBackup(self):
        Backup.effettuaBackup()

    def eliminaAccount(sel,IDAccount):
        Account.eliminaAccount(self, IDAccount)

    def eliminaProdotto(self, id):
        Prodotto.spostaProdotto(self, id,"InVendita", "Eliminati")


    def filtraClienti(self):
        pass

    def inserisciProdotto(self,codiceCategoria,dataEsposizione, IDAccount,
                          nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale):
        pathFile = 'Database/Prodotti/InVendita.txt'
        prodotto = Prodotto.aggiungiProdotto(self,codiceCategoria,dataEsposizione, IDAccount
                          nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale)
        prodotto.mettiProdottoSuFile(self,pathFile, prodotto)

    def ricercaAccount(self):
        pass

    def vendiProdotto(self, prodottoList):
        list = []
        for x in prodottoList:
            list.append(Prodotto.vendiProdotto())
        ricevuta = Ricevuta.__init__(self, list)
        ricevuta.emettiRicevuta()




    def visualizzaStatistiche(self):
        Statistiche.visualizzaStatistiche()