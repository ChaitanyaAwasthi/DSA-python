# graphs contain nodes, edges, directional-edges, bi-directional-edges, weighted-edges, edges

# defining an Adjacency list
# we define it using a dictionary which holds the key value pair
# as the vector and the vectors which are being pointed by the edges


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        # to not have duplicates in the graph as vertices
        # key function accesses the key of the dictionary
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ' : ', self.adj_list[vertex])


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()
