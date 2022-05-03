from data_structures.stack import Stack
from data_structures.linked_list import Node

class PseudoQueue:
    def __init__ (self):
        self.inbox = Stack()
        self.outbox = Stack ()

    def enqueue(self,value):
        ## Push value onto inbox
        self.inbox.push(value)


    def dequeue(self):
        while self.inbox.top:
            inbox_thing = self.inbox.pop()
            self.outbox.push(inbox_thing)

        if self.outbox.top:
            return_node = self.outbox.pop()
        while self.outbox.top:
            outbox_thing = self.outbox.pop()
            self.inbox.push(outbox_thing)
            # self.inbox.push(outbox_thing)

        return return_node






