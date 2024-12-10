
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


if __name__ == "__main__":

    my_tree = BinarySearchTree()
    my_tree.insert(2)
    my_tree.insert(1)
    my_tree.insert(3)

    print(my_tree.root.value)
    print(my_tree.root.left.value)
    print(my_tree.root.right.value)
