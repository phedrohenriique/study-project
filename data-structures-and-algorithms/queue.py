class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.back = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next



if __name__ == "__main__":
    print('script')
