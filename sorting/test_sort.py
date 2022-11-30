import unittest
from sort import *


class TestSort(unittest.TestCase):
    def test_ClosestCities(self):
        distances = [[0, 11, 10], [11, 0, 5], [10, 5, 0]]
        self.assertEqual(ClosestCities(distances), [1, 2])

    def test_NumElements(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 32]
        self.assertEqual(NumElements(A, 3, 11), 8)
