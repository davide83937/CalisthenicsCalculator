from SetBuilder import setBuilder
from DecoratorCompletezza import DecoratorCompletezza

class DirectorBuilder:
    def __init__(self, sb: setBuilder, listaSkill):
        self.sb = sb
        self.listaSkill = listaSkill
        self.result_builder = self.checkBonusCompletezza()


    def checkBonusCompletezza(self):
        tempListaCategorie = []
        for e in self.sb.elenco_skills_riferimento:
            categoria = next((s.categoria for s in self.listaSkill if s.nome == e.skill), None)
            if categoria not in tempListaCategorie:
                tempListaCategorie.append(categoria)
        if len(tempListaCategorie) == 4:
            print("Bonus completezza presente")
            return DecoratorCompletezza(self.sb)
        return self.sb

    def get_result(self):
        return self.result_builder