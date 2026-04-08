class Set:
    def __init__(self, cod_atleta):
        self.cod_atleta = cod_atleta
        self.lista_linee = []  # Conterrà gli oggetti SetLine
        self.punteggio_totale = 0.0
        self.bonus_applicati = []

    def __str__(self):
        return (f"Set Atleta {self.cod_atleta}: "
                f"{len(self.lista_linee)} skill, "
                f"Punteggio: {self.punteggio_totale} "
                f"(Bonus: {', '.join(self.bonus_applicati) if self.bonus_applicati else 'Nessuno'})")