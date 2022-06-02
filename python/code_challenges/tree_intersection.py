from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

def tree_intersection(tree1, tree2):
    ht = Hashtable()
    #create an empty list to store common values
    commons = set()

    # traverse through first tree
    tree1_values = tree1.pre_order()
    # traverse through first tree
    tree2_values = tree2.pre_order()

    # loop through first set
    for value in tree1_values:

        ht.set(value, value)
    for values in tree2_values:

        if ht.contains(values):

            commons.add(values)

    return commons

