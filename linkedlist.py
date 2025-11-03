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
    
    def insertAtEnd(self, value):

        node = Node(value)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        prev_last = curr.next
        curr.next = node
        node.next = prev_last


ll = LinkedList()
ll.insertAtBeginning(10)
ll.insertAtBeginning(20)
ll.insertAtBeginning(30)
ll.insertAtEnd(40)
ll.insertAtEnd(50)
ll.print_linkedlist()
        

