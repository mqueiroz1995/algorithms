'''
    Heap (aka PriorityQueue): 
    
    In a Heap, for any given node C, if P is a parent node of C, 
    then the key (the value) of P has a priority greater than or 
    equal to the priority of C. 
    
    The node at the "top" of the heap (with no parents) is the node
    with biggest priority and is called the root node.
'''
class Heap():

    ERROR_LOOKUP = "Heap is empty." # pragma: [CRP]


    def __init__(self, priority_function):
        self.__heap = []
        self.priority_function = priority_function


    def insert(self, data):
        self.__heap.append(data)
        self.__heapify_up()


    def extract_max_priority(self):
        heap = self.__heap
        if not heap:
            raise LookupError(self.ERROR_LOOKUP)
        else:
            element = heap[0]

            # swaps max priority element with the last element 
            # in the heap and deletes last element
            heap[0] = heap[len(heap) - 1]
            heap.pop()

            self.__heapify_down()
            
            return element


    def peek_max_priority(self):
        return self.__heap[0]
        


    def __heapify_down(self, current_index=0):
        heap = self.__heap

        if(len(heap) == 0):
            return

        current = heap[current_index]

        left_index, left = self.__get_left_child(current_index)
        right_index, right = self.__get_right_child(current_index)

        if left is None:
            return
        else:
            # create test where left = right
            if right is None or self.priority_function(left, right) >= 0:
                swap_index = left_index
                swap_element = left
            else:
                swap_index = right_index
                swap_element = right

        if self.priority_function(current, swap_element) < 0: # pragma: [CRP]
            heap[current_index] = swap_element
            heap[swap_index] = current
            self.__heapify_down(swap_index)


    def __heapify_up(self, current_index=None):
        heap = self.__heap

        if current_index is None:
            current_index = len(heap) - 1

        if current_index > 0:
            current = heap[current_index]
            parent_index, parent = self.__get_parent_index(current_index)

            if self.priority_function(parent, current) < 0:
                heap[current_index] = parent
                heap[parent_index] = current
                self.__heapify_up(parent_index)
        

    def __get_parent_index(self, index):
        parent_index = index // 2
        
        return parent_index, self.__get_element(parent_index)


    def __get_left_child(self, index):
        # create bigger test
        left_index = index * 2 + 1

        return left_index, self.__get_element(left_index)


    def __get_right_child(self, index):
        # create bigger test
        right_index = index * 2 + 2

        return right_index, self.__get_element(right_index)

    def __get_element(self, index):
        element = None
        if index < len(self.__heap):
            element = self.__heap[index]

        return element

