# CTM\test_report_controller.py

import unittest
from unittest.mock import patch, MagicMock
from Controllers.ReportController import ReportController

class TestReportController(unittest.TestCase):
    def setUp(self):
        self.report_controller = ReportController()

    @patch('Controllers.ReportController.Report.load_players', return_value=[
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Alice', 'last_name': 'Smith'},
        {'first_name': 'Bob', 'last_name': 'Johnson'}
    ])
    def test_players_alphabetical(self, mock_load_players):
        sorted_players = self.report_controller.players_alphabetical()
        expected_result = [
            {'first_name': 'John', 'last_name': 'Doe'},
            {'first_name': 'Bob', 'last_name': 'Johnson'},
            {'first_name': 'Alice', 'last_name': 'Smith'}
        ]
        self.assertEqual(sorted_players, expected_result)

    @patch('Controllers.ReportController.Report.load_tournaments', return_value=[
        {'name': 'Tournament 1', 'round_list': [], 'id': 1},
        {'name': 'Tournament 2', 'round_list': [], 'id': 2},
        {'name': 'Tournament 3', 'round_list': [], 'id': 3}
    ])
    @patch('builtins.input', side_effect=['2'])
    def test_select_tournament_from_list(self, mock_input, mock_load_tournaments):
        selected_tournament = self.report_controller.select_tournament_from_list()
        expected_result = {'name': 'Tournament 2', 'round_list': [], 'id': 2}
        self.assertEqual(selected_tournament, expected_result)

    @patch('Controllers.ReportController.Report.load_tournaments', return_value=[
        {'name': 'Tournament 1', 'player_list': [{'first_name': 'John', 'last_name': 'Doe', 'score': 5},
                                                 {'first_name': 'Alice', 'last_name': 'Smith', 'score': 8},
                                                 {'first_name': 'Bob', 'last_name': 'Johnson', 'score': 7}],
         'id': 1}
    ])
    def test_tournament_players_alphabetical(self, mock_load_tournaments):
        with patch('builtins.input', return_value='1'):
            sorted_players = self.report_controller.tournament_players_alphabetical()
        expected_result = [{'first_name': 'John', 'last_name': 'Doe', 'score': 5},
                           {'first_name': 'Bob', 'last_name': 'Johnson', 'score': 7},
                           {'first_name': 'Alice', 'last_name': 'Smith', 'score': 8}]
        self.assertEqual(sorted_players, expected_result)

    @patch('Controllers.ReportController.Report.load_tournaments', return_value=[
        {'name': 'Tournament 1', 'round_list': [], 'id': 1},
        {'name': 'Tournament 2', 'round_list': [], 'id': 2},
        {'name': 'Tournament 3', 'round_list': [], 'id': 3}
    ])
    @patch('builtins.input', return_value='2')
    def test_get_tournament_rounds_and_matches(self, mock_input, mock_load_tournaments):
        tournament_name, rounds, tournament_id = self.report_controller.get_tournament_rounds_and_matches()
        expected_tournament_name = 'Tournament 2'
        expected_rounds = []
        expected_tournament_id = 2
        self.assertEqual(tournament_name, expected_tournament_name)
        self.assertEqual(rounds, expected_rounds)
        self.assertEqual(tournament_id, expected_tournament_id)

    @patch('Controllers.ReportController.Report.load_tournaments', return_value=[
        {'name': 'Tournament 1', 'player_list': [{'first_name': 'John', 'last_name': 'Doe', 'score': 5},
                                                 {'first_name': 'Alice', 'last_name': 'Smith', 'score': 8},
                                                 {'first_name': 'Bob', 'last_name': 'Johnson', 'score': 7}],
         'id': 1}
    ])
    def test_get_tournament_players_sorted(self, mock_load_tournaments):
        sorted_players = self.report_controller.get_tournament_players_sorted(1)
        expected_result = [{'first_name': 'Alice', 'last_name': 'Smith', 'score': 8},
                           {'first_name': 'Bob', 'last_name': 'Johnson', 'score': 7},
                           {'first_name': 'John', 'last_name': 'Doe', 'score': 5}]
        self.assertEqual(sorted_players, expected_result)

if __name__ == '__main__':
    unittest.main()
