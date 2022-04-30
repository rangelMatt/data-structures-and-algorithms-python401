from logging import NullHandler
from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self,value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        past = self.top
        self.top = self.top.next
        past.next = None

        return past.value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value
