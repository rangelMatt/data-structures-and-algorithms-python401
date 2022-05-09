
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Class Binary Tree containing 3 methods; pre-order, in-order, post-order.
    """
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Traverse the tree in a pre-order fashion
        return list of the values in correct order
        """
        def climb(root, values): # root = a Node or more. Recursive function
            if not root:
                return
            # Task 1: do something
            values.append(root.value)
            # Task 2: go left
            climb(root.left, values)
            # Task 3: go right
            climb(root.right, values)
        ordered_values = []
        climb(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        Traverse the tree in a in-order fashion
        return list of the values in correct order
        """
        def climb(root, values): # root = a Node or more. Recursive function
            if not root:
                return
            # Task 1: go left
            climb(root.left, values)
            # Task 2: do something
            values.append(root.value)
            # Task 3: go right
            climb(root.right, values)
        ordered_values = []
        climb(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        """
        Traverse the tree in a post-order fashion
        return list of the values in correct order
        """
        def climb(root, values): # root = a Node or more. Recursive function
            if not root:
                return
            # Task 1: go left
            climb(root.left, values)
            # Task 2: go right
            climb(root.right, values)
            # Task 3: do something
            values.append(root.value)

        ordered_values = []

        climb(self.root, ordered_values)



        return ordered_values


    def find_maximum_value(self):
        if self.root:
            value = self.in_order()
            max_value = value[0]

            for num in value:
                if num > max_value:
                    max_value = num

            return max_value

        else:

            return 'We Aint found Root!'
