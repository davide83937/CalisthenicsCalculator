from Semifinale import Semifinale
from Turno import Turno

class Quarto(Turno):

    def avanza(self):
        self.context.passaIlTurno(Semifinale())