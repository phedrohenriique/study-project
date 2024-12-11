class Graph:

    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        print(self.adj_list)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.add_vertex[vertex]
            return True
        return False


if __name__ == "__main__":
    my_grap = Graph()

    my_grap.add_vertex('A')
    my_grap.add_vertex('B')
    my_grap.add_vertex('C')
    
    my_grap.add_edge('A','B')
    my_grap.add_edge('A','C')
    my_grap.add_edge('C','B')


    my_grap.print_graph()
