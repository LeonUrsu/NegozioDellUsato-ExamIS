import json

class File:


    #Costruttore della classe
    def __init__(self):
        pass



    #Metodo per la lettura su un file
    def leggi(self, fileName):
        with open(fileName, 'r') as in_file:
            letto = in_file.read()
        return letto


    #Metodo per la scrittura su un file
    def scrivi(self, fileName, contenuto):
        with open(fileName, 'w') as in_file:
            in_file.write(contenuto)


    #Metodo per appendere su un file
    def appendi(self, fileName, contenuto):
        with open(fileName, 'a') as in_file:
            in_file.write(contenuto)