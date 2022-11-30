# 1. Write a function whose input is a list A. The function should return an
# index of the largest element of A.
def maxArg(arr: list[int]) -> int:
    maxIdx = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[maxIdx]:
            maxIdx = i

    return maxIdx


# 2. Write a function that returns the second largest element of the given list A
# To avoid extra input checks assume that A consists of at least two elements.
def secondLargest(arr: list[int]) -> int:
    maxEl = max(arr[0], arr[1])
    secMax = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > maxEl:
            secMax = maxEl
            maxEl = arr[i]
        elif arr[i] > secMax:
            secMax = arr[i]

    return secMax


# 3. Write a function that returns the largest even element of the given list A
def maxEven(arr: list[int]) -> int:
    maxEven = -1

    for e in arr:
        if e % 2 == 0 and e > maxEven:
            maxEven = e

    return maxEven


# 4. Write a function that returns an index of the largest even element of the input list A.
def maxArgEven(arr: list[int]) -> int:

    maxEvenIdx = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and (maxEvenIdx == -1 or arr[i] > arr[maxEvenIdx]):
            maxEvenIdx = i

    return maxEvenIdx


# 5. Write a function that returns True if the given list A contains two dtsinct
# elements that sum up to 20 and F alse otherwise.
def sumTo20(arr: list[int]) -> bool:

    n = len(arr)
    SUM = 20

    map = {}

    for a in arr:
        b = SUM - a

        if b in map.keys():
            return True
        map[a] = 1

    return False
