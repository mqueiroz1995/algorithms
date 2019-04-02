import unittest
from src.LinkedList import LinkedList


class LinkedListTest(unittest.TestCase):

    def __build_linked_list(self, lst=[]):
        linked_list = LinkedList()
        for item in lst:
            linked_list.insert_tail(item)

        return linked_list

    def __validate_linked_list(self, lst):
        if lst.head is None:
            self.assertIsNone(lst.tail)
        else:
            self.assertIsNone(lst.head.prv)
            self.assertIsNone(lst.tail.nxt)

            prv = lst.head.prv
            curr = lst.head
            nxt = lst.head.nxt
            while nxt is not None:
                if prv is not None:
                    self.assertEqual(prv.nxt, curr)
                else:
                    self.assertIsNone(curr.prv)

                self.assertEqual(nxt.prv, curr)

                prv = curr
                curr = nxt
                nxt = nxt.nxt

    def test_insert_head(self):
        lst = self.__build_linked_list([1, 2, 3, 4, 5])
        lst.insert_head(0)
        self.assertEqual(lst.get(0), 0)
        self.assertEqual(len(lst), 6)
        self.__validate_linked_list(lst)

    def test_insert_head_emptyList(self):
        lst = self.__build_linked_list()
        lst.insert_head(0)
        self.assertEqual(lst.get(0), 0)
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst.head, lst.tail)
        self.__validate_linked_list(lst)

    def test_insert_tail(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4])
        lst.insert_tail(5)
        self.assertEqual(lst.get(5), 5)
        self.assertEqual(len(lst), 6)
        self.__validate_linked_list(lst)

    def test_insert_tail_emptyList(self):
        lst = self.__build_linked_list()
        lst.insert_tail(0)
        self.assertEqual(lst.get(0), 0)
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst.head, lst.tail)
        self.__validate_linked_list(lst)

    def test_insert(self):
        lst = self.__build_linked_list([0, 1, 2, 4, 5])
        lst.insert(3, 3)
        self.assertEqual(lst.get(3), 3)
        self.assertEqual(len(lst), 6)
        self.__validate_linked_list(lst)

    def test_insert_indexIs0_insertsInHead(self):
        lst = self.__build_linked_list([1, 2, 3, 4])
        lst.insert(0, 0)
        self.assertEqual(lst.get(0), 0)
        self.assertEqual(len(lst), 5)
        self.__validate_linked_list(lst)

    def test_insert_indexIsLstLen_insertsInTail(self):
        lst = self.__build_linked_list()
        lst.insert(len(lst), 0)
        self.assertEqual(lst.get(0), 0)
        self.assertEqual(len(lst), 1)
        self.__validate_linked_list(lst)

    def test_insert_indexOutOfBounds_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.insert(1, 0)

    def test_insert_indexIsNegative_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.insert(-1, 0)

    def test_remove_head(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        self.assertEqual(lst.remove_head(), 0)
        self.assertEqual(len(lst), 5)

    def test_remove_head_listSizeIs1(self):
        lst = self.__build_linked_list([0])
        self.assertEqual(lst.remove_head(), 0)
        self.assertEqual(len(lst), 0)
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.__validate_linked_list(lst)

    def test_remove_head_emptyList_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.remove_head()

    def test_remove_tail(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        self.assertEqual(lst.remove_tail(), 5)
        self.assertEqual(len(lst), 5)
        self.__validate_linked_list(lst)

    def test_remove_tail_listSizeIs1(self):
        lst = self.__build_linked_list([0])
        self.assertEqual(lst.remove_tail(), 0)
        self.assertEqual(len(lst), 0)
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.__validate_linked_list(lst)

    def test_remove_tail_emptyList_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.remove_tail()

    def test_remove(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        self.assertEqual(lst.remove(3), 3)
        self.assertEqual(len(lst), 5)
        self.__validate_linked_list(lst)

    def test_remove_indexIs0_removesHead(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        self.assertEqual(lst.remove(0), 0)
        self.assertEqual(len(lst), 5)
        self.__validate_linked_list(lst)

    def test_remove_indexIsLstLen_removesTail(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        self.assertEqual(lst.remove(5), 5)
        self.assertEqual(len(lst), 5)
        self.__validate_linked_list(lst)

    def test_remove_indexOutOfBounds_raisesIndexError(self):
        lst = self.__build_linked_list([0, 1, 2])
        with self.assertRaises(IndexError):
            lst.remove(3)

    def test_remove_indexIsNegative_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.remove(-1)

    def test_clear(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        lst.clear()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(len(lst), 0)
        self.__validate_linked_list(lst)

    def test_get_head(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4])
        self.assertEqual(lst.get_head(), 0)

    def test_get_head_emptyList_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.get_head()

    def test_get_tail(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4])
        self.assertEqual(lst.get_tail(), 4)

    def test_get_tail_emptyList_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.get_tail()

    def test_get_emptyList_raisesIndexError(self):
        lst = self.__build_linked_list()
        with self.assertRaises(IndexError):
            lst.get(0)

    def test_get_negativeNumberAsIndex_raisesIndexError(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4])
        with self.assertRaises(IndexError):
            lst.get(-1)

    def test_constains(self):
        lst = self.__build_linked_list([0, 1, 2, 3, 4, 5])
        self.assertTrue(lst.contains(3))
        self.__validate_linked_list(lst)

    def test_contains_elementNotInList_returnsFalse(self):
        lst = self.__build_linked_list([0, 1, 2, 4, 5])
        self.assertFalse(lst.contains(3))
        self.__validate_linked_list(lst)

    def test_contains_emptyList_returnsFalse(self):
        lst = self.__build_linked_list()
        self.assertFalse(lst.contains(0))
        self.__validate_linked_list(lst)
