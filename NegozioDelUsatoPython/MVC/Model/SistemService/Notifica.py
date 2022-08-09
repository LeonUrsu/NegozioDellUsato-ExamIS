import smtplib, ssl

from MVC.Model.SistemService.File import File


class Notifica():

    # Costruttore della classe
    def __init__(self):
        pass


    # Metodo che invia al utente un email dove comunica la vendita del oggetto
    def gestioneEmailDIRegistrazione(self, email, password):
        filePath = "emailFormat\messaggioRegistrazione"
        testoEmail = self.emailGetFormat(filePath)
        #listClienti = File.deserializza("Database\Clienti\Clienti.txt")
        frase = f"- email:{email}   -password:{password} "
        try:
            self.invioAlServer(email, testoEmail + frase)
        except:
            pass


    # Metodo che invia al utente un email dove comunica la vendita del oggetto
    def gestioneEmailDiVendita(self, listProdottiVenduti):
        filePath = "emailFormat\messaggioVenditaProdotti"
        testoEmail = self.emailGetFormat(filePath)
        listProprietari = self.getListProprietari()
        for prodotto in listProdottiVenduti:
            for proprietario in listProprietari:
                if proprietario.idAccount == prodotto.idAccount:
                    frase = f"  euro:  {prodotto.prezzoCorrente} "
                    try:
                        self.invioAlServer(proprietario.email, testoEmail + frase)
                    except: pass


    # Metodo che invia al utente un email dove comunica l'avvenuta eliminazione del prodotto
    def gestioneEmailDiEliminazione(self, prodotto):
        filePath = "emailFormat\messaggioEliminazioneProdotti"
        testoEmail = self.emailGetFormat(filePath)
        idProprietario = prodotto.idAccount
        listProprietari = self.getListProprietari()
        for proprietario in listProprietari:
            if proprietario.idAccount == prodotto.idAccount:
                frase = f" Il prodotto {prodotto.nomeProdotto} : è eliminato/scaduto "
                try:
                    self.invioAlServer(proprietario.email, testoEmail + frase)
                except:
                    pass


    # Metodo che prende il formato dell'email dal database in formato stringa
    def emailGetFormat(self, fileName):
        message = None
        with open(fileName, 'r') as t:
            message = t.read()
        t.close()
        return message


    # Metodo che invia il messaggio sull'email
    def invioAlServer(self, receiver_email, message):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "my@gmail.com"  # Enter your address
        #receiver_email = "your@gmail.com"  # Enter receiver address
        password = "mypassword"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


    # Metodo che prende fi account dei Proprietari degli oprodotti
    def getListProprietari(self):
        pathProprietari = "Database\Clienti\Clienti.txt"
        listProprietari = File.deserializza(pathProprietari)
        return listProprietari


    # Metodo che prende la lista dei prodotti disponibili in vendita
    def getListProdotti(self):
        pathProdotti = "Database\Prodotti\InVendita.txt"
        listProdotti = File.deserializza(pathProdotti)
        return listProdotti