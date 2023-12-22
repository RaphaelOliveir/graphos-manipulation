import networkx as nx
import random
import time

from pontes import Pontes

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = self.generate_graph()

    def generate_graph(self):
        G = nx.Graph()
        for i in range(self.num_vertices):
            G.add_node(i)
        for i in range(self.num_vertices):
            for j in range(i+1, self.num_vertices):
                if random.random() < 0.5:  # Ajuste a probabilidade conforme necessário
                    G.add_edge(i, j)
        return G
    
    def remove_random_edges(self, percentage=0.01):
        num_edges = len(self.graph.edges())
        num_edges_to_remove = int(percentage * num_edges)

        edges = list(self.graph.edges())
        for _ in range(num_edges_to_remove):
            edge_to_remove = random.choice(edges)
            self.graph.remove_edge(*edge_to_remove)
            edges.remove(edge_to_remove)

# Grafo de 100 vértices

print("Grafo de 100 vértices:\n")

graph_100 = Graph(100)
graph_100.remove_random_edges()
pontes_100 = Pontes(graph_100.graph)

start_time = time.time()
pontes_100.naive()
end_time = time.time()
print(f"Tempo de execução do método naive para 100 vértices: {end_time - start_time} segundos")

start_time = time.time()
pontes_100.find_bridges()
end_time = time.time()
print(f"Tempo de execução do método tarjan para 100 vértices: {end_time - start_time} segundos")

# Grafo de 1.000 vértices

print("Grafo de 1.000 vértices:\n")

graph_1000 = Graph(1000)
graph_1000.remove_random_edges()
pontes_1000 = Pontes(graph_1000.graph)

start_time = time.time()
pontes_1000.naive()
end_time = time.time()
print(f"Tempo de execução do método naive para 1000 vértices: {end_time - start_time} segundos")

start_time = time.time()
pontes_1000.find_bridges()
end_time = time.time()
print(f"Tempo de execução do método tarjan para 1000 vértices: {end_time - start_time} segundos")

# Grafo de 10.000 vértices

print("Grafo de 10.000 vértices:\n")

graph_10000 = Graph(10000)
graph_10000.remove_random_edges()
pontes_10000 = Pontes(graph_1000.graph)

start_time = time.time()
pontes_10000.naive()
end_time = time.time()
print(f"Tempo de execução do método naive para 10000 vértices: {end_time - start_time} segundos")

start_time = time.time()
pontes_10000.find_bridges()
end_time = time.time()
print(f"Tempo de execução do método tarjan para 10000 vértices: {end_time - start_time} segundos")

# Grafo de 100.000 vértices

print("Grafo de 100.000 vértices:\n")

graph_100000 = Graph(100000)
graph_100000.remove_random_edges()
pontes_100000 = Pontes(graph_1000.graph)

start_time = time.time()
pontes_100000.naive()
end_time = time.time()
print(f"Tempo de execução do método naive para 100000 vértices: {end_time - start_time} segundos")

start_time = time.time()
pontes_1000.find_bridges()
end_time = time.time()
print(f"Tempo de execução do método tarjan para 100000 vértices: {end_time - start_time} segundos")

