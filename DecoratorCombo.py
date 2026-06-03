from DecoratorSet import decoratorSet
from SetBuilder import setBuilder

class DecoratorCombo(decoratorSet):
    def __init__(self, corrente: setBuilder, n_combo):
        super().__init__(corrente)
        self.my_corrente = corrente
        self.nome = "combo"
        self.n_combo = n_combo
        self.bonus = 6*n_combo
        self.applica_bonus()


    def applica_bonus(self):
        self.my_corrente._prodotto.punteggio_totale += self.bonus
        for i in range(self.n_combo):
            self.my_corrente._prodotto.bonus_applicati.append(self.nome)