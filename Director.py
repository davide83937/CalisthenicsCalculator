from SetBuilder import setBuilder
from DecoratorCompletezza import DecoratorCompletezza

class DirectorBuilder:
    def __init__(self, sb: setBuilder, listaSkill):
        self.sb = sb
        self.listaSkill = listaSkill
        self.result_builder = self.checkBonusCompletezza()


    def checkBonusCompletezza(self):
        tempListaCategorie = []
        print("Dentro il decorator")

        for e in self.sb._prodotto.lista_linee:
            #tempListaCategorie.append(e.skill.nome)
            categoria = next((s.categoria for s in self.listaSkill if s.nome == e.skill), None)
            if categoria not in tempListaCategorie:
                print(f"Categoria {categoria}")
                tempListaCategorie.append(categoria)
        if len(tempListaCategorie) == 4:
            print("Bonus completezza presente")
            return DecoratorCompletezza(self.sb)
        return self.sb

    def get_result(self):
        return self.result_builder

