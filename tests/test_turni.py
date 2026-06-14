import unittest
from Ottavo import Ottavo
from Quarto import Quarto
from Semifinale import Semifinale
from Finale import Finale
from StatoQualificazioni import StatoQualificazioni
from StatoTurni import StatoTurni
from StatoConcluso import StatoConcluso


# --- Mock Context per testare isolatamente gli stati ---
class MockCompetizione:
    def __init__(self):
        self.statoCorrente = None

    def transitionTo(self, nuovo_stato):
        self.statoCorrente = nuovo_stato


class MockAtletaInGara:
    def __init__(self):
        self.stato_turno = None

    def passaIlTurno(self, nuovo_stato):
        self.stato_turno = nuovo_stato


# --- Suite di Test per lo State Pattern ---
class TestStatePattern(unittest.TestCase):

    def test_transizioni_stato_competizione(self):
        # 1. Testiamo il ciclo di vita principale del torneo
        comp = MockCompetizione()
        stato_iniziale = StatoQualificazioni(comp)
        comp.statoCorrente = stato_iniziale

        # Dalle qualificazioni passiamo ai turni a eliminazione
        comp.statoCorrente.avanza()
        self.assertIsInstance(comp.statoCorrente, StatoTurni)

        # Dai turni passiamo alla conclusione del torneo
        comp.statoCorrente.avanza()
        self.assertIsInstance(comp.statoCorrente, StatoConcluso)

    def test_transizione_turno_ottavo_a_quarto(self):
        # 2. Testiamo l'avanzamento nel tabellone di un atleta
        atleta_mock = MockAtletaInGara()
        stato_ottavo = Ottavo()
        stato_ottavo.context = atleta_mock

        # L'atleta vince e avanza
        stato_ottavo.avanza()

        # Verifichiamo l'oggetto reale dello State Pattern, non la stringa!
        self.assertIsInstance(atleta_mock.stato_turno, Quarto)

    def test_transizione_turno_quarto_a_semifinale(self):
        atleta_mock = MockAtletaInGara()
        stato_quarto = Quarto()
        stato_quarto.context = atleta_mock

        stato_quarto.avanza()
        self.assertIsInstance(atleta_mock.stato_turno, Semifinale)

    def test_transizione_turno_semifinale_a_finale(self):
        atleta_mock = MockAtletaInGara()
        stato_semifinale = Semifinale()
        stato_semifinale.context = atleta_mock

        stato_semifinale.avanza()
        self.assertIsInstance(atleta_mock.stato_turno, Finale)