from src.LinkedList import LinkedList


class Queue:

    def __init__(self):
        self.lst = LinkedList()

    def is_empty(self):
        return len(self.lst) == 0

    def enqueue(self, data):
        self.lst.insert_tail(data)

    def dequeue(self):
        return self.lst.remove_head()

    def peek(self):
        return self.lst.get_head()
