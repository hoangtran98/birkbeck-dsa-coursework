import unittest
from binaryTree import *


class test_binaryTree(unittest.TestCase):
    def test_linearize(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(1)
        root.right.left.right = TreeNode(2)

        self.assertEqual(
            linearize(root),
            [1, None, 3, None, None, 4, 5, None, None, None, None, 1, 2, None, None],
        )
