from Atleta import Atleta
from DataUploader import DataUploader


class Storage:

    def __init__(self):
        self.dataUploader = DataUploader()
        self.elencoAtleti = {}
        self.elencoSkills = []

    def carica_atleti(self):
        self.elencoAtleti = self.dataUploader.carica_atleti()

    def carica_skill(self):
        self.elencoSkills = self.dataUploader.carica_skill()

    def getSkillList(self):
        return self.elencoSkills

    def getElencoAtleti(self):
        return self.elencoAtleti

    def getAtletaByIndex(self, index):
        atleta = self.elencoAtleti[index]
        return atleta

    def salvaAtleta(self, atleta: 'Atleta'):
        self.elencoAtleti[atleta.codice] = atleta
        line = (
                    str(atleta.codice) + " " + atleta.nome + " " + atleta.cognome + " " + str(
                atleta.età) +
                    " " + atleta.codice_fiscale + " " + atleta.numero_cellulare + " " + atleta.email + " "
                    + str(atleta.altezza) + " " + str(atleta.peso)+ "\n")
        self.dataUploader.salvaAtleta(line)