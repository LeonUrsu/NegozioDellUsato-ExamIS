

class Categoria:


    #Costruttore della Categoria, create() in EA
    def __init__(self):
        self.codiceCategoria = None
        self.impattoCO2 = None
        self.nome = None
        self.oggettiTotali = None

    #Metodo per aggiungere i valori alla categoria da creare
    def aggiungiCategoria(self, codiceCategoria, impattoCO2, nome, oggettiTotali)
        self.codiceCategoria = codiceCategoria
        self.impattoCO2 = impattoCO2
        self.nome = nome
        self.oggettiTotali = oggettiTotali


    #Distruttore della classe, destroy() in EA
    def __del__(self):
        todo
        return

    
    # Metodo che permette di clonare un'istanza della classe
    # return Categoria
    def clone(self):
        categoria = Categoria()
        categoria.codiceCategoria = self.codiceCategoria
        categoria.impattoCO2 = self.impattoCO2
        categoria.nome = self.nome
        categoria.oggettiTotali = self.oggettiTotali
        return categoria


    #Metodo che permette di eliminare una categoria salvata nel database
    def deleteInDatabase(self):
        todo
        return


    #Metodo che permette di salvare una categoria nel database
    def createInDatabase(self):
        todo
        return