from collections import deque

llist = deque('abcde')
print(llist)

llist.appendleft('z')
print(llist)

print(llist.popleft())
print(llist)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

first_node = Node("a")
llist = LinkedList()
llist.head = first_node
second_node = Node("b")
third_node = Node("c")

first_node.next = second_node
second_node.next = third_node
print(llist)