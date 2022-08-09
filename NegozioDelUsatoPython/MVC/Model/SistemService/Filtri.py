from MVC.Model.SistemService.File import File


class Filtri:


    # Costruttore della classe
    def __init__(self):
        self.filtrati = None


    # Metodo di filtraggio dei prodotti in base all prezzo
    # prezzoMin = prezzo minimo di filtraggio
    # prezzoMax = prezzo massimo di filtraggio
    def filtraPrezzo(self, prezzoMin, prezzoMax, file):
        fileName = f"Database\Prodotti\{file}.txt"
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if prezzoMin <= prodotto.prezzoCorrente and prodotto.prezzoCorrente <= prezzoMax:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList


    # Metodo di filtraggio dei prodotti in base alla data
    # dataInizio = data di inizio filtraggio
    # dataFine = data di fine filtraggio
    def filtraData(self, dataInizio, dataFine, file):
        fileName = f"Database\Prodotti\{file}.txt"
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if dataInizio <= prodotto.dataScadenza and prodotto.dataScadenza <= dataFine:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList


    # Metodo di filtraggio dei prodotti in base alla categoria
    # codiceCategoria = codice della categoria su cui fare la selezione
    # file =
    def filtraCategoria(self, codiceCategoria, file):
        fileName = f"Database\Prodotti\{file}.txt"
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if codiceCategoria == prodotto.codiceCategoria:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList
