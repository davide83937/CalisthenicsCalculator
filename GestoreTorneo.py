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
                # 1. Usa Atleta1 con la A maiuscola (correzione precedente)
                # 2. Usa .Atleta.codice per accedere correttamente all'ID (nuova correzione)
                if match.Atleta1.Atleta.codice == cod:
                    # 3. Usa l'operatore di assegnazione "=" e non le parentesi (nuova correzione)
                    match.Atleta1.setCorrente = setCorrente
                else:
                    match.Atleta2.setCorrente = setCorrente

                indexMatch, winner = match.risolvi()
                if winner is not None:
                    return indexMatch, winner
        return 10000, None


