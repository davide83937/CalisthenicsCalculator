from SetBuilder import setBuilder
from DecoratorCompletezza import DecoratorCompletezza

class DirectorBuilder:
    def __init__(self, sb: setBuilder, listaSkill):
        self.sb = sb
        self.listaSkill = listaSkill
        self.bonusCompletezza = self.checkBonusCompletezza()


    def checkBonusCompletezza(self):
        tempListaCategorie = []
        for e in self.sb.listaSkill:
            categoria = next((s.categoria for s in self.listaSkill if s.nome == e.skill), None)
            if categoria not in tempListaCategorie:
                tempListaCategorie.append(categoria)
        if len(tempListaCategorie) == 4:
            print("Bonus completezza presente")
            self.sb = DecoratorCompletezza(self.sb)
            return True

        else:
            print("Bonus completezza non presente")
            return False

