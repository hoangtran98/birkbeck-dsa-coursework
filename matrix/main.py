# 1. Write a function MaxAvColumn(A) whose input is a matrix A. The
# function should return the largest average of a column. Feel free to use
# functions sum and max

def MaxAvColumn(A: list[list[int]]) -> int:

    n = len(A)
    m = len(A[0])

    avgColumns = []

    for i in range(m):
        columnSum = 0

        for j in range(n):
            columnSum += A[j][i]

        avgColumns.append(columnSum / n)

    return max(avgColumns)

# 2. Write a function AllIndices whose input is a list A. For convenience, let
# us denote the length of A by n. The function should return True if A
# contains all the numbers 0 to n − 1 and each number occurs exactly once.
# Otherwise, the function should return False
def AllIndicies(A: list[int]) -> bool:
    n = len(A)

    allIndicies = list(range(n))

    for e in A:
        if e not in allIndicies or A.count(e) > 1:
          return False

    return True

# 3. A Latin square is an n×n matrix where each row and each column contains
# numbers 0 to n−1 and each number occurs exactly once. Write a function
# IsLatinSquare whose input is a square matrix A of integers. The function
# should return True if A is a Latin square and False otherwise. Hint: use
# the function AllIndices as in the previous question.

def isLatinSquare(A: list[list[int]]) -> bool:
    n = len(A)
    m = len(A[0])

    if n != m:
        return False
    else:
        # check if each row contains numbers 0 to n-1 occuring exactly once
        for i in range(n):
            if AllIndicies(A[i]) == False:
                return False

        # check if each column contains numbers 0 to n-1 occuring exactly once
        for i in range(n):

            col = []

            for j in range(n):
                col.append(A[j][i])

            if AllIndicies(col) == False:
                return False

        return True


# 4. In this question we will consider the table Distances as in Week 2 slides.
# Let S be a list of cities (that is, elements of S are 0, . . . , len(Distances)−
# 1). Cities can occur more than once in S. Imagine a person starting at S[0]
# then moving to S[1] then to S[2] and so on until s/he reaches S[len(S)−1].
# The total distance covered by the person is the distance between S[0] and
# S[1] plus the distance between S[1] and S[2] and so on. Write a function
# JourneyLength(A, S) that returns the distance covered by the person.
def journeyLength(A: list[list[int]], S: list[int]) -> int:
    # A: Distances matrix

    totalDis = 0

    for i in range(0, len(S) - 1):
        curCity = S[i]
        nextCity = S[i + 1]

        totalDis += A[curCity][nextCity]

    return totalDis

# 5. In this problem we continue to work with Distances matrix. Let us say
# that two cities are close to each other if the distance between them is at
# most 10 miles. Write a program CloseCities(Distances) that returns the
# number of pairs of cities close to each other. Make sure that the pairs of
# a city with itself do not count and each pair of cities is counted only once.
def closeCities(distances: list[list]) -> int:
    # distances is a nxn matrix
    n = len(distances)

    count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            # check if two cities are close cities
            if distances[i][j] <= 10:
                count += 1

    return count
