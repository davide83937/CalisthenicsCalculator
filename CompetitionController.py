import Competizione as comp

class CompetitionController:
    def __init__(self, storage):
        self.storage = storage
        self.competizioneAttuale = None

    def registraSet(self, final_set, code , index ):
        winner, stato = self.competizioneAttuale.requestRegistraSet(final_set, code, index)
        if winner is not None:
            return winner, stato
        return None, stato


    def generaClassifica(self):
        return self.competizioneAttuale.requestGeneraClassifica()


    def creaMatch(self):
        index, first, second = self.competizioneAttuale.getDueSfidanti()
        return index, first, second



    def creaNuovaCompetizione(self, lista):
        self.competizioneAttuale = comp.Competizione()

        for cod in lista:
            if cod in self.storage.elencoAtleti:
                atleta = self.storage.elencoAtleti[cod]
                self.competizioneAttuale.inserisciPartecipanti(atleta)