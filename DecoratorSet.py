from SetBuilder import setBuilder


class decoratorSet(setBuilder):

    def __init__(self, component: setBuilder):
        self._component = component

    @property
    def punteggio_complessivo(self):
        # Delega il calcolo al componente interno
        return self._component.punteggio_complessivo

    @property
    def listaSkill(self):
        return self._component.listaSkill

    def creaSetLine(self, skill, malus):
        return self._component.creaSetLine(skill, malus)

    def calcolaPunteggioParziale(self, sl, elencoSkills):
        return self._component.calcolaPunteggioParziale(sl, elencoSkills)


