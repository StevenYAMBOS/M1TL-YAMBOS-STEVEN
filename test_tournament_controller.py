# CTM\test_tournament_controller.py

import unittest
from unittest.mock import patch, MagicMock
from Controllers.TournamentController import TournamentController

class TestTournamentController(unittest.TestCase):
    def setUp(self):
        self.controller = TournamentController()

    @patch('Controllers.TournamentController.TournamentView.get_tournament_info', return_value=('Tournament Name', 'Location', '2024-01-01', '2024-01-05', 4, 'Description'))
    @patch('Controllers.TournamentController.Tournament.save_tournament')
    def test_create_tournament(self, mock_save_tournament, mock_get_tournament_info):
        self.controller.create_tournament()
        mock_get_tournament_info.assert_called_once()
        mock_save_tournament.assert_called_once()

    @patch('Controllers.TournamentController.Tournament.get_tournaments', return_value=[{'id': 1, 'name': 'Tournament 1', 'rounds': 3, 'player_list': []}])
    @patch('Controllers.TournamentController.Player.get_players', return_value=[{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'score': 0}])
    @patch('Controllers.TournamentController.TournamentView.select_tournament', return_value=1)
    @patch('Controllers.TournamentController.PlayerView.select_player', return_value=0)
    @patch('builtins.input', side_effect=['n'])
    def test_add_player_to_tournament(self, mock_input, mock_select_player, mock_select_tournament, mock_get_players, mock_get_tournaments):
        self.controller.add_player_to_tournament()
        mock_get_tournaments.assert_called_once()
        mock_get_players.assert_called_once()
        mock_select_tournament.assert_called_once()
        mock_select_player.assert_called_once()
        mock_input.assert_called_once()

if __name__ == '__main__':
    unittest.main()