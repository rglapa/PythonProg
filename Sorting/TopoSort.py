from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency list
        self.V = vertices # No of vertices
    
    def addEdge(self, u, v) -> None:
        '''Function to add an edge to graph'''
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack) -> None:
        '''Recursive function used by topologicalSort'''

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        
        # Push current vertex to stack which stores result
        stack.insert(0, v)
    
    def topologicalSort(self) -> None:
        '''Uses recursive topologicalSortUtil'''
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        
        # Print contents of stack
        print(stack)

g = Graph(6)

g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)

print("Following is a topological sort of the given graph")
g.topologicalSort()
