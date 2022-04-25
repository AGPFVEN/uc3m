from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        ...

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        ...

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        ...

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
directed_graph = Graph2(vertices)
directed_graph.add_edge('A', 'B')
directed_graph.add_edge('A', 'C')
directed_graph.add_edge('B', 'C')
directed_graph.add_edge('B', 'D')
directed_graph.add_edge('C', 'E')
directed_graph.add_edge('D', 'E')
directed_graph.add_edge('E', 'F')
directed_graph.add_edge('F', 'G')
print(directed_graph)

undirected_graph = Graph2(vertices, False)
undirected_graph.add_edge('A', 'B')
undirected_graph.add_edge('A', 'C')
undirected_graph.add_edge('B', 'C')
undirected_graph.add_edge('B', 'D')
undirected_graph.add_edge('C', 'E')
undirected_graph.add_edge('D', 'E')
undirected_graph.add_edge('E', 'F')
undirected_graph.add_edge('F', 'G')
print(undirected_graph)