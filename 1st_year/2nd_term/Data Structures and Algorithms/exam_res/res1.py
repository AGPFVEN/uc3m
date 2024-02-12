import sys

def addConnection(self, start, end):
    """adds an edge from start to end"""
    if start not in self.vertices.keys():
        return
    if end not in self.vertices.keys():
        return
    
    self.vertices[start].append(end)
 
def minDistance(self, distances, visited):
    # Initilaize minimum distance for next node
    min = sys.maxsize
    #returns the vertex with minimum distance from the non-visited vertices
    for i in self.vertices:
        if distances[i] <= min and visited[i] == False:
            min = distances[i]
            min_index = i

    return min_index

def dijkstra(self, origin):
    #we use a Python list of boolean to save those nodes that have already been visited
    # Mark all the vertices as not visited
    visited={}
    for v in self.vertices.keys():
        visited[v]=False
    
    #this list will save the previous vertex
    previous={}

    for v in self.vertices.keys():
        previous[v]=-1

    #This array will save the accumulate distance from v to each node
    distances={}
    for v in self.vertices.keys():
        distances[v]=sys.maxsize

    #The distance from v to itself is 0
    distances[origin] = 0

    for n in range(len(self.vertices)):
        # Pick the vertex with the minimum distance vertex.
        # u is always equal to v in first iteration
        u = self.minDistance(distances, visited)
        # Put the minimum distance vertex in the shortest path tree
        visited[u] = True

    for i in self.vertices[u]:
        if visited[i]==False and distances[i]>distances[u]+1:
            distances[i]=distances[u]+1
            previous[i]=u

    #finally, we print the minimum path from v to the other vertices
    return distances,previous

def minimumPath(self,start,end):
    """returns a list containing the minimum path from start to end"""
    distances,previous=self.dijkstra(start)
    minimum_path=[]
    if start==end:
        print('start == end ')
        pass
    elif distances[end]==sys.maxsize:
        print("There is not path from ",start,' to ',end)
        pass
    else:
        prev=previous[end]

        while prev!=-1:
            minimum_path.insert(0,prev)
            prev=previous[prev]

        minimum_path.append(end)
    return minimum_path