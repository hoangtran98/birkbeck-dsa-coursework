from recursion import *

def test_largestElement():
  assert largestElement([1,2,6,3,4,5]) == 2
  assert largestElement([9,10,3,11,0,4]) == 3

def test_secondLargestElement():
  assert secondLargestElement([1,2,6,3,4,5]) == 5
  assert secondLargestElement([9,10,45,10,0,4]) == 10

def test_largestEvenElement():
  assert largestEvenElement([2,1,4,2,3,6,3]) == 6
  assert largestEvenElement([2,1,4,10,3,6,3]) == 10
  assert largestEvenElement([2,1,100,10,3,6,3]) == 100

def test_largestEvenElementIndex():
  assert largestEvenElementIndex([2,1,4,2,3,6,3]) == 5
  assert largestEvenElementIndex([2,1,4,10,3,6,3]) == 3
  assert largestEvenElementIndex([2,1,100,10,3,6,3]) == 2

def test_containsTwoSpecialElements():
  assert containsTwoSpecialElements([5,6,15,2]) == True
  assert containsTwoSpecialElements([5,6,150,2]) == False
  assert containsTwoSpecialElements([5,20,150,2]) == False