#implement Breadth First Search using Graph
#task1---------
class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self,start):
        visited=[]
        queue=[]

        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

g=Graph()
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)

print("BFS Traversal:")
g.BFS(2)


#task2-------------------
#implement Breadth First Search using Graph and find the Goal G and stop there...
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, start,goal):
        visited=[]
        queue=[start]
        visited.append(start)

        while len(queue)>0:
            node = queue.pop(0)
            print(node,end=" ")

            if node==goal:
                print("\nGoal found!")
                return

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        print("\nGoal not found!")

g=Graph()
g.add_edge('A','B')
g.add_edge('A','F')
g.add_edge('A','D')
g.add_edge('A','E')
g.add_edge('B','K')
g.add_edge('B','J')
g.add_edge('D','G')
g.add_edge('E','C')
g.add_edge('E','H')
g.add_edge('E','I')
g.add_edge('K','N')
g.add_edge('K','M')
g.add_edge('I','L')

print("BFS Traversal:")
g.BFS('A', 'Z')


#task3--------------
#Implement Priority Queue
class PriorityQueue:
    def __init__(self):
        self.items = []
        self.priorities = []

    def enqueue(self, item, priority):
        self.items.append(item)
        self.priorities.append(priority)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty!")
            return

        highest = 0

        for i in range(1, len(self.priorities)):
            if self.priorities[i] < self.priorities[highest]:
                highest = i

        item = self.items[highest]
        priority = self.priorities[highest]

        self.items.pop(highest)
        self.priorities.pop(highest)

        print(item, "Priority:", priority)

pq = PriorityQueue()

pq.enqueue("Ali", 3)
pq.enqueue("Sara", 1)
pq.enqueue("Ahmed", 2)

print("Priority Queue:")
pq.dequeue()
pq.dequeue()
pq.dequeue()