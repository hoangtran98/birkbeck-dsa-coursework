from unittest import TestCase
from main import *


class Test_main(TestCase):
    def test_differBy20(self):
        self.assertEqual(differBy20([1, 2, 3, 4, 5, 6]), False)
        self.assertEqual(differBy20([1, 2, 3, 4, 5, 31]), True)
        self.assertEqual(differBy20([1, 2, 33, 4, 5, 63]), True)

    def test_missingElements(self):
        self.assertEqual([1, 2, 3, 4, 5], [3, 4, 5, 2], 1)
        self.assertEqual([6, 7, 8, 9], [6, 7, 8], 9)

    def test_occurOnce(self):
        self.assertEqual(occurOnce([1, 3, 3, 5, 5, 7, 8]), 3)
        self.assertEqual(occurOnce([1, 2, 3, 4, 5, 6]), 6)
