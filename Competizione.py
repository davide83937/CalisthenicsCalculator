import Classifica as c

class Competizione:
    def __init__(self):
        self.lista_partecipanti = []
        self.stati_partecipanti = {}
        self.classifica = c.Classifica()

    def getStatiPartecipanti(self):
        return self.stati_partecipanti

    def inserisciPartecipanti(self, atleta):
        for a in self.lista_partecipanti:
            if a.codice == atleta.codice:
                return
        self.lista_partecipanti.append(atleta)
        self.stati_partecipanti[atleta.codice] = "qualificazione"

    def inserisciSetInClassifica(self, set):
        self.classifica.listaSet.append(set)

    def getClassificaOrdinata(self):
        return self.classifica.getClassificaOrdinata()