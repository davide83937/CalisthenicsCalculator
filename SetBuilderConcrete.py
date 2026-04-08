from SetBuilder import setBuilder
import SetLine as sl

class SetBuilderConcrete(setBuilder):
    def __init__(self, cod_atleta, listaSkill, punteggio_complessivo, bonus):
        super().__init__(cod_atleta, listaSkill, punteggio_complessivo, bonus)

    def creaSetLine(self, skill, malus):
        self.setL = sl.setLine(skill.nome, malus)
        return self.setL

    def calcolaPunteggioParziale(self, sl, elencoSkills):
        punteggio = float(next((s.punteggio for s in elencoSkills if s.nome == sl.skill), None))
        self.punteggio_complessivo += punteggio - punteggio*sl.malus

    def __repr__(self):
        return super().__repr__()





