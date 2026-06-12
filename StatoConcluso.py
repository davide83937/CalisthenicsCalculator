from StatoCompetizione import StatoCompetizione


class StatoConcluso(StatoCompetizione):
    def registraSet(self, finalSet, codice=0, indexMatch=0):
        print("Non puoi registrare un set se il torneo è finito")
        return None, None

    def avanza(self):
        print("Sei già alla fase finale")
        pass

    def generaClassifica(self):
        print("Non puoi generare una classifica se il torneo è finito")
        return None