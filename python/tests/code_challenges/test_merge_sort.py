import pytest

from code_challenges.merge_sort import merge_sort

def test_merge_sort():
  lst = [20,18,12,8,5,-2]
  actual = merge_sort(lst)
  expected = [-2, 5, 8, 12, 18,20]
  assert actual == expected


def test_merge_sort2():
  lst = [5,12,7,5,5,7]
  actual = merge_sort(lst)
  expected = [5,5,5,7,7,12]
  assert actual == expected

def test_merge_sort3():
  lst = [20,18,12,8,5,-2]
  actual = merge_sort(lst)
  expected = [-2,5,8,12,18,20]
  assert actual == expected

def test_merge_sort_even():
  lst = [10,2,8,4,6]
  actual = merge_sort(lst)
  expected = [2,4,6,8,10]
  assert actual == expected

def test_merge_sort_odd():
  lst = [9,7,5,3,1]
  actual = merge_sort(lst)
  expected = [1,3,5,7,9]
  assert actual == expected

def test_merge_sort_all_neg():
  lst = [-1,-3,-5,-7,-9]
  actual = merge_sort(lst)
  expected = [-9,-7,-5,-3,-1]
  assert actual == expected
