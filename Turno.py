from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from AtletaInGara import AtletaInGara

class Turno(ABC):
    @property
    def context(self) -> 'AtletaInGara':
        return self._context

    @context.setter
    def context(self, context: 'AtletaInGara') -> None:
        self._context = context

    @abstractmethod
    def avanza(self):
        pass

    @abstractmethod
    def get_destinazione_vincitore(self, current_match):
        pass

    def is_finale(self):
        return False