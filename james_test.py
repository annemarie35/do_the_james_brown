# coding=utf-8

import unittest
from james import *

class TestJames(unittest.TestCase):
    def setUp(self):
        self.james = James()

    def test_james_answer_to_question(self):
        self.assertEqual(self.james.ask("How are you?"), "I feel Good !")

if __name__ == '__main__':
    unittest.main()
