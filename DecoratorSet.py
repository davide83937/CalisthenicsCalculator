from SetBuilder import setBuilder


class decoratorSet(setBuilder):

    def __init__(self, component: setBuilder):
        self._component = component


    def applicaBonus(self):
        pass


