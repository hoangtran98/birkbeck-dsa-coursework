import unittest
from graph_tutorials import *


class test_graph_tutorials(unittest.TestCase):
    def test_isWalk(self):
        graphMatrix = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]

        walk = [0, 1, 2, 3, 4, 5]
        notWalk = [1, 2, 3, 5]
        self.assertEqual(isWalk(graphMatrix, walk), True)
        self.assertEqual(isWalk(graphMatrix, notWalk), False)

    def test_isTrail(self):
        graphMatrix = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]

        trail1 = [1, 2, 3, 4]
        trail2 = [1, 2, 3, 1, 0]
        notTrail1 = [1, 2, 3, 1, 2]
        notTrail2 = [1, 2, 3, 2]

        self.assertEqual(isTrail(graphMatrix, trail1), True)
        self.assertEqual(isTrail(graphMatrix, trail2), True)
        self.assertEqual(isTrail(graphMatrix, notTrail1), False)
        self.assertEqual(isTrail(graphMatrix, notTrail2), False)

    def test_isPath(self):
        graphMatrix = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]

        path = [0, 1, 2, 3, 4]
        trail = [0, 1, 2, 3, 1]
        walk = [0, 1, 2, 3, 2]

        self.assertEqual(isPath(graphMatrix, path), True)
        self.assertEqual(isPath(graphMatrix, trail), False)
        self.assertEqual(isPath(graphMatrix, walk), False)

    def test_toAdjList(self):
        graphMatrix = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]

        self.assertEqual(
            toAdjList(graphMatrix), [[1], [0, 2, 3], [1, 3], [1, 2, 4], [3, 5], [4]]
        )

    def test_toAdjMatrix(self):
        adjList = [[1], [0, 2, 3], [1, 3], [1, 2, 4], [3, 5], [4]]
        graphMatrix = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]

        self.assertEqual(toAdjMatrix(adjList), graphMatrix)
