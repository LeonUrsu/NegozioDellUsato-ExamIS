from abc import abstractmethod


class AmministratoreInterface:

    @abstractmethod
    # utilizzabile per account nel sistema
    def aggiornaAccount(self, nome, cognome, dataDiNascitaStr, email, idAccount, numeroTelefonico, residenza):
        pass

    @abstractmethod
    # utilizzabile per aggiornare un prodotto nel sistema
    def aggiornaProdotto(self, nomeCategoria, dataEsposizione,
                         nomeProdotto, prezzoOriginale, nomeScaffale, idProdotto):
        pass

    @abstractmethod
    # utilizzabile per effettuare un backup
    def effettuaBackup(self):
        pass

    @abstractmethod
    # utilizzabile per eliminare un account dal sistema
    def eliminaAccount(sel, idAccount):
        pass

    @abstractmethod
    # utilizzabile per filtrare clienti
    def filtraClienti(self, nome, cognome):
        pass

    @abstractmethod
    # utilizzabile per inserire un acocunt nel sistema
    def inserisciAccount(self, nome, cognome, dataDiNascita, email, password,
                         numeroTelefonico, cap, citofono, citta, civico, piazza, via):
        pass

    @abstractmethod
    # utilizzabile per inserire un prodotto nel sistema
    def inserisciProdotto(self, dataEsposizione, idAccount,
                          nomeProdotto, prezzoOriginale, nomeScaffaleLe, nomeCategoria):
        pass


