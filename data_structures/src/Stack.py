from ..src.LinkedList import LinkedList


class Stack:

    def __init__(self):
        self.lst = LinkedList()

    def is_empty(self):
        return len(self.lst) == 0

    def push(self, data):
        self.lst.insert_tail(data)

    def peek(self):
        return self.lst.get_tail()

    def pop(self):
        return self.lst.remove_tail()
