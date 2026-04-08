from abc import ABC, abstractmethod
from Set import Set

class setBuilder(ABC):

    def __init__(self, cod_atleta):
        # Inizializza il prodotto finale
        self._prodotto = Set(cod_atleta)
        self.elenco_skills_riferimento = []

    @property
    def punteggio_complessivo(self):
        return self._punteggio_complessivo

    @punteggio_complessivo.setter
    def punteggio_complessivo(self, value):
        self._punteggio_complessivo = value

    @abstractmethod
    def creaSetLine(self, skill, malus):
        """Crea una riga del set (Skill + Malus)"""
        pass

    @abstractmethod
    def calcolaPunteggioParziale(self, sl, elencoSkills):
        """Calcola il punteggio di una riga e lo somma al totale"""
        pass

    """
    @abstractmethod
    def calcolaBonus(self, listaSkillSet, listaSkill):
        pass
    """