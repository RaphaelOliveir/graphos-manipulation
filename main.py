import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

from pontes import Pontes
from extra import Extra

print("\n=-=-=-=-=-=-=-=- MANIPULAÇÃO DE GRAFOS =-=-=-=-=-=-=-\n")

num_vertices = int(input("Digite o número de vértices que você deseja que o grafo tenha: "))
G = nx.Graph()

for i in range(num_vertices):
 weight = float(input(f"Digite a ponderação para o vértice {i}: "))
 label = input(f"Digite a rotulação para o vértice {i}: ")
 G.add_node(i, weight=weight, label=label)

 os.system('clear')

pontes = Pontes(G)

while True:
   num_arestas = int(input("Digite o número de arestas que você deseja que o grafo tenha: "))
   if num_arestas > num_vertices * (num_vertices - 1) / 2 or num_arestas < 0:
       print("Número de arestas inválido!")
   else:
       break

for _ in range(num_arestas):
   v1 = int(input("Digite o vértice de origem da aresta: "))
   v2 = int(input("Digite o vértice de destino da aresta: "))
   weight = float(input("Digite a ponderação para a aresta: "))
   label = input("Digite a rotulação para a aresta: ")
   G.add_edge(v1, v2, weight=weight, label=label)


os.system('clear')

while True:
    num_edges_to_remove = int(input("Quantas arestas você deseja remover? "))
    if num_edges_to_remove <= G.number_of_edges():
        for _ in range(num_edges_to_remove):
            edge_label_to_remove = input("Digite a label da aresta que deseja remover: ")

            for edge in list(G.edges(data=True)):
                if edge[2]['label'] == edge_label_to_remove:
                    removed_edge = (edge[0],edge[1])

                    G.remove_edge(*removed_edge)
                    pontes.naive(removed_edge)
                    break   
        break
    else:
        print("O número de arestas a remover é maior do que o número total de arestas no grafo. Por favor, insira um número menor ou igual a " + str(G.number_of_edges()))

print(f"O grafo tem {G.number_of_nodes()} vértices e {G.number_of_edges()} arestas.")
print(f"O grafo é vazio? {nx.is_empty(G)}, O grafo é completo? {G.number_of_edges() == num_vertices * (num_vertices - 1) / 2}")

def draw_graph(G):
   pos = nx.spring_layout(G)

   nx.draw_networkx_nodes(G, pos)

   nx.draw_networkx_edges(G, pos)

   vertex_labels = {i: G.nodes[i].get('label', i) for i in G.nodes}
   nx.draw_networkx_labels(G, pos, labels=vertex_labels)

   edge_labels = {edge: G.edges[edge].get('weight', '') for edge in G.edges}
   nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

   plt.show()

draw_graph(G)

os.system('clear')

while True:
  print("Selecione uma opção")
  print("1. Representar grafo por matriz de adjacência")
  print("2. Representar grafo por lista de adjacência")
  print("3. Encontrar quais são as pontes no grafo restante")
  print("4. Verificar se existe um caminho euleriano")
  print("5. Exportar grafo em GraphML")
  print("6. Sair do programa")

  try:
      choice = int(input("Digite o número da opção escolhida: "))
  except ValueError:
      print("Por favor, insira um número válido.")
      continue

  os.system('clear')

  if choice == 1:
       adj_matrix_weighted = nx.to_numpy_array(G)
       adj_matrix = np.where(adj_matrix_weighted != 0, 1, 0)
       print(adj_matrix)

  elif choice == 2:
       adj_list = G.adjacency()
       for node, neighbors in adj_list:
           print(f"Node {node} is connected to {neighbors}")

  elif choice == 3:
       bridges = pontes.find_bridges()
       for bridge in bridges:
           print(f"A aresta {bridge} é uma ponte.")

  elif choice == 4:
       eulerian_path = pontes.eulerian()
       print(eulerian_path)

  elif choice == 5:
    filename = input("Digite o nome do arquivo para exportar (inclua .graphml): ")
    Extra.graphml(G, filename)

  elif choice == 6:
       print("Saindo do programa...")
       break

  else:
      print("Opção inválida")
