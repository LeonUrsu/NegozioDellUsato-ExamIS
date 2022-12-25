from MVC.Model.Attività.Account import Account
from MVC.Model.Attività.Amministratore import Amministratore
from MVC.Model.Attività.Indirizzo import Indirizzo
from MVC.Model.Attività.User import User
from MVC.Model.Servizio.Categoria import Categoria
from MVC.Model.Servizio.Prodotto import Prodotto
from MVC.Model.SistemService.Filtri import Filtri
from MVC.Model.SistemService.Logging import Logging
from MVC.Model.SistemService.Statistiche import Statistiche


class Controller(object):

    def userLoginController(self, email, password):
        ret = None
        try:
            ret = User().login(email, password)
        except:
            pass
        return ret

    def amministratoresaveProdottoBtn(self, dataEsposizione, idAccount,
                                      nomeProdotto, prezzoOriginale, nomeScaffaleLe, nomeCategoria):
        ret = None
        try:
            ret = Amministratore().inserisciProdotto(dataEsposizione, idAccount, nomeProdotto, prezzoOriginale,
                                                     nomeScaffaleLe, nomeCategoria)
        except:
            pass

        return ret

    def recuperaListaProdottiInVendita(self):
        ret = None
        try:
            ret = Prodotto().recuperaListaProdottiInVendita()
        except:
            pass
        return ret

    def saveCLienteBtnClicked(self, nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe, capLe,
                              cittaLe, viaLe, piazzaLe, civicoLe, citofonoLe):
        ret = None
        try:
            ret = Amministratore().inserisciAccount(nomeLe, cognomeLe, dataNascitaLe, emailLe, passwordLe, telefonoLe,
                                                    capLe, citofonoLe, cittaLe, civicoLe, piazzaLe, viaLe)
        except:
            pass
        return ret

    def recuperaListaAccounts(self):
        ret = None
        try:
            ret = Account().recuperaListaOggetti()
        except:
            pass
        return ret

    def effettuaBackup(self):
        ret = None
        try:
            Amministratore().effettuaBackup()
        except:
            pass

    def trovaUltimeStatistiche(self):
        ret = None
        try:
            ret = Statistiche().trovaUltimeStatistiche()
        except:
            pass
        return ret

    def trovaProdottoTramiteId(self, idProdotto):
        ret = None
        try:
            ret = Prodotto().trovaOggettoTramiteId(idProdotto)
        except:
            pass
        return ret

    def trovaAccountTramiteId(self, idAccount):
        ret = None
        try:
            ret = Account().trovaOggettoTramiteId(idAccount)
        except:
            pass
        return ret

    def eliminaProdottiTramiteListaId(self, listaId):
        ret = None
        try:
            Amministratore().eliminaProdottiTramiteListaId(listaId)
        except:
            pass

    def vendiProdottiTramiteListaId(self, listaId):
        ret = None
        try:
            ret = Amministratore().vendiProdottiTramiteListaId(listaId)
        except:
            pass
        return ret

    def eliminaAccountTramiteListaId(self, listaId):
        ret = None
        try:
            Amministratore().eliminaAccountTramiteListaId(listaId)
        except:
            pass

    def filtraDataEsposizione(self, start, stop, fileName):
        ret = None
        try:
            ret = Filtri().filtraDataEsposizione(start, stop, fileName)
        except:
            pass
        return ret

    def filtraPrezzo(self, start, stop, fileName):
        ret = None
        try:
            ret = Filtri().filtraPrezzo(start, stop, fileName)
        except:
            pass
        return ret

    def filtraClienti(self, nome, cognome):
        ret = None
        try:
            ret = Filtri().filtraClienti(nome, cognome)
        except:
            pass
        return ret

    def recuperaListaCategorie(self):
        ret = None
        try:
            ret = Categoria().recuperaListaOggetti()
        except:
            pass
        return ret

    def checkEsistenzaCategoriaInDatabase(self, str):
        ret = None
        try:
            ret = Categoria().checkEsistenzaCategoriaInDatabase(str)
        except:
            pass
        return ret

    def recuperaProdottiInVenditaConAccount(self, account):
        ret = None
        try:
            ret = Prodotto().recuperaListaProdottiInAssociatiAdAccount(account,
                                                                       Prodotto().recuperaListaProdottiInVendita())
        except:
            pass
        return ret

    def recuperaProdottiScadutiConAccount(self, account):
        ret = None
        try:
            ret = Prodotto().recuperaListaProdottiInAssociatiAdAccount(account,
                                                                       Prodotto().recuperaListaProdottiScaduti())
        except:
            pass
        return ret

    def recuperaProdottiVendutiConAccount(self, account):
        ret = None
        try:
            ret = Prodotto().recuperaListaProdottiInAssociatiAdAccount(account,
                                                                       Prodotto().recuperaListaProdottiVenduti())
        except:
            pass
        return ret

    def elaboraCercaProdottoBtnClicked(self, name, textData, textPrezzo, textCategoria):
        ret = None
        try:
            ret = Filtri().elaboraCercaProdottoBtnClicked(name, textData, textPrezzo, textCategoria)
        except:
            pass
        return ret

    def aggiornaProdotto(self, nomeCategoriaLe, data, nomeProdotto, prezzoLe, nomeScaffaleLe, idProdotto):
        ret = None
        try:
            Amministratore().aggiornaProdotto(nomeCategoriaLe, None, nomeProdotto, prezzoLe, nomeScaffaleLe, idProdotto)
        except:
            pass

    def aggiornaAccount(self, idAccount, nomeLe, cognomeLe, dataDiNascitaLe, emailLe, telefonoLe, capLe, citofonoLe,
                        cittaLe, viaLe, piazzaLe, civicoLe):
        ret = None
        try:
            residenza = Indirizzo(capLe, citofonoLe, cittaLe, civicoLe, piazzaLe, viaLe)
            Amministratore().aggiornaAccount(nomeLe, cognomeLe, dataDiNascitaLe, emailLe, idAccount, telefonoLe,
                                             residenza)
        except:
            pass

    def logout(self):
        ret = None
        try:
            ret = Logging.logout()
        except:
            pass
        return ret
