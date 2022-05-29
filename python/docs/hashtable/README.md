# Hashtable
<!-- Short summary or background information -->
Implement a Hashtable Class with the following methods:

- set
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.
- get
  - Arguments: key
  - Returns: Value associated with that key in the table
- contains
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
- keys
  - Returns: Collection of keys
- hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Challenge
<!-- Description of the challenge -->
New implementation

## Whiteboard Process

Note required

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:

- set
  - O(1) operation, because it is just inserting
- get
  - O(1) operation, because it is getting by index address
- contains
  - O(N) operation, because it needs to search through the hash table to identify if the key exists or not.
- Keys
  - O(N) operation, because it take (n) amount of times to return the collection of keys
- hash
  - O(N) operation, because it needs to search through the keys to find the index.

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->

Wrote a tests that:

- Tests if set, get, contains, keys, hash methods exists
- Test if setting a key/value to the hashtable results in the value being in the data structure
- Test if retrieving based on a key returns the value stored
- Test if returns null for a key that does not exist in the hashtable
- Test if returns a list of all unique keys that exist in the hashtable
- Test if handle a collision within the hashtable
- Test if retrieve a value from a bucket within the hashtable that has a collision
- Test if hash a key to an in-range value

## Links and Resources

- [set add()in python](https://www.geeksforgeeks.org/set-add-python/)
- Afternoon Lecture
- Chloe Nott
- Bishal Khanal
- Roger Wells
- Dwight Lindquist
