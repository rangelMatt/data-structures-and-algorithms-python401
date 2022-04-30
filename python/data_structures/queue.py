
from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        if not self.front:
            self.front = Node(value)
            self.rear = self.front
            return

        temp = self.rear
        self.rear =Node(value)
        temp.next = self.rear
        return


    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        past = self.front
        self.front = past.next
        past.next = None
        return past.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        return self.front is None
