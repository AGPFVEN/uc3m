from cmath import inf
from graph import Graph

class Graph2(Graph):
    def Dijktras(self, origin, end):
        if origin not in self._vertices.keys():
            print("Invalid Origin")
        if end not in self._vertices.keys():
            print("Invalid End")

        #This table will show us the minimum found and which vertex has been visited
        table = {}
        for i in self._vertices.keys():
            table[i] = [inf, False]

        #The distance between a node and itself is 0
        table[origin] = 0

        for i in self._vertices[origin]:
            table[i] = self._vertices[origin]
            ...
        
    def Dijkstras_(self, point, visited: dict, reco):
        for i in self._vertices[point]:
            visited[i] = [reco, True]

#labels = ['A', 'B', 'C', 'D', 'E']
#g = Graph(labels, False)
#g.add_edge('A', 'B')  # A:0,  B:1
#g.add_edge('A', 'C')  # A:0,  C:2
#g.add_edge('A', 'E')  # A:0,  E:5
#g.add_edge('B', 'D')  # B:1,  D:4
#g.add_edge('B', 'E')  # C:2,  B:1
## g.add_edge('A', 'H', 8)

#print(g)

# Now,  we use the implementation to represent this graph:
# <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

labels = ['A', 'B', 'C', 'D', 'E']
g = Graph(labels)

# Now, we add the edges
g.add_edge('A', 'C', 12)  # A->(12)C
g.add_edge('A', 'D', 60)  # A->(60)D
g.add_edge('B', 'A', 10)  # B->(10)A
g.add_edge('C', 'B', 20)  # C->(20)B
g.add_edge('C', 'D', 32)  # C->(32)D
g.add_edge('E', 'A', 7)   # E->(7)A

#print(g)
print(type(g._vertices["A"]))