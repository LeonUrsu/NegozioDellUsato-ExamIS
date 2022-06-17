import json
import pickle
import time
from collections import namedtuple
from types import SimpleNamespace

from MVC.Model.Interfacce.DictionaryToPythonObject import JsonObjectToPythonObject
from MVC.Model.SistemService.File import File



# This is a sample Python script.
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Test(JsonObjectToPythonObject):
    def __init__(self, var):
        self.var = var

    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def DictionaryEndcoder(self, contenuto):
        json_string = json.dumps([self.__dict__ for self in contenuto])
        return json_string

    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def DictionaryDecoder(self, letto):
        pyLetto = json.loads(letto, object_hook=lambda d: SimpleNamespace(**d))
        return pyLetto


"""
filename = 'testo.txt'
test1 = Test(1)
test2 = Test(2)
lista =list()
lista.append(test1)
lista.append(test2)
tradotto = Test.DictionaryEndcoder(Test,lista)
File.scrivi(File, filename, tradotto)
time.sleep(2)
letto = File.leggi(File,filename)
decodificato = Test.DictionaryDecoder(Test,letto)
print(decodificato[0].var)
"""










"""
print('-------------------------')

testArray = list()
testArray.append(test1)
testArray.append(test2)
file = File()
fileName = 'testo.txt'
json_string = json.dumps([ob.__dict__ for ob in testArray])
print(json_string)
x = json.loads(json_string, object_hook =
               lambda d : namedtuple('X', d.keys())
               (*d.values()))
               #stringa = file.leggi('testo.txt')
#dict = {'nome' : 'Leon', 'Cognome' : 'ursu'}
print(x[0]
print('-------------------------')


print('-------------------------')
fileName = 'testo.txt'
test1 = Test(1,3)
test2 = Test(2,4)
file = File()
lista = list()
lista.append(test1)
lista.append(test2)
json_string = json.dumps([test1.__dict__ for test1 in lista])
print(json_string)
lista2 = json.dumps(json_string)

from types import SimpleNamespace

x.append(vars(Test(9,9)))
print(x)


file.scrivi('testo.txt', dict.__str__())
dict2 = file.leggi('testo.txt')
print(dict2)
print('-------------------------')
"""
