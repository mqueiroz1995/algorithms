class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.prv = None
            self.nxt = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, data):
        node = LinkedList.Node(data)
        node.nxt = self.head

        if self.head is not None:
            self.head.prv = node

        if self.tail is None:
            self.tail = node

        self.head = node
        self.size += 1

    def insert_tail(self, data):
        node = LinkedList.Node(data)
        node.prv = self.tail

        if self.tail is not None:
            self.tail.nxt = node

        if self.head is None:
            self.head = node

        self.tail = node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError('List index out of range.')
        elif index == self.size:
            self.insert_tail(data)
        elif index == 0:
            self.insert_head(data)
        else:
            node = LinkedList.Node(data)

            curr = self.head
            for i in range(index):
                curr = curr.nxt

            if curr.prv is not None:
                curr.prv.nxt = node
                node.prv = curr.prv

            node.nxt = curr
            curr.prv = node

            self.size += 1

    def remove_head(self):
        if self.head is None:
            raise IndexError('List index out of range.')
        old_head = self.head
        nxt = self.head.nxt
        if nxt is not None:
            nxt.prv = None
            self.head = nxt
        else:
            self.tail = None
            self.head = None

        self.size -= 1
        return old_head.data

    def remove_tail(self):
        if self.tail is None:
            raise IndexError('List index out of range.')
        old_tail = self.tail
        prv = old_tail.prv
        if prv is not None:
            prv.nxt = None
            self.tail = prv
        else:
            self.head = None
            self.tail = None

        self.size -= 1
        return old_tail.data

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('List index out of range.')
        elif index == self.size - 1:
            return self.remove_tail()
        elif index == 0:
            return self.remove_head()
        else:
            curr = self.head

            for i in range(index):
                curr = curr.nxt

            curr.nxt.prv = curr.prv
            curr.prv.nxt = curr.nxt
            self.size -= 1

            return curr.data

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('List index out of range.')
        curr = self.head
        for i in range(index):
            curr = curr.nxt
        return curr.data

    def contains(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return True

            curr = curr.nxt

        return False

    def __str__(self):  # pragma: no cover
        lst = []
        lst.append("[")
        curr = self.head
        while curr is not None:
            lst.append(str(curr.data))
            if curr.nxt is not None:
                lst.append(", ")
            curr = curr.nxt

        lst.append("]")

        return ''.join(lst)

    def __len__(self):
        return self.size