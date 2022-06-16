from select import select
from Graph_Skeleton import MyGraph

class MyGraph2(MyGraph):

    #Exercise 1 
    def get_adjacents(self, vertex:str):
        if self.check_vertex(vertex):
            return self._vertices[vertex]
        else:
            return "Not in the graph"

first_grapgh = MyGraph2(["A", "B", "C", "D"])
first_grapgh.add_edge("A", "B")
first_grapgh.add_edge("B", "C")
first_grapgh.add_edge("C", "A")
first_grapgh.add_edge("D", "D")

print(first_grapgh.get_adjacents("A"))