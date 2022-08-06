from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService import File, Statistiche
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Ricevuta import Ricevuta


class Amministratore:

    # Metodo che aggiorna un account in base ai parametri passati dall'amministratore
    def aggiornaAccount(self,cliente, nome, cognome, dataDiNascita, email,
        iDAccount, numeroTelefonico, residenza):
        account = Account.prendiAccountDaFile(fileName, iDAccount)
        if nome != account.nome: account.nome = nome
        if cognome != account.cognome: account.cognome = cognome
        if dataDiNascita != account.dataDiNascita: account.dataDiNascita = dataDiNascita
        if email != account.email: account.email = email
        if iDProdotti != account.iDProdotti: account.iDProdotti = iDProdotti
        #if numeroTelefonico != account.numeroTelefonico: account.numeroTelefonico = numeroTelefonico
        if residenza != account.residenza: account.residenza = residenza
        fileName = "Database\Clienti\Clienti.txt"
        listAccount.append(account)
        File.serializza(fileName, listAccount)


    # Metodo che aggiorna un prodotto in base ai parametri passati dall'amministratore
    def aggiornaProdotto(self, codiceCategoria, dataEsposizione, iDAccount,
            nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale):
        fileName = "Database/Prodotti/InVendita.txt"
        listProdotti = File.deserializza(fileName)


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


    # Metodo per inserire un prodotto nel database
    def inserisciProdotto(self, codiceCategoria, dataEsposizione, iDAccount,
          nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale):
    pathFile = "Database/Prodotti/InVendita.txt"
    prodotto = Prodotto.aggiungiProdotto(codiceCategoria, dataEsposizione, IDAccount, nomeProdotto, prezzoOriginale, statoDiVendita , IDScaffale)
    prodotto.mettiProdottoSuFile(self,pathFile, prodotto)


    def ricercaAccount(self, id):
    Account.trovaAccountTramiteId(id)


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


