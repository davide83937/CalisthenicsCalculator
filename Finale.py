from Turno import Turno
from Campione import Champion

class Finale(Turno):
    def avanza(self):
        statoVecchio = self
        self.context.passaIlTurno(Champion())
        return statoVecchio

    def get_destinazione_vincitore(self, current_match):
        # Questo non dovrebbe mai essere chiamato se is_finale() viene verificato prima
        return None, None, None, None

    def is_finale(self):
        return True