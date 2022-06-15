import datetime

#CLasse Prodotto che rappresenta il prodotto con le sue caratteristiche che verrà esposto nel negozio
class Prodotto:


    #Costruttore della classe, create() in EA
    def __init__(self):
        self.codiceCategoria = None
        self.dataEsposizione = datetime.datetime(year = None, month = None, day = None)
        self.dataScadenza = datetime.datetime(year = None, month = None, day = None)
        self.IDAccount = None
        self.IDProdotto = None
        self.nomeProdotto = None
        self.prezzoCorrente = None
        self.prezzoOriginale = None
        self.statoDiVendita = None


    #Distruttore della classe, destroy() in EA
    def __del__(self):
        todo


    #Metodo che permette di clonare un'istanza della classe
    #return Prodotto
    def clone(self):
        todo


    #Metodo che entra in azione quanado l'oggetto matura un determinato tempo di esistenza nel
    #negozio e viene applicato dolo agli oggetti che sono esposti alla vendita
    #return valore booleano
    def scontaProdotto(self):
        todo


    #Metodo che sposta un determinato prodotto all'interno della memoria quando il suo stato è in cambiamento
    #return valore booleano
    def spostaProdotto(self):
        todo


    #Metodo che permette la vendita di un prodotto, lo stato dell'oggetto passa a venduto e viene spostato
    #dove vendono archviati tutti gli oggetti venduti nel database
    #return valore booleano
    def vendiProdotto(self):
        todo