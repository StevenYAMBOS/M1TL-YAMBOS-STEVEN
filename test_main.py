# CTM\tests\test_main.py

"""
Fichier qui va tester si main() peut être exécuté sans erreur.
"""

import unittest


# Importez maintenant la fonction main du module main
from main import main

class TestMain(unittest.TestCase):
    def test_main_execution(self):
        try:
            main()
        except Exception as e:
            self.fail(f"Éxcécution de la méthode Main() échouée avec l'erreur : {str(e)}")

if __name__ == '__main__':
    unittest.main()

