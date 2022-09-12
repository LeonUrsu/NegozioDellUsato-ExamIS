
from MVC.Model.Attività.Amministratore import Amministratore


for iter in range(3):
        acc = Amministratore().inserisciAccount("Regina", "Elisabetta", "21/04/1926",
                                          "regiElisabetta26@mail.com".__add__(iter.__str__()),
                                          "password", "0000000001", "62100", "Elisabetta", "Crathie", None, None,
                                          None)
print(acc)

