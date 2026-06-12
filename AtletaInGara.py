from typing import TYPE_CHECKING

# Spostiamo l'import qua dentro
if TYPE_CHECKING:
    import Turno as t

class AtletaInGara():

    _stato = None

    def __init__(self, atleta):
        self.Atleta = atleta
        self.setCorrente = None
        from Ottavo import Ottavo
        self.passaIlTurno(Ottavo())

    def getCodiceAtletaInGara(self):
        return self.Atleta.codice


    def passaIlTurno(self, stato: 't.Turno'): # Usa gli apici per il tipo!
        self._stato = stato # Nota: ho corretto _state in _stato per coerenza con la classe
        self._stato.context = self
        print(f"ATLETA: {self.Atleta.nome} PASSA A")
        print(self._stato)
        return self._stato