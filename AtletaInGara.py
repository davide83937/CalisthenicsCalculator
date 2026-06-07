import Turno as t

class AtletaInGara():

    _stato = None

    def __init__(self, atleta):
        self.Atleta = atleta
        self.setCorrente = None



    def passaIlTurno(self, stato: t.Turno):
        self._state = stato
        self._state.AtletaInGara = self
        print(f"ATLETA: {self.Atleta.nome} PASSA A")
        print(self._state)