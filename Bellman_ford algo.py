import sys
n = int(input())
e = int(input())
d = {}
graph = {} 

for i in range(1,n+1):
    d[i] = []
for i in range(e):
    u,v,dist = list(map(int,input().split()))
    graph[u,v] = dist
    d[u].append(v)

final_list = {}
source = int(input())

for i in range(1,n+1):
    if i != source:
        final_list[i] = graph.get((source,i),sys.maxsize)

print(d)
for loop in range(n-1):
    print("ok")
    tmp_list =[i for i in range(1,n+1) if i != source]
    print(tmp_list)
    while tmp_list:
        mini = sys.maxsize
        key = -1
        for i in tmp_list:
            if final_list[i] < mini:
                key = i
                mini = final_list[i]

        tmp_list.remove(key)
        for i in d[key]:
            final_list[i] = min(final_list[key]+graph[key,i],final_list[i])

print(final_list)
tmp_list = [i for i in range(1,n+1) if i != source]
while tmp_list:
    mini = sys.maxsize
    key = -1
    for i in tmp_list:
        if final_list[i] < mini:
            key = i
            mini = final_list[i]

    tmp_list.remove(key)
    for i in d[key]:
        if final_list[i] != min(final_list[key]+graph[key,i],final_list[i]):
            print("negative edge detected")

print(final_list)
