from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Questo blocco viene eseguito solo dai linter/IDE, non a runtime.
# Evita l'importazione circolare.
if TYPE_CHECKING:
    from AtletaInGara import AtletaInGara

class Turno(ABC):
    @property
    def context(self) -> 'AtletaInGara': # Usa gli apici per il tipo!
        return self._context

    @context.setter
    def context(self, context: 'AtletaInGara') -> None: # Usa gli apici!
        self._context = context

    @abstractmethod
    def avanza(self):
        pass

    @abstractmethod
    def get_destinazione_vincitore(self, current_match):
        pass

    def is_finale(self):
        return False