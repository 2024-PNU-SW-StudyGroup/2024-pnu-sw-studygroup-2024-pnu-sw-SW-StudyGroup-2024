from collections import deque
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=[]

def fill(x1,y1):
    queue=deque()
    queue.append((x1,y1))
    part_answer=1
    graph[x1][y1]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=n or nx<0 or ny>=n or ny<0:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                part_answer+=1
                graph[nx][ny]=0
    return part_answer
    
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            part=fill(i,j)
            answer.append(part)
print(len(answer))
answer.sort()
for i in answer:
    print(i)