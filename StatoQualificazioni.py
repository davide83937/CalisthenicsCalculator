
from StatoCompetizione import StatoCompetizione


class StatoQualificazioni(StatoCompetizione):
    def __init__(self, competizione):
        super().__init__(competizione)

    def registraSet(self, finalSet, codice=0, indexMatch=0):
        self.competizione.classifica.listaSet.append(finalSet)
        print("SetInClassifica")
        return None, None

    def avanza(self):
        from StatoTurni import StatoTurni
        self.competizione.transitionTo(StatoTurni(self.competizione))

    def generaClassifica(self):
        return self.competizione.classifica.getClassificaOrdinata()