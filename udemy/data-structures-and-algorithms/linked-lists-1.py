# to create a linked list we need to create a node
# the node is the main core and componente of our list

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value=None) -> None:
        """constructor recieves a initial value for a node and starts the list"""
        # in python None is a singleton, it is better for performance and
        # readability the "is" over "==" it
        # it checks for consistency, in the entire python runtime there is one object None
        # and "checks" the object identity

        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
            self.list_items = []

        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
            self.list_items = [new_node]

    def print_list(self):
        """ this method prints the whole list, it gets the head node and then goes on with the next node"""
        temp = self.head
        if temp is None:
            print('linked list is empty')
            return
        while temp is not None:
            print(temp.value)
            temp = temp.next
        # print(self.list_items)

        # for item in self.list_items:
        #     print(item.value)

    def append_list(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
            self.list_items.append(new_node)
            return

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.list_items.append(new_node)
            self.length = self.length + 1
        

linked_list = LinkedList(999)
#linked_list.append_list(5)
#linked_list.append_list(10)
#linked_list.append_list(15)
# linked_list = LinkedList(10)
# linked_list.append_list(5)

linked_list.print_list()

