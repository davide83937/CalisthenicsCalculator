from SetBuilder import setBuilder
from DecoratorCompletezza import DecoratorCompletezza
from DecoratorCombo import DecoratorCombo

class DirectorBuilder:
    def __init__(self, sb: setBuilder, listaSkill, n_combo):
        self.sb = sb
        self.listaSkill = listaSkill
        self.n_combo = n_combo
        self.result_builder = self.checkBonusCompletezza()
        self.result_builder = self.checkBonusCombo()


    def checkBonusCompletezza(self):
        tempListaCategorie = []
        print("Dentro il decorator")

        for e in self.sb._prodotto.lista_linee:
            categoria = next((s.categoria for s in self.listaSkill if s.nome == e.skill), None)
            if categoria not in tempListaCategorie:
                print(f"Categoria {categoria}")
                tempListaCategorie.append(categoria)
        if len(tempListaCategorie) == 4:
            print("Bonus completezza presente")
            return DecoratorCompletezza(self.sb)
        return self.sb

    def checkBonusCombo(self):
        if(self.n_combo > 0):
           n_skill = len(self.sb._prodotto.lista_linee)
           if(n_skill>=(self.n_combo*4)):
               return DecoratorCombo(self.sb, self.n_combo)
           else:
               self.n_combo = n_skill//4
               return DecoratorCombo(self.sb, self.n_combo)
        return self.sb



    def get_result(self):
        return self.result_builder

