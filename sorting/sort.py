# Write a function ClosestCities(Distances) whose input is the Distances
# matrix considered in CW1. The function should return two distinct cities
# that are most closely located to each other. The runtime of the function
# should be O(n^2) where n = len(Distances).


def ClosestCities(distances: list[list[int]]) -> list:

    n = len(distances)
    res = []

    for i in range(n - 1):
        for j in range(i + 1, n):

            dis = distances[i][j]

            if not res or distances[res[0]][res[1]] > dis:
                res = [i, j]

    return res


# Design a function NumElements(A, minval, maxval) where A is a sorted
# list of integers, minval and maxval are two integers such that minval ≤
# maxval. The function should return the number of elements of A lying
# between minval and maxval (meaning elements greater than or equal to
# minval and smaller than or equal to maxval). The runtime of the function
# should be O(log n).
def NumElements(A: list[int], minval: int, maxval: int) -> int:

    n = len(A)

    startIdx = 0

    for i in range(n):
        if A[i] >= minval:
            startIdx = i
            break

    endIdx = n - 1

    for i in range(n - 1, startIdx, -1):
        if A[i] <= maxval:
            endIdx = i
            break

    return endIdx - startIdx + 1
