import os
import shutil
import tempfile
from shutil import copytree

from Database.PathDatabase import PathDatabase
from MVC.Model.SistemService.File import File


class Backup(object):

    # Costruttore del metodo
    def __init__(self):
        pass

    # Metodo che quando richiamato effettua il backup dei dati e li copia nella cartella to_path
    def effettuaBackup(self):
        from_path = os.path.join(PathDatabase.mainDirPath, "Database")
        to_path = os.path.join(PathDatabase.mainDirPath, "BackupFiles")
        self.eliminaCartella(to_path)
        copytree(from_path, to_path)

    # Metodo che elimina una cartella se esistente
    def eliminaCartella(self, pathName):
        if os.path.exists(pathName):
            tmp = tempfile.mktemp(dir=os.path.dirname(pathName))
            shutil.move(pathName, tmp)
            shutil.rmtree(tmp)

    # Metodo che copia i dati da un percorso ad un altro
    # form_path = percorso copia
    # to_path = percorso incolla
    def copiaDati(self, from_path, to_path):
        copytree(from_path, to_path)

    # Metodo che controlla il path
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
