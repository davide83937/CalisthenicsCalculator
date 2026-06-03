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
                # Questo userà automaticamente il metodo __str__ di Set.py
                print(s)
        print("--------------------------------------\n")
        # --- FINE DEBUG ---

        # Da qui in poi lasci il tuo codice di ordinamento...
        # (Ti consiglio sempre di usare il sorted() che ti ho mostrato prima)

        n = len(self.listaSet)
        i = n
        pos = 1
        lista_temp = []

        while i > 0:
            max = 0
            set_max = None
            item_classifica = []
            for set in self.listaSet:
                if set.punteggio_totale > max and set.cod_atleta not in lista_temp:
                    max = set.punteggio_totale
                    set_max = set
            item_classifica.append(set_max.cod_atleta)
            item_classifica.append(set_max.punteggio_totale)
            item_classifica.append(pos)
            lista_temp.append(set_max.cod_atleta)
            self.classificaOrdinata.append(item_classifica)
            pos = pos + 1
            i = i - 1

    def getClassificaOrdinata(self):
        self.ordinaClassifica()
        return self.classificaOrdinata

