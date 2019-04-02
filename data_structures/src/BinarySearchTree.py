class BinarySearchTree():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
        elif data > self.data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)

    def remove(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove(data)
        else:  # data == self.data:
            if self.left and self.right:
                self.data = self.right.__get_min()
                self.right = self.right.remove(self.data)
            else:
                if self.left is not None:
                    return self.left
                elif self.right is not None:
                    return self.right
                else:  # self.left is None and self.right is None:
                    return None

        return self

    def lookup(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left is not None:
                return self.left.lookup(data)
            else:
                return False
        else:  # data > self.data
            if self.right is not None:
                return self.right.lookup(data)
            else:
                return False

    def __get_min(self):
        if self.left:
            return self.left.__get_min()
        else:
            return self.data
