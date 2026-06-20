from Turno import Turno

class Champion(Turno):

    def avanza(self):
        pass

    def get_destinazione_vincitore(self, current_match):
        return None, None, None, None

    def is_finale(self):
        return True