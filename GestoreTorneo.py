import Match as m


class GestoreTorneo:
    def __init__(self):
        self.listaMatch = []

    def aggiungiMatch(self, first, second):
        match = m.Match(first, second)
        self.listaMatch.append(match)