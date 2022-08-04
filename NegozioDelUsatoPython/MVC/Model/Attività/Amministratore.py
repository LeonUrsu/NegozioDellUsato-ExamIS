from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService import File, Statistiche
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Ricevuta import Ricevuta


class Amministratore:

    # Metodo che aggiorna un account in base ai parametri passati dall'amministratore
    def aggiornaAccount(self):




    # Metodo che aggiorna un prodotto in base ai parametri passati dall'amministratore
    def aggiornaProdotto(self):


    # Metodo che effettua il backup del sistema in maniera manuale dall amministratore
    # mentre il metodo nella classe Backup verra' richiamato dal sistema ad una determinata ora
    def effettuaBackup(self):
        Backup.effettuaBackup()


    # Metodo che elimina un account dal database
    def eliminaAccount(sel,IDAccount):
        Account.eliminaAccount(IDAccount)


    # Metodo che elimina un prodotto dagli oggetti in vendita a quelli eliminati
    def eliminaProdotto(self, id):
        Prodotto.spostaProdotto(self, id, "InVendita", "Eliminati")


    # Metodo che filtra i clienti in base al nome o al cognome
    # return = lista delle persone con dati passati
    def filtraClienti(self, nome, cognome):
        listClientiConNome = None
        listClientiConCognome = None
        listClienti = self.recuperaClienti()
        if nome != None:
            listClientiConNome = list()
            for cliente in listClienti:
                if cliente.nome == nome:
                    listClientiConNome.append(cliente)
            return listClientiConNome
        elif cognome != None:
            listClientiConCognome = list()
            for cliente in listClienti:
                if cliente.cliente == cliente:
                    listClientiConCognome.append(cliente)
            return listClientiConCognome
        else:
            return None


    def inserisciProdotto(self,codiceCategoria,dataEsposizione, IDAccount,
                          nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale):
        pathFile = 'Database/Prodotti/InVendita.txt'
        prodotto = Prodotto.aggiungiProdotto(self,codiceCategoria,dataEsposizione, IDAccount
                          nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale)
        prodotto.mettiProdottoSuFile(self,pathFile, prodotto)


    def ricercaAccount(self):


    def vendiProdotto(self, prodottoList):
        list = []
        for x in prodottoList:
            list.append(Prodotto.vendiProdotto())
        ricevuta = Ricevuta.__init__(self, list)
        ricevuta.emettiRicevuta()




    def visualizzaStatistiche(self):
        Statistiche.visualizzaStatistiche()


    # Metodo che recupera dal database la lista dei clienti nel database
    # return = lista di Clienti
    def recuperaClienti(self):
        fileName = 'Database\Clienti\Clienti.txt'
        listClienti = File.deserializza(fileName)
        return listClienti

    def filtraggioClienti(self, stringa, list):
        for cliente in list:
            if
