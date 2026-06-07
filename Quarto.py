from Semifinale import Semifinale
import Turno

class Quarto(Turno):

    def avanza(self):
        self.AtletaInGara.passaIlTurno(Semifinale())