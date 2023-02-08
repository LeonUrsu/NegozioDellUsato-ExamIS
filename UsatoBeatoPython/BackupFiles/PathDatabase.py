import os.path
import pathlib
import sys


class PathDatabase(object):

    def __init__(self):
        pat = sys.argv[0]
        pat = os.path.dirname(pat)
        self.setup(pat)


    def setup(self, mainDirPath):
        self.mainDirPath = mainDirPath
        PathDatabase.mainDirPath = mainDirPath
        PathDatabase.amministratoreTxt = os.path.join(mainDirPath, "Database", "Amministratore", "Amministratore.txt")
        PathDatabase.categorieTxt = os.path.join(mainDirPath, "Database", "Categorie", "Categorie.txt")
        PathDatabase.accountTxt = os.path.join(mainDirPath, "Database", "Account", "Account.txt")
        PathDatabase.loggingTxt = os.path.join(mainDirPath, "Database", "Logging", "Logging.txt")
        PathDatabase.eliminatiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Eliminati.txt")
        PathDatabase.inVenditaTxt = os.path.join(mainDirPath, "Database", "Prodotti", "InVendita.txt")
        PathDatabase.scadutiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Scaduti.txt")
        PathDatabase.vendutiTxt = os.path.join(mainDirPath, "Database", "Prodotti", "Venduti.txt")
        PathDatabase.ricevuteTxt = os.path.join(mainDirPath, "Database", "Ricevute", "Ricevute.txt")
        PathDatabase.scaffaliTxt = os.path.join(mainDirPath, "Database", "Scaffali", "Scaffali.txt")
        PathDatabase.parametriTxt = os.path.join(mainDirPath, "Database", "parametri.txt")
        PathDatabase.statisticheTxt = os.path.join(mainDirPath, "Database", "Statistiche", "Statistiche.txt")
        PathDatabase.messaggioEliminazioneProdotti = os.path.join(mainDirPath, "Database", "emailFormat",
                                                                  "messaggioEliminazioneProdotti.txt")
        PathDatabase.messaggioRegistrazioneProdotti = os.path.join(mainDirPath, "Database", "emailFormat",
                                                                   "messaggioRegistrazione.txt")
        PathDatabase.messaggioVenditaProdotti = os.path.join(mainDirPath, "Database", "emailFormat",
                                                             "messaggioVenditaProdotti.txt")

    """
    def resetDatabase(self, mainDirPath):
        self.setup(mainDirPath)
        obj = PathDatabase()
        members = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
        for name in members:
            if name == "parametriTxt":
                self.scrivi(os.path.join(mainDirPath, "Database", "parametri.txt"),
                            str({"lastIdProdotto": 0, "lastIdRicevuta": 0, "lastIdAccount": 0, "lastidCategoria": 0,
                                 "lastIdScaffale": 0}))
                print(f"parametri.txt resettato")
            else:
                attribut = getattr(other, name)
                self.scrivi(obj.attribut, "")
                print(f"{name} - cancellato")
        # getattr(other, "name_of_variable")

    def scrivi(self, fileName, contenuto):
        with open(fileName, 'w') as in_file:
            in_file.write(contenuto)
        in_file.close()
    """