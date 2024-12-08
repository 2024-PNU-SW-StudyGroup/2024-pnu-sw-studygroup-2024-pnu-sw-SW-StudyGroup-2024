import sys
sys.setrecursionlimit(10000)
n=int(input())
graph = [ [j for j in input()] for i in range(n) ]
visited = [[False for _ in range(n)] for _ in range(n)]
visited_ir = [[False for _ in range(n)] for _ in range(n)]
def find_regular(x, y, start): #좌표값
    if x <= -1 or x >= n or y <= -1 or y >= n: # 범위를 벗어나버리면 false로 바로 종료
        return False
    if visited[x][y] == False and start == graph[x][y]: #방문한적 한번도 없는 노드라면, 그리고 시작점의 색이 현 좌표 색이랑 같을때만 방문 처리
        visited[x][y] = True
        find_regular(x - 1, y, start)
        find_regular(x + 1, y, start)
        find_regular(x, y - 1, start)
        find_regular(x, y + 1, start)
        return True
def find_irregular(x, y, start):
    if x <= -1 or x >= n or y <= -1 or y >= n: # 범위를 벗어나버리면 false로 바로 종료
        return False
    if visited_ir[x][y] == False and (start == graph[x][y] or (start == 'R' and graph[x][y] =='G') or (start == 'G' and graph[x][y] =='R')): #방문한적 한번도 없는 노드라면 또는 시작점이 적록중에 하나라면
        visited_ir[x][y] = True
        find_irregular(x - 1, y, start)
        find_irregular(x + 1, y, start)
        find_irregular(x, y - 1, start)
        find_irregular(x, y + 1, start)
        return True

result_regular = 0
for i in range(n):
    for j in range(n):
        start = graph[i][j]
        if find_regular(i, j, start) == True:
            result_regular += 1
print(result_regular, end=' ')
result_irregular = 0
for i in range(n):
    for j in range(n):
        start = graph[i][j]
        if find_irregular(i, j, start) == True:
            result_irregular += 1
print(result_irregular)
