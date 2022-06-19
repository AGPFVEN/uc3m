from Graph_Skeleton import Graph

class MyGraph2(Graph):

    #Exercise 1 
    def get_adjacents(self, vertex:str):
        if self.check_vertex(vertex):
            return self._vertices[vertex]
        else:
            return "Not in the graph"
    
    #Exercise 2
    def get_origins(self, vertex:str):
        if self.check_vertex(vertex):
            result = []

            for i in self._vertices:
                for j in self._vertices[i]:
                    if j == vertex:
                        result.append(i)
            
            return result
        else:
            print(vertex, "not in graph")
            return None

    """The approach is to get a list with all the vertices of the graph,
        then, use an auxiliar recursive function to remove the accessible vertices"""
    def not_accessible(self, vertex:str):
        #Take a list with all vertices
        not_visited = list(self._vertices.keys())

        #If vertex doesn't exist return None
        if self._vertices[vertex]:
            result = self.not_accessible_(not_visited, vertex)
            
            return result
        else:
            print("Vertex not in graph")
            return None

    def not_accessible_(self, na:list, vertex:str):
        #For each vertex of the input vertex 
        for i in self._vertices[vertex]:
            print(i.vertex)
            if i.vertex in na:
                na.remove(i.vertex)
                self.not_accessible_(na, i.vertex)
            
        return na

first_grapgh = MyGraph2(["A", "B", "C", "D"], True)
first_grapgh.add_edge("A", "B")
first_grapgh.add_edge("B", "C")
first_grapgh.add_edge("C", "A")
first_grapgh.add_edge("D", "B")

#print(list(first_grapgh._vertices.keys()))
print(first_grapgh.not_accessible("A"))