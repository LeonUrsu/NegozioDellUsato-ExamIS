import yagmail
from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account


class Notifica(object):

    # Costruttore della classe
    def __init__(self):
        pass


    # Metodo che invia al utente un email dove comunica la vendita del oggetto
    def gestioneEmailDIRegistrazione(self, email, password):
        filePath = PathDatabase.messaggioRegistrazioneProdotti
        testoEmail = self.emailGetFormat(filePath)
        frase = f"- email:{email}   -password:{password} "
        try:
            self.invioAlServerV2(email, "Negozio Del Usato", testoEmail + frase)
        except:
            pass



    # Metodo che invia al utente un email dove comunica la vendita del oggetto se la notifica non ha buon fine per un
    # cliente si salta questo clietne e si notifica i clienti successivi nella lista
    def gestioneEmailDiVendita(self, listProdottiVenduti):
        filePath = PathDatabase.messaggioVenditaProdotti
        testoEmail = self.emailGetFormat(filePath)
        listProprietari = Account().recuperaListaOggetti()
        for prodotto in listProdottiVenduti:
            for proprietario in listProprietari:
                if proprietario.idAccount == prodotto.idAccount:
                    frase = f"  euro:  {prodotto.prezzoCorrente} "
                    try:
                        self.invioAlServerV2(proprietario.email, "Negozio Del Usato", testoEmail + frase)
                    except: pass


    # Metodo che invia al utente un email dove comunica l'avvenuta eliminazione del prodotto
    def gestioneEmailDiEliminazione(self, prodotto):
        filePath = PathDatabase.messaggioEliminazioneProdotti
        testoEmail = self.emailGetFormat(filePath)
        proprietario = Account().trovaOggettoTramiteId(prodotto.idAccount)
        frase = f" Il prodotto {prodotto.nomeProdotto} : è eliminato/scaduto "
        try:
            self.invioAlServerV2(proprietario.email, "Negozio Del Usato" ,testoEmail + frase)
        except:
            pass


    # Metodo che prende il formato dell'email dal database in formato stringa
    def emailGetFormat(self, fileName):
        message = None
        with open(fileName, 'r') as t:
            message = t.read()
        t.close()
        return message


    """    # Metodo che invia il messaggio sull'email
    def invioAlServer(self, receiver_email, message):
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "proggetto.negozio.is@gmail.com"
        password = "UrsuLe0n!"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)"""

    # Metodo che invia il messaggio sull'email in versione aggionata
    def invioAlServerV2(self, receiver_email, subject, message, yag=None):
        yag = yagmail.SMTP('progetto.negozio.is@gmail.com', 'ktvfqnyjuicdpwsz')
        yag.send(receiver_email, subject, message)
        """contents = ['This is the body, and here is just text http://somedomain/image.png',
                    'You can find an audio file attached.', '/local/path/song.mp3']"""
