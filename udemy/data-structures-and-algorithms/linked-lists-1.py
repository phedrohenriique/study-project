# to create a linked list we need to create a node
# the node is the main core and componente of our list

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value) -> None:
        """constructor recieves a initial value for a node and starts the list"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """ this method prints the whole list, it gets the head node and then goes on with the next node"""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_list(self):
        pass

linked_list = LinkedList(10)

linked_list.print_list()

