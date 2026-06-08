from Turno import Turno
from Quarto import Quarto


class Ottavo(Turno):

    def avanza(self):
        stato = self.context.passaIlTurno(Quarto())
        return stato

    def get_destinazione_vincitore(self, current_match):
        # Se vinci l'ottavo n. 1 o 2, vai al quarto n. 1 (match 9), ecc.
        next_match = 8 + (current_match + 1) // 2
        fase = "Quarti"
        indice_fase = next_match - 8
        posizione = 1 if current_match % 2 != 0 else 2

        return next_match, fase, indice_fase, posizione