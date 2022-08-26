class Node:

    def __init__(self, data):
        self.data = data
        self.next: Node = None

class LinkedList:

    def __init__(self):
        self.head: Node = None
    
    def reverse(self):
        prev: Node = None
        current: Node = self.head
        while current is not None:
            next: Node = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def push(self, new_data: int):
        new_node: Node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp: Node = self.head
        print(type(self))
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given linked list:")
llist.printList()
print("Reversed Linked List:")
llist.reverse()
llist.printList()