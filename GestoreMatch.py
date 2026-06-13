import Match as m


class GestoreMatch:
    def __init__(self):
        self.listaMatch = []

    def aggiungiMatch(self, first, second, index):
        match = m.Match(index, first, second)
        self.listaMatch.append(match)
        # AGGIUNGI QUESTA RIGA:
        return index, first, second

    def aggiungiSetPartecipante(self, index, cod, setCorrente):
        for match in self.listaMatch:
            if match.numeroMatch == index:
                # 1. Usa Atleta1 con la A maiuscola (correzione precedente)
                # 2. Usa .Atleta.codice per accedere correttamente all'ID (nuova correzione)
                if match.getCodiceAtletaInGara1() == cod:
                    # 3. Usa l'operatore di assegnazione "=" e non le parentesi (nuova correzione)
                    match.setSetAtletaInGara1(setCorrente)
                else:
                    match.setSetAtletaInGara2(setCorrente)

                winner = match.risolvi()
                if winner is not None:
                    return  winner
        return None


