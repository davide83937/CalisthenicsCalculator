from SetBuilder import setBuilder


class decoratorSet(setBuilder):

    def __init__(self, component: setBuilder):
        self._component = component

        # Delega la creazione della riga al builder/decoratore contenuto
    def creaSetLine(self, skill, malus):
        return self._component.creaSetLine(skill, malus)

        # Delega il calcolo parziale
    def calcolaPunteggioParziale(self, sl, elencoSkills):
        return self._component.calcolaPunteggioParziale(sl, elencoSkills)

        # Delega il recupero del risultato finale
    def get_result(self):
        return self._component.get_result()

    def applicaBonus(self):
        pass


