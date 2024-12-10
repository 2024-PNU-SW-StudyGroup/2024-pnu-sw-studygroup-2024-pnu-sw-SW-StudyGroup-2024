import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph,start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for n in graph[node]:
            n_dist, n_node = n
            cost = distance[node] + n_dist
            if cost < distance[n_node]:
                distance[n_node] = cost
                q.append((cost, n_node))

    return distance

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
reversed_graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t,e))
    reversed_graph[e].append((t,s))

# 마을 X -> 각 마을
come = dijkstra(graph,X)
# 각 마을 -> 마을 X
go = dijkstra(reversed_graph,X)

max_dist = 0
for i in range(1, N+1):
    total_dist = go[i] + come[i]
    max_dist = max(max_dist, total_dist)

print(max_dist)