import sys
from collections import deque

n_com = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

graph = [[] for i in range(n_com+1)]
visited = [False] * (n_com+1)

def bfs(graph, s_node, visited):
    queue = deque([s_node])
    visited[s_node] = True

    count = 0

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count+=1
    return count

for _ in range(edge):
    inp = list(map(int, sys.stdin.readline().split(" ")))
    graph[inp[0]].append(inp[1])
    graph[inp[1]].append(inp[0])

# print(graph)

print(bfs(graph, 1, visited))

