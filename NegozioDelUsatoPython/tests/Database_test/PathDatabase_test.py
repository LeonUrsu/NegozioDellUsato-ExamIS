import pathlib


class PathDatabase(object):

    def __init__(self):
        pass



    def setup(self, mainDirPath):
        mainDirPath = str(mainDirPath)
        PathDatabase.amministratoreTxt = mainDirPath + self.amministratoreTxt
        PathDatabase.categorieTxt = mainDirPath + self.categorieTxt
        PathDatabase.clientiTxt = mainDirPath + self.clientiTxt
        PathDatabase.loggingTxt = mainDirPath + self.loggingTxt
        PathDatabase.eliminatiTxt = mainDirPath + self.eliminatiTxt
        PathDatabase.inVenditaTxt = mainDirPath + self.inVenditaTxt
        PathDatabase.scadutiTxt = mainDirPath + self.scadutiTxt
        PathDatabase.vendutiTxt = mainDirPath + self.vendutiTxt
        PathDatabase.ricevuteTxt = mainDirPath + self.ricevuteTxt
        PathDatabase.scaffaliTxt = mainDirPath + self.scaffaliTxt
        PathDatabase.parametriTxt = mainDirPath + self.parametriTxt
        PathDatabase.statisticheTxt = mainDirPath + self.statisticheTxt


    #Amministratore__________________________________________
    amministratoreTxt = "Database_test\Amministratore\Amministratore.txt"
    #Categorie__________________________________________
    categorieTxt = "Database_test\Categorie\Categorie.txt"
    #Clienti__________________________________________
    clientiTxt = "Database_test\Clienti\Clienti.txt"
    # Logging__________________________________________
    loggingTxt = "Database_test\Logging\Logging.txt"
    # Prodotti__________________________________________
    eliminatiTxt = "Database_test\Prodotti\Eliminati.txt"
    inVenditaTxt = "Database_test\Prodotti\InVendita.txt"
    scadutiTxt = "Database_test\Prodotti\Scaduti.txt"
    vendutiTxt = "Database_test\Prodotti\Venduti.txt"
    # Ricevute__________________________________________
    ricevuteTxt = "Database_test\Ricevute\Ricevute.txt"
    # Scaffali__________________________________________
    scaffaliTxt = "Database_test\Scaffali\Scaffali.txt"
    # Parametri__________________________________________
    parametriTxt = "Database_test\parametri.txt"
    # statistiche_____________________________________
    statisticheTxt = "Database_test\Statistiche\Statistiche.txt"

