from asyncore import write
import Director as d
import Atleta as a
import Skill as sk
import SetBuilderConcrete as set
from Set import Set

class Caliculator:
    _instance = None  # Qui memorizziamo l'istanza unica

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Se non esiste ancora
            cls._instance = super().__new__(cls)
        return cls._instance  # Restituiamo sempre la stessa istanza

    def __init__(self, app):
        if not hasattr(self, "_initialized"):
            print("Inizializzo la calcolatrice...")
            self._initialized = True
            self.elencoAtleti = {}
            self.elencoSkills = []
            self.app = app
            self.atletaCorrente = None
            self.setCorrente = None


    def carica_atleti(self):
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
            self.elencoAtleti[atleta.codice] = atleta
            line = f.readline()
        for codice, atl in self.elencoAtleti.items():
            self.app.add_line(codice, atl.nome, atl.cognome)
        f.close()


    def carica_skill(self):
        f = open("skills.txt", "r")
        line = f.readline()
        while line !="":
            attributi = line.strip().split()
            nome = attributi[0]
            categoria = attributi[1]
            valore = float(attributi[2])
            skill = sk.Skill(nome, categoria, valore)
            self.elencoSkills.append(skill)
            line = f.readline()
        f.close()


    def getSkillList(self):
        return self.elencoSkills


    def calcola_codice(self, lista):
        if not lista:
            return 0
        else:
            i = 0
            for cod in lista.keys():
                if i != cod:
                    return i
                i = i + 1
            return i


    def inserisciDati(self, nome, cognome, età, codice_fiscale, numero_cellulare, email, altezza, peso):
        cod = self.calcola_codice(self.elencoAtleti)
        if nome == "":
            return 1
        elif cognome == "":
            return 2
        elif not isinstance(età, int):
            return 3
        elif str(codice_fiscale).__len__() != 16:
            return 4
        elif str(numero_cellulare).__len__() != 10:
            return 5
        elif email == "":
            print("Email:"+ email)
            return 6
        elif not isinstance(altezza, float):
            return 7
        elif not isinstance(peso, float):
            print("Peso:" + peso)
            return 8
        else:
            self.atletaCorrente = a.Atleta(cod, nome, cognome, età, codice_fiscale, numero_cellulare, email, altezza, peso)
            return 0


    def terminaRegistrazione(self):
        self.elencoAtleti[self.atletaCorrente.codice] = self.atletaCorrente
        f = open("atleti.txt", "a")
        print("file aperto")
        line = (str(self.atletaCorrente.codice)+" "+self.atletaCorrente.nome+" "+self.atletaCorrente.cognome+" "+str(self.atletaCorrente.età)+
                " "+self.atletaCorrente.codice_fiscale+" "+self.atletaCorrente.numero_cellulare+" "+self.atletaCorrente.email+" "
                +str(self.atletaCorrente.altezza)+" "+str(self.atletaCorrente.peso))
        f.write(line)
        f.close()
        self.app.add_line(self.atletaCorrente.codice, self.atletaCorrente.nome, self.atletaCorrente.cognome)

    def valutaAtleta(self, cod):
        self.setCorrente = set.SetBuilderConcrete(0)
        self.setCorrente.cod_atleta = cod

    def inserisciSkillInSet(self, nomeSkill, malus):
        for sk in self.elencoSkills:
            if sk.nome == nomeSkill.get():
                self.setCorrente.creaSetLine(sk, malus)
                #self.setCorrente.listaSkill.append(sl)

    def calcolaPunteggioSet(self):
        # Otteniamo il prodotto dal builder/decorator
        set_prodotto = self.setCorrente.get_result()

        # Iteriamo sulle linee salvate nel prodotto
        for sl in set_prodotto.lista_linee:
            self.setCorrente.calcolaPunteggioParziale(sl, self.elencoSkills)

        # Il DirectorBuilder analizza il set e decide se applicare decorator
        director = d.DirectorBuilder(self.setCorrente, self.elencoSkills)
        self.setCorrente = director.get_result()

        # Recuperiamo il prodotto finale (potenzialmente decorato)
        final_set = self.setCorrente.get_result()
        return f"Punteggio complessivo = {final_set.punteggio_totale}"








