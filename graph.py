# A graph has two components: 1. A finite set of vertices called nodes and 2. a finite set of orered pair of called edges.
# The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.
# Graphs are reprsented using Adjacency Matrix(2D array of size V x V) and Adjacency List

# Representation of graph using adjacency matrix



from time import sleep


class Graph:
    def __init__(self,numvertex):
        self.adjmatrix = [[-1]* numvertex for x in range(numvertex)]
        print(self.adjmatrix)
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist = [0]*numvertex

    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjmatrix[frm][to] = cost
        self.adjmatrix[to][frm] = cost
    
    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                edges.append((self.verticeslist[i],self.verticeslist[j],self.adjmatrix[i][j]))
            return edges
    
    def get_matrix(self):
        return self.adjmatrix

G = Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())