class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None


    def insert(self,value):
        # creating a new Node with the correct value
        self.head = Node(value, self.head)

    def includes(self, target_value):
        current = self.head

        ## if anything that's not a none, its a node
        while current:
            if current.value == target_value:
                return True

            current = current.next


        return False

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TargetError:
    pass
