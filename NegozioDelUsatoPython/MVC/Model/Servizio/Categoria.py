import copy
from operator import index

from MVC.Model.SistemService import File


class Categoria(ServizioInterface):


    #Costruttore della Categoria, create() in EA
    def __init__(self, impattoCO2, nome, oggettiTotali):
        self.codiceCategoria = self.newID()
        self.impattoCO2 = impattoCO2
        self.nome = nome
        self.oggettiTotali = oggettiTotali


    # Metodo che permette di clonare un'istanza della classe
    # return Categoria
    def clone(self):
        deepCopy =  copy.deepcopy(self)
        return deepCopy


    # Metodo che permette di eliminare una categoria salvata nel database
    def deleteInDatabase(self, codiceCategoria):
        fileName = 'Database\Categorie\Categorie.txt'
        listcategorie = self.leggiCategorie(fileName)
        for x in listcategorie:
            if x.codiceCategoria == codiceCategoria:
                listcategorie.pop(index(x))
        File.serializza(fileName, listcategorie)


    # Metodo che serve per leggere la lista delle categorie all'interno del Database
    def leggiCategorie(self):
        fileName = 'Database\Categorie\Categorie.txt'
        listCategorie = File.deserializza(self, fileName)
        return listCategorie


    # Metodo per trovare una categoria tramite codiceCategoria
    def trovaCategoria(self, codiceCategoria):
        listCategorie = self.leggiCategorie(self)
        for x in listCategorie:
            if x.codiceCategoria == codiceCategoria:
                return listCategorie.pop(index(x))
        return None


    # Metodo che ritorna il nuovo id da assegnare alla Categoria da inserire
    # return = nuovo ID per la Categoria
    def newID(self):
        fileName = 'Databasa\parametri.txt'
        letto = File.deserializza(fileName)
        newID = letto['lastcodiceCategoria'] + 1
        letto['lastcodiceCategoria'] = newID
        File.serializza(fileName, letto)
        return newID
