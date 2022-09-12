import copy
import json
from operator import index
from Database.PathDatabase import PathDatabase
from MVC.Model.Interfacce.ServizioInterface import ServizioInterface
from MVC.Model.SistemService.File import File


class Categoria(ServizioInterface):

    # Costruttore nullo
    def __init__(self):
        pass

    # Costruttore della Categoria, create() in EA
    def aggiungiCategoria(self, nome):
        self.idCategoria = self.newID()
        self.nome = nome
        self.oggettiTotali = 0
        self.creaInDatabase()


    # Metodo che permette di clonare un'istanza della classe
    # return Categoria
    def clone(self):
        deepCopy = copy.deepcopy(self)
        return deepCopy


    # Metodo che salva una categoria nel database
    def creaInDatabase(self):
        fileName = PathDatabase().categorieTxt
        listcategorie = Categoria().recuperaListaOggetti()
        listcategorie.append(self)
        File().serializza(fileName, listcategorie)

    # Metodo che permette di eliminare una categoria salvata nel database
    def deleteInDatabase(self, idCategoria):
        fileName = PathDatabase().categorieTxt
        listcategorie = self.recuperaListaOggetti()
        for x in listcategorie:
            if x.idCategoria == idCategoria:
                listcategorie.pop(index(x))
        file = File()
        file.serializza(fileName, listcategorie)

    # Metodo che serve per leggere la lista delle categorie all'interno del Database
    def recuperaListaOggetti(self):
        fileName = PathDatabase().categorieTxt
        file = File()
        listCategorie = file.deserializza(fileName)
        return listCategorie

    # Metodo per trovare una categoria tramite idCategoria
    def trovaCategoria(self, idCategoria):
        listCategorie = self.recuperaListaOggetti()
        for x in listCategorie:
            if x.idCategoria == idCategoria:
                return listCategorie.pop(index(x))
        return None

    # Metodo che ritorna il nuovo id da assegnare alla Categoria da inserire
    # return = nuovo ID per la Categoria
    def newID(self):
        fileName = PathDatabase().parametriTxt
        letto = File().leggi(fileName)
        dictLetto = json.loads(letto)
<<<<<<< HEAD
        newId = dictLetto['lastcodiceCategoria'] + 1
        dictLetto['lastcodiceCategoria'] = newId
=======
        newId = dictLetto['lastidCategoria'] + 1
        dictLetto['lastidCategoria'] = newId
>>>>>>> 5a97589bdcc387e34a15198dd5904d5ce27b5a74
        File().scrivi(fileName, json.dumps(dictLetto))
        return newId

    # Metodo che serve ad aggiornare la lista delle categorie, cerca la caegoria con il codiceVecchio
    # e diminuisce il numero di oggetti di quella categoria di uno, cerca la categoria nuova grazie al codiceNuovo
    # e al suo interno aumenta di uno il numero di oggetti presenti
    def aggiornaCategoriaProdotto(self, prodotto, codiceVecchio, codiceNuovo):
        fileName = PathDatabase().categorieTxt
        file = File()
        listCategorie = file.deserializza(fileName)
        for categoria in listCategorie:
            if categoria.idCategoria == codiceVecchio:
                categoria.oggettiTotali -= 1
        for categoria in listCategorie:
            if categoria.idCategoria == codiceNuovo:
                categoria.oggettiTotali += 1

    # Metodo che incrementa il numero di oggetti all'interno di una categoria
    def aggiungiProdottiInCategoria(self, prodotto):
        listCategorie = Categoria().recuperaListaOggetti()
        fileName = PathDatabase().categorieTxt
        for categoria in listCategorie:
<<<<<<< HEAD
            if categoria.idCategoria == prodotto.codiceCategoria:
=======
            if categoria.idCategoria == prodotto.idCategoria:
>>>>>>> 5a97589bdcc387e34a15198dd5904d5ce27b5a74
                categoria.oggettiTotali += 1
                File().serializza(fileName, listCategorie)
                return True
        return False

    # Metodo che decrementa il numero di oggetti all'interno di una categoria
    def diminuisciProdottiInCategoria(self, prodotto):
        listCategorie = Categoria().recuperaListaOggetti()
        for categoria in listCategorie:
            if categoria.idCategoria == prodotto.idCategoria:
                categoria.oggettiTotali -= 1
                return True
        return False
