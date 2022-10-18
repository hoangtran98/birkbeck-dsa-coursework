from turtle import distance
from main import *

def test_MaxAvColumn():

  assert MaxAvColumn([[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7]]) == 6

  assert MaxAvColumn([[9,8,7], [8,7,6], [7,6,5]]) == 8

def test_AllIndicies():
  assert AllIndicies([0,1,1,2,3,4]) == False

  assert AllIndicies([0,1,2,3,4]) == True

  assert AllIndicies([1,2,3,4,5]) == False

  assert AllIndicies([3,4,5,6]) == False

def test_isLatinSquare():
  assert isLatinSquare([[0,1,2], [2,0,1], [1,2,0]]) == True

  assert isLatinSquare([[1,2,3], [4,5,6]]) == False

  assert isLatinSquare([[0,1,2], [2,0,1], [2,1,0]]) == False

  assert isLatinSquare([[0,1,2], [2,0,1], [2,1,3]]) == False

def test_journeyLength():
  distances = [
    [1,2,3],
    [1,1,1],
    [3,2,1]
  ]

  assert journeyLength(distances, [0, 2, 0, 1]) == 8

  assert journeyLength(distances, [1, 2, 0]) == 4

def test_closeCities():
  distances = [
    [0, 11, 10],
    [11, 0, 5],
    [10, 5, 0]
  ]

  assert closeCities(distances) == 2
  assert closeCities(distances) != 3
  assert closeCities(distances) != 1