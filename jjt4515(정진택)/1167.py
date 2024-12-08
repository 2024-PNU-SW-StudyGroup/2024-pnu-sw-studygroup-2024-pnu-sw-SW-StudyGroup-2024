# 트리는 다익스트라 이런거 필요 없다
# 트리에서 임의의 한 점에서 가장 멀리 있는 노드를 찾고 그 노드에서 또 가장 멀리 있는 
# 노드까지의 거리를 찾으면 트리의 지름이 된다.

import sys
sys.setrecursionlimit(10**6) ## 재귀 쓸땐 이거 필수

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    line = list(map(int, input().split()))
    start = line[0]
    i = 1
    while line[i] != -1:
        tree[start].append((line[i], line[i + 1]))
        i += 2

def dfs(start, cost):
    visited[start] = cost

    for n, d in tree[start]:
        if visited[n] == -1:
            dfs(n, d + cost)

visited = [-1 for _ in range(v+1)]

dfs(1, 0)

temp = 0
idx = 0
for i in range(1, v+1):
    if temp < visited[i]:
        temp = visited[i]
        idx = i

visited = [-1]*(v+1)
visited[idx] = 0
dfs(idx, 0)


print(max(visited))