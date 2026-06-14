import unittest
from Skill import Skill
from SetBuilderConcrete import SetBuilderConcrete
from Director import DirectorBuilder


class TestBuilderPattern(unittest.TestCase):
    def setUp(self):
        # 1. Creiamo un catalogo fittizio di Skill per i test
        self.skill_1 = Skill("Planche", "Isometriche", 10.0)
        self.skill_2 = Skill("Muscle Up", "Dinamiche", 8.0)
        self.skill_3 = Skill("Pike", "Flessibilita", 5.0)
        self.skill_4 = Skill("Pull Up", "Endurance", 6.0)

        self.elenco_skills = [self.skill_1, self.skill_2, self.skill_3, self.skill_4]

    def test_punteggio_parziale_senza_bonus(self):
        # Verifica il corretto funzionamento del ConcreteBuilder
        builder = SetBuilderConcrete(cod_atleta=1, lista=self.elenco_skills)

        # Aggiungiamo una skill con malus del 20% (0.2)
        riga = builder.creaSetLine(self.skill_1, 0.2)
        builder.calcolaPunteggioParziale(riga, self.elenco_skills)

        # Planche vale 10.0. 10.0 - 20% = 8.0
        set_finito = builder.get_result()
        self.assertEqual(set_finito.punteggio_totale, 8.0)
        self.assertEqual(len(set_finito.bonus_applicati), 0)

    def test_director_applica_bonus_completezza(self):
        # Verifica che il Director applichi il DecoratorCompletezza (+7 punti)
        builder = SetBuilderConcrete(cod_atleta=1, lista=self.elenco_skills)

        # Inseriamo 4 skill di 4 categorie diverse
        builder.creaSetLine(self.skill_1, 0.0)
        builder.creaSetLine(self.skill_2, 0.0)
        builder.creaSetLine(self.skill_3, 0.0)
        builder.creaSetLine(self.skill_4, 0.0)

        # Affidiamo il builder al Director. n_combo = 0.
        director = DirectorBuilder(builder, self.elenco_skills, n_combo=0)
        set_finito = director.get_result().get_result()

        # Ci aspettiamo 7 punti base (per via del bonus) e la stringa in lista
        self.assertIn("completezza", set_finito.bonus_applicati)
        self.assertEqual(set_finito.punteggio_totale, 7.0)

    def test_director_non_applica_completezza(self):
        # Verifica che NON applichi il bonus se mancano le categorie
        builder = SetBuilderConcrete(cod_atleta=1, lista=self.elenco_skills)

        # Inseriamo solo 2 skill
        builder.creaSetLine(self.skill_1, 0.0)
        builder.creaSetLine(self.skill_2, 0.0)

        director = DirectorBuilder(builder, self.elenco_skills, n_combo=0)
        set_finito = director.get_result().get_result()

        self.assertNotIn("completezza", set_finito.bonus_applicati)
        self.assertEqual(set_finito.punteggio_totale, 0.0)

    def test_director_applica_bonus_combo(self):
        # Verifica che il DecoratorCombo funzioni (n_combo * 6 punti)
        builder = SetBuilderConcrete(cod_atleta=1, lista=self.elenco_skills)

        # Inseriamo 4 skill qualsiasi per fare una combo (la regola è >= n_combo*4)
        for _ in range(4):
            builder.creaSetLine(self.skill_1, 0.0)

        # Richiediamo 1 combo (n_combo = 1)
        director = DirectorBuilder(builder, self.elenco_skills, n_combo=1)
        set_finito = director.get_result().get_result()

        # bonus = 6 * 1 = 6 punti
        self.assertIn("combo", set_finito.bonus_applicati)
        self.assertEqual(set_finito.punteggio_totale, 6.0)