# Insertion Sort
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
  temp = 1
  position = 0
  [10, 40, 30, 20] ---> [10, 40, 30, 20]
   0   1   2   3

  position > temp

```

In the first pass through of insertion sort, we store the array at index in a temp variable, by temporarily removing it from the array and if position is greater than temp. We then take each value to the left at the gap and compare it to the value in the temporary variable. The smaller number is then determined and placed on the left side of the array.

### Second pass

```json

      temp=30
           ^
  [10, 40,  , 20] ---> [10, ~~>, 40, 20]
        ^ = position

  [10, 30, 40, 20]
```

The second pass through we will repeat the same evaluation as the first loop. We resume by moving to the right one index and assign that number to temp. The position variable has moved to the right as well.
Temp variable is now compared to position variable. Since position is greater than the temp, the position variable then is shifted one index over.
The position is decremented by 1 to the left, and is compared to temp, in this instance, it is less than temp and then the temp is assigned to the position plus 1, into the empty slot of the array.

### Third pass

```json
           temp=20
                ^
  [10, 30, 40,  ] --->  [10, 30,~~>,40]
            ^ = position       ^ = position

  [10,~~>, 30, 40]
    ^ = position

  result = [10, 20, 30, 40]
```

The third pass through repeats the first and second pass through steps by taking out the new temp value, 20, that is on the right of the last temp, and assign new position, 40, to the left of the temp, and compare those numbers. Since the new position, 40, is greater than the temp, 20, the position is shifted to the right and then position is then reassigned and (decrement 1) moved to the left, to 30, and temp is compared to the new position. Since 30 is greater than the temp, 30 gets shifted and the new position is passed to 10. 10 is less than 20, so temp is now reassigned to the position + 1, and inserted into the empty slot.

After all pass through have been completed, we return the sorted array.

After completing the iteration, we break out of the outer loop and leaving our array now sorted.

## Code

[Insertion Sort Code](/python/code_challenges/blog-insertion-sort.py)

[Insertion Sort Testing](/python/tests/code_challenges/test-blog-insertion-sort.py)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:

Time: Trees are O(n) operation, for storing and returning a max value. This is because the tree has `n` nodes, then in the worst case we will have to look at `n` times.

Space: is O(1) nothing is being added, just storing the value already in the tree, while searching.

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->
Wrote a tests that:

- Tests if Node exists
- Test if Node is created, and if left and right node has `None`.
- Test if BinaryTree exists
- Test if tree returns a pre ordered/in order/post order traversal

### Binary Search Tree Unit Tests

Wrote a tests that:

- Tests what is max value within leaves of tree
- Test what max value within left/right child of tree
- Test if root has no value

## Links and Resources

- Bishal Khanal
- Trees documentation in CodeFellows Readings.
