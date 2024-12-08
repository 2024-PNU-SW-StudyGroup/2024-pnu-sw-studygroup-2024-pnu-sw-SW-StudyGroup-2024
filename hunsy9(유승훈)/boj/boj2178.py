import sys
from collections import deque

sys.setrecursionlimit(10000)

n,m = map(int, sys.stdin.readline().split(" "))

dxdy = [(0,1), (1,0), (0,-1), (-1,0)]

visited = [[False] * (m+1) for i in range(n+1)]
predecessor = [[0] * (m+1) for i in range(n+1)]

miro = [['0'] * (m+1)]
for i in range(n):
    miro.append(['0'] + list(sys.stdin.readline()))

def backTracking(start,count):
    if start == [1,1]:
        print(count)
        return
    count+=1
    return backTracking(predecessor[start[0]][start[1]], count)

def bfs(miro, s_x, s_y, visited):

    queue = deque([(s_x, s_y)])
    visited[s_x][s_y] = True

    while queue:
        node = queue.popleft()
        if node[0] == n and node[1] == m:
            return
        for i in dxdy:
            x = node[0] + i[0]
            y = node[1] + i[1]
            if (x > 0 and x < n+1) and (y>0 and y < m+1):
                if miro[x][y] != '0' and not visited[x][y]:
                    predecessor[x][y] = [node[0], node[1]]
                    visited[x][y] = True
                    queue.append((x,y))

bfs(miro, 1, 1, visited)

start = [n,m]
backTracking(start,1)
