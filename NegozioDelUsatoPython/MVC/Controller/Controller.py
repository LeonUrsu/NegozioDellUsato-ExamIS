from MVC.Model.Attività.Account import Account
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Attività.User import User
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Filtri import Filtri
from MVC.Model.SistemService.Statistiche import Statistiche


class Controller(object):

    def userLoginController(self, email, password):
        return User().login(email, password)

    def amministratoresaveProdottoBtn(self, nomeLe, idAccountLe, dataEsposizione, prezzoLe, idCategoriaLe,
                                      idScaffaleLe):
        return Amministratore().inserisciProdotto(idCategoriaLe, dataEsposizione, idAccountLe, nomeLe, prezzoLe,
                                                  idScaffaleLe)

    def recuperaListaProdottiInVendita(self):
        return Prodotto().recuperaListaProdottiInVendita()

    def saveCLienteBtnClicked(self, nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                              cittaLe, viaLe, piazzaLe, civicoLe, citofonoLe):
        return Amministratore().inserisciAccount(nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe,
                                                 capLe, citofonoLe, cittaLe, civicoLe, piazzaLe, viaLe)

    def recuperaListaAccounts(self):
        return Account().recuperaListaOggetti()

    def effettuaBackup(self):
        Amministratore().effettuaBackup()

    def trovaUltimeStatistiche(self):
        return Statistiche().trovaUltimeStatistiche()

    def trovaProdottoTramiteId(self, idProdotto):
        return Prodotto().trovaOggettoTramiteId(idProdotto)

    def trovaAccountTramiteId(self, idAccount):
        return Account().trovaOggettoTramiteId(idAccount)

    def eliminaProdottiTramiteListaId(self, listaId):
        Amministratore().eliminaProdottiTramiteListaId(listaId)

    def vendiProdottiTramiteListaId(self, listaId):
        Amministratore().vendiProdottiTramiteListaId(listaId)

    def eliminaAccountTramiteListaId(self, listaId):
        Amministratore().eliminaAccountTramiteListaId(listaId)

    def filtraDataEsposizione(self, start, stop, fileName):
        return Filtri().filtraDataEsposizione(start, stop, fileName)

    def filtraPrezzo(self, start, stop, fileName):
        return Filtri().filtraPrezzo(start, stop, fileName)

    def filtraClienti(self, nome, cognome):
        return Filtri().filtraClienti(nome, cognome)