import json
import os
import pickle
from types import SimpleNamespace


class File:


    #Costruttore della classe
    def __init__(self):
        pass


    #Metodo per la lettura di un dizionario su un file un file
    def leggi(self, fileName):
        with open(fileName, 'r') as in_file:
            letto = in_file.read()
        in_file.close()
        return letto


    #Metodo per la scrittura su un file
    def scrivi(self, fileName, contenuto):
        with open(fileName, 'w') as in_file:
            in_file.write(contenuto)
        in_file.close()


    #Metodo per la lettura du un oggetto arbirtario su un file
    def deserializza(self, fileName):
        data = None
        if os.path.getsize(fileName) > 0:
            with open(fileName, 'rb') as f:
                data = pickle.load(f)
        return data


    #Metodo per la scrittura du un oggetto arbirtario su un file
    def serializza(self, fileName, contenuto):
        with open(fileName, 'wb') as f:
            pickle.dump(contenuto, f, pickle.HIGHEST_PROTOCOL)


