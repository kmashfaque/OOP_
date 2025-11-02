class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
        print("None")

    def searhAVal(self,value):
        if self.head is None:
           return print("The value is Not in the list")
        curr = self.head
        while curr:
            if curr.value == value:a
                print(f"found the value {value}")
                return 
            curr = curr.next
        return print("Not Found the value")


linkedlist = LinkedList()
linkedlist.append(13)
linkedlist.append(14)
linkedlist.append(15)
linkedlist.append(16)
linkedlist.printLinkedList()
linkedlist.searhAVal(17)