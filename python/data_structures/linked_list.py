class LinkedList:
    """
    New Implementation for linked list
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    """

    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        # create result
        current = self.head
        return_str = ""
        while current:
            return_str += f'{{ {current.value} }} -> '
            current = current.next
        return return_str + "NULL"


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
