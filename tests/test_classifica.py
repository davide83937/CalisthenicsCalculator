import unittest
from Classifica import Classifica
from Set import Set


class TestClassifica(unittest.TestCase):
    def setUp(self):
        self.classifica = Classifica()

    def test_ordina_meno_di_16_set(self):
        # Inseriamo solo 5 set (simulando i primi atleti in gara)
        for i in range(5):
            mio_set = Set(i)
            self.classifica.listaSet.append(mio_set)

        # La classifica non deve essere generata se non ci sono 16 set
        self.assertIsNone(self.classifica.getClassificaOrdinata())

    def test_ordina_piu_di_16_set_ordinamento_corretto(self):
        # Inseriamo 16 set con punteggi crescenti da 1.0 a 16.0
        for i in range(1, 17):
            mio_set = Set(cod_atleta=i)
            mio_set.punteggio_totale = float(i)
            self.classifica.listaSet.append(mio_set)

        risultato = self.classifica.getClassificaOrdinata()

        self.assertIsNotNone(risultato)
        self.assertEqual(len(risultato), 16)

        # Verifica l'ordinamento: Il primo in classifica (indice 0)
        # deve essere l'atleta 16 con punteggio 16.0
        primo_classificato = risultato[0]
        self.assertEqual(primo_classificato[0], 16)  # cod_atleta
        self.assertEqual(primo_classificato[1], 16.0)  # punteggio_totale
        self.assertEqual(primo_classificato[2], 1)  # posizione

    def test_scarto_set_peggiori_stesso_atleta(self):
        # Inseriamo 16 set per 16 atleti diversi (tutti con 10.0 punti)
        for i in range(1, 17):
            mio_set = Set(cod_atleta=i)
            mio_set.punteggio_totale = 10.0
            self.classifica.listaSet.append(mio_set)

        # Manuel Caruso (atleta 1) fa un secondo set clamoroso da 25.0 punti!
        set_migliore = Set(cod_atleta=1)
        set_migliore.punteggio_totale = 25.0
        self.classifica.listaSet.append(set_migliore)

        risultato = self.classifica.getClassificaOrdinata()

        # L'atleta 1 deve essere primo in classifica con 25.0 punti
        self.assertEqual(risultato[0][0], 1)
        self.assertEqual(risultato[0][1], 25.0)

        # Verifichiamo che l'atleta 1 NON compaia due volte in classifica
        presenze_atleta_1 = sum(1 for riga in risultato if riga[0] == 1)
        self.assertEqual(presenze_atleta_1, 1)