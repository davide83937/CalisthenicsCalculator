from Turno import Turno
from Finale import Finale

class Semifinale(Turno):
    def avanza(self):
        statoVecchio = self
        self.context.passaIlTurno(Finale())
        return statoVecchio

    def get_destinazione_vincitore(self, current_match):
        next_match = 15
        fase = "Finale"
        indice_fase = 1
        posizione = 1 if current_match == 13 else 2

        return next_match, fase, indice_fase, posizione