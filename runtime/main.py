# 1. Which of the two runtimes below is O(n^2)? Explain your answer.
# (a) 1000n + 25
# (b) n^2 + 200n + 300
# (c) n^3 − 100n^2 − 800n − 1000

# Answer: a and b. Because n^2 > 1000n + 25 and O(2n^2) > n^2 + 200n + 300

# 2. Which of the two functions below takes time O(n)? Explain your answer.
# def TwoLoops1(n):
#   for i in range (0,n):
#     for j in range (0,4):
#       print(i,j)
# def TwoLoops2(n):
#   for i in range (n/4,n/2):
#     for j in range (n/4,n/2):
#       print(i,j)

# Answer: The TwoLoops1 function takes time O(n) because the outer loop takes O(n) while the inner loop takes 4 operations

# 3. Write a function whose input is a list A of integers. The function should
# return True if any two elements in the list differ by at most 20 and False
# otherwise. The runtime of the function should be O(n).


def differBy20(A: list[int]) -> bool:

    return max(A) - min(A) >= 20


# 4. Let A and B be two lists of integers without repetitions so that A contains
# all the elements of B but one. Write a function whose input are A and B.
# The function should return the element missing in A. The runtime of the
# function should be O(n).


def missingElement(A: list[int], B: list[int]) -> int:

    return sum(A) - sum(B)


# 5. Write a function whose input is a list A of integers sorted in the increasing
# order. The function should return the number of elements having only a
# single occurrence in A[i]. For example, in the list [1, 3, 3, 5, 5, 7, 8] such
# elements are 1, 7, 8 that is there are three of them. The runtime of the
# function should be O(n).
def occurOnce(A: list[int]) -> int:

    n = len(A)
    count = 0
    lastDup = -1

    for i in range(1, len(A)):
        if A[i] != A[i - 1] and A[i - 1] != lastDup:
            count += 1
            continue

        lastDup = A[i - 1]

    if A[n - 1] > A[n - 2]:
        count += 1

    return count
