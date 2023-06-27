class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class PrintList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
