import Classifica as c

class Competizione:
    def __init__(self):
        self.lista_partecipanti = []
        self.classifica = c.Classifica()



    def inserisciPartecipanti(self, atleta):
        for a in self.lista_partecipanti:
            if a.codice == atleta.codice:
                return
        self.lista_partecipanti.append(atleta)


    def inserisciSetInClassifica(self, set):
        self.classifica.listaSet.append(set)

    def getClassificaOrdinata(self):
        return self.classifica.getClassificaOrdinata()