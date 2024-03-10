# test_player_controller.py

import unittest
from unittest.mock import patch
from Controllers.PlayerController import PlayerController

class TestPlayerController(unittest.TestCase):
    def setUp(self):
        self.player_controller = PlayerController()

    @patch('Controllers.PlayerController.PlayerView.get_player_info', return_value=('John', 'Doe', '1990-01-01', '12345'))
    @patch('Controllers.PlayerController.Player.save_player')
    def test_add_player(self, mock_save_player, mock_get_player_info):
        self.player_controller.add_player()
        mock_save_player.assert_called_once()  # Vérifie que la méthode save_player() est appelée une fois

if __name__ == '__main__':
    unittest.main()
