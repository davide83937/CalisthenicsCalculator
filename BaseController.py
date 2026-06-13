import Atleta as a
import Storage as s
import Calcolatore as c
from Storage import Storage


class BaseController:
    def __init__(self, storage):
        self.storage = storage
        self.Calcolatore = c.Calcolatore(storage)

    def calcola_codice(self, lista):
        if not lista:
            return 0
        else:
            i = 0
            for cod in lista.keys():
                if i != cod:
                    return i
                i = i + 1
            return i


    def inserisciDati(self, nome, cognome, età, codice_fiscale, numero_cellulare, email, altezza, peso):
        cod = self.calcola_codice(self.storage.elencoAtleti)
        if nome == "":
            return 1
        elif cognome == "":
            return 2
        elif not isinstance(età, int):
            return 3
        elif str(codice_fiscale).__len__() != 16:
            return 4
        elif str(numero_cellulare).__len__() != 10:
            return 5
        elif email == "":
            print("Email:"+ email)
            return 6
        elif not isinstance(altezza, float):
            return 7
        elif not isinstance(peso, float):
            print("Peso:" + peso)
            return 8
        else:
            self.atletaCorrente = a.Atleta(cod, nome, cognome, età, codice_fiscale, numero_cellulare, email, altezza, peso)
            return 0


    def terminaRegistrazione(self):
        self.storage.salvaAtleta(self.atletaCorrente)
        return self.atletaCorrente

    def valutaAtleta(self, cod):
        self.Calcolatore.setSetCorrente(cod)

    def calcolaPunteggioSet(self, n_combo):
        return self.Calcolatore.calcolaPunteggioSet(n_combo)

    def inserisciSkillInSet(self, nomeSkill, malus):
        self.Calcolatore.inserisciSkillInSet(nomeSkill, malus)

    def getElencoAtleti(self):
        self.storage.getElencoAtleti()

    def getElencoSkills(self):
        self.storage.getElencoSkills()
