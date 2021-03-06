import os
import pickle


class File:


    # Costruttore della classe
    def __init__(self):
        pass


    # Metodo per la lettura da un file
    def leggi(self, fileName):
        with open(fileName, 'r') as in_file:
            letto = in_file.read()
        in_file.close()
        return letto


    # Metodo per la scrittura su un file
    # filename = nome del file su cui scrivere
    # contenuto = il contenuto da essere scritto su un file
    def scrivi(self, fileName, contenuto):
        with open(fileName, 'w') as in_file:
            in_file.write(contenuto)
        in_file.close()


    # Metodo per la lettura di un oggetto di tipo arbirtario su un file
    # filename = nome del file da cui deserializzare
    def deserializza(self, fileName):
        data = None
        if os.path.getsize(fileName) > 0:
            with open(fileName, 'rb') as f:
                data = pickle.load(f)
        return data


    # Metodo per la scrittura di un oggetto di tipo arbirtario su un file
    # filename = nome del file su cui serializzare
    # contenuto = il contenuto da essere serializzato su un file
    def serializza(self, fileName, contenuto):
        with open(fileName, 'wb') as f:
            pickle.dump(contenuto, f, pickle.HIGHEST_PROTOCOL)


