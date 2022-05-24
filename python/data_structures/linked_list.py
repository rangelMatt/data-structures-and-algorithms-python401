from collections import deque


class LinkedList:
    """
    New Implementation for linked list
    Create a Node class that has properties for the value stored in the Node, and a current to the next Node.
    """

    def __init__(self, value=[], next=None):
        # initialization here
        self.head = None
        self.value = value
        self.next = next

    def __str__(self):
        # create result
        current = self.head
        return_str = ""
        while current:
            return_str += f'{{ {current.value} }} -> '
            current = current.next
        return return_str + "NULL"

    def kth_from_end(self, k):
        length = 0
        # setting current to head
        current_node = self.head
        # traverse through the linked list
        while current_node:
            length += 1
            current_node = current_node.next

        current_node = self.head

        run_length = length - k

        if  k + 1 > length or k == -1:
            raise TargetError
        else:
            for i in range(run_length - 1):
                current_node = current_node.next

        return current_node.value

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def isEmpty(self):
        return self.head.next is None

    def insert_before(self,value,new_value):
        if not self.head:
            raise TargetError

        if self.includes(value) is False:
            raise TargetError

        current = self.head

        if current.value == value:
            self.head = Node(new_value, current)
            return
        while current is not None:

            if value == current.next.value:
                current.next = Node(new_value, current.next)
                return
            current = current.next

    def insert_after(self,value,new_value):
        if not self.head:
            raise TargetError

        if self.includes(value) is False:
            raise TargetError

        current = self.head
        while current is not None:

            if value == current.value:
                current.next = Node(new_value, current.next)
                return
            current = current.next

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
    """
    Properties for the value stored in the Node, and a pointer to the next node.
    """
    # creating a box, now you need contents of a box and address
    def __init__(self, value, next=None):
        #the box is holding
        self.value = value

        #label for the box
        self.next = next



class TargetError(Exception):
    pass


class LinkedList():
#linked list(train) is made up of train cars(nodes)
    def __init__(self, head=None):
#train car has contents knows the next train
    self.head = head


# add a car instruction set
def append(self, node):
# person start at the head
    current = self.head
# find the caboose by going to the next node, do this as many times to get to the end.
    while current.next is not None:
        current = current.next
# once caboose is found, add a train car to the end of the train
    current.next = node
    # node = current.next <- bad

# insert is at the beginning
# append is at the end


