
# Hashtable Left Join Table
<!-- Short summary or background information -->
- Write a function that LEFT JOINs two hashmaps into a single data structure.

- Write a function called left join
- Arguments: two hash maps
  - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
  - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Challenge
<!-- Description of the challenge -->
Code Challenge /Algorithm

## Whiteboard Process

![Hashtable left join](README.md)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:
Space and Time: O(2n) because you are iterating and then going through a list and checking the the list for duplicates. Once you find a duplicate, you append and the return result.

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->

Wrote a tests that:

- Tests if left table key match the left and right table values, then add the values to the key and return.

## Links and Resources

- Bishal Khanal
- Roger Wells
- Afternoon Lecture
  - JB mentioned to go ahead and rearrange the arrays in the tests to comply with the code.
