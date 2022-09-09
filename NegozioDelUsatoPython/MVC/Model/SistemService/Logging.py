from datetime import datetime, timedelta

from Database.PathDatabase import PathDatabase
from MVC.Model.Attività.Account import Account
from MVC.Model.SistemService.File import File


class Logging:
    accountLoggato = None

    # Costruttore della classe
    def __init__(self):
        pass

    def aggiungiLogging(self, idAccount):
        self.idAccount = idAccount
        self.tentativi = 0
        self.prossimoTentativo = datetime.today()

    # Metodo che salva le credeniali di un utente su un file quando viene inserito nel sistema
    # return = True if l'operazinone è andata bene
    def inserisciLoggingNelDatabase(self):
        fileName = PathDatabase().loggingTxt
        listLogging = File().deserializza(fileName)
        listLogging.append(self)
        File().serializza(fileName, listLogging)
        return True

    # Metodo che gestisce il login di un utente
    # return valore booleano a seconda se il login è andato a buon fine
    def login(self, email, password):
        account = Account().trovaOggettoTramiteEmail(email)
        if email == "admin":
            return self.loginAdmin(password)
        if account == None:
            return None
        log = self.trovaLogin(account.idAccount)
        if log != None:
            if self.verificaDettagliLogin(log):
                pass
            else:
                return None
            if self.checkPassword(password, account):
                pass
            else:
                return None
        else:
            return None
        self.accountLoggato = account
        return account


    # Metodo per effettuare il logout
    def logout(self):
        self.accountLoggato = None
        return True

    # Metodo che verifica se un utente si è mai loggato
    def trovaLogin(self, account):
        fileName = PathDatabase().loggingTxt
        listLogging = File().deserializza(fileName)
        for logging in listLogging:
            if logging.idAccount == account.idAccount:
                return logging
        return None

    # Metodo che verifica la validità dei dettagli del login
    # log = credenziali di accesso di tipo Logging
    # return = True if il login è valido
    def verificaDettagliLogin(self, log):
        if self.checkData(log) and self.checkTentativi(log):
            return True
        else:
            return False

    # Metodo che controlla se la password inserita corrisponde alla password dell'utente
    def checkPassword(self, password, account):
        if password == account.password:
            return True
        return False

    # Metodo per controllare se la data di accesso al profilo è valida oppure il profilo
    # risulta bloccato temporaneamente
    # log = credenziali di accesso di tipo Logging
    # return = True se la data è valida per effettuare un nuovo accesso
    def checkData(self, log):
        if log.prossimoTentativo >= datetime.today():
            return False
        else:
            return True

    # Metodo per controllare se sono permessi altri tentativi di login
    # log = credenziali di accesso di tipo Logging
    # return = True if la soglia non è stata ancora raggiunta
    def checkTentativi(self, log):
        if log.tentativi < 5:
            return True
        else:
            self.timeout(log)
            return False

    # Metodo per gestire il raggiungimento della soglia massima di tentativi permessi all'utente
    # log = credenziali di accesso di tipo Logging
    def timeout(self, log):
        log.prossimoTentativo = datetime.today() + timedelta(minutes=30)
        log.tentativi = 0

    # metodo per loggare l'amministratore
    def loginAdmin(self, password):
        fileName = PathDatabase().amministratoreTxt
        admin = File().deserializza(fileName)
        if admin.password == password:
            return True
        return False


