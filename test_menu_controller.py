# CTM\test_menu_controller.py

import unittest
import sys
from unittest.mock import patch
from Controllers.MenuController import MenuController
import io

class TestMenuController(unittest.TestCase):
    def setUp(self):
        self.menu_controller = MenuController()

    def test_report_menu_choice(self):
        # Simulation de l'entrée utilisateur
        with patch('builtins.input', side_effect=['0']):
            # Appel de report_menu_choice et capture de la sortie
            output = io.StringIO()
            sys.stdout = output  # Redirection de la sortie standard

            self.menu_controller.report_menu_choice()

            sys.stdout = sys.__stdout__  # Restauration de la sortie standard

            # Vérification que le message de sortie attendu est dans la sortie capturée
            self.assertIn("Au revoir!", output.getvalue().strip())

        # Simulation de l'entrée utilisateur
        with patch('builtins.input', side_effect=['0']):
            # Appel de report_menu_choice et vérification du comportement attendu (par exemple, affichage d'un message)
            output = io.StringIO()
            sys.stdout = output  # Redirection de la sortie standard

            self.menu_controller.report_menu_choice()

            sys.stdout = sys.__stdout__  # Restauration de la sortie standard

            # Vérification que le message de sortie attendu est dans la sortie capturée
            self.assertIn("Au revoir!", output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
