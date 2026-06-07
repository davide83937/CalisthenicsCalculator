import Match as m
from Match import Match


class GestoreTorneo:
    def __init__(self):
        self.listaMatch = []

    def aggiungiMatch(self, first, second, index):
        match = m.Match(index, first, second)
        self.listaMatch.append(match)

    def aggiungiSetPartecipante(self, index, cod, setCorrente):
        for match in self.listaMatch:
            if match.numeroMatch == index:
                if match.atleta1.cod == cod:
                   match.atleta1.setCorrente(setCorrente)
                else:
                   match.atleta2.setCorrente(setCorrente)
                match.risolvi()

