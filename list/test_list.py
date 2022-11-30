import unittest
from _list import *


class Test_list(unittest.TestCase):
    def test_maxArg(self):
        self.assertEqual(maxArg([1, 3, 4, 9, 2]), 3)

    def test_secondLargest(self):
        self.assertEqual(secondLargest([1, 4, 6, 2, 24, 9, 14]), 14)
        self.assertEqual(secondLargest([1, 4, 6, 2, 24, 9]), 9)
        self.assertEqual(secondLargest([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)

    def test_maxEven(self):
        self.assertEqual(maxEven([1, 2, 3, 4, 5, 2, 6, 4]), 6)
        self.assertEqual(maxEven([1, 3, 5, 7, 9, 11, 13]), -1)

    def test_maxEvenArg(self):
        self.assertEqual(maxArgEven([1, 2, 3, 4, 5, 66, 2, 3]), 5)

    def test_sumTo20(self):
        self.assertEqual(sumTo20([1, 3, 3, 4, 5, 2, 1, 3, 19, 0, 3, 4]), True)
        self.assertEqual(sumTo20([1, 2, 3, 4, 4, 5, 6]), False)
