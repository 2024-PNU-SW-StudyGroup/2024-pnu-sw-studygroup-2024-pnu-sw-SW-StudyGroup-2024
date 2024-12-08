# 11/10
# dfs, bfs
# 백준 11725번 트리의 부모 찾기: https://www.acmicpc.net/problem/11725
# 접근 방법: dfs bfs 둘다 가능한데 bfs 선택하였다. 
# 트리이기 때문에 루트 노드를 시작으로 bfs를 돌면서 다음 노드를 방문할 때, 그 이전 노드가 부모 노드가 된다.
# 이 점을 이용하여 간단히 구현했다.

from collections import deque 

n = int(input())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = list(map(int, input().split()))
    edge[a].append(b)
    edge[b].append(a)

visited = [0 for _ in range(n+1)]
q = deque()     
def bfs(start):
    q.append(start)
    visited[start] = start
    while q:
        node = q.popleft()
        for next in edge[node]:
            if not visited[next]:
                visited[next] = node
                q.append(next)
    
bfs(1)
for i in range(2, n+1):
    print(visited[i])
