from abc import ABC, abstractmethod
from Set import Set

class setBuilder(ABC):

    def __init__(self, cod_atleta, lista):
        self._prodotto = Set(cod_atleta)
        self.elenco_skills_riferimento = lista


    @abstractmethod
    def creaSetLine(self, skill, malus):
        pass

    @abstractmethod
    def calcolaPunteggioParziale(self, sl, elencoSkills):
        pass

