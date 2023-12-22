import networkx as nx

class Extra:
    def graphml(G, filename):
        nx.write_graphml(G, filename + ".graphml")
