class MaxHeap:
    """ the greatest value index will be 0, the helper functions may change if it becomes 1 """

    def __init__(self) -> None:
        self.heap = []

    def _print_heap(self):
        print(self.heap)

    def _left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def _right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def _parent_index(self, child_index):
        return (child_index - 1)//2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap)-1

        while current_index > 0 and self.heap[current_index] > self.heap[self._parent_index(current_index)]:
            self.swap(current_index, self._parent_index(current_index))
            current_index = self._parent_index(current_index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(index=0)

    def sink_down(self, index=0):
        max_index = index
        while True:
            left_index = self._left_child_index(index)
            right_index = self._right_child_index(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self.swap(max_index, index)
                index = max_index
            else:
                return


if __name__ == "__main__":
    my_heap = MaxHeap()
    my_heap.insert(99)
    my_heap.insert(72)
    my_heap.insert(61)
    my_heap.insert(58)

    my_heap._print_heap()

    my_heap.insert(100)

    my_heap._print_heap()

    my_other_heap = MaxHeap()
    my_other_heap.insert(95)
    my_other_heap.insert(75)
    my_other_heap.insert(80)
    my_other_heap.insert(55)
    my_other_heap.insert(60)
    my_other_heap.insert(50)
    my_other_heap.insert(65)

    my_other_heap._print_heap()

    my_other_heap.remove()

    my_other_heap._print_heap()
