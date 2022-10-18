# 1. Write a function whose input is a list A. The function should return an
# index of the largest element of A.
def maxArg(arr: list) -> int:
  max = 0

  for e in arr:
    if e > max:
      max = e

  return arr.index(max) 



# 2. Write a function that returns the second largest element of the given list A
# To avoid extra input checks assume that A consists of at least two elements.
def secondLargest(arr: list) -> int:
  a = [0]

  for e in arr:
    if a[-1] < e:
      a.append(e)

  return a[-2]



# 3. Write a function that returns the largest even element of the given list A
def maxEven(arr: list) -> int:
  maxEven = 0

  for e in arr:
    if e % 2 == 0 and e > maxEven:
      maxEven = e

  return maxEven
 

# 4. Write a function that returns an index of the largest even element of the input list A.
def maxArgEven (arr: list) -> int:

  return arr.index(maxEven(arr))
# 5. Write a function that returns True if the given list A contains two dtsinct
# elements that sum up to 20 and F alse otherwise.
def containsTwoSpecialElements(arr: list) -> bool:

  n = len(arr)

  for i in range(n-1):
    for j in range(i+1, n):
      if arr[i] + arr[j] == 20:
        return True

  return False

