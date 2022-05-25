def merge_sort(lst):
  n = len(lst)
  print(f"merge_sort {lst}")
  if n > 1:
    mid = n // 2
    left = lst[0:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, lst)

  return lst

def merge(left,right,lst):
  i = j = k = 0

  print(f"merge: left{left}, right {right}")

  while i < len(left) and j < len(right):

    print(f"selecting smallest of {left[i:]} and {right[j:]}")

    if left[i] <= right[j]:
      lst[k] = left[i]
      i += 1
    else:
      lst[k] = right[j]
      j += 1

    print(f"appending {lst[k]}")

    k += 1

    print(f"result in {lst[:k]}")

  # add any remaining values once we've exhausted on sub list
  if i == len(left):
    for x in range(j, len(right)):
      print(f"append remaining entry {right[x]}")
      lst[k] = right[x]
      k += 1

  else:
    for x in range(i, len(left)):
      print(f"append remaining entry {left[x]}")
      lst[k] = left[x]
      k += 1

  print(f"result of merge {lst}")
  return lst

if __name__ == '__main__':
  nums = [5, 3, 6, 1, 4, 7, 2, 8]

  merge_sort(nums)

  print(f"sorted: {nums}")

  assert nums == [1, 2, 3, 4, 5, 6, 7, 8]
