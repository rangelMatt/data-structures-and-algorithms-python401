# Singly Linked List
<!-- Short summary or background information -->
Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.

Insert :
    - Arguments: Value
    - Returns: Nothing
    - Adds a new node with that value to the `head` of the list with an O(1) Time Performance.

Includes:
    - Arguments: Value
    - Returns: Boolean
        - Indicates whether that value exists as a Node's value somewhere within the list.

to string:
    - Arguments: none
    - Returns: a string representing al lthe values in the Linked List, formatted as:
    - `"[ a ] -> [ b ] -> [ c ] -> NULL"`

## Challenge
<!-- Description of the challenge -->
New Implementation,
Node value.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

It is between O(1) and O(n), depending on if you are accessing the head/tail/mid.
When accessing it an O(n), because you start at the head and head to the tail, and then accessing the upper half, then the lower half. Traversing the space
O(1) when inserting or deleting, because this takes time to perform that operation.

## API
<!-- Description of each method publicly available to your Linked List -->
