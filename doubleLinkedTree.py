class Node:
    def __init__(self, data):
        self.data:int = data
        self.left:Node = None
        self.right:Node = None

class BinaryTreeToDLL:
    def __init__(self):
        self.root:Node = None
        self.head:Node = None
        self.tail:Node = None
    
    def convertbtToDLL(self, node: Node):
        if node == None:
            return
        
        #Convert left subtree to doubly linked list
        self.convertbtToDLL(node.left)
        
        # If list is empty, add node as head of list
        if self.head == None:
            # Both head and tail will point to node
            self.head = self.tail = node
        # Otherwise, add node to end of the list
        else:
            # node will be added after tail such that tail's right point will point to node
            self.tail.right = node
            # node's left will point to tail
            node.left = self.tail
            # node will become new tail
            self.tail = node
        
        # Convert right subtree to doubly linked list
        self.convertbtToDLL(node.right)

    # display() will print out nodes of the list
    def display(self):
        # Node current will point to head
        current = self.head
        if self.head == None:
            print("List is empty")
            return
        print("Nodes of generated doubly linked list is: ")
        while current != None:
            # Prints each node by incrementing pointer
            print(current.data)
            current = current.right

bt = BinaryTreeToDLL()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

# Converts the given binary tree to doubly linked list
bt.convertbtToDLL(bt.root)

# Displays the nodes present in the list
bt.display()