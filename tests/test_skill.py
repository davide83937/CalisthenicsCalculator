import unittest
from Skill import Skill


class TestSkill(unittest.TestCase):
    def test_creazione_e_repr(self):
        skill = Skill("Planche", "Spinta", 5.0)

        # Test degli attributi
        self.assertEqual(skill.nome, "Planche")
        self.assertEqual(skill.categoria, "Spinta")
        self.assertEqual(skill.punteggio, 5.0)

        # Test della rappresentazione a stringa
        stringa_attesa = "Skill(nome='Planche', categoria='Spinta', punteggio=5.0)"
        self.assertEqual(repr(skill), stringa_attesa)