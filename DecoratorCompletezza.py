from DecoratorSet import decoratorSet
from SetBuilder import setBuilder

class DecoratorCompletezza(decoratorSet):
    def __init__(self, corrente: setBuilder):
        super().__init__(corrente)
        self.my_corrente = corrente
        self.bonus = 5
        self.applica_bonus()

    def applica_bonus(self):
        self.my_corrente.punteggio_complessivo += self.bonus