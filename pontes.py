import networkx as nx
import sys

sys.setrecursionlimit(3000)

class Pontes:
    def __init__(self, G):
        self.G = G
        self.visited = {node: False for node in G.nodes()}
        self.cnt = 0
        self.disc = {node: float('inf') for node in G.nodes()}
        self.parent = {node: None for node in G.nodes()}
        self.low = {node: float('inf') for node in G.nodes()}
        self.bridges = []

    def naive(self,removed_edge):
        is_connected = nx.is_connected(self.G)

        if is_connected:
            print("O grafo continua conectado após a remoção da aresta.")
        else:
            print("O grafo não está mais conectado após a remoção da aresta.")
            self.bridges.append(removed_edge)
            print(self.bridges)


    def tarjan(self, node):
        self.visited[node] = True
        self.disc[node] = self.cnt
        self.low[node] = self.cnt
        self.cnt += 1

        for neighbor in self.G.neighbors(node):
            if not self.visited[neighbor]:
                self.parent[neighbor] = node
                self.tarjan(neighbor)
                self.low[node] = min(self.low[node], self.low[neighbor])

                if self.low[neighbor] > self.disc[node]:
                    self.bridges.append((node, neighbor))
            else:
                if neighbor != self.parent[node]:
                    self.low[node] = min(self.low[node], self.disc[neighbor])

    def find_bridges(self):
       for node in self.G.nodes():
           if not self.visited[node]:
               self.tarjan(node)
       return self.bridges
    
    def eulerian(self):
        visited = {node: False for node in self.G.nodes()}
        path = []
        stack = [0]

        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                for neighbor in self.G.neighbors(node):
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        break
            else:
                path.append(stack.pop())

        return path
