
from StatoCompetizione import StatoCompetizione
from typing import TYPE_CHECKING

# RIMUOVI da qui: from StatoConcluso import StatoConcluso
# Questo previene l'import circolare con Competizione
if TYPE_CHECKING:
    from Competizione import Competizione



class StatoTurni(StatoCompetizione):
    def __init__(self, competizione: 'Competizione'):
        super().__init__(competizione)

    def registraSet(self, finalSet, codice=0, indexMatch=0):
        winner = self.competizione.gestoreTorneo.aggiungiSetPartecipante(indexMatch, codice, finalSet)
        if winner is not None:
            stato = self.competizione.avanzaTurnoAtleta(indexMatch, winner)  # Richiama il nuovo metodo universale
            return winner, stato
        return None, None

    def avanza(self):
        from StatoConcluso import StatoConcluso
        self.competizione.transitionTo(StatoConcluso())

    def generaClassifica(self):
        return None