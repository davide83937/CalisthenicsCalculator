class Classifica:
    def __init__(self):
        self.listaSet = []
        self.classificaOrdinata = []

    def ordinaClassifica(self):
        if len(self.listaSet) < 16:
            return None
        self.classificaOrdinata = []
        set_ordinati = sorted(self.listaSet, key=lambda x: x.punteggio_totale, reverse=True)
        pos = 1
        lista_atleti_inseriti = []

        for s in set_ordinati:
            if s.cod_atleta not in lista_atleti_inseriti:
                item_classifica = [s.cod_atleta, s.punteggio_totale, pos]
                self.classificaOrdinata.append(item_classifica)
                lista_atleti_inseriti.append(s.cod_atleta)
                pos += 1
        return True

    def getClassificaOrdinata(self):
        b = self.ordinaClassifica()
        if b is None:
            return None
        return self.classificaOrdinata

