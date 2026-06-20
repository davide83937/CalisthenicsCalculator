import Match as m


class GestoreMatch:
    def __init__(self):
        self.listaMatch = []

    def aggiungiMatch(self, first, second, index):
        match = m.Match(index, first, second)
        self.listaMatch.append(match)
        return index, first, second

    def aggiungiSetPartecipante(self, index, cod, setCorrente):
        for match in self.listaMatch:
            if match.numeroMatch == index:
                if match.getCodiceAtletaInGara1() == cod:
                    match.setSetAtletaInGara1(setCorrente)
                else:
                    match.setSetAtletaInGara2(setCorrente)
                winner = match.risolvi()
                if winner is not None:
                    return  winner
        return None


