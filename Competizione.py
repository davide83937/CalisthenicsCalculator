import GestoreTorneo as gt
import Classifica as c
import AtletaInGara as ag

class Competizione:
    def __init__(self):
        self.lista_partecipanti = []
        self.stati_partecipanti = {}
        self.classifica = c.Classifica()
        self.gestoreTorneo = gt.GestoreTorneo()
        self.index = 0

    def getPartecipante(self, codice):
        atleta = next((a for a in self.lista_partecipanti if a.codice == codice), None)
        return atleta

    def getStatiPartecipanti(self):
        return self.stati_partecipanti

    def inserisciPartecipanti(self, atleta):
        for a in self.lista_partecipanti:
            if a.codice == atleta.codice:
                return
        self.lista_partecipanti.append(atleta)
        self.stati_partecipanti[atleta.codice] = "qualificazione"

    def inserisciSetInClassifica(self, set):
        self.classifica.listaSet.append(set)

    def getClassificaOrdinata(self):
        return self.classifica.getClassificaOrdinata()

    def getDueSfidanti(self):

        firstAtlhete, secondAtlhete = self.classifica.getDuesfidenti(self.index, self.index + 8)
        atleta1 = self.getPartecipante(firstAtlhete[0])
        atletaInGara1 = ag.AtletaInGara(atleta1)
        atleta2 = self.getPartecipante(secondAtlhete[0])
        atletaInGara2 = ag.AtletaInGara(atleta2)

        self.index = self.index + 1
        self.setDueSfidenti(atletaInGara1, atletaInGara2, self.index)
        return self.index, firstAtlhete, secondAtlhete

    def setDueSfidenti(self, first, second, index):
        self.gestoreTorneo.aggiungiMatch(first, second, index)

    def aggiungiSetSfidante(self, final_set, cod, index):
        self.gestoreTorneo.aggiungiSetPartecipante(index,cod, final_set)


