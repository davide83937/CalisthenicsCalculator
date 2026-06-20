from SetBuilder import setBuilder


class decoratorSet(setBuilder):

    def __init__(self, component: setBuilder):
        self._component = component

    def creaSetLine(self, skill, malus):
        return self._component.creaSetLine(skill, malus)

    def calcolaPunteggioParziale(self, sl, elencoSkills):
        return self._component.calcolaPunteggioParziale(sl, elencoSkills)

    def get_result(self):
        return self._component.get_result()

    def applicaBonus(self):
        pass


