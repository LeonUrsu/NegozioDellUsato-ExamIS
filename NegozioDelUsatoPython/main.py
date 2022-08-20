import datetime
import inspect
import os
from pathlib import Path

from Database.PathDatabase import PathDatabase
from MVC.Model.SistemService.File import File

import pathlib

# impostare all'avvio del programma i path del sistema

PathDatabase().pathSetup(pathlib.Path().resolve())

#print(pathlib.Path(__file__).parent.resolve())






















"""class Persona(object):
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
"""
