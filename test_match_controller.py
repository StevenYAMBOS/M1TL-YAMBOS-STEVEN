import unittest
from unittest.mock import MagicMock
from Controllers.MatchController import MatchController

class TestMatchController(unittest.TestCase):
    def setUp(self):
        self.match_controller = MatchController()

    def test_create_matches(self):
        # Définir une liste de paires de joueurs
        pairs = [('Player1', 'Player2'), ('Player3', 'Player4')]

        # Appeler la méthode pour créer des matches à partir des paires de joueurs
        matches = self.match_controller.create_matches(pairs)

        # Vérifier que la liste de matches est correcte
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].players, ('Player1', 'Player2'))
        self.assertEqual(matches[1].players, ('Player3', 'Player4'))


    def test_create_matches(self):
        # Définir une liste de paires de joueurs
        pairs = [('Player1', 'Player2'), ('Player3', 'Player4')]

        # Appeler la méthode pour créer des matches à partir des paires de joueurs
        matches = self.match_controller.create_matches(pairs)

        # Vérifier que la liste de matches est correcte
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].players, ('Player1', 'Player2'))
        self.assertEqual(matches[1].players, ('Player3', 'Player4'))

    def test_pair_players(self):
        # Définir une liste de joueurs triée par score et une liste de matches joués précédemment
        sorted_players = [{'first_name': 'Player1_firstname', 'last_name': 'Player1_lastname'}, 
                        {'first_name': 'Player2_firstname', 'last_name': 'Player2_lastname'}, 
                        {'first_name': 'Player3_firstname', 'last_name': 'Player3_lastname'}, 
                        {'first_name': 'Player4_firstname', 'last_name': 'Player4_lastname'}]
        played_matches = [[('Player1_firstname', 'Player2_firstname'), ('Player3_firstname', 'Player4_firstname')]]

        # Appeler la méthode pour appairer les joueurs
        paired_players = self.match_controller.pair_players(sorted_players, played_matches)

        # Vérifier que les joueurs sont correctement appairés
        self.assertEqual(len(paired_players), 2)
        self.assertNotIn(('Player1_firstname', 'Player2_firstname'), paired_players)
        self.assertNotIn(('Player3_firstname', 'Player4_firstname'), paired_players)

    def test_has_played_together(self):
        # Définir deux joueurs et une liste de matches joués précédemment
        player1 = {'first_name': 'Player1_firstname', 'last_name': 'Player1_lastname'}
        player2 = {'first_name': 'Player2_firstname', 'last_name': 'Player2_lastname'}
        played_matches = [[('Player1_firstname', 'Player2_firstname'), ('Player3_firstname', 'Player4_firstname')]]

        # Appeler la méthode pour vérifier si les joueurs ont joué ensemble
        result = self.match_controller.has_played_together(player1, player2, played_matches)

        # Vérifier que le résultat est correct
        self.assertFalse(result)  # False car player1 et player2 n'ont pas joué ensemble dans played_matches

if __name__ == '__main__':
    unittest.main()
