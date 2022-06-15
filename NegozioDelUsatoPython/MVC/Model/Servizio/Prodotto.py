import datetime


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


    #Metodo per clonare la classe per un backpu dei dati
    def clone(self):
        todo

    #Distruttore della classe, destroy() in EA
    def __del__(self):
        pass

    #Metodo che entra in azione quanado l'oggetto matura un determinato tempo di esistenza nel
    #negozio e viene applicato dolo agli oggetti che sono esposti alla vendita
    #athribute
    #return boolean
    def scontaProdotto(self):