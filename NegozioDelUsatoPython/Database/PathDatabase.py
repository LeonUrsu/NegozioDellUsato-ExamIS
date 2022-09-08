import os.path
import pathlib


class PathDatabase(object):

    def __init__(self):
        pass

    def setup(self, mainDirPath):
        PathDatabase.amministratoreTxt = os.path.join(mainDirPath, "Database", "Amministratore", "Amministratore.txt")
        PathDatabase.categorieTxt = os.path.join(mainDirPath, "Database", "Categorie", "Categorie.txt")
        PathDatabase.clientiTxt = os.path.join(mainDirPath, "Database", "Clienti", "Clienti.txt")
        PathDatabase.loggingTxt = os.path.join(mainDirPath, "Database", "Logging", "Logging.txt")
        PathDatabase.eliminatiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Eliminati.txt")
        PathDatabase.inVenditaTxt = os.path.join(mainDirPath, "Database", "Prodotti", "InVendita.txt")
        PathDatabase.scadutiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Scaduti.txt")
        PathDatabase.vendutiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Venduti.txt")
        PathDatabase.ricevuteTxt = os.path.join(mainDirPath, "Database", "Ricevute", "Ricevute.txt")
        PathDatabase.scaffaliTxt = os.path.join(mainDirPath, "Database", "Scaffali", "Scaffali.txt")
        PathDatabase.parametriTxt = os.path.join(mainDirPath, "Database", "parametri.txt")
        PathDatabase.statisticheTxt = os.path.join(mainDirPath, "Database", "Statistiche", "Statistiche.txt")
        PathDatabase.messaggioEliminazioneProdotti = os.path.join(mainDirPath, "Database", "emailFormat", "messaggioEliminazioneProdotti.txt")
        PathDatabase.messaggioRegistrazioneProdotti = os.path.join(mainDirPath, "Database", "emailFormat", "messaggioRegistrazione.txt")
        PathDatabase.messaggioVenditaProdotti = os.path.join(mainDirPath, "Database", "emailFormat", "messaggioVenditaProdotti.txt")




    mainDirPath = pathlib.Path().resolve()
    amministratoreTxt = ""
    categorieTxt = ""
    clientiTxt = ""
    loggingTxt = ""
    eliminatiTxt = ""
    inVenditaTxt = ""
    scadutiTxt = ""
    vendutiTxt = ""
    ricevuteTxt = ""
    scaffaliTxt = ""
    parametriTxt = ""
    statisticheTxt = ""
    messaggioEliminazioneProdotti = ""
    messaggioRegistrazioneProdotti = ""
    messaggioVenditaProdotti = ""