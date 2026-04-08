from SetBuilder import setBuilder
import SetLine as sl
from Set import Set

class SetBuilderConcrete(setBuilder):
    def __init__(self, cod_atleta):
        # Inizializza il prodotto finale
        super().__init__(cod_atleta)

    def creaSetLine(self, skill, malus):
        nuova_linea = sl.setLine(skill.nome, malus)
        self._prodotto.lista_linee.append(nuova_linea)
        return nuova_linea

    def calcolaPunteggioParziale(self, riga, elencoSkills):
        # Trova il valore base della skill
        valore_base = float(next((s.punteggio for s in elencoSkills if s.nome == riga.skill), 0))
        # Calcola il punteggio della riga con malus
        punteggio_riga = valore_base - (valore_base * riga.malus)
        # Aggiorna il prodotto
        self._prodotto.punteggio_totale += punteggio_riga

        # Aggiungi questa property per far funzionare il DirectorBuilder
        @property
        def listaSkill(self):
            return self._prodotto.lista_linee

    def get_result(self) -> Set:
        return self._prodotto





