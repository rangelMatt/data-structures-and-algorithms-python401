class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.adjacency_list = {}

    def add_node(self, value):

        """
        add node
        Arguments: value
        Returns: The added node
        Add a node to the graph

        """
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def size(self):
        """
        size
        Arguments: none
        Returns the total number of nodes in the graph
        """

        return len(self.adjacency_list)

    def get_nodes(self):
        """
        get nodes
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        return self.adjacency_list.keys()

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        add edge
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        """
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError

        edge = Edge(end_vertex, weight)

        self.adjacency_list[start_vertex].append(edge)

    def get_neighbors(self,vertex):
        """
        get neighbors
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        """
        return self.adjacency_list[vertex]

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self,vertex, weight):
        self.vertex = vertex
        self.weight = weight
