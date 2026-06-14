import unittest
from Atleta import Atleta


class TestAtleta(unittest.TestCase):
    def test_creazione_e_get_codice(self):
        atleta = Atleta(1, "Mario", "Rossi", 25, "RSSMRA99M01H501Z", "3331234567", "mario@email.com", 1.80, 75.0)

        self.assertEqual(atleta.getCodice(), 1)
        self.assertEqual(atleta.nome, "Mario")
        self.assertEqual(atleta.cognome, "Rossi")
        self.assertEqual(atleta.peso, 75.0)
        self.assertEqual(atleta.codice_fiscale, "RSSMRA99M01H501Z")