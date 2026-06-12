class Match:
    def __init__(self, numeroMatch, si1, si2):
        self.numeroMatch = numeroMatch
        self.Atleta1 = si1
        self.Atleta2 = si2
        self.Winner = None


    def getCodiceAtletaInGara1(self):
        return self.Atleta1.getCodiceAtletaInGara()

    def getCodiceAtletaInGara2(self):
        return self.Atleta2.getCodiceAtletaInGara()

    def setSetAtletaInGara1(self, setCorrente):
        self.Atleta1.setCorrente = setCorrente

    def setSetAtletaInGara2(self, setCorrente):
        self.Atleta2.setCorrente = setCorrente


    def risolvi(self):
        if self.Atleta1.setCorrente is not None and self.Atleta2.setCorrente is not None:
            if self.Atleta1.setCorrente.punteggio_totale >= self.Atleta2.setCorrente.punteggio_totale:
                self.Winner = self.Atleta1
            elif self.Atleta1.setCorrente.punteggio_totale <= self.Atleta2.setCorrente.punteggio_totale:
                self.Winner = self.Atleta2
            else:
                pass

        if self.Winner is not None:
            print(f"Il vincitore è {self.Winner.Atleta.cognome}")
            return self.Winner
        return None


