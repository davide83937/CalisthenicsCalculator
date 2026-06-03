class Classifica:
    def __init__(self):
        self.listaSet = []
        self.classificaOrdinata = []

    def ordinaClassifica(self):
        # --- INIZIO DEBUG ---
        print("\n--- VERIFICA PUNTEGGI IN LISTA SET ---")
        if not self.listaSet:
            print("ATTENZIONE: self.listaSet è VUOTA! Nessun set è stato aggiunto alla classifica.")
        else:
            for s in self.listaSet:
                print(s)
        print("--------------------------------------\n")
        # --- FINE DEBUG ---

        # Svuotiamo la classifica per ricrearla pulita
        self.classificaOrdinata = []

        # Ordiniamo la lista dei set in base al punteggio_totale, in ordine decrescente
        set_ordinati = sorted(self.listaSet, key=lambda x: x.punteggio_totale, reverse=True)

        pos = 1
        lista_atleti_inseriti = []

        for s in set_ordinati:
            # Opzionale: inseriamo solo il set con il punteggio migliore per un atleta.
            # Se vuoi che un atleta appaia più volte in classifica con set diversi,
            # puoi rimuovere questo 'if'.
            if s.cod_atleta not in lista_atleti_inseriti:
                item_classifica = [s.cod_atleta, s.punteggio_totale, pos]
                self.classificaOrdinata.append(item_classifica)

                lista_atleti_inseriti.append(s.cod_atleta)
                pos += 1

    def getClassificaOrdinata(self):
        self.ordinaClassifica()
        return self.classificaOrdinata

