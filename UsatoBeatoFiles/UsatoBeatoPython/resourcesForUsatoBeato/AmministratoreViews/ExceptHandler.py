from PySide6.QtWidgets import QMessageBox

class ExceptHandler():

    #METODO CHE RESITUISCE UNA FINESTRA DI DIALOGO DI ERRORE IN CASO SI CREI UN NUOVO ADMIN
    def erroreCreazioneAdmin(self):
        error_message = "IMPOSSIBILE CREARE UN NUOVO ADMIN!"
        QMessageBox.critical(None, "Errore grave", error_message, QMessageBox.Ok)

    def erroreAutenticazione(self):
        error_message = "CREDENZIALI ERRATE"
        QMessageBox.critical(None, "Errore grave", error_message, QMessageBox.Ok)

    def erroreTimeoutAutenticazione(self):
        error_message = "TENTATIVI DI LOGIN ESAURITI ASPETTA 30 MINUTI"
        QMessageBox.critical(None, "Errore grave", error_message, QMessageBox.Ok)