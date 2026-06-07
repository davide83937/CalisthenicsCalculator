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
        indexMatch, winner = self.gestoreTorneo.aggiungiSetPartecipante(index,cod, final_set)
        if winner is not None:
            self.aggiungiQuarto(index, winner)
            return indexMatch, winner
        return 10000, None

    def aggiungiQuarto(self, index, vincitore):
        if 1 <= index <= 8:
            # Calcola in quale quarto va (1, 2, 3 o 4)
            quarto_index = (index - 1) // 2 + 1

            # Mettiamo l'atleta in attesa per quel quarto di finale
            self.slot_quarti[quarto_index].append(vincitore)

            # Se lo slot si è riempito (entrambi hanno vinto i rispettivi ottavi)
            if len(self.slot_quarti[quarto_index]) == 2:
                atleta1 = self.slot_quarti[quarto_index][0]
                atleta2 = self.slot_quarti[quarto_index][1]

                # Creiamo l'indice per il nuovo match.
                # Se gli ottavi sono 1-8, i quarti saranno 9, 10, 11 e 12.
                nuovo_indice_match = 8 + quarto_index
                self.gestoreTorneo.aggiungiMatch(atleta1, atleta2, nuovo_indice_match)
                print(f"Creato Match {nuovo_indice_match} per i Quarti di Finale!")

