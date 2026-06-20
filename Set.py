class Set:
    def __init__(self, cod_atleta):
        self.cod_atleta = cod_atleta
        self.lista_linee = []
        self.punteggio_totale = 0.0
        self.bonus_applicati = []



    def __str__(self):
        separator = "\n"
        stringa_bonus = separator.join(self.bonus_applicati) if self.bonus_applicati else "Nessuno"

        return (
            f"Set Atleta {self.cod_atleta}:\n"
            f"{len(self.lista_linee)} skill, \n"
            f"Punteggio: {self.punteggio_totale} \n"
            f"Bonus:\n{stringa_bonus}"
        )