import json
import pickle
import time
from collections import namedtuple

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
class Test:
    def __init__(self, var):
        self.var = var


print('-------------------------')
test1 = Test(1)
test2 = Test(2)
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
print(x[0]

print('-------------------------')


"""
print('-------------------------')
file = File()
#stringa = file.leggi('testo.txt')
dict = {'nome' : 'Leon', 'Cognome' : 'ursu'}
file.scrivi('testo.txt', dict.__str__())
dict2 = file.leggi('testo.txt')
print(dict2)
print('-------------------------')

"""