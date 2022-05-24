# Blog Notes: Insertion Sort

## Insertion Sort
<!-- Short summary or background information -->
Insertion sort is an algorithm that takes in an array and sorts it by taking out the "chosen" number, which shall be in the first index, and compare it to the number ahead of it. If the number ahead of it is greater, shift that number to the right and insert the chosen number in the zero index. This sequence is repeated to the next index number to the right till all numbers have been evaluated.

## Challenge
<!-- Description of the challenge -->
- Provide a visual step through for each of the sample arrays based on the provided pseudo code
- Convert the pseudo-code into working code in your language
- Present a complete set of working tests

## Pseudocode

```json
insertionSort(arr)
  for index **in** range (1, len(arr))

  DECLARE temp <-- arr[index]
  DECLARE position <-- index - 1

    while position >= 0
      **if** arr[position] > temp
        arr[position + 1] = arr[position]
        position = position - 1
      **else:**
       **break**
    arr[position + 1] = temp
  return array
```

## Trace

Sample: `[10, 40, 30, 20]`

### First pass

```json

  position >= 0

  temp = 1
  position = 0
  [10, 40, 30, 20] ---> [10, 40, 30, 20]
   0   1   2   3

  position > temp

```

So all of these passes will occur while position is greater equal 0. So we will be talking about the inner loop if position is greater than the temp value.
In the first pass through of insertion sort, we store the array at index in a temp variable, by temporarily removing it from the array. Now we check if position is greater than temp. If it is, then the smaller number is then determined and placed on the left side of the array. So for now, position is smaller than temp so both temp and position stay put.

### Second pass

```json

  inner loop 1

  temp = 2                   stored temp value = 30
  position = 1               position = position - 1 = 0

  [10, 40, 30, 20] --> position > temp --> [10, ~~>, 40, 20]
   0   1   2    3                           0    1   2   3
  position > temp
  position value = 10 > stored temp value = 30

  [10, 30, 40, 20]

```

The second pass through we will repeat the same evaluation as the first loop. We resume by moving to the right index and assign that number to temp. The position variable has moved to the right as well.
Temp variable is now compared to position variable. Since position is greater than the temp, the position variable then is shifted one index over.
The position is decremented by 1 to the left, and is compared to temp, in this instance, it is less than temp and then the temp is assigned to the position plus 1, into the empty slot of the array.

### Third pass

```json

  temp = 3
  stored temp value = 20
  position = 2                            position = position - 1 = 1 > stored temp value = 20


  [10, 30, 40, 20] --> position > temp -->[10, 30,~~>,40]
   0   1   2   3                            0  1   2   3

  position = position - 1 = 0 > stored temp value = 20

  [10,~~>, 30, 40] --> position !> temp --> [10, 20, 30, 40]

  result = [10, 20, 30, 40]
```

The third pass through repeats the first and second pass through steps by taking out the new temp value, 20, that is at the next index 3, and assign new position to index 2, which the value is 40, and compare those numbers. Since the new position value, 40, is greater than the temp value, 20, that position index is shifted to the right and then position index is then reassigned and (decrement 1) moved to the left, to position index 1 with a value of 30, and temp value is compared to the new position value. Since 30 is greater than the temp, the position value gets shifted to the right one, and the new position index is passed to 10. Position index 10 is less than stored temp value 20. So temp value is then slotted into the empty space in the array.

After all pass throughs have been completed, we return the sorted array.

After completing the iteration, we break out of the outer loop and leaving our array now sorted.

## Code

[Insertion Sort Code](/python/code_challenges/insertion_sort.py)

[Insertion Sort Testing](/python/tests/code_challenges/test_blog_insertion_sort.py)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:

Time and Space: Insertion Sort is O(n^2) at the worse case scenario, when all the values of the array are out of order. Best case, when the values are in order, it is an O(n).

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->
Wrote a tests that:

- Tests if Node exists
- Test if Node is created, and if left and right node has `None`.
- Test if BinaryTree exists
- Test if tree returns a pre ordered/in order/post order traversal

## Links and Resources

- Bishal Khanal
- Common-Sense Guide to Data Structures and Algorithms
- Morning Lecture
