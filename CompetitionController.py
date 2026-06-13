import Competizione as comp

class CompetitionController:
    def __init__(self, storage):
        self.storage = storage
        self.competizioneAttuale = None

    def registraSet(self, final_set, code , index ):
        winner, stato = self.competizioneAttuale.requestRegistraSet(final_set, code, index)

        #result = f"Punteggio complessivo = {final_set.punteggio_totale}"
        if winner is not None:
            return winner, stato
        return None, stato


    def generaClassifica(self):
        return self.competizioneAttuale.requestGeneraClassifica()


    def creaMatch(self):
        index, first, second = self.competizioneAttuale.getDueSfidanti()
        return index, first, second



    def creaNuovaCompetizione(self, lista):
        # 1. Crei l'istanza della competizione
        self.competizioneAttuale = comp.Competizione()

        # 2. Cicli direttamente sui codici ricevuti nella lista
        for cod in lista:
            # 3. Verifichi se il codice esiste nell'elenco degli atleti
            if cod in self.storage.elencoAtleti:
                # Prendi l'oggetto atleta usando la chiave 'cod'
                atleta = self.storage.elencoAtleti[cod]
                # 4. Chiami il metodo SULL'ISTANZA appena creata, passando l'atleta
                self.competizioneAttuale.inserisciPartecipanti(atleta)