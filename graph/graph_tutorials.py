# Write a function whose input is an adjacency matrix A of a graph G and a list
# L whose elements are vertices of G (possibly with repetitions). The function
# should return true if L is a walk and false otherwise.
# The runtime of the function should be O(len(L)).
def isWalk(A: list[list[int]], L: list[int]) -> bool:

    for i in range(1, len(L)):
        if not A[L[i - 1]][L[i]]:
            return False

    return True


# Write a function whose input is an adjacency matrix A of a graph G and a list
# L whose elements are vertices of G (possibly with repetitions). The function
# should return true if L is a trail and false otherwise.
# The runtime of the function should be O(len(L))
def isTrail(A: list[list[int]], L: list[int]) -> bool:
    # need to optimise
    if not isWalk(A, L):
        return False

    edges = []

    for i in range(1, len(L)):
        edge = sorted([L[i], L[i - 1]])

        if edge in edges:
            return False

        edges.append(edge)

    return True


# Write a function whose input is an adjacency matrix A of a graph G and a list
# L whose elements are vertices of G (possibly with repetitions). The function
# should return true if L is a path and false otherwise.
# The runtime of the function should be O(len(L)).


def isPath(A: list[list[int]], L: list[int]) -> bool:
    # Need to optimise
    if not isTrail(A, L):
        return False

    for vertex in L:
        if L.count(vertex) > 1:
            return False

    return True


# Write a function whose input is an adjacency matrix of a graph G and the output
# is the adjacency lists of G. The runtime of the function should be O(n^2).
def toAdjList(A: list[list[int]]) -> list[list[int]]:
    n = len(A)
    res = [[] for _ in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i][j] == 1:
                res[i].append(j)
                res[j].append(i)

    return res


# Write a function is input is adjacency lists L The function should return an
# adjacency matrix A of G. The runtime of the function should be O(n^2).
def toAdjMatrix(A: list[list[int]]) -> list[list[int]]:
    n = len(A)

    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if j in A[i]:
                res[i][j] = res[j][i] = 1

    return res
