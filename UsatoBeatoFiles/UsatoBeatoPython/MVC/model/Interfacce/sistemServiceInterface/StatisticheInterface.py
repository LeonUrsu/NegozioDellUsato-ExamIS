from abc import abstractmethod


class StatisticheInterface:

    @abstractmethod
    # utilizzabile per trovare le categorie di tendenza
    def tendenzaCategorie(self):
        pass

    @abstractmethod
    # utilizzabile per visualizzare le statistiche
    def visualizzaStatistiche(self):
        pass

