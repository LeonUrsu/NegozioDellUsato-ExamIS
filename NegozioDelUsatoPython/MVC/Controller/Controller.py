from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Attività.User import User
from MVC.Model.Servizio.Prodotto import Prodotto


class Controller(object):


    def userLoginController(self, email, password):
        return User().login(email, password)

    def amministratoresaveProdottoBtn(self, nomeLe, idAccountLe, dataEsposizione, prezzoLe, idCategoriaLe, idScaffaleLe):
        return Amministratore().inserisciProdotto(idCategoriaLe, dataEsposizione, idAccountLe, nomeLe, prezzoLe, idScaffaleLe)

    def recuperaListaProdottiInVendita(self):
        return Prodotto().recuperaListaProdottiInVendita()