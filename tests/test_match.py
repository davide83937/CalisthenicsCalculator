import unittest
from Match import Match
from GestoreMatch import GestoreMatch


class MockSet:
    def __init__(self, punteggio):
        self.punteggio_totale = punteggio


class MockAtleta:
    def __init__(self, cognome):
        self.cognome = cognome


class MockAtletaInGara:
    def __init__(self, codice, cognome):
        self.codice = codice
        self.Atleta = MockAtleta(cognome)
        self.setCorrente = None

    def getCodiceAtletaInGara(self):
        return self.codice


class TestGestioneMatch(unittest.TestCase):
    def setUp(self):
        self.gaggi = MockAtletaInGara(1, "Yatarov")
        self.manuel = MockAtletaInGara(2, "Caruso")
        self.match = Match(1, self.gaggi, self.manuel)

        self.gestore = GestoreMatch()
        self.gestore.listaMatch.append(self.match)

    def test_risolvi_match_vince_atleta1(self):
        self.match.setSetAtletaInGara1(MockSet(25.0))
        self.match.setSetAtletaInGara2(MockSet(20.0))

        vincitore = self.match.risolvi()

        self.assertIsNotNone(vincitore)
        self.assertEqual(vincitore.codice, 1)
        self.assertEqual(self.match.Winner.Atleta.cognome, "Yatarov")

    def test_risolvi_match_vince_atleta2(self):
        self.match.setSetAtletaInGara1(MockSet(15.0))
        self.match.setSetAtletaInGara2(MockSet(28.5))
        vincitore = self.match.risolvi()

        self.assertEqual(vincitore.codice, 2)
        self.assertEqual(self.match.Winner.Atleta.cognome, "Caruso")

    def test_gestore_match_aggiungi_set_e_risolvi(self):
        risultato_parziale = self.gestore.aggiungiSetPartecipante(index=1, cod=1, setCorrente=MockSet(30.0))
        self.assertIsNone(risultato_parziale)

        vincitore_finale = self.gestore.aggiungiSetPartecipante(index=1, cod=2, setCorrente=MockSet(32.0))

        self.assertIsNotNone(vincitore_finale)
        self.assertEqual(vincitore_finale.Atleta.cognome, "Caruso")