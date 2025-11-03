class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def print_linkedlist(self):
        
        curr = self.head
        while curr:
            print(curr.value, end = " => ")
            curr = curr.next

        print("None")

ll = LinkedList()
ll.insertAtBeginning(10)
ll.insertAtBeginning(20)
ll.insertAtBeginning(30)

ll.print_linkedlist()
        

