import Director as d
import Atleta as a
import SetBuilderConcrete as set
import Competizione as comp
import DataUploader as du


class Caliculator:
    _instance = None  # Qui memorizziamo l'istanza unica

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Se non esiste ancora
            cls._instance = super().__new__(cls)
        return cls._instance  # Restituiamo sempre la stessa istanza

    def __init__(self):
        if not hasattr(self, "_initialized"):
            print("Inizializzo la calcolatricee...")
            self.competizioneAttuale = None
            self._initialized = True
            self.elencoAtleti = {}
            self.elencoSkills = []
            self.atletaCorrente = None
            self.setCorrente = None
            self.du = du.DataUploader()



    def getCompetizioneAttuale(self):
        return self.competizioneAttuale


    def getElencoAtleti(self):
        return self.elencoAtleti

    def carica_atleti(self):
        self.elencoAtleti = self.du.carica_atleti()

    def carica_skill(self):
        self.elencoSkills = self.du.carica_skill()


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
        line = (
                    str(self.atletaCorrente.codice) + " " + self.atletaCorrente.nome + " " + self.atletaCorrente.cognome + " " + str(
                self.atletaCorrente.età) +
                    " " + self.atletaCorrente.codice_fiscale + " " + self.atletaCorrente.numero_cellulare + " " + self.atletaCorrente.email + " "
                    + str(self.atletaCorrente.altezza) + " " + str(self.atletaCorrente.peso))
        f.write(line)
        f.close()
        return self.atletaCorrente

    def valutaAtleta(self, cod):
        self.setCorrente = set.SetBuilderConcrete(cod, self.elencoSkills)
        self.setCorrente.cod_atleta = cod

    def inserisciSkillInSet(self, nomeSkill, malus):
        for sk in self.elencoSkills:
            if sk.nome == nomeSkill.get():
                self.setCorrente.creaSetLine(sk, malus)

    def calcolaPunteggioSet(self, n_combo, mode):
        set_prodotto = self.setCorrente.get_result()

        for sl in set_prodotto.lista_linee:
            self.setCorrente.calcolaPunteggioParziale(sl, self.elencoSkills)

        director = d.DirectorBuilder(self.setCorrente, self.elencoSkills, n_combo)
        self.setCorrente = director.get_result()

        final_set = self.setCorrente.get_result()
        if mode == "classifica":
            self.competizioneAttuale.inserisciSetInClassifica(final_set)

        return f"Punteggio complessivo = {final_set.punteggio_totale}"

    def generaClassifica(self):
        return self.competizioneAttuale.getClassificaOrdinata()

    def getAtletaByIndex(self, lista):
        for cod in lista:
            if cod in self.elencoAtleti:
                atleta = self.elencoAtleti[cod]
                return atleta

    def creaNuovaCompetizione(self, lista):
        self.competizioneAttuale = comp.Competizione()

        for cod in lista:
            if cod in self.elencoAtleti:
                atleta = self.elencoAtleti[cod]
                self.competizioneAttuale.inserisciPartecipanti(atleta)












