import SetLine as sl

class Set:
    def __init__(self, cod_atleta, listaSkill, punteggio_complessivo, bonus):
        self.cod_atleta = cod_atleta
        self.listaSkill = listaSkill
        self.punteggio_complessivo = punteggio_complessivo
        self.bonus = bonus

    def creaSetLine(self, skill, malus):
        self.setL = sl.setLine(skill.nome, malus)
        return self.setL

    def calcolaPunteggioParziale(self, sl, elencoSkills):
            punteggio = float(next((s.punteggio for s in elencoSkills if s.nome == sl.skill), None))
            print(punteggio)
            self.punteggio_complessivo += punteggio - punteggio*sl.malus

    def calcolaBonus(self, listaSkillSet, listaSkill):
        tempListaCategorie = []
        for e in listaSkillSet:
            categoria = next((s.categoria for s in listaSkill if s.nome == e.skill), None)
            if categoria not in tempListaCategorie:
                tempListaCategorie.append(categoria)
        if len(tempListaCategorie) == 4:
            self.bonus = True
            self.punteggio_complessivo += 5
            print("Bonus presente")
        else:
            print("Bonus non presente")



    def __repr__(self):
        return super().__repr__()





