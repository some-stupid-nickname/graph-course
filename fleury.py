from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def removedg(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def reachable(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.reachable(i, visited)
        return count


    def isValidNextEdge(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        else:
            visited = [False] * (self.V)
            count1 = self.reachable(u, visited)

            self.removedg(u, v)
            visited = [False] * (self.V)
            count2 = self.reachable(u, visited)

            self.addEdge(u, v)

            return False if count1 > count2 else True

    def printEulerUtil(self, u):
        for v in self.graph[u]:
            if self.isValidNextEdge(u, v):
                print("%d->%d " % (u, v))
                self.removedg(u, v)
                self.printEulerUtil(v)

    def printEulerTour(self):
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        self.printEulerUtil(u)




g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.printEulerTour()
