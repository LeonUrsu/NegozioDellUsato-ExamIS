

class Scaffale(DictionaryToPythonObject):


    # Costruttore della classe, create() in EA
    def __init__(self, ID, IDProdotti, posto):
        self.ID = ID
        self.IDProdotti = IDProdotti
        self.posto = posto
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File.deserializza(filename)
        scaffaliList.append(self)
        File.serializza(self, filename, scaffaliList)


    # Metodo che permette di clonare un'istanza della classe
    # return Scaffale
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    #Metodo che permette di eliminare uno scaffale salvato nel database
    #return valore booleano
    def deleteInDatabase(self, ID):
        filename = 'Database\Scaffali\Scaffali.txt'
        scaffaliList = File.deserializza(filename)
        for x in scaffaliList:
            if x.ID == ID:
                scaffaliList.pop(index(x))
        File.serializza(filename, scaffaliList)


    """
    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    #contenuto list
    #return dictionary
    def dictionaryEndcoder(self, contenuto):
        dict = json.dumps([self.__dict__ for self in contenuto])
        return dict


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    #contenuto dictionary
    #return list
    def dictionaryDecoder(self, contenuto):
        return [Test(x['var'], x['var2']) for x in letto]
    """