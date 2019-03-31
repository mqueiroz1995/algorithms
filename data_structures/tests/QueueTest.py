import unittest
from ..src.Queue import Queue


class QueueTest(unittest.TestCase):

    def __build_queue(self, lst=[]):
        queue = Queue()
        for i in lst:
            queue.enqueue(i)

        return queue

    def test_is_empty(self):
        queue = self.__build_queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(0)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_peek(self):
        queue = self.__build_queue([0, 1, 2, 3])
        self.assertEqual(queue.peek(), 0)

    def test_enqueue(self):
        queue = self.__build_queue()
        queue.enqueue(0)
        self.assertEqual(queue.dequeue(), 0)

    def test_dequeue(self):
        queue = self.__build_queue([0, 1, 2, 3])
        self.assertEqual(queue.dequeue(), 0)
