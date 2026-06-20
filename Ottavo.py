from Turno import Turno
from Quarto import Quarto


class Ottavo(Turno):

    def avanza(self):
        statoVecchio = self
        self.context.passaIlTurno(Quarto())
        return statoVecchio

    def get_destinazione_vincitore(self, current_match):
        next_match = 8 + (current_match + 1) // 2
        fase = "Quarti"
        indice_fase = next_match - 8
        posizione = 1 if current_match % 2 != 0 else 2

        return next_match, fase, indice_fase, posizione