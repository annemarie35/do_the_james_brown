import unittest
from james_dance import *

class TestDance(unittest.TestCase): 
    def setUp(self):
    	self.dance = Dance()

    def test_james_dance_boogaloo(self):
    	self.assertEqual(self.dance.jamesdance("Boogaloo"), "Boogaloo")

if __name__ == '__main__':
    unittest.main()
