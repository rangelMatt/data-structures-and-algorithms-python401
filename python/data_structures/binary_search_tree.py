from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    A Binary Search Tree (BST) is a type of tree that does have some structure attached to it.
    """

    def add(self, value):

        def walk(root, new_node): #(10), (5)
            # base case
            if not root:
                return
            # we have (5) to add to tree with overall tree root of (10)
            if new_node.value < root.value:
                # go left
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                # go right
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

        node_to_add = Node(value)

        if not self.root:
            self.root = node_to_add
            return

        walk(self.root, node_to_add)

    def contains(self,value):
        # Base
        if self.root is None:
            return False

        while self.root: # while on the root
            if self.root.value == value: # check if root value is equal to given value
                return True
            elif value > self.root.value: #else, if given value greater than root value
                self.root = self.root.right # reassign right root to root.
            else:
                self.root = self.root.left # reassign left root to root
        return False
