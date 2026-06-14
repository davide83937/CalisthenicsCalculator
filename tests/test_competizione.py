import unittest
from Competizione import Competizione
from Atleta import Atleta
from Set import Set


class TestCompetizione(unittest.TestCase):
    def setUp(self):
        self.comp = Competizione()
        # Creiamo un paio di atleti per i test
        self.a1 = Atleta(1, "Gaggi", "Yatarov", 30, "YTRGGG90M01H501Z", "3331112222", "gaggi@email.it", 1.70, 65.0)
        self.a2 = Atleta(2, "Manuel", "Caruso", 25, "CRSMNL95M01H501Z", "3339998888", "manuel@email.it", 1.75, 70.0)

    def test_inserisci_partecipanti_nuovi(self):
        self.comp.inserisciPartecipanti(self.a1)
        self.comp.inserisciPartecipanti(self.a2)

        self.assertEqual(len(self.comp.lista_partecipanti), 2)
        self.assertEqual(self.comp.lista_partecipanti[0].nome, "Gaggi")

    def test_rifiuta_partecipanti_duplicati(self):
        # Inseriamo Gaggi due volte
        self.comp.inserisciPartecipanti(self.a1)
        self.comp.inserisciPartecipanti(self.a1)

        # La lista deve contenere un solo atleta
        self.assertEqual(len(self.comp.lista_partecipanti), 1)

    def test_inserisci_set_in_classifica(self):
        mio_set = Set(1)
        mio_set.punteggio_totale = 15.5

        self.comp.inserisciSetInClassifica(mio_set)

        # Verifica che il set sia passato correttamente all'oggetto Classifica interno
        self.assertEqual(len(self.comp.classifica.listaSet), 1)
        self.assertEqual(self.comp.classifica.listaSet[0].punteggio_totale, 15.5)