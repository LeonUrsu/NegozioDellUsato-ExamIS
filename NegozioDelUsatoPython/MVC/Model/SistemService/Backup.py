import shutil
import tempfile
from shutil import copytree
from MVC.Model.SistemService.File import *

class Backup:

    def __init__(self):
        self.id = 0

    #Metodo che effettua il backup dei dati come impostato
    def effettuaBackup(self):
        from_path = 'Database/'
        to_path = 'BackupFiles/DatabaseBackup'
        self.eliminaCartella(to_path)
        copytree(from_path, to_path)


    #Metodo che elimina una cartella se esistente
    def eliminaCartella(self,pathName):
        if (os.path.exists(pathName)):
            tmp = tempfile.mktemp(dir=os.path.dirname(pathName))
            shutil.move(pathName, tmp)
            shutil.rmtree(tmp)
        #os.makedirs(pathName)


    #Metodo che copia i dati da Database a DatabaseBackup
    def copiaDati(self, from_path, to_path):
        copytree(from_path, to_path)


    #Metodo deprecato
    def pathControl(self, backupFileName):
        file = None
        temp = File()
        if os.path.exists(backupFileName):
            if os.path.getsize(backupFileName) > 0:
                file = temp.deserializza(backupFileName)
                return file
        file = Backup()
        with open(backupFileName, 'w') as bf:
            bf.close()
        return file
