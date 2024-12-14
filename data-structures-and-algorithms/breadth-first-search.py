# BFS algorithm

import random


def random_list(n):
    generated_list = []
    for n in range(n):
        generated_list.append(random.randint(0, 100))
    return generated_list


class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value) -> bool:
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:  # it makes the statements exclusives, if one happens the other do not
                temp = temp.right
            else:
                return True
        return False

    def bfs(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop()
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result


if __name__ == "__main__":
    contains_number = 8
    my_tree = BinarySearchTree()
    my_new_list = random_list(10)
    for item in my_new_list:
        my_tree.insert(item)
    print('the list is :', my_new_list)
    does_contain = my_tree.contains(contains_number)
    if does_contain is True:
        print('tree contains : ', contains_number)
    if does_contain is False:
        print('three does not contains :', contains_number)

    # my_tree.insert(2)
    # my_tree.insert(1)
    # my_tree.insert(3)

    # print(my_tree.root.value)
    # print(my_tree.root.left.value)
    # print(my_tree.root.right.value)
        print(my_tree.bfs())
