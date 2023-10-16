from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_bridge(self, u, v):
        visited = [False] * self.V
        count1 = self.dfs(u, visited)
        self.graph[u].remove(v)
        self.graph[v].remove(u)
        visited = [False] * self.V
        count2 = self.dfs(u, visited)
        self.add_edge(u, v)
   #     return count1 > count2

    def dfs(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.dfs(i, visited)
            return count

    def fleury_algorithm(self, start):
        if self.has_eulerian_cycle():
            path = []
            self.fleury_util(start, path)
            return '->'.join(map(str, path))
        else:
            return "Граф не содержит эйлерового цикла."

    def fleury_util(self, u, path):
        for v in self.graph[u]:
            if not self.is_bridge(u, v):
                path.append(u)
                self.graph[u].remove(v)
                self.graph[v].remove(u)
            self.fleury_util(v, path)

    def has_eulerian_cycle(self):
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                return False
            return True

# Проверка:

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

start_vertex = 0

print("Эйлеров путь: ", g.fleury_algorithm(start_vertex))
