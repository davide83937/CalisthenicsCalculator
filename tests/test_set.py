import unittest
from Set import Set


class TestSet(unittest.TestCase):
    def test_creazione_set(self):
        # Passiamo SOLO il cod_atleta, come richiede il tuo nuovo codice!
        mio_set = Set(1)

        self.assertEqual(mio_set.cod_atleta, 1)
        self.assertEqual(mio_set.lista_linee, [])
        self.assertEqual(mio_set.punteggio_totale, 0.0)
        self.assertEqual(mio_set.bonus_applicati, [])

    def test_stampa_str_senza_bonus(self):
        mio_set = Set(1)
        stringa_attesa = (
            "Set Atleta 1:\n"
            "0 skill, \n"
            "Punteggio: 0.0 \n"
            "Bonus:\n"
            "Nessuno"
        )
        self.assertEqual(str(mio_set), stringa_attesa)

    def test_stampa_str_con_bonus_e_skill(self):
        mio_set = Set(2)
        # Simuliamo l'aggiunta di skill e bonus
        mio_set.lista_linee = ["Skill_Finta_1", "Skill_Finta_2"]
        mio_set.punteggio_totale = 12.5
        mio_set.bonus_applicati = ["Completezza (+5)", "Combo (+2)"]

        stringa_attesa = (
            "Set Atleta 2:\n"
            "2 skill, \n"
            "Punteggio: 12.5 \n"
            "Bonus:\n"
            "Completezza (+5)\n"
            "Combo (+2)"
        )
        self.assertEqual(str(mio_set), stringa_attesa)