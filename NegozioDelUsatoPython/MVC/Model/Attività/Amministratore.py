import json

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Indirizzo import Indirizzo
from MVC.Model.Attività.User import User
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.Servizio.Scaffale import Scaffale
from MVC.Model.SistemService.File import File
from MVC.Model.SistemService.Backup import Backup
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Ricevuta import Ricevuta
from MVC.Model.SistemService.Filtri import Filtri
from MVC.Model.SistemService.Logging import Logging
from MVC.Model.SistemService.Notifica import Notifica
from MVC.Model.SistemService.Statistiche import Statistiche


class Amministratore(User):

    def __init__(self):
        super().__init__()
        self.email = "admin"
        self.password = "admin"

    # Metodo che aggiorna un account in base ai parametri passati dall'amministratore
    def aggiornaAccount(self, nome, cognome, dataDiNascita, email,
                        idAccount, numeroTelefonico, residenza):
        Account().aggiornaAccount(nome, cognome, dataDiNascita, email,
                                  idAccount, numeroTelefonico, residenza)

    # Metodo che aggiorna un prodotto in base ai parametri passati dall'amministratore
    def aggiornaProdotto(self, codiceCategoria, dataEsposizione,
                         nomeProdotto, prezzoOriginale, idScaffale, idProdotto):
        Prodotto().aggiornaProdotto(codiceCategoria, dataEsposizione,
                         nomeProdotto, prezzoOriginale, idScaffale, idProdotto)

    # Metodo che effettua il backup del sistema in maniera manuale dall amministratore
    # mentre il metodo nella classe Backup verra' richiamato dal sistema ad una determinata ora
    def effettuaBackup(self):
        Backup().effettuaBackup()

    # Metodo che elimina un account dal database
    def eliminaAccount(sel, IDAccount):
        Account().eliminaAccount(IDAccount)

    # Metodo che elimina un prodotto dagli oggetti in vendita a quelli eliminati
    def eliminaProdotto(self, prodotto):
        Prodotto().eliminaProdotto(prodotto.idProdotto)
        try:
            Notifica().gestioneEmailDiEliminazione(prodotto)
        except:
            pass

    # Metodo che filtra i clienti in base al nome o al cognome
    # return = lista delle persone con dati passati
    def filtraClienti(self, nome, cognome):
        return Filtri().filtraClienti(nome, cognome)

    # Metodo per inserire un prodotto nel database
    def inserisciProdotto(self, idCategoria, dataEsposizione, idAccount,
                          nomeProdotto, prezzoOriginale, idScaffale):
        pathFile = PathDatabase().inVenditaTxt
        prodotto = Prodotto()
        prodotto.aggiungiProdotto(idCategoria, dataEsposizione, idAccount, nomeProdotto, prezzoOriginale, idScaffale)
        prodotto.mettiOggettoSuListaNelFile(pathFile)
        if idScaffale != None: Scaffale().associaProdottoAScaffale(prodotto)
        Account().associaProdottoAdAccount(prodotto)
        Categoria().aggiungiProdottiInCategoria(prodotto)
        return prodotto

    # Metodo che serve per l'inserimento di un cliente Proprietario all'interno del database e la comunicazione delle
    # credenziali via email
    def inserisciAccount(self, nome, cognome, dataDiNascita, email, password,
                           numeroTelefonico, cap, citofono, citta, civico, piazza, via):
        account = Account()
        if account.checkEmailUtente(email) == True:
            return False
        indirizzo = Indirizzo(cap, citofono, citta, civico, piazza, via)
        account = Account().aggiungiAccount(nome, cognome, dataDiNascita, email, numeroTelefonico, password, indirizzo)
        Logging().aggiungiLogging(account.idAccount)
        Logging().inserisciLoggingNelDatabase()
        Notifica().gestioneEmailDIRegistrazione(email, password)
        return account

    # Metodo di passaggio per la ricerca di un account
    def ricercaAccount(self, id):
        return Account().trovaOggettoTramiteId(id)

    # Metodo per la vendita di una lista di oggetti
    # return = dizionario con info di oggetti venduti
    def vendiProdotti(self, prodottoList):
        listaInfo = list()  # lista per scontrino
        for prodotto in prodottoList:
            Prodotto().spostaProdotto(prodotto.idProdotto, PathDatabase.inVenditaTxt, PathDatabase.vendutiTxt)
            listaInfo.append(Ricevuta().getInfoProdotto(prodotto))
        ricevuta = Ricevuta()
        ricevuta.aggiungiProdotti(listaInfo)
        ricevuta.salvaRicevuta()
        try:
            Notifica().gestioneEmailDiVendita(prodottoList)
        except:
            pass
        print(json.dumps(ricevuta.__dict__))
        return ricevuta

    # Metodo che recupera le statistiche sul sistema
    def visualizzaStatistiche(self):
        Statistiche().visualizzaStatistiche()

