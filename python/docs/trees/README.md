# Trees
<!-- Short summary or background information -->
Using trees as the underlying data storage mechanism, implement both a **Binary Tree** and a **Binary Search Tree**

## Node

- Create a Node class that has properties for the values stored in the Node, the left child node, and the right child node.

## Binary Tree

- Create a Binary Tree class:
  - Define a method for each of the depth first traversals:
    - pre order
    - in order
    - post order which returns an array of the values, ordered appropriately.

## Binary Search Tree

- Create a Binary Search Tree class
  - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  - Add
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value in the correct location in the binary search tree.
  - Contains
    - Arguments: value
    - Returns: boolean indicating whether or not the value is in the tree at least once.

## Challenge
<!-- Description of the challenge -->
New Implementation

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:

Trees are O(n) operation, for inserting a new node. Because of lack of organizational structure in a Binary Tree, the worst case for most operations will involve traversing the entire tree. If we assume that a tree has `n` nodes, then in the worst case we will have to look at `n` times.

Binary Search Tree is O(height). Worst case we will have to search all the way down to a leaf, which will require searching through as many nodes as the tree is tall.

In the search for BST, it would be O(1), during the search, we are not allocating any additional space.

## API

pre order -> ["a", "b", "d", "e", "c", "f", "g"]

in order -> ["d", "b", "e", "a", "f", "c", "g"]

post order -> ["g", "c", "f", "e", "b", "d", "a"]

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->

### Binary Tree Unit Tests

Wrote a tests that:

- Tests if Node exists
- Test if Node is created, and if left and right node has `None`.
- Test if BinaryTree exists
- Test if tree returns a pre ordered/in order/post order traversal

### Binary Search Tree Unit Tests

Wrote a tests that:

- Tests if Binary Search Tree exists
- Test if root has None
- Test add a root value
- Test if left/right values
- Test adding deeper right values
- Test if tree contains/not contains `n` number, return Boolean
- Test if dequeue value is empty
- Test if dequeue works when full
- Test if empty

## Links and Resources

- Benjamin Carter
- Justin Hammerly
- Dwight Lindquist
- Roger Wells
- Bishal Khanal
- Afternoon Lecture
