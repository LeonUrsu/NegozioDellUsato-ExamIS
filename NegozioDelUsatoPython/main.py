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
class Test():
    def __init__(self, var,var2):
        self.var = var
        self.var2 = var2


    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def dictionaryEncoder(self, contenuto):
        json_string = json.dumps([self.__dict__ for self in contenuto])
        return json_string

    #metodo overiding dell'interfaccia JsonObjectToPythonObject
    def dictionaryDecoder(self, letto):

        return [Test(x['var'], x['var2']) for x in letto]




""""
filename = 'testo.txt'
test1 = Test(1, 11)
test2 = Test(2, 22)
test3 = Test(3, 33)
test4 = Test(4, 44)
liste = list()
liste.append(test1)
liste.append(test2)
liste.append(test3)
liste.append(test4)
print(liste)
translated = Test.DictionaryEncoder(Test,liste)
print(translated)
#File.scrivi(File, filename, translated)
#letto = File.leggi(File, filename)
print(dictionaryDecoder(Test, json.loads(translated)))



with open(filename, 'wb') as f:
    pickle.dump(liste, f, pickle.HIGHEST_PROTOCOL)
with open(filename, 'rb') as f:
    data = pickle.load(f)
print(data)


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
