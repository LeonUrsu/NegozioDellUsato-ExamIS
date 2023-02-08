from abc import abstractmethod


class AccountInterface:

    @abstractmethod
    # utilizzabile per aggiornare un account
    def aggiornaAccount(self, nome, cognome, dataDiNascita, email, idAccount, numeroTelefonico, indirizzo):
        pass

    @abstractmethod
    # utilizzabile per aggiungere nel sistema un account
    def aggiungiAccount(self, nome, cognome, dataDiNascita, email, numeroTelefonico, password, residenza):
        pass

    @abstractmethod
    # utilizzabile per eliminare un acocunt tramite id account
    def eliminaAccount(self, idAccount):
        pass
