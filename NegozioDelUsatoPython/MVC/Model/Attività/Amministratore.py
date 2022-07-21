from MVC.Model.Servizio.Prodotto import Prodotto

class Amministratore:


    def aggiornaAccount(self):
        pass

    def aggiornaProdotto(self):
        pass

    def effettuaBackup(self):
        pass

    def eliminaAccount(self):
        pass

    def eliminaProdotto(self, id):
        Prodotto.spostaProdotto(self, id,"InVendita", "Eliminati")


    def filtraClienti(self):
        pass

    def inserisciProdotto(self):
        pass

    def ricercaAccount(self):
        pass

    def vendiProdotto(self):
        pass

    def visualizzaStatistiche(self):
        pass