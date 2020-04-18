class Graph:
    graph_dict = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
        else:
            self.graph_dict[node].append(neighbor)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbor in self.graph_dict[node]:
                print("(",node,", ",neighbor,")")

    def find_path(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
                return None
    
    def BFS(self, s):
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        queue = []
        queue.append(s)
        visited[s] = True
        while len(queue) != 0:
            s = queue.pop(0)
            for node in self.graph_dict[s]:
                if visited[node] != True:
                    visited[node] = True
                    queue.append(node)
            print(s, end=" ")


g= Graph()
g.add_edge('1', '2')
g.add_edge('1', '3')
g.add_edge('2', '3')
g.add_edge('2', '1')
g.add_edge('3', '1')
g.add_edge('3', '2')
g.add_edge('3', '4')
g.add_edge('4', '3')
# g.show_edges()
print(g.find_path('4', '1'))