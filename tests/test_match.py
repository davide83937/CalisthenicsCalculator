import unittest
from Match import Match
from GestoreMatch import GestoreMatch


# --- Classi Mock per isolare i test ---
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


# --- Suite di Test ---
class TestGestioneMatch(unittest.TestCase):
    def setUp(self):
        # Prepariamo due sfidanti simulati
        self.gaggi = MockAtletaInGara(1, "Yatarov")
        self.manuel = MockAtletaInGara(2, "Caruso")

        # Creiamo un match di prova (Match numero 1)
        self.match = Match(1, self.gaggi, self.manuel)

        # Creiamo il gestore
        self.gestore = GestoreMatch()
        self.gestore.listaMatch.append(self.match)

    def test_risolvi_match_vince_atleta1(self):
        # Assegniamo i set: Gaggi 25.0, Manuel 20.0
        self.match.setSetAtletaInGara1(MockSet(25.0))
        self.match.setSetAtletaInGara2(MockSet(20.0))

        vincitore = self.match.risolvi()

        # Deve vincere Gaggi (Atleta 1)
        self.assertIsNotNone(vincitore)
        self.assertEqual(vincitore.codice, 1)
        self.assertEqual(self.match.Winner.Atleta.cognome, "Yatarov")

    def test_risolvi_match_vince_atleta2(self):
        # Assegniamo i set: Gaggi 15.0, Manuel 28.5
        self.match.setSetAtletaInGara1(MockSet(15.0))
        self.match.setSetAtletaInGara2(MockSet(28.5))

        vincitore = self.match.risolvi()

        # Deve vincere Manuel (Atleta 2)
        self.assertEqual(vincitore.codice, 2)
        self.assertEqual(self.match.Winner.Atleta.cognome, "Caruso")

    def test_gestore_match_aggiungi_set_e_risolvi(self):
        # Testiamo il flusso completo tramite il GestoreMatch
        # Il match è ancora in sospeso (manca il set di Manuel)
        risultato_parziale = self.gestore.aggiungiSetPartecipante(index=1, cod=1, setCorrente=MockSet(30.0))
        self.assertIsNone(risultato_parziale)  # Non c'è ancora un vincitore

        # Manuel inserisce il suo set, la funzione dovrebbe ora restituire il vincitore
        vincitore_finale = self.gestore.aggiungiSetPartecipante(index=1, cod=2, setCorrente=MockSet(32.0))

        self.assertIsNotNone(vincitore_finale)
        self.assertEqual(vincitore_finale.Atleta.cognome, "Caruso")