from StatoCompetizione import StatoCompetizione
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Competizione import Competizione

class StatoTurni(StatoCompetizione):
    def __init__(self, competizione: 'Competizione'):
        super().__init__(competizione)

    def registraSet(self, finalSet, codice=0, indexMatch=0):
        winner = self.competizione.aggiungiSetPartecipante(indexMatch, codice, finalSet)
        print("Set in Turni")
        if winner is not None:
            stato = self.competizione.avanzaTurnoAtleta(indexMatch, winner)  # Richiama il nuovo metodo universale
            return winner, stato
        return None, None

    def avanza(self):
        from StatoConcluso import StatoConcluso
        self.competizione.transitionTo(StatoConcluso(self.competizione))

    def generaClassifica(self):
        print("Nella fase di turni non puoi generare una classifica")
        return None