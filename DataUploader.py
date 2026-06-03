import Skill as sk
import Atleta as a

class DataUploader:

    def carica_atleti(self, elencoAtleti, app):
        f = open("atleti.txt","r")
        line = f.readline()
        while line !="":
            attributi = line.strip().split()
            codice = int(attributi[0])
            nome = attributi[1]
            cognome = attributi[2]
            età = int(attributi[3])
            cod_fiscale = attributi[4]
            n_cellulare = attributi[5]
            email = attributi[6]
            altezza = float(attributi[7])
            peso = float(attributi[8])
            atleta = a.Atleta(codice, nome, cognome, età, cod_fiscale, n_cellulare, email, altezza, peso)
            elencoAtleti[atleta.codice] = atleta
            line = f.readline()
        for codice, atl in elencoAtleti.items():
            app.add_line(codice, atl.nome, atl.cognome)
        f.close()


    def carica_skill(self, elencoSkills):
        f = open("skills.txt", "r")
        line = f.readline()
        while line !="":
            attributi = line.strip().split()
            nome = attributi[0]
            categoria = attributi[1]
            valore = float(attributi[2])
            skill = sk.Skill(nome, categoria, valore)
            elencoSkills.append(skill)
            line = f.readline()
        f.close()