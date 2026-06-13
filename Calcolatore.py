import Storage as s
import SetBuilderConcrete as set
import Director as d

class Calcolatore:

    def __init__(self, storage):
        self.setCorrente = None
        self.storage = storage


    def setSetCorrente(self, cod):
        self.setCorrente = set.SetBuilderConcrete(cod, self.storage.elencoSkills)
        self.setCorrente.cod_atleta = cod

    def inserisciSkillInSet(self, nomeSkill, malus):
        for sk in self.storage.elencoSkills:
            if sk.nome == nomeSkill.get():
                self.setCorrente.creaSetLine(sk, malus)

    def calcolaPunteggioSet(self, n_combo):
        set_prodotto = self.setCorrente.get_result()
        for sl in set_prodotto.lista_linee:
            self.setCorrente.calcolaPunteggioParziale(sl, self.storage.elencoSkills)
        director = d.DirectorBuilder(self.setCorrente, self.storage.elencoSkills, n_combo)
        self.setCorrente = director.get_result()
        final_set = self.setCorrente.get_result()
        return final_set

    def getPunteggioFinale(self):
        final_set = self.setCorrente.get_result()
        result = f"Punteggio complessivo = {final_set.punteggio_totale}"
        return result