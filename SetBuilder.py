from abc import ABC, abstractmethod

class setBuilder(ABC):

    def __init__(self, cod_atleta, listaSkill, punteggio_complessivo, bonus):
        self.cod_atleta = cod_atleta
        self.listaSkill = listaSkill
        self.punteggio_complessivo = punteggio_complessivo
        self.bonus = bonus


    def creaSetLine(self, skill, malus):
        pass

    def calcolaPunteggioParziale(self, sl, elencoSkills):
        pass









    """
    @abstractmethod
    def calcolaBonus(self, listaSkillSet, listaSkill):
        pass
    """