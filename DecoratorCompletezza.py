from DecoratorSet import decoratorSet
from SetBuilder import setBuilder

class DecoratorCompletezza(decoratorSet):
    def __init__(self, corrente: setBuilder):
        super().__init__(corrente)
        self.my_corrente = corrente
        self.nome = "completezza"
        self.bonus = 7
        self.applica_bonus()

    def applica_bonus(self):
        self.my_corrente._prodotto.punteggio_totale += self.bonus
        self.my_corrente._prodotto.bonus_applicati.append(self.nome)