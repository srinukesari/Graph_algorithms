import sys 
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = {}
        
    def nextkey(self, key, visit):
        min = sys.maxsize
        for v in range(self.v):
            if key[v] < min and visit[v] == False:
                min = key[v]
                min_index = v
        return min_index
  
    def prims(self):
        key = [sys.maxsize] * self.v
        parent = [None] * self.v
        key[0] = 0 
        visited = [False] * self.v
        parent[0] = -1 
        for cout in range(self.v):
            u = self.nextkey(key, visited)
            visited[u] = True
            for v in range(self.v):
                if self.graph.get((u,v),0) > 0 and visited[v] == False and key[v] > self.graph.get((u,v)):
                        key[v] = self.graph.get((u,v))
                        parent[v] = u
                        
        cost = 0
        for i in range(1, self.v):
            cost += self.graph.get((i,parent[i]))

        print("minimum spanning tree cost : ", cost)

if __name__ == "__main__":
    v = int(input())
    g = Graph(v)
    e = int(input())
    for i in range(e):
        u,v,w = list(map(int,input().split()))
        g.graph[(u,v)] = w
        g.graph[(v,u)] = w
    g.prims();
