from collections import deque


class LinkedList:
    """
    New Implementation for linked list
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
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
        current_node = self.head

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
        # if self.head is None:
        #     self.head = new_node
        #     return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

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
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TargetError(Exception):
    pass
