import json
import os.path
import sys


class PathDatabase(object):

    def __init__(self):
        self.setup()

    def setup(self):
        mainPath = sys.argv[0]
        mainDirPath = os.path.dirname(mainPath)
        self.mainDirPath = mainDirPath
        self.amministratoreTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database",
                                              "Amministratore", "Amministratore.txt")
        self.categorieTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Categorie",
                                         "Categorie.txt")
        self.accountTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Account",
                                       "Account.txt")
        self.loggingTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Logging",
                                       "Logging.txt")
        self.eliminatiTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Prodotti",
                                         "Eliminati.txt")
        self.inVenditaTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Prodotti",
                                         "InVendita.txt")
        self.scadutiTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Prodotti",
                                       "Scaduti.txt")
        self.vendutiTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Prodotti",
                                       "Venduti.txt")
        self.ricevuteTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Ricevute",
                                        "Ricevute.txt")
        self.scaffaliTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Scaffali",
                                        "Scaffali.txt")
        self.parametriTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "parametri.txt")
        self.statisticheTxt = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database", "Statistiche",
                                           "Statistiche.txt")
        self.messaggioEliminazioneProdotti = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database",
                                                          "emailFormat",
                                                          "messaggioEliminazioneProdotti.txt")
        self.messaggioRegistrazioneProdotti = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database",
                                                           "emailFormat",
                                                           "messaggioRegistrazione.txt")
        self.messaggioVenditaProdotti = os.path.join(mainDirPath, "resourcesForUsatoBeato", "Database",
                                                     "emailFormat",
                                                     "messaggioVenditaProdotti.txt")

    def resetDatabase(self):
        with open(self.categorieTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.accountTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.loggingTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.eliminatiTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.inVenditaTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.scadutiTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.scadutiTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.scadutiTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.vendutiTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.ricevuteTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        with open(self.scaffaliTxt, 'r+') as file:
            file.truncate(0)
        file.close()
        di = {"lastIdProdotto": 0, "lastIdRicevuta": 0, "lastIdAccount": '0', "lastidCategoria": 0, "lastIdScaffale": 0}
        self.scrivi(self.parametriTxt, json.dumps(di))


    def scrivi(self, fileName, contenuto):
        with open(fileName, 'w') as in_file:
            in_file.write(contenuto)
        in_file.close()
