# Graph
<!-- Short summary or background information -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
    - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph

## Challenge
<!-- Description of the challenge -->
New implementation

## Whiteboard Process

Note required

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O:

O(1) for space and time as the graph data structure is very efficient built on a structure of hashtables.

## Unit Tests
<!-- Description of each method publicly available to your Linked List -->

Wrote a tests that:

- Tests if graph exists
- Test if adding a node to the graph
- Test if the method size is empty
- Test if size cane be measured
- Test if adding an edge
- Tests bouquet
- Test adding edge to vertex in the beginning and end
- Test getting nodes
- Tests getting neighbors

## Links and Resources

- Afternoon Lecture
- Bishal Khanal
- Roger Wells
