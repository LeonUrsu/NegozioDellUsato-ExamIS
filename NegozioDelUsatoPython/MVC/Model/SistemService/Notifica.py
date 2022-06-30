import smtplib, ssl

from MVC.Model.SistemService.File import File


class Notifica():


    def __init__(self, receiver_email, message):
        todo


    def gestioneEmailDIRegistrazione(self):
        filePath = "emailFormat\messaggioRegistrazione"
        testoEmail = self.emailFormat(filePath)
        todo



    def gestioneEmailDiVendita(self, listProdottiVenduti):
        filePath = "emailFormat\messaggioVenditaProdotti"
        testoEmail = self.emailFormat(filePath)
        listProprietari = self.getListProprietari()
        for prodotto in listProdottiVenduti:
            for proprietario in listProprietari:
                if proprietario.idAccount == prodotto.idAccount:
                    frase = f"  euro:  {prodotto.prezzoCorrente} "
                    try:
                        self.invioAlServer(proprietario.email, testoEmail.append(prodotto.prezzoCorrente))
                    except: pass


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
        password = ""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


    # Metodo che prende fi account dei Proprietari degli oprodotti
    def getListProprietari(self):
        pathProprietari = "Database\Clienti\Clienti.txt"
        listProprietari = File.deserializza(pathProprietari)
        return listProprietari