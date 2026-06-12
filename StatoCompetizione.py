from abc import ABC, abstractmethod


class StatoCompetizione(ABC):
    def __init__(self, competizione):
        self.competizione = competizione

    @abstractmethod
    def registraSet(self, finalSet, codice=0, indexMatch=0):
        pass

    @abstractmethod
    def avanza(self):
        pass

    @abstractmethod
    def generaClassifica(self):
        pass