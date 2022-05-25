# Blog Notes: Merge Sort

## Merge Sort
<!-- Short summary or background information -->
Merge sort is a 'divide and conquer' algorithm. It divides the input array into two halves, calls itself for the two halves, and the it merges the two sorted halves.

## Challenge
<!-- Description of the challenge -->
- Provide a visual step through for each of the sample arrays based on the provided pseudo code
- Convert the pseudo-code into working code in your language
- Present a complete set of working tests

## Pseudocode

```json
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace

merge_sort [5, 3, 6, 1, 4, 7, 2, 8]

### First pass

merge_sort [5, 3, 6, 1, 4, 7, 2, 8]

#### Split the list and look at the left side

merge_sort [5, 3, 6, 1]

#### Further split again the list and look at the left side

merge_sort [5, 3]

### Until the leftest part of the list is individual

merge_sort [5]
merge_sort [3]

### Now we start merging the 2 left numbers, but first we find the smallest and then append the remaining

merge: left[5], right [3]
selecting smallest of [5] and [3]
appending 3
result in [3]
append remaining entry 5
result of merge [3, 5]

### And then we continue the process for the next 2 left numbers

merge_sort [6, 1]

### Breaking those 2 apart before we find the smallest

merge_sort [6]
merge_sort [1]
merge: left[6], right [1]
selecting smallest of [6] and [1]

### And then append the smallest and the next smallest

appending 1
result in [1]
append remaining entry 6
result of merge [1, 6]

### Now we compare the two pair arrays and select the smallest out of the left and right and insert the smallest into the result until both pairs have been entered in a sorted fashion

merge: left[3, 5], right [1, 6]
selecting smallest of [3, 5] and [1, 6]
appending 1
result in [1]
selecting smallest of [3, 5] and [6]
appending 3
result in [1, 3]
selecting smallest of [5] and [6]
appending 5
result in [1, 3, 5]
append remaining entry 6

### Finally the result of the furthest left side!

result of merge [1, 3, 5, 6]

### Now we move on to the right side and start the same pattern here as we did for the left side

merge_sort [4, 7, 2, 8]

### Breaking down the left side of the right portion of the array to individuals and then appending those to the merge portion of the function

merge_sort [4, 7]
merge_sort [4]
merge_sort [7]
merge: left[4], right [7]
selecting smallest of [4] and [7]
appending 4
result in [4]
append remaining entry 7
result of merge [4, 7]
merge_sort [2, 8]
merge_sort [2]
merge_sort [8]
merge: left[2], right [8]
selecting smallest of [2] and [8]
appending 2
result in [2]
append remaining entry 8
result of merge [2, 8]

### Being cautious to not repeat myself, I skipped all the steps that were covered for the left side to bring us to the merging of the right side

### The right side gets compared and appended to the result

merge: left[4, 7], right [2, 8]
selecting smallest of [4, 7] and [2, 8]
appending 2
result in [2]
selecting smallest of [4, 7] and [8]
appending 4
result in [2, 4]
selecting smallest of [7] and [8]
appending 7
result in [2, 4, 7]
append remaining entry 8
result of merge [2, 4, 7, 8]

### Now we merge the left and right sorted and compare them to find the smallest and append them to the final result array

merge: left[1, 3, 5, 6], right [2, 4, 7, 8]
selecting smallest of [1, 3, 5, 6] and [2, 4, 7, 8]
appending 1
result in [1]
selecting smallest of [3, 5, 6] and [2, 4, 7, 8]
appending 2
result in [1, 2]
selecting smallest of [3, 5, 6] and [4, 7, 8]
appending 3
result in [1, 2, 3]
selecting smallest of [5, 6] and [4, 7, 8]
appending 4
result in [1, 2, 3, 4]
selecting smallest of [5, 6] and [7, 8]
appending 5
result in [1, 2, 3, 4, 5]
selecting smallest of [6] and [7, 8]
appending 6
result in [1, 2, 3, 4, 5, 6]
append remaining entry 7
append remaining entry 8
result of merge [1, 2, 3, 4, 5, 6, 7, 8]

### Now they are sorted!

sorted: [1, 2, 3, 4, 5, 6, 7, 8]

## Code

[Merge Sort Code](/python/code_challenges/merge_sort.py)

[Merge Sort Testing](/python/tests/code_challenges/test_merge_sort.py)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:

Time and Space: Merge Sort is O(N log N) at all scenarios. It always will have to divide the list in half, which will take the equal amount of time.

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->
Wrote a tests that:

- Tests if merge sort at single digits
- Tests if merge sort at double digits
- Tests if merge sort with negative mixed with positive
- Tests if evens can sort
- Tests if odds can sort
- Tests if negatives can sort

## Links and Resources

- Bishal Khanal
- Roger Wells
- Common-Sense Guide to Data Structures and Algorithms
- Geeks For Geeks
- Morning Lecture
