import Atleta as a
from Eccezioni import RegistraAtletaError
import Calcolatore as c



class BaseController:
    def __init__(self, storage):
        self.storage = storage
        self.Calcolatore = c.Calcolatore(storage)
        self.atletaCorrente = None

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
            raise RegistraAtletaError("Il nome non può essere vuoto.", "nome")
        elif cognome == "":
            raise RegistraAtletaError("Il cognome non può essere vuoto.", "cognome")
        elif not isinstance(età, int) or età <= 0:
            raise RegistraAtletaError("L'età deve essere un numero intero valido.", "età")
        elif len(str(codice_fiscale)) != 16:
            raise RegistraAtletaError("Il Codice Fiscale deve contenere 16 caratteri.", "codice_fiscale")
        elif len(str(numero_cellulare)) != 10:
            raise RegistraAtletaError("Il numero di cellulare deve avere 10 cifre.", "cellulare")
        elif email == "":
            raise RegistraAtletaError("L'email non può essere vuota.", "email")
        elif not isinstance(altezza, float) or altezza <= 0:
            raise RegistraAtletaError("L'altezza deve essere un numero decimale valido.", "altezza")
        elif not isinstance(peso, float) or peso <= 0:
            raise RegistraAtletaError("Il peso deve essere un numero decimale valido.", "peso")

        # Se tutto va bene, crea e restituisci l'atleta (niente più "return 0")
        self.atletaCorrente = a.Atleta(cod, nome, cognome, età, codice_fiscale, numero_cellulare, email, altezza, peso)
        return self.atletaCorrente


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
        return self.storage.getElencoAtleti()

    def getSkillList(self):
        return self.storage.getSkillList()
