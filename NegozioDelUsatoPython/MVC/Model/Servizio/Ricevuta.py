

# Classe per la gestione di una ricevuta
class Ricevuta(ServizioInterface):


    # Costruttore della classe, create() in EA
    def __init__(self,prodotti ):
        date_format = '%d/%m/%Y'
        today = date.today()
        self.ID = newID()
        self.datetime = today.strftime(date_format)
        self.prodotti = prodotti


    # Metodo che permette di clonare un'istanza della classe
    # return Ricevuta
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    # Metodo per emettere una ricevuta al cliente che acquista un prodotto
    # propabilmente sarà implementata come una schermata che appare con la lista degli oggetti
    def emettiRicevuta(self):
        fileName = 'Database\Ricevute\Ricevute.txt'
        ricevuteList = File.deserializza(filename)
        ricevuteList.append(self)
        salvaRicevute(ricevuteList)
        return dictionaryEncoder(ricevuteList)


    # metodo overiding dell'interfaccia JsonObjectToPythonObject
    # contenuto list
    # return dictionary
    def dictionaryEndcoder(self, contenuto):
        dict = json.dumps([self.__dict__ for self in contenuto])
        return dict


    # Medoto che prende una lsita di ricevute e le salva su un file
    def salvaRicevute(self, listRicevute):
        fileName = 'Database\Ricevute\Ricevute.txt'
        File.serializza(fileName, listRicevute)


    # Metodo che legge un file serializzato e deserializza le ricevute dal file
    def leggiRicevute(self):
        fileName = 'Database\Ricevute\Ricevute.txt'
        listRicevute = File.deserializza(fileName)
        return listRicevute


    # Metodo che ritorna il nuovo id da assegnare alla Ricevuta da inserire
    # return = nuovo ID per la Ricevuta
    def newID(self):
        fileName = 'Databasa\parametri.txt'
        letto = File.leggi(fileName)
        dictLetto = letto.__dict__
        newID = dictLetto['lastIDRicevuta'] + 1
        dictLetto['lastIDRicevuta'] = newID
        File.scrivi(fileName, dictLetto.__str__)
        return newID