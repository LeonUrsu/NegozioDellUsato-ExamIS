import yagmail
from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.Servizio.Prodotto import Prodotto


class Notifica(object):

    # Costruttore della classe
    def __init__(self):
        pass

    # Metodo che invia al utente un email con le credenziali
    # al cliente e comunica l'avvenuta registrazione nel sistema
    def gestioneEmailDIRegistrazione(self, email, password):
        filePath = PathDatabase.messaggioRegistrazioneProdotti
        testoEmail = self.emailGetFormat(filePath)
        frase = f"- email: >{email}< - password: >{password}< "
        try:
            self.invioAlServerV2(email, "Negozio Del Usato", testoEmail + frase)
        except:
            print("Email non inviata")

    # Metodo che invia al utente un email dove comunica la vendita del oggetto se la notifica non ha buon fine per un
    # cliente si salta questo clietne e si notifica i clienti successivi nella lista
    def gestioneEmailDiVendita(self, listProdottiVenduti):
        filePath = PathDatabase.messaggioVenditaProdotti
        testoEmail = self.emailGetFormat(filePath)
        listProprietari = Account().recuperaListaOggetti()
        for prodotto in listProdottiVenduti:
            for proprietario in listProprietari:
                if proprietario.idAccount == prodotto.idAccount:
                    frase = f" nome Prodotto: {prodotto.nomeProdotto} a euro: {prodotto.prezzoCorrente} "
                    try:
                        self.invioAlServerV2(proprietario.email, "Negozio Del Usato", testoEmail + frase)
                    except:
                        print("Email non inviata")

    # Metodo che invia al utente un email dove comunica l'avvenuta eliminazione del prodotto
    def gestioneEmailDiEliminazione(self, idProdotto):
        filePath = PathDatabase.messaggioEliminazioneProdotti
        testoEmail = self.emailGetFormat(filePath)
        prodotto = Prodotto().trovaOggettoTramiteId(idProdotto)
        proprietario = Account().trovaOggettoTramiteId(prodotto.idAccount)
        frase = f" Il prodotto {prodotto.nomeProdotto} : è eliminato/scaduto "
        try:
            self.invioAlServerV2(proprietario.email, "Negozio Del Usato", testoEmail + frase)
        except:
            print("Email non inviata")

    # Metodo che prende il formato dell'email dal database in formato stringa
    def emailGetFormat(self, fileName):
        message = None
        with open(fileName, 'r') as t:
            message = t.read()
        t.close()
        return message

    # Metodo che invia il messaggio sull'email in versione aggionata
    def invioAlServerV2(self, receiver_email, subject, message, yag=None):
        yag = yagmail.SMTP('progetto.negozio.is@gmail.com', 'ktvfqnyjuicdpwsz')
        yag.send(receiver_email, subject, message)
