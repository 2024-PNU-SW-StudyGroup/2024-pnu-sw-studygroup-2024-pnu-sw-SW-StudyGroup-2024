from collections import deque

dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

n, m = map(int, input().split())
graph = []


visited = [[False] * n for i in range(m)]
s_node = []

for i in range(m):
    row = list(map(int, input().split(" ")))
    if 1 in row:
        s_node.append([m-1,row.index(1)])
    graph.append(row)

def bfs(graph, s_node, visited):
    # s_node[[1,2],[1,4]]
    depth = 0
    queue = deque([])

    for starting_node in s_node:
        visited[starting_node[0]][starting_node[1]] = True
        nnode = [starting_node[0], starting_node[1], depth]
        queue.append(nnode)

    node_track = []

    while queue:
        node = queue.popleft()
        node_track.append(node)
        for dx_dy in dxdy:
            nx = node[0] + dx_dy[0]
            ny = node[1] + dx_dy[1]
            if ( nx >= 0 and nx < m ) and ( ny >= 0 and ny < n ): #범위를 벗어나면 안되니까
                if graph[nx][ny] == 0 and not visited[nx][ny]: #새 구역이 0이 아니고
                    queue.append([nx,ny,node[2]+1])#
                    visited[nx][ny] = True
                    graph[nx][ny] = 1
                if graph[nx][ny] == -1: #만약 토마토가 없는 구역으로 노드가 설정된다면?
                    continue

    return node_track[-1][2]

result = bfs(graph, s_node,visited)

flag = False
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            flag = True

if flag:
    print(-1)
else:
    print(result)
