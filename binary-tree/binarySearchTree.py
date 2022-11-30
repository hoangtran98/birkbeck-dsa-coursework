from TreeNode import *

# Write a function LastBelow(T, x) where T is a binary search tree and x
# is an integer number. The function should return the largest content of
# an element of T that is smaller than x. If such an element does not exist,
# the function should return None.
def lastBelow(T: TreeNode, x: int) -> int:
    largest = -1

    if not T:
        return largest

    if x <= T.content:
        largest = lastBelow(T.left, x)
    elif x > T.content:
        largest = lastBelow(T.right, x)

    if x > T.content > largest:
        largest = T.content

    return largest


# Write a function Layerorder(T). The function should print the contents
# of the elements of T starting from the root then elements of distance 1
# from the root (that is the children of the root) then the elemnts at distance
# 2 then at distance 3 and so on. Essentially, this is a BFS algorithm applied
# to the root of T


def layerOrder(T: TreeNode):
    if not T:
        return

    q = []
    q.append(T)

    while q:
        cur = q.pop(0)
        print(cur.content, end=" ")

        if cur.left:
            q.append(cur.left)

        if cur.right:
            q.append(cur.right)


# Uncomment for testing
# root = TreeNode(10)
# root.left = TreeNode(7)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(8)
# root.left.left.left = TreeNode(5)
# root.left.right.right = TreeNode(9)
# root.right = TreeNode(15)
# root.right.left = TreeNode(12)
# root.right.left.left = TreeNode(10.5)
# root.right.right = TreeNode(17)

# print(lastBelow(root, 16))

# layerOrder(root)
