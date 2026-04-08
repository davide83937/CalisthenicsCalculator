from SetBuilder import setBuilder


class decoratorSet(setBuilder):
    _component : setBuilder = None
    def __init__(self, component: setBuilder):
       self._component = component

    def applica_bonus(self):
        pass



