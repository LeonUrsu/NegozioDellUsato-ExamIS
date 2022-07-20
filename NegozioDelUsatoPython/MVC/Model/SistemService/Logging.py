from datetime import datetime

class Logging():

    #Costruttore della classe
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.tentativi = 0
        self.prossimoTentativo = datetime.today()


    # Metodo che salva le credeniali di un utente su un file quando viene inserito nel sistema
    # newLog = parametro di tipo Logging
    # return = True if l'operazinone è andata bene
    def salvaLogging(self, newLog):
        fileName = 'Database\Logging\Logging.txt'
        listLogging = File.deserializza(fileName)
        if self.checkEmailUtente(listLogging, newLog.email):
            return False
        listLogging.append(newLog)
        return True


    # Metodo che gestisce il login di un utente
    # return valore booleano a seconda se il login è andato a buon fine
    def loging(self, email , password):
        fileName = 'Database\Logging\Logging.txt'
        listLogging = File.deserializza(fileName)
        today = datetime.today()
        for x in listLogging:
            if x.email == email:
                if x.password == password:
                   if self.verificaDettagliLogin(x):
                        return True
        return False


    #Metodo che verifica la validità dei dettagli del login
    # log = credenziali di accesso di tipo Logging
    # return = True if il login è valido
    def verificaDettagliLogin(self, log):
        if self.checkData(log) and self.checkTentativi(log):
            return True
        else:
            return False


    # Metodo per controllare se la data di accesso al profilo è valida oppure il profilo
    # risulta bloccato temporaneamente
    # log = credenziali di accesso di tipo Logging
    # return = True se la data è valida per effettuare un nuovo accesso
    def checkData(self, Log):
        if log.prossimoTentativo >= datetime.today():
            return False
        else:
            return True


    # Metodo per controllare se sono permessi altri tentativi di login
    # log = credenziali di accesso di tipo Logging
    # return = True if la soglia non è stata ancora raggiunta
    def checkTentativi(self, log):
        if Log.tentativi < 5:
            return True
        else:
            self.timeout()
            return False


    # Metodo per gestire il raggiungimento della soglia massima di tentativi permessi all'utente
    # log = credenziali di accesso di tipo Logging
    def timeout(self, log):
        log.prossimoTentativo = datetime.today() + timedelta(minutes=30)
        log.tentativi = 0


    # Metodo che controlla se sul file esiste un utente con lo stesso indirizzo email
    # per liminare l'inconsistenza dei dati
    # listLogging = lista di credenziali utente
    # email = email da verificare
    # return = True if esiste già l'email nel sistema
    def checkEmailUtente(self, listLogin, email):
        for x in listLogin:
            if x.email == email:
                return True
        return False