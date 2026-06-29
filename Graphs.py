from collections import defaultdict
graph=defaultdict(list)

edges=[(0,1),(0,2),(1,2),(2,0),(2,3)]

for u,v in edges:
    graph[u].append(v)

def bfs(graph,start):
    queue=deque([start])
    visited=set
    for node in queue: