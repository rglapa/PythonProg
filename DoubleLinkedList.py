
class Node:
    def __init__(self, data) -> None:
        self.item = data
        self.next = None
        self.prev = None
# Class for Double Linked List
class doubleLinkedList:
    def __init__(self) -> None:
        self.start_node: Node = None

    # Insert element to empty list
    def InsertToEmptyList(self, data):
        if self.start_node == None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    
    # Insert element at end
    def InsertToEnd(self, data):
        # Check if list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None
        
    # Delete the elements from the end
    def DeleteAtEnd(self):
        # Check if list is empty
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node is None:
            self.start_node = None
            return
        n = self.start_node
        # Make n be the last node of the list
        while n.next is not None:
            n = n.next
        n.prev.next = None
    
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

dLinkedList = doubleLinkedList()
dLinkedList.InsertToEmptyList(10)
dLinkedList.InsertToEnd(20)
dLinkedList.InsertToEnd(30)
dLinkedList.InsertToEnd(40)
dLinkedList.InsertToEnd(50)
dLinkedList.InsertToEnd(60)
dLinkedList.DeleteAtEnd()

dLinkedList.Display()