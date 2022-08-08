from MVC.Model.SistemService.File import File




class Persona(object):
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

list = list()
list.append(Persona("leon", "ursu"))
list.append(Persona("patrizia", "giacovelli"))
fileName = "Database\Clienti\Clienti.txt"
file = File()
file.serializza(fileName, list)
list = file.deserializza(fileName)
print(list[0].nome)
print(list[1].nome)
