class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree:
    def __init__(self):
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
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root  # to traverse through the linked list
        while temp is not None:
            # we use value and not self.value cause we don't only wanna check current_node_value but all
            if self.value < temp.value:
                temp = temp.left
            elif self.value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = Binary_Search_Tree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.left.value)
