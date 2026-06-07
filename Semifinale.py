from Turno import Turno
from Finale import Finale

class Semifinale(Turno):
    def avanza(self):
        self.context.passaIlTurno(Finale())