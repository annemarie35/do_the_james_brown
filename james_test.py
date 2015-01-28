# coding=utf-8

import unittest
from james import *

class TestJames(unittest.TestCase):
    def setUp(self):
        self.james = James()

    def test_james_answer_to_question(self):
        self.assertEqual(self.james.ask("How are you?"), "Sure")

    # def test_bob_answer_to_yelling(self):
    #     self.assertEqual(self.bob.ask("HELLO"), "Woah")

    # def test_bob_answer_to_yelling_question(self):
    #     self.assertEqual(self.bob.ask("HELLO?"), "Woah")

    # def test_bob_answer_to_yelling_question_with_trailing_spaces(self):
    #     self.assertEqual(self.bob.ask("HELLO?   "), "Woah")

    # def test_bob_answer_to_asking_question_with_trailing_spaces(self):
    #     self.assertEqual(self.bob.ask("hello?   "), "Sure")

    # def test_bob_answer_to_stating_nothing(self):
    #     self.assertEqual(self.bob.ask(" "), "Fine")

    # def test_bob_answer_to_stating_nothing_very_long(self):
    #     self.assertEqual(self.bob.ask("            "), "Fine")

    # def test_bob_answer_to_no_tone_sentence(self):
    #     self.assertEqual(self.bob.ask("Go buy me some Club Maté."), "Whatever")

    # def test_bob_answer_to_stating_numbers(self):
    #     self.assertEqual(self.bob.ask("1, 2, 3"), "Whatever")

    # def test_bob_answer_to_question_with_anarchic_punctuation_and_capitalization(self):
    #     self.assertEqual(self.bob.ask("hEllO, hOw Are: yOu?   "), "Sure")

if __name__ == '__main__':
    unittest.main()
