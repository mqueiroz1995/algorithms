import unittest
from src.Heap import Heap

class HeapTest(unittest.TestCase):

    def __priority_comparator(self, a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

    def __build_heap(self, lst=[]):
        heap = Heap(self.__priority_comparator)
        for i in lst:
            heap.insert(i)

        return heap

    def test_peek_should_return_max_priority_element(self):
        heap = self.__build_heap([1])
        self.assertEqual(heap.peek_max_priority(), 1)

    def test_extract_max_priority_should_return_max_priority_element(self):
        heap = self.__build_heap([1])
        self.assertEqual(heap.extract_max_priority(), 1)

    def test_extract_max_priority_should_raise_lookup_error_when_heap_is_empty(self):
        heap = self.__build_heap()
        with self.assertRaises(LookupError):
            heap.extract_max_priority()

    def test_should_always_return_max_priority_element(self):
        heap = self.__build_heap([1, 5, 3, 2, 4, 2, 6, 7, 10, 8, 9, 15, 14, 12, 11, 14, 16, 13])

        self.assertEqual(heap.extract_max_priority(), 16)
        self.assertEqual(heap.extract_max_priority(), 15)
        self.assertEqual(heap.extract_max_priority(), 14)
        self.assertEqual(heap.extract_max_priority(), 14)
        self.assertEqual(heap.extract_max_priority(), 13)
        self.assertEqual(heap.extract_max_priority(), 12)
        self.assertEqual(heap.extract_max_priority(), 11)
        self.assertEqual(heap.extract_max_priority(), 10)
        self.assertEqual(heap.extract_max_priority(), 9)
        self.assertEqual(heap.extract_max_priority(), 8)
        self.assertEqual(heap.extract_max_priority(), 7)
        self.assertEqual(heap.extract_max_priority(), 6)
        self.assertEqual(heap.extract_max_priority(), 5)
        self.assertEqual(heap.extract_max_priority(), 4)
        self.assertEqual(heap.extract_max_priority(), 3)
        self.assertEqual(heap.extract_max_priority(), 2)
        self.assertEqual(heap.extract_max_priority(), 2)
        self.assertEqual(heap.extract_max_priority(), 1)
