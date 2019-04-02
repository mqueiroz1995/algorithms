import unittest
from src.BinarySearchTree import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):

    def __isBST(self, bst):
        is_left_bst = True

        if bst.left is not None:
            left = bst.left
            is_left_bst = self.__isBST(left) and bst.data > left.data

        is_right_bst = True
        if bst.right is not None:
            right = bst.right
            is_right_bst = self.__isBST(right) and bst.data < right.data

        return is_left_bst and is_right_bst

    def test_insert_smallerData(self):
        # setup
        bst = BinarySearchTree(2)
        bst.insert(1)
        # test
        bst.insert(0)
        self.assertTrue(bst.lookup(0))
        self.assertTrue(self.__isBST(bst))

    def test_insert_biggerData(self):
        # setup
        bst = BinarySearchTree(0)
        bst.insert(1)
        # test
        bst.insert(2)
        self.assertTrue(bst.lookup(2))
        self.assertTrue(self.__isBST(bst))

    def test_insert_repeatedData(self):
        # setup
        bst = BinarySearchTree(0)
        # test
        bst.insert(0)
        self.assertTrue(bst.lookup(0))
        bst = bst.remove(0)
        self.assertIsNone(bst)

    def test_remove_nodeWithoutLeftChild(self):
        # setup
        bst = BinarySearchTree(0)
        bst.insert(1)
        # test
        bst = bst.remove(0)
        self.assertFalse(bst.lookup(0))
        self.assertTrue(self.__isBST(bst))

    def test_remove_nodeWithoutRightChild(self):
        # setup
        bst = BinarySearchTree(1)
        bst.insert(0)
        # test
        bst = bst.remove(1)
        self.assertFalse(bst.lookup(1))
        self.assertTrue(self.__isBST(bst))

    def test_remove_NodeWithBothChildren(self):
        # setup
        bst = BinarySearchTree(5)
        bst.insert(3)
        bst.insert(1)
        bst.insert(2)
        bst.insert(7)
        bst.insert(6)
        bst.insert(8)
        # test
        bst = bst.remove(5)
        self.assertFalse(bst.lookup(5))
        self.assertTrue(self.__isBST(bst))

    def test_remove_onlyNode(self):
        # setup
        bst = BinarySearchTree(0)
        # test
        bst = bst.remove(0)
        self.assertIsNone(bst)

    def test_remove_rightLeaf(self):
        # setup
        bst = BinarySearchTree(1)
        bst.insert(0)
        bst.insert(2)
        # test
        bst = bst.remove(2)
        self.assertFalse(bst.lookup(2))
        self.assertTrue(self.__isBST(bst))

    def test_remove_leftLeaf(self):
        # setup
        bst = BinarySearchTree(1)
        bst.insert(0)
        bst.insert(2)
        # test
        bst = bst.remove(0)
        self.assertFalse(bst.lookup(0))
        self.assertTrue(self.__isBST(bst))
