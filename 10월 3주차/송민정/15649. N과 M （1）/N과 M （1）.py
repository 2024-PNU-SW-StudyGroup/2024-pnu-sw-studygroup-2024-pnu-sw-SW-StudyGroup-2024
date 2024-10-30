def dfs(depth, n, m):
    if depth == m: 
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        result.append(i)
        dfs(depth+1, n, m)
        visited[i] = False
        result.pop()

n, m = map(int, input().split())
visited = [False] * (n+1)
result = []
dfs(0, n, m)

