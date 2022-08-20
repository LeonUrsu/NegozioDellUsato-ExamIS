import pathlib


class PathDatabase(object):

    def __init__(self):
        pass



    def pathSetup(self, mainDirPath):
        mainDirPath = str(mainDirPath) + "\\"
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
    amministratoreTxt = "Database\Amministratore\Amministratore.txt"
    #Categorie__________________________________________
    categorieTxt = "Database\Categorie\Categorie.txt"
    #Clienti__________________________________________
    clientiTxt = "Database\Clienti\Clienti.txt"
    # Logging__________________________________________
    loggingTxt = "Database\Logging\Logging.txt"
    # Prodotti__________________________________________
    eliminatiTxt = "Database\Prodotti\Eliminati.txt"
    inVenditaTxt = "Database\Prodotti\InVendita.txt"
    scadutiTxt = "Database\Prodotti\Scaduti.txt"
    vendutiTxt = "Database\Prodotti\Venduti.txt"
    # Ricevute__________________________________________
    ricevuteTxt = "Database\Ricevute\Ricevute.txt"
    # Scaffali__________________________________________
    scaffaliTxt = "Database\Scaffali\Scaffali.txt"
    # Parametri__________________________________________
    parametriTxt = "Database\parametri.txt"
    # statistiche_____________________________________
    statisticheTxt = "Database\Statistiche\Statistiche.txt"

