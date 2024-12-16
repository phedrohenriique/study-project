class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node  # element at top is the new node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

# INTERVIEW QUESTIONS


class StackInterview:

    def __init__(self) -> None:
        self.stack_list = []

    def stack_push(self, value):
        self.stack_list.append(value)

    def stack_pop(self):
        item = self.stack_list.pop()
        return item

    def stack_list(self):
        return self.stack_list


if __name__ == "__main__":

    # stack = Stack(1)
    # stack.push(2)
    # stack.push(3)
    # stack.print_stack()
    # stack.pop()
    # stack.pop()
    # stack.print_stack()

    my_stack = StackInterview()
    my_stack.stack_push(1)
    my_stack.stack_push(3)
    my_stack.stack_push(5)
    print(my_stack.stack_list)
    my_stack.stack_pop()
    print(my_stack.stack_list)
