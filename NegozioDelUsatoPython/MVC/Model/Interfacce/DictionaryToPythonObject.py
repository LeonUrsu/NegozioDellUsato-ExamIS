

class JsonObjectToPythonObject:


    #Ogni classe che implementer√† questa interfaccia deve garantire di poter codificare
    #un oggetto della classe nel formato Dictionary impelementando questo metodo
    def dictionaryEncoder(self, contenuto):
        pass


    #Ogni classe che implementer√† questa interfaccia deve garantire di poter decodificare
    #un formato Dictionary in un oggetto della classe impelementando questo metodo
    def dictionaryDecoder(self, contenuto):
        pass