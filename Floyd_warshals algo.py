import sys
n = int(input())
e = int(input())
graph = {}
for i in range(e):
    u,v,d = list(map(int,input().split()))
    graph[u,v] = d

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i,j) in graph.keys():
                graph[i,j] = min(graph.get((i,k),sys.maxsize)+graph.get((k,j),sys.maxsize),graph[i,j])

print(graph)
