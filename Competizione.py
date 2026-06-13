import GestoreMatch as gt
import Classifica as c
import AtletaInGara as ag
from StatoCompetizione import StatoCompetizione


class Competizione:
    _state = None

    def __init__(self):
        self.lista_partecipanti = []
        self.classifica = c.Classifica()
        self.gestoreMatch = gt.GestoreMatch()
        self.index = 0
        self.slot_attesa = {i: [] for i in range(9, 16)}
        import StatoQualificazioni as sq
        _state = self.transitionTo(sq.StatoQualificazioni(self))


    def transitionTo(self, stato: 'StatoCompetizione'):
        self._state = stato

    def nextPhase(self):
        self._state.avanza()
        print("NUOVO STATO TORNEO")
        print(self._state)

    def requestRegistraSet(self, finalSet, codice, index):
        return self._state.registraSet(finalSet, codice, index)

    def requestGeneraClassifica(self):
        classifica = self._state.generaClassifica()
        if classifica is not None:
            self.nextPhase()
        return classifica

    def getClassificaOrdinata(self):
        return self.classifica.getClassificaOrdinata()


    def getPartecipante(self, codice):
        atleta = next((a for a in self.lista_partecipanti if a.codice == codice), None)
        return atleta

    def inserisciPartecipanti(self, atleta):
        for a in self.lista_partecipanti:
            if a.codice == atleta.codice:
                return
        self.lista_partecipanti.append(atleta)



    def getDueSfidanti(self):
        firstAtlhete, secondAtlhete = self.classifica.getDuesfidenti(self.index, self.index + 8)
        atleta1 = self.getPartecipante(firstAtlhete[0])
        atletaInGara1 = ag.AtletaInGara(atleta1)
        atleta2 = self.getPartecipante(secondAtlhete[0])
        atletaInGara2 = ag.AtletaInGara(atleta2)
        self.index = self.index + 1
        index, first, second = self.setDueSfidenti(atletaInGara1, atletaInGara2, self.index)
        return index, first, second

    def setDueSfidenti(self, first, second, index):
        index, first, second = self.gestoreMatch.aggiungiMatch(first, second, index)
        return index, first, second


    def avanzaTurnoAtleta(self, current_match, vincitore):
        vincitore.setCorrente = None
        stato = None
        if vincitore._stato is not None:
            stato = vincitore._stato.avanza()
        if current_match == 15:
            print(f"IL VINCITORE DEL TORNEO È {vincitore.Atleta.cognome}!")
            self.nextPhase()
            return stato
        next_match = 8 + (current_match + 1) // 2
        self.slot_attesa[next_match].append(vincitore)

        if len(self.slot_attesa[next_match]) == 2:
            atleta1 = self.slot_attesa[next_match][0]
            atleta2 = self.slot_attesa[next_match][1]
            self.gestoreMatch.aggiungiMatch(atleta1, atleta2, next_match)
            print(f"Creato Match {next_match}!")

        return stato

    def aggiungiSetPartecipante(self, indexMatch, codice, finalSet):
        return self.gestoreMatch.aggiungiSetPartecipante(indexMatch, codice, finalSet)
