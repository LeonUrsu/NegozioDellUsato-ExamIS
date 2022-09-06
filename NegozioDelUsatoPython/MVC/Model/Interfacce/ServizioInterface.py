class ServizioInterface:

    # Metodo Astratto da essere implementato nella clase che implementa l'interfaccia
    def newID(self):
        pass

    # Metodo Astratto da essere implementato nella clase che implementa l'interfaccia.
    # questo metodo crea un'istanza uguale all'istanza di partenza tramite la clonazione profonda
    # ciò restituisce un oggetto con un nuovo riferimeto
    def clone(self):
        pass


    # Metodo Astratto da essere implementato nella classe de implementa l'interfaccia
    # serve a recupera la lista degli oggetti all'interno del database
    def recuperaListaOggetti(self):
        pass

    # Metodo che salva la lista delgli oggetti passati nel file
    def salvaListaOggetti(self, lista):
        pass

    # Metodo Astratto da essere implementato nella classe che implementa l'interfaccia
    # questo metodo posiziona un oggetto su un file passato per argomento
    def mettiOggettoSuListaNelFile(self, fileName):
        pass