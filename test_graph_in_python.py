class Node:
    neighbors = None
    def __init__(self, value, neighbors = []):
        self.value = value
        self.neighbors = neighbors

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self):
        return self.neighbors


class Graph:
    def __init__(self, graph_dict = {}):
        self.graph_dict = graph_dict

    def add_node(self, graph_node):
        self.graph_dict[graph_node.value] = graph_node

    def search_node(self, node_value):
        return self.graph_dict[node_value]



def main():
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_a.add_neighbor(node_b)
    node_b.add_neighbor(node_c)
    node_c.add_neighbor(node_d)
    graph = Graph()
    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_node(node_c)
    graph.add_node(node_d)
    neighbors_b = graph.search_node('b').get_neighbors()
    for elem in neighbors_b:
        print(elem.value)

main()





