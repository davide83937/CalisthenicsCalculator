class Set:
    def __init__(self, cod_atleta):
        self.cod_atleta = cod_atleta
        self.lista_linee = []  # Conterrà gli oggetti SetLine
        self.punteggio_totale = 0.0
        self.bonus_applicati = []

    """def __str__(self):
      
        return (f"Set Atleta {self.cod_atleta}:\n"
                f"{len(self.lista_linee)} skill, \n"
                f"Punteggio: {self.punteggio_totale} \n"
                f"(Bonus: {', '.join(self.bonus_applicati) if self.bonus_applicati else 'Nessuno'})")"""

    def __str__(self):
        # 1. Prepariamo la stringa dei bonus con il separatore 'a capo' fuori dalla f-string
        separator = "\n"
        stringa_bonus = separator.join(self.bonus_applicati) if self.bonus_applicati else "Nessuno"

        # 2. Componiamo il return usando la variabile d'appoggio
        return (
            f"Set Atleta {self.cod_atleta}:\n"
            f"{len(self.lista_linee)} skill, \n"
            f"Punteggio: {self.punteggio_totale} \n"
            f"Bonus:\n{stringa_bonus}"
        )