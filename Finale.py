from Turno import Turno
from Campione import Champion

class Finale(Turno):
    def avanza(self):
        self.context.passaIlTurno(Champion())