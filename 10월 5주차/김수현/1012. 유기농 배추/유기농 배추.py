# 백준 1012번
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    
    queue = deque([])
    queue.append([y, x])

    while queue:
        y, x = queue.pop()
        
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < M and 0 <= newY < N:
                if L[newY][newX] == 1:
                    L[newY][newX] = 0
                    queue.append([newY, newX])
            
T = int(input())
for _ in range(T):
    cnt = 0
    M,N,K = map(int,input().split())
    L = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x,y = map(int,input().split())
        L[y][x] = 1
        
    for j in range(N):
        for k in range(M):
            if L[j][k] == 1:
                bfs(j,k)
                cnt += 1
    print(cnt)