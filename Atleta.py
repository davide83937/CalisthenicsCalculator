class Atleta:
    def __init__(self, codice, nome, cognome, età, codice_fiscale, numero_cellulare, email, altezza, peso):
        self.email = email
        self.peso = peso
        self.altezza = altezza
        self.numero_cellulare = numero_cellulare
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def getCodice(self):
        return self.codice
