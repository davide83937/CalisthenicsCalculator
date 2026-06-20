from typing import TYPE_CHECKING


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


    def passaIlTurno(self, stato: 't.Turno'):
        self._stato = stato
        self._stato.context = self
        print(f"ATLETA: {self.Atleta.nome} PASSA A")
        print(self._stato)
        return self._stato