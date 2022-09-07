import os.path
import pathlib


class PathDatabase(object):

    def __init__(self):
        pass



    def setup(self, mainDirPath):
        #mainDirPath = pathlib.Path().resolve().__str__().replace("tests", "")
        """        if self.setupState == True: return
        else: PathDatabase.setupState = True"""
        PathDatabase.amministratoreTxt = os.path.join(mainDirPath, "Database", "Amministratore","Amministratore.txt")
        PathDatabase.categorieTxt = os.path.join(mainDirPath, "Database", "Categorie","Categorie.txt")
        PathDatabase.clientiTxt = os.path.join(mainDirPath, "Database", "Clienti","Clienti.txt")
        PathDatabase.loggingTxt = os.path.join(mainDirPath, "Database", "Logging","Logging.txt")
        PathDatabase.eliminatiTxt = os.path.join(mainDirPath, "Database", "Prodotti","Eliminati.txt")
        PathDatabase.inVenditaTxt = os.path.join(mainDirPath, "Database", "Prodotti","InVendita.txt")
        PathDatabase.scadutiTxt = os.path.join(mainDirPath, "Database", "Prodotti","Scaduti.txt")
        PathDatabase.vendutiTxt = os.path.join(mainDirPath, "Database", "Prodotti","Venduti.txt")
        PathDatabase.ricevuteTxt = os.path.join(mainDirPath, "Database", "Ricevute","Ricevute.txt")
        PathDatabase.scaffaliTxt = os.path.join(mainDirPath, "Database", "Scaffali","Scaffali.txt")
        PathDatabase.parametriTxt = os.path.join(mainDirPath, "Database", "parametri.txt")
        PathDatabase.statisticheTxt = os.path.join(mainDirPath, "Database", "Statistiche","Statistiche.txt")
        self.setupState = True

    mainDirPath = pathlib.Path().resolve()
    amministratoreTxt = os.path.join(mainDirPath, "Database", "Amministratore", "Amministratore.txt")
    categorieTxt = os.path.join(mainDirPath, "Database", "Categorie", "Categorie.txt")
    clientiTxt = os.path.join(mainDirPath, "Database", "Clienti", "Clienti.txt")
    loggingTxt = os.path.join(mainDirPath, "Database", "Logging", "Logging.txt")
    eliminatiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Eliminati.txt")
    #inVenditaTxt = os.path.join(mainDirPath, "Database", "Prodotti", "InVendita.txt")
    inVenditaTxt = "---"
    scadutiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Scaduti.txt")
    vendutiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Venduti.txt")
    ricevuteTxt = os.path.join(mainDirPath, "Database", "Ricevute", "Ricevute.txt")
    scaffaliTxt = os.path.join(mainDirPath, "Database", "Scaffali", "Scaffali.txt")
    parametriTxt = os.path.join(mainDirPath, "Database", "parametri.txt")
    statisticheTxt = os.path.join(mainDirPath, "Database", "Statistiche", "Statistiche.txt")