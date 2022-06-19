

#Classe per la gestione di una ricevuta
class Ricevuta:


    # Costruttore della classe, create() in EA
    def __init__(self):
        datetime = None
        prodotti = None


    #Metodo per aggiungere i valori all'istanza creata della classe
    def aggiungiRicevuta(self, datetime, prodotti ):
        date_format = '%d/%m/%Y'
        today = date.today()
        self.datetime = today.strftime(date_format)
        self.prodotti = prodotti




    #Metodo che permette di clonare un'istanza della classe
    #return Ricevuta
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    #metodo per emettere una ricevuta al cliente che acquista un prodotto
    # propabilmente sarà implementata come una schermata che appare con la lista degli oggetti
    def emettiRicevuta(self):
        fileName = 'Database\Ricevute\Ricevute.txt'
        ricevuteList = File.deserializza(filename)
        ricevuteList.append(self)
        File.serializza(self, filename, List)
        return dictionaryEncoder(ricevuteList)


    # metodo overiding dell'interfaccia JsonObjectToPythonObject
    # contenuto list
    # return dictionary
    def dictionaryEndcoder(self, contenuto):
        dict = json.dumps([self.__dict__ for self in contenuto])
        return dict