# So to Create a node we can make a class which is going to contain the function which creates a node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # we call the Node class to create node with the value of object we create
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


# we are going to create a new node with 4 as the integer in it
My_Linked_list = LinkedList(4)
print(My_Linked_list.head.value)
print(My_Linked_list.length)

# in this we create a NODE


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# in this we architect a whole perimeter of the linked list


class Linked_List:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


# creatinf an object
Chaitanya_Linked_List = Linked_List(10)
print(Chaitanya_Linked_List.head.value)
