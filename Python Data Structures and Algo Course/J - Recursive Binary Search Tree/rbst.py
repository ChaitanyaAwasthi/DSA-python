# recusive binary search tree 

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
    # we use the private method to hide the underhood of contains method to increase code modularity
    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False 
        if current_node.value == value:
            return True 
        if value < current_node.value: 
            return self.__r_contains(current_node.left, value)
        if value < current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        # self.root is passed on as the startingg point of the search (contains method)
        return self.__r_contains(self.root, value) 
    
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)
        if value < current_node.value: 
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node 
    
    # public wrapper of the private method-- __r_insert()
    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None: 
            current_node = current_node.left 
        return current_node.value # returning value which leads to None
     
    # delete a node
    def __delete_node(self, current_node, value):
        if current_node == None: 
            return None 
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value) # added instance to the call-stack
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right , value)
        else:
            # to check if it's a leaf node 
            if current_node.left is None and current_node.right is None: 
                return None 
            # to check if self.left == None 
            elif current_node.left is None: 
                current_node = current_node.right 
            # to check if self.right == None 
            elif current_node.right is None: 
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min 
                current_node.right = self.__delete_node(current_node.right, sub_tree_min) 
                return current_node # to the calling method
        return current_node 
    
    # public wrapper for private method 
    def delete_node(self, value):
         self.__delete_node(self.root, value)