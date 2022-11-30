import unittest
from graph_tutorials_2 import *


class Test_graph_tutorials_2(unittest.TestCase):
    def test_adjListInduced(self):
        adjList = [[1, 3], [0, 2, 3], [1, 3], [0, 1, 2, 3]]

        induced = adjListInduced(adjList, [1, 2, 3])

        self.assertEqual(induced, [[], [2, 3], [1, 3], [1, 2, 3]])

    def test_isConnected(self):
        adjList = [[1], [0, 2], [1, 3], [2], [5], [4]]

        self.assertEqual(isConnected(adjList, [1, 2, 3]), True)
        self.assertEqual(isConnected(adjList, [1, 2, 4]), False)
