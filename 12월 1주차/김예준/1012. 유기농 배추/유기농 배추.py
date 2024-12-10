import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<0 or x >= n or y < 0 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if not visited[x][y] and arr[x][y] == 1:
        # 해당 노드 방문 처리
        visited[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False
        
for _ in range(t):
  m,n,k = map(int, input().split())
  arr = [[0]*m for _ in range(n)]
  visited = [[0]*m for _ in range(n)]
  cnt = 0
  for _ in range(k):
    i,j = map(int, input().split())
    arr[j][i] = 1
  for x in range(n):
    for y in range(m):
      if dfs(x,y):
        cnt += 1
  print(cnt)