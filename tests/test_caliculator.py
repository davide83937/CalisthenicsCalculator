import unittest
from Caliculator import Caliculator


class MockApp:
    def add_line(self, *args):
        pass


class TestCaliculator(unittest.TestCase):
    def setUp(self):
        # Resetta il Singleton per evitare che i test si influenzino a vicenda
        Caliculator._instance = None
        self.app = MockApp()
        self.calc = Caliculator(self.app)

    def test_singleton(self):
        # Verifica che istanziando di nuovo si ottenga lo stesso oggetto in memoria
        calc2 = Caliculator(self.app)
        self.assertIs(self.calc, calc2)

    def test_calcola_codice(self):
        # Testiamo il calcolo dell'ID progressivo
        self.calc.elencoAtleti = {0: "mock_atleta_0", 1: "mock_atleta_1"}
        nuovo_codice = self.calc.calcola_codice(self.calc.elencoAtleti)
        self.assertEqual(nuovo_codice, 2)

    def test_inserisciDati_successo(self):
        # Inserimento dati corretto che restituisce 0
        res = self.calc.inserisciDati("Luigi", "Verdi", 30, "VRDLGU90M01H501Z", "3337654321", "luigi@email.com", 1.75,
                                      70.0)
        self.assertEqual(res, 0)
        self.assertIsNotNone(self.calc.atletaCorrente)
        self.assertEqual(self.calc.atletaCorrente.nome, "Luigi")

    def test_inserisciDati_errori(self):
        # Valori validi di base per testare le varianti errate
        dati = ["Luigi", "Verdi", 30, "VRDLGU90M01H501Z", "3337654321", "luigi@email.com", 1.75, 70.0]

        # Errore 1: nome vuoto
        self.assertEqual(self.calc.inserisciDati("", dati[1], dati[2], dati[3], dati[4], dati[5], dati[6], dati[7]), 1)
        # Errore 2: cognome vuoto
        self.assertEqual(self.calc.inserisciDati(dati[0], "", dati[2], dati[3], dati[4], dati[5], dati[6], dati[7]), 2)
        # Errore 3: età non intera
        self.assertEqual(self.calc.inserisciDati(dati[0], dati[1], "30", dati[3], dati[4], dati[5], dati[6], dati[7]),
                         3)
        # Errore 4: CF non di 16 caratteri
        self.assertEqual(
            self.calc.inserisciDati(dati[0], dati[1], dati[2], "CF_ERRATO", dati[4], dati[5], dati[6], dati[7]), 4)
        # Errore 5: cellulare non di 10 caratteri
        self.assertEqual(self.calc.inserisciDati(dati[0], dati[1], dati[2], dati[3], "333", dati[5], dati[6], dati[7]),
                         5)
        # Errore 6: email vuota
        self.assertEqual(self.calc.inserisciDati(dati[0], dati[1], dati[2], dati[3], dati[4], "", dati[6], dati[7]), 6)
        # Errore 7: altezza non float
        self.assertEqual(self.calc.inserisciDati(dati[0], dati[1], dati[2], dati[3], dati[4], dati[5], 175, dati[7]), 7)
        # Errore 8: peso non float
        self.assertEqual(self.calc.inserisciDati(dati[0], dati[1], dati[2], dati[3], dati[4], dati[5], dati[6], 70), 8)