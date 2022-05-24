import pytest

from code_challenges.insertion_sort import insertion_sort

def test_insertion_sort():
  array = [20,40,30,60,10]
  actual = insertion_sort(array)
  expected = [10,20,30,40,60]
  assert actual == expected

def test_insertion_sort2():
  array = [-30,40,20,15]
  actual = insertion_sort(array)
  expected = [-30,15,20,40]
  assert actual == expected

def test_insertion_sort3():
  array = [100,0,-1,2]
  actual = insertion_sort(array)
  expected = [-1,0,2,100]
  assert actual == expected
