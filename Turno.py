from abc import ABC, abstractmethod

from AtletaInGara import AtletaInGara


class Turno(ABC):
    @property
    def context(self) -> AtletaInGara:
        return self._context

    @context.setter
    def context(self, context: AtletaInGara) -> None:
        self._context = context

    @abstractmethod
    def avanza(self):
        pass