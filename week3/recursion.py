# 1. Write a function whose input is a list A. The function should return an
# index of the largest element of A. 

def largestElement(A:list, curIdx = 0, maxIdx = 0) -> int:
  
  # Perform comparison
  if (curIdx > 0 and A[curIdx] > A[maxIdx]): 
    maxIdx = curIdx

  # Stopping condition
  if (curIdx == len(A)-1):
    return maxIdx

  return largestElement(A, curIdx+1, maxIdx)



# 2. Write a function that returns the second largest element of the given list
# A. To avoid extra input checks assume that A consists of at least two
# elements.

def secondLargestElement(A: list) -> int:
  
  largestIdx = largestElement(A)
  
  A.pop(largestIdx)

  return A[largestElement(A)]

# 3. Write a function that returns the largest even element of the given list A
  
def largestEvenElement(A: list, i = 0, max = 0) -> int:

  # check if the current element is even and greater than max
  if A[i]%2 ==0 and A[i] > max: 
    max = A[i]
  
  # stopping condition
  if i == len(A)-1:
    return max

  return largestEvenElement(A, i+1, max)
# 4. Write a function that returns an index of the largest even element of the
# input list A.
def findFirstEvenElementIdx(A: list, i = 0) -> int:

  if A[i]%2 == 0:
    return i

  # stopping condition
  if i == len(A) - 1:
    return -1;

  return findFirstEvenElementIdx(A, i+1)


def largestEvenElementIndex(A: list, i = 0, maxIdx = -1) -> int:
  # if maxIdx hasn't been found
  if maxIdx == -1: 
    maxIdx = findFirstEvenElementIdx(A)
    
    if maxIdx == -1:
      print('There is no even elements in this list');
      return -1;

  # if maxIdx has been found
  if A[i]%2 == 0 and A[i] > A[maxIdx]:
    maxIdx = i

  # stopping condition
  if i == len(A) - 1:
    return maxIdx
  
  return largestEvenElementIndex(A, i+1, maxIdx)

# 5. Write a function that returns True if the given list A contains two distinct
# elements that sum up to 20 and F alse otherwise.
def containsTwoSpecialElements(A: list, i = 0, j = 1):

  # if found two special elements adding up to 20
  if A[i] + A[j] == 20:
    return True
  
  # if j is not last idx
  if j != len(A)-1:
    # increment j
    j += 1
  else:
    # increment i and adjust j
    i += 1
    j = i + 1

  # stopping condition if i is second last index
  if i == len(A)-2:
    return False

  return containsTwoSpecialElements(A, i, j)
