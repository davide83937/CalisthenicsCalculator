from StatoCompetizione import StatoCompetizione


class StatoConcluso(StatoCompetizione):
    def registraSet(self, finalSet, codice=0, indexMatch=0):
        return None, None

    def avanza(self):
        pass

    def generaClassifica(self):
        return None