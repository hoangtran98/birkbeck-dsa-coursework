from TreeNode import *

# Binary tree linearization is a procedure whose input is a binary tree and
# the output is a list whose elements are the contents of all nodes. Put it
# differently, linearization is traversal of nodes where the contents are not
# printed but rather appended in a particular order to the output list.
# Modify the Preorder, Inorder, and Postorder procedure so that the resulting
# programs return lists of elements occurring in exactly the same order as
# when they are printed in the respective original procedures.


def linearize(root: TreeNode) -> list:

    if not root:
        return []

    level = 1
    res = [root]

    while True:
        curLevel = level
        numChildrenNodes = 2**level  # num of children nodes at a particular level

        res += [None] * numChildrenNodes
        startIdx = numChildrenNodes - 1

        for i in range(numChildrenNodes):
            idx = startIdx + i

            if idx % 2 != 0:
                parentIdx = (idx - 1) // 2

                if res[parentIdx]:
                    res[idx] = res[parentIdx].left
            else:
                parentIdx = (idx - 2) // 2

                if res[parentIdx]:
                    res[idx] = res[parentIdx].right

            if res[idx] and (res[idx].left or res[idx].right):
                level += 1

        if level == curLevel:
            break

    output = []

    for node in res:
        if node:
            output.append(node.content)
        else:
            output.append(None)

    return output
