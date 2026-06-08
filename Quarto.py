from Semifinale import Semifinale
from Turno import Turno

class Quarto(Turno):

    def avanza(self):
        self.context.passaIlTurno(Semifinale())

    def get_destinazione_vincitore(self, current_match):
        # Se vinci il quarto n. 1 o 2, vai alla semifinale n. 1 (match 13)
        next_match = 8 + (current_match + 1) // 2
        fase = "Semifinali"
        indice_fase = next_match - 12
        posizione = 1 if current_match % 2 != 0 else 2

        return next_match, fase, indice_fase, posizione