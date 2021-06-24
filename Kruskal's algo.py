class Graph:
    def __init__(self, vertex):
        self.v = vertex
        self.graph = []
 
    def addedge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, p, i):
        if p[i] == i:
            return i
        return self.find(p, p[i])
 
    def union(self, p, rank, x, y):
        x = self.find(p, x)
        y = self.find(p, y) 
        if rank[x] < rank[y]:
            p[x] = y
        elif rank[x] > rank[y]:
            p[y] = x
        else:
            p[y] = x
            rank[x] += 1

    def Kruskal(self):
 
        result = []  
        i = 0
        e = 0
        self.graph = sorted(self.graph,key=lambda ab:ab[2])
        p = []
        rank = []
        for node in range(self.v):
            p.append(node)
            rank.append(0)
            
        while e < self.v - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(p, u)
            y = self.find(p, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(p, rank, x, y)
        cost = 0
        for u, v, weight in result:
            cost += weight
        print("Minimum Spanning Tree Cost : " , cost)
 
if __name__ == "__main__":
    print("enter no of vertices: " ,end=" ")
    v = int(input())
    print("enter no of edges: ",end= " ")
    g = Graph(v)
    e = int(input())
    for i in range(e):
        u,v,w = list(map(int,input().split()))
        g.addedge(u,v,w)

    g.Kruskal()
