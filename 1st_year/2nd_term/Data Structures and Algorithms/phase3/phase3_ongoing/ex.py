from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        visited_vertices_ = []
        count = self.min_number_edges_(visited_vertices_, start, end)

        if count == None:
            return 0
        elif count == 0:
            return 1
        else:
            return count

    def min_number_edges_(self, visited_vertices:list, vertex, end):
        if type(vertex) != str:
            vertex = vertex.vertex

        print(vertex)
        for i in self._vertices[vertex]:
            if i.vertex == end:
                if self._directed == True:
                    return 0
                else:
                    return 1
            else:
                if i not in visited_vertices:
                    visited_vertices.append(i)

                    count_aux = self.min_number_edges_(visited_vertices, i, end)

                    if count_aux != None:
                        return count_aux + 1
            
            return None

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
        for i in list(self._vertices.keys()):
            print(i)
            visited_vertices_ = {i:True}

            if self.is_strongly_connected_(visited_vertices_, i) == None:
                return False
        
        return True

    def is_strongly_connected_(self, visited_vertices:dict, vertex:str):
        for i in self._vertices[vertex]:

            if i.vertex not in visited_vertices.keys():
                visited_vertices[i.vertex] = False
                print(visited_vertices.keys())
                print(self._vertices.keys())

                if self._vertices.keys() == visited_vertices.keys():

                    return True

                return self.is_strongly_connected_(visited_vertices, i.vertex)

#""" (grafo no conexo) """
#labels = ['a', 'b', 'c', 'e', 'f', 'g']
#graph = Graph2(labels, False)
#graph.add_edge('a', 'b')
#graph.add_edge('a', 'c')
#graph.add_edge('b', 'e')
#graph.add_edge('c', 'e')
#graph.add_edge('e', 'a')
#graph.add_edge('f', 'g')

#result = graph.is_strongly_connected()

""" strongly connected graph """
labels = ['a', 'b', 'c', 'e', 'f', 'g']
graph = Graph2(labels)
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'e')
graph.add_edge('c', 'e')
graph.add_edge('e', 'a')
graph.add_edge('e', 'f')
graph.add_edge('f', 'g')
graph.add_edge('g', 'e')
result = graph.is_strongly_connected()