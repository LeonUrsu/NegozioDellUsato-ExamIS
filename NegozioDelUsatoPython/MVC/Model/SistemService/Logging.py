

class Logging():

    def __init__(self):
        pass

    # Metodo che prende
    def aggiungiLogging(self, email, password):
        self.email = email
        self.password = password


    # Metodo che salva le credeniali di Logging su un file
    def salvaLogging(self, newLog):
        fileName = 'Database\Logging\Logging.txt'
        listLogging = File.deserializza(fileName)
        listLogging.append(newLog)


    # Metodo che gestisce il login di un utente
    # return valore booleano a seconda se il login è andato a buon fine
    def loging(self, email, password):
        fileName = 'Database\Logging\Logging.txt'
        listLogging = File.deserializza(fileName)
        for x in listLogging:
            if x.email == email:
                if x.password == password:
                    return True
                else:
                    return False
        return False

