from Turno import Turno
from Quarto import Quarto


class Ottavo(Turno):

    def avanza(self):
        self.context.passaIlTurno(Quarto())