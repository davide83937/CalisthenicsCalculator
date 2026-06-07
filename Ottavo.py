import Turno
from AtletaInGara import AtletaInGara
from Quarto import Quarto


class Ottavo(Turno):

    def avanza(self):
        self.AtletaInGara.passaIlTurno(Quarto())