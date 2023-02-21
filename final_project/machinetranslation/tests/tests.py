import unittest
import sys
import os

print(os.getcwd())
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test_null_input(self):
        self.assertRaises(Exception, english_to_french, (None,))
    
    def test_hello_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
            
    def test_wrong_hello_translation(self):
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')


class TestF2E(unittest.TestCase):
    def test_null_input(self):
        self.assertRaises(Exception, french_to_english, (None,))
    
    def test_bonjour_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
            
    def test_wrong_bonjour_translation(self):
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello')

unittest.main()