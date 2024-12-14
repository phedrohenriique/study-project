# DFS algorithm

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

    def dfs(self):
        result = []
        self.traverse(self.root, result)
        return result

    def dfs_post_order(self):
        result = []
        self.traverse_post_oder(self.root, result)
        return result

    def dfs_in_order(self):
        result = []
        self.traverse_in_order(self.root, result)
        return result

    def traverse(self, current_node, result_list):  # pre order
        result_list.append(current_node.value)
        if current_node.left is not None:
            self.traverse(current_node.left, result_list)
        if current_node.right is not None:
            self.traverse(current_node.right, result_list)

    def traverse_post_oder(self, current_node, result_list):
        if current_node.left is not None:
            self.traverse_post_oder(current_node.left, result_list)
        if current_node.right is not None:
            self.traverse_post_oder(current_node.right, result_list)
        result_list.append(current_node.value)

    def traverse_in_order(self, current_node, result_list):
        if current_node.left is not None:
            self.traverse_in_order(current_node.left, result_list)
        result_list.append(current_node.value)
        if current_node.right is not None:
            self.traverse_in_order(current_node.value, result_list)


if __name__ == "__main__":
    contains_number = 8
    my_tree = BinarySearchTree()
    my_new_list = random_list(7)
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

    # print(my_tree.dfs())
    print(my_tree.dfs_post_order())
