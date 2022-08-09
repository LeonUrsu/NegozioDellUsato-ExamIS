from MVC.Model.Attività.Indirizzo import Indirizzo
from MVC.Model.Attività.User import User
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.Servizio.Scaffale import Scaffale
from MVC.Model.SistemService.File import File
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Ricevuta import Ricevuta
from MVC.Model.SistemService.Logging import Logging
from MVC.Model.SistemService.Notifica import Notifica
from MVC.Model.SistemService.Statistiche import Statistiche


class Amministratore(User):

    def __init__(self):
        super().__init__()
        self.email = "admin"
        self.password = "admin"

    # Metodo che aggiorna un account in base ai parametri passati dall'amministratore
    def aggiornaAccount(self,cliente, nome, cognome, dataDiNascita, email,
        idAccount, numeroTelefonico, residenza):
        Account().aggiornaAccount(cliente, nome, cognome, dataDiNascita, email,
        idAccount, numeroTelefonico, residenza)


    # Metodo che aggiorna un prodotto in base ai parametri passati dall'amministratore
    def aggiornaProdotto(self, codiceCategoria, dataEsposizione, idAccount,
            nomeProdotto, prezzoOriginale, idScaffale, idProdotto):
        fileName = "Database/Prodotti/InVendita.txt"
        listProdotti = File().deserializza(fileName)
        prodottoTrovato = Prodotto().prendiProdottoDaFile(fileName, idProdotto)
        if codiceCategoria != prodottoTrovato.codiceCategoria:
            categoria = Categoria()
            categoria.aggiornaCategoriaProdotto(prodottoTrovato, prodottoTrovato.codiceCategoria, codiceCategoria)
        if dataEsposizione != prodottoTrovato.dataEsposizione: prodottoTrovato.dataEsposizione = dataEsposizione
        if idAccount != prodottoTrovato.iDAccount:
            account = Account()
            account.aggiornaIdProdottoInAccount(prodottoTrovato, prodottoTrovato.idAccount, idAccount)
        if nomeProdotto != prodottoTrovato.nomeProdotto: prodottoTrovato.nomeProdotto = nomeProdotto
        if prezzoOriginale != prodottoTrovato.prezzoOriginale: prodottoTrovato.prezzoOriginale = prezzoOriginale
        if idScaffale != prodottoTrovato.idScaffale:
            scaffale = Scaffale()
            scaffale.cambiaScaffale(prodottoTrovato.idScaffale, idScaffale, prodottoTrovato.idProdotto)



    # Metodo che effettua il backup del sistema in maniera manuale dall amministratore
    # mentre il metodo nella classe Backup verra' richiamato dal sistema ad una determinata ora
    def effettuaBackup(self):
        Backup().effettuaBackup()


    # Metodo che elimina un account dal database
    def eliminaAccount(sel,IDAccount):
        Account().eliminaAccount(IDAccount)


    # Metodo che elimina un prodotto dagli oggetti in vendita a quelli eliminati
    def eliminaProdotto(self, prodotto):
        Prodotto().eliminaProdotto(prodotto.idProdotto)
        try:
            Notifica().gestioneEmailDiEliminazione(prodotto)
        except: pass


    # Metodo che filtra i clienti in base al nome o al cognome
    # return = lista delle persone con dati passati
    def filtraClienti(self, nome, cognome):
        listClientiConNome = None
        listClientiConCognome = None
        listClienti = self.recuperaClienti()
        if nome != None:
            listClientiConNome = list()
            for cliente in listClientiConNome:
                if cliente.nome == nome:
                    listClientiConNome.append(cliente)
                    return listClientiConNome
        elif cognome != None:
            listClientiConCognome = list()
            for cliente in listClientiConCognome:
                if cliente.cliente == cliente:
                    listClientiConCognome.append(cliente)
                    return listClientiConCognome
        else:
            return None


    # Metodo per inserire un prodotto nel database
    def inserisciProdotto(self, idCategoria, dataEsposizione, idAccount,
          nomeProdotto, prezzoOriginale, statoDiVendita, idScaffale):
        pathFile = "Database/Prodotti/InVendita.txt"
        prodotto = Prodotto().aggiungiProdotto(idCategoria, dataEsposizione, idAccount, nomeProdotto, prezzoOriginale,
                                                statoDiVendita)
        prodotto.mettiProdottoSuFile(self, pathFile, prodotto)
        if idScaffale != None: Scaffale().aggiungiProdottoAScaffale(prodotto, idScaffale)
        Account().aggiungiProdottoAAccount(prodotto)
        Categoria().aggiungiProdottiInCategoria(prodotto)



    # Metodo che serve per l'inserimento di un cliente Proprietario all'interno del database e la comunicazione delle
    # credenziali via email
    def inserisciAccount(self, nome, cognome, dataDiNascita, email, password,
                        idAccount, idProdotti, numeroTelefonico, cap, citofono, citta, civico, piazza, via):
        if Account().checkEmailUtente(email) == True:
            return False
        indirizzo = Indirizzo(cap, citofono, citta, civico, piazza, via)
        Account().aggiungiAccount(nome, cognome, dataDiNascita, email, numeroTelefonico, password, indirizzo)
        Logging().aggiungiLogging(idAccount)
        Logging().inserisciLoggingNelDatabase()
        Notifica().gestioneEmailDIRegistrazione(email, password)
        return True


    # Metodo di passaggio per la ricerca di un account
    def ricercaAccount(self, id):
        return Account().trovaAccountTramiteId(id)


    # Metodo per la vendita di una lista di oggetti
    # return = dizionario con info di oggetti venduti
    def vendiProdotti(self, prodottoList):
        list = []
        for prodotto in prodottoList:
            list.append(Prodotto().vendiProdotto(prodotto.idProdotto))
        ricevuta = Ricevuta(list)
        try:
            Notifica().gestioneEmailDiVendita(prodottoList)
        except: pass
        return ricevuta.emettiRicevuta()


    # Metodo che recupera le statistiche sul sistema
    def visualizzaStatistiche(self):
        Statistiche().visualizzaStatistiche()


    # Metodo che recupera dal database la lista dei clienti nel database
    # return = lista di Clienti
    def recuperaClienti(self):
        fileName = 'Database\Clienti\Clienti.txt'
        listClienti = File().deserializza(fileName)
        return listClienti



