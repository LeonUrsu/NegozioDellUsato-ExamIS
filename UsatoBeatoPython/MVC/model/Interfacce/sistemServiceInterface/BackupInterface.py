from abc import abstractmethod


class BackupInterface:

    @abstractmethod
    # utilizzabile per copiare dati
    def copiaDati(self, from_path, to_path):
        pass

    @abstractmethod
    # utilizzabile per effettuare in backup
    def effettuaBackup(self):
        pass



