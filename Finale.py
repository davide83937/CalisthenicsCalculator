import Turno
from Campione import Champion

class Finale(Turno):
    def avanza(self):
        self.AtletaInGara.passaIlTurno(Champion())