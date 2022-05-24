

def insertion_sort(array):
  for index in range(1,len(array)):
    temp = array[index]
    pos = index - 1

    while pos >= 0:
      if array[pos] > temp:
        array[pos + 1] = array[pos]
        pos = pos - 1
      else:
        break
      array[pos + 1] = temp
  return array

insertion_sort([4,2,7,1,3])
