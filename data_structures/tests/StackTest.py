import unittest
from ..src.Stack import Stack


class StackTest(unittest.TestCase):

    def __build_stack(self, lst=[]):
        stack = Stack()
        for i in lst:
            stack.push(i)

        return stack

    def test_is_empty(self):
        stack = self.__build_stack()
        self.assertTrue(stack.is_empty())
        stack.push(0)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_peek(self):
        stack = self.__build_stack([0, 1, 2, 3])
        self.assertEqual(stack.peek(), 3)

    def test_push(self):
        stack = self.__build_stack([0, 1, 2, 3])
        stack.push(4)
        self.assertEqual(stack.peek(), 4)

    def test_pop(self):
        stack = self.__build_stack([0, 1, 2, 3])
        self.assertEqual(stack.pop(), 3)
